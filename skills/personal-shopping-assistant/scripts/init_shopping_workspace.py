#!/usr/bin/env python3
"""Create a personal shopping workspace from bundled starter files."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path


STARTER = Path(__file__).resolve().parent.parent / "assets" / "starter"


def local_timestamp() -> str:
    return datetime.now().astimezone().isoformat(timespec="minutes")


def render(
    text: str,
    *,
    owner: str,
    market_region: str,
    locale: str,
    currency: str,
    measurement_system: str,
    precision: str,
    stamp: str,
) -> str:
    replacements = {
        'owner_name: ""': f'owner_name: {json.dumps(owner, ensure_ascii=False)}',
        'market_region: ""': f'market_region: {json.dumps(market_region, ensure_ascii=False)}',
        'locale: ""': f'locale: {json.dumps(locale, ensure_ascii=False)}',
        'currency: ""': f'currency: {json.dumps(currency, ensure_ascii=False)}',
        'measurement_system: ""': (
            f'measurement_system: {json.dumps(measurement_system, ensure_ascii=False)}'
        ),
        'stock_precision: "approximate"': f'stock_precision: {json.dumps(precision, ensure_ascii=False)}',
        'created_at: ""': f'created_at: "{stamp}"',
        'updated_at: ""': f'updated_at: "{stamp}"',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", required=True, help="Destination workspace directory")
    parser.add_argument("--owner", default="", help="Optional owner display name")
    parser.add_argument("--market-region", default="", help="Country or broad shopping region")
    parser.add_argument("--locale", default="", help="Optional locale such as en-GB")
    parser.add_argument("--currency", default="", help="Optional ISO 4217 code such as GBP")
    parser.add_argument(
        "--measurement-system",
        default="",
        choices=("metric", "us_customary", "imperial", "mixed"),
        help="Optional preference: metric, us_customary, imperial, or mixed",
    )
    parser.add_argument("--stock-precision", default="approximate")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    target = Path(args.path).expanduser().resolve()
    skill_root = Path(__file__).resolve().parent.parent
    if target == skill_root or skill_root in target.parents:
        raise SystemExit(
            "Destination must be outside the installed skill directory: "
            f"{skill_root}"
        )
    if target.exists() and not target.is_dir():
        raise SystemExit(f"Destination is not a directory: {target}")
    if not STARTER.is_dir():
        raise SystemExit(f"Bundled starter is missing: {STARTER}")

    source_files = sorted(path for path in STARTER.rglob("*") if path.is_file())
    created: list[str] = []
    kept: list[str] = []
    stamp = local_timestamp()

    for source in source_files:
        relative = source.relative_to(STARTER)
        destination = target / relative
        if destination.exists():
            kept.append(relative.as_posix())
            continue
        created.append(relative.as_posix())
        if args.dry_run:
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix.lower() == ".md":
            source_text = source.read_text(encoding="utf-8")
            destination.write_text(
                render(
                    source_text,
                    owner=args.owner,
                    market_region=args.market_region,
                    locale=args.locale,
                    currency=args.currency,
                    measurement_system=args.measurement_system,
                    precision=args.stock_precision,
                    stamp=stamp,
                ),
                encoding="utf-8",
                newline="\n",
            )
        else:
            shutil.copy2(source, destination)

    if not args.dry_run:
        (target / "history").mkdir(parents=True, exist_ok=True)

    warnings: list[str] = []
    if not args.market_region:
        warnings.append("market_region_not_set")
    if not args.currency:
        warnings.append("currency_not_set")
    if not args.measurement_system:
        warnings.append("measurement_system_not_set")

    result = {
        "status": "dry_run" if args.dry_run else "initialized",
        "path": str(target),
        "created": created,
        "kept_existing": kept,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
