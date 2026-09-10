#!/usr/bin/env python3
"""Validate the durable structure of a personal shopping workspace."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


REQUIRED_FILES = (
    "shopping-workspace.md",
    "preferences.md",
    "stock.md",
    "current-shopping.md",
    "product-notes.md",
    "stores.md",
    "purchases/_template.md",
)
ALLOWED_STAGES = {"idle", "draft", "list_agreed", "cart_building", "cart_ready", "ordered", "closed"}
ALLOWED_LIST_STATUSES = {"not_started", "draft", "agreed", "superseded"}
ALLOWED_ORDER_STATUSES = {"ordered", "in_delivery", "delivered_by_store", "received_by_user", "cancelled"}
ALLOWED_MEASUREMENT_SYSTEMS = {"metric", "us_customary", "imperial", "mixed"}
SENSITIVE_KEYS = {
    "address",
    "full_address",
    "delivery_address",
    "phone",
    "phone_number",
    "card_number",
    "payment_token",
    "password",
    "cookie",
    "session_cookie",
    "auth_token",
    "token",
}


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"').strip("'")
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", required=True, help="Workspace directory")
    args = parser.parse_args()
    root = Path(args.path).expanduser().resolve()

    errors: list[str] = []
    warnings: list[str] = []
    if not root.is_dir():
        errors.append(f"workspace_not_found:{root}")
    else:
        for relative in REQUIRED_FILES:
            path = root / relative
            if not path.is_file():
                errors.append(f"missing_file:{relative}")
                continue
            meta = frontmatter(path)
            if meta.get("schema_version") != "1":
                errors.append(f"schema_version:{relative}")

        workspace = root / "shopping-workspace.md"
        if workspace.is_file():
            meta = frontmatter(workspace)
            if not meta.get("market_region"):
                warnings.append("market_region_not_set")
            currency = meta.get("currency", "")
            if not currency:
                warnings.append("currency_not_set")
            elif not re.fullmatch(r"[A-Z]{3}", currency):
                errors.append(f"invalid_currency:{currency}")
            measurement_system = meta.get("measurement_system", "")
            if not measurement_system:
                warnings.append("measurement_system_not_set")
            elif measurement_system not in ALLOWED_MEASUREMENT_SYSTEMS:
                errors.append(f"invalid_measurement_system:{measurement_system}")

        stores = root / "stores.md"
        if stores.is_file():
            table_lines = [
                line for line in stores.read_text(encoding="utf-8").splitlines()
                if line.strip().startswith("|")
            ]
            if len(table_lines) <= 2:
                warnings.append("stores_not_configured")

        current = root / "current-shopping.md"
        if current.is_file():
            meta = frontmatter(current)
            if meta.get("stage") not in ALLOWED_STAGES:
                errors.append(f"invalid_stage:{meta.get('stage', '')}")
            if meta.get("list_status") not in ALLOWED_LIST_STATUSES:
                errors.append(f"invalid_list_status:{meta.get('list_status', '')}")

        order_keys: dict[tuple[str, str], str] = {}
        purchases = root / "purchases"
        if purchases.is_dir():
            for path in sorted(purchases.glob("*.md")):
                if path.name == "_template.md":
                    continue
                meta = frontmatter(path)
                store = meta.get("store", "")
                order_id = meta.get("order_id", "")
                if not store:
                    errors.append(f"order_without_store:{path.name}")
                if not order_id:
                    warnings.append(f"order_without_id:{path.name}")
                elif store:
                    order_key = (store.casefold(), order_id)
                    if order_key in order_keys:
                        errors.append(
                            f"duplicate_order_key:{store}:{order_id}:"
                            f"{order_keys[order_key]}:{path.name}"
                        )
                    else:
                        order_keys[order_key] = path.name
                status = meta.get("status", "")
                if status not in ALLOWED_ORDER_STATUSES:
                    errors.append(f"invalid_order_status:{path.name}:{status}")

        markdown_files = sorted(root.rglob("*.md"))
        for path in markdown_files:
            meta = frontmatter(path)
            for key, value in meta.items():
                if key.endswith("_at") and value:
                    try:
                        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
                    except ValueError:
                        parsed = None
                    if parsed is None or parsed.tzinfo is None:
                        relative = path.relative_to(root).as_posix()
                        errors.append(f"invalid_timestamp:{relative}:{key}:{value}")
            total = meta.get("total", "")
            if total and not re.fullmatch(r"-?\d+(?:\.\d+)?", total):
                relative = path.relative_to(root).as_posix()
                errors.append(f"invalid_decimal:{relative}:total:{total}")

            lines = path.read_text(encoding="utf-8").splitlines()
            for line_number, line in enumerate(lines, start=1):
                match = re.match(r"^\s*([\w-]+):\s*(.+)$", line, flags=re.UNICODE)
                if match and match.group(1).lower() in SENSITIVE_KEYS:
                    relative = path.relative_to(root).as_posix()
                    warnings.append(
                        f"possible_sensitive_field:{relative}:{line_number}:{match.group(1)}"
                    )

    result = {
        "status": "invalid" if errors else "valid",
        "path": str(root),
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
