#!/usr/bin/env python3
"""Validate the six-result closure connector and one resolved destination."""

from __future__ import annotations

import argparse
import json
import ntpath
import sys
from pathlib import Path


RESULT_IDS = {str(index) for index in range(1, 7)}
ROUTE_TYPES = {"resolved_owner", "literal", "path_template"}
REQUIRED_FIELDS = {"name", "route", "destination", "verification"}


def fail(message: str) -> None:
    raise ValueError(message)


def normalized(path: str) -> str:
    return ntpath.normcase(ntpath.normpath(path))


def is_under(path: str, root: str) -> bool:
    try:
        return ntpath.commonpath([normalized(path), normalized(root)]) == normalized(root)
    except ValueError:
        return False


def load_connector(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("schema_version must be 1")
    if not data.get("connector_id"):
        fail("connector_id is required")
    results = data.get("results")
    if not isinstance(results, dict) or set(results) != RESULT_IDS:
        fail("results must contain exactly keys 1 through 6")
    for result_id, route in results.items():
        if not isinstance(route, dict):
            fail(f"result {result_id} must be an object")
        missing = REQUIRED_FIELDS - set(route)
        if missing:
            fail(f"result {result_id} missing fields: {', '.join(sorted(missing))}")
        if route["route"] not in ROUTE_TYPES:
            fail(f"result {result_id} has unsupported route: {route['route']}")
        if route["route"] == "resolved_owner" and not route.get("allowed_route_sources"):
            fail(f"result {result_id} requires allowed_route_sources")
        if route["route"] == "path_template" and "{content_id}" not in route.get("path_template", ""):
            fail(f"result {result_id} path_template must contain {{content_id}}")
    return data


def validate_route(args: argparse.Namespace, connector: dict) -> None:
    route = connector["results"][args.result]
    destination = args.destination

    for root in route.get("forbidden_roots", []):
        if is_under(destination, root):
            fail(f"result {args.result} destination is under forbidden root: {root}")

    route_type = route["route"]
    if route_type == "literal":
        if destination != route["destination"]:
            fail(f"result {args.result} must use literal destination: {route['destination']}")
    elif route_type == "resolved_owner":
        if args.route_source not in route["allowed_route_sources"]:
            allowed = ", ".join(route["allowed_route_sources"])
            fail(f"result {args.result} route_source must be one of: {allowed}")
    elif route_type == "path_template":
        if not args.content_id:
            fail(f"result {args.result} requires --content-id")
        expected = route["path_template"].format(content_id=args.content_id)
        if normalized(destination) != normalized(expected):
            fail(f"result {args.result} destination mismatch; expected: {expected}")
        required_status = route.get("required_status")
        if required_status and args.status != required_status:
            fail(f"result {args.result} status must be: {required_status}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--connector", type=Path, required=True)
    parser.add_argument("--check-connector", action="store_true")
    parser.add_argument("--result", choices=sorted(RESULT_IDS))
    parser.add_argument("--destination")
    parser.add_argument("--route-source")
    parser.add_argument("--content-id")
    parser.add_argument("--status")
    args = parser.parse_args()

    try:
        connector = load_connector(args.connector)
        if args.result or args.destination:
            if not args.result or not args.destination:
                fail("--result and --destination must be used together")
            validate_route(args, connector)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
