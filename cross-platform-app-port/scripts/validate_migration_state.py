#!/usr/bin/env python3
"""Validate a MIGRATION_STATE.json file without external dependencies."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ALLOWED_STATUSES = {
    "planned",
    "in_progress",
    "verification",
    "completed",
    "deferred",
    "blocked",
    "unsupported",
}


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "MIGRATION_STATE.json")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: File not found: {path}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"ERROR: Invalid JSON: {exc}", file=sys.stderr)
        return 1

    errors: list[str] = []
    for key in ("schema_version", "project", "slices", "summary"):
        if key not in data:
            errors.append(f"Missing top-level key: {key}")

    slices = data.get("slices", [])
    if not isinstance(slices, list):
        errors.append("`slices` must be a list")
        slices = []

    seen: set[str] = set()
    counts = {status: 0 for status in ALLOWED_STATUSES}
    in_scope_total = 0

    for index, item in enumerate(slices):
        label = f"slices[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{label} must be an object")
            continue
        slice_id = item.get("id")
        if not slice_id:
            errors.append(f"{label} is missing `id`")
        elif slice_id in seen:
            errors.append(f"Duplicate slice id: {slice_id}")
        else:
            seen.add(slice_id)

        status = item.get("status")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{label} has invalid status: {status!r}")
        else:
            counts[status] += 1

        if item.get("in_scope", True):
            in_scope_total += 1

        if status == "completed":
            evidence = item.get("evidence") or {}
            evidence_count = sum(len(evidence.get(key, [])) for key in ("tests", "screenshots", "commits", "reports"))
            if evidence_count == 0:
                errors.append(f"{label} is completed but has no evidence")

        if status == "blocked" and not item.get("blocker"):
            errors.append(f"{label} is blocked but has no blocker description")

    active = data.get("active_slice_id")
    if active is not None and active not in seen:
        errors.append(f"active_slice_id references unknown slice: {active}")

    summary = data.get("summary") or {}
    expected = {
        "in_scope_total": in_scope_total,
        "completed": counts["completed"],
        "deferred": counts["deferred"],
        "blocked": counts["blocked"],
        "unsupported": counts["unsupported"],
    }
    for key, value in expected.items():
        if summary.get(key) != value:
            errors.append(f"summary.{key} is {summary.get(key)!r}; expected {value}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Valid migration state: {len(slices)} slice(s), {in_scope_total} in scope.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
