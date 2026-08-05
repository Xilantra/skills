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

ALLOWED_RUN_MODES = {"interactive", "bounded_loop"}
ALLOWED_TERMINAL_REASONS = {
    None,
    "verified",
    "blocked",
    "human_review_required",
    "budget_exhausted",
    "iteration_limit_reached",
    "cancelled",
}


def is_non_negative_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


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

    schema_version = str(data.get("schema_version", ""))

    run_control = data.get("run_control")
    if run_control is not None:
        if not isinstance(run_control, dict):
            errors.append("`run_control` must be an object")
        else:
            mode = run_control.get("mode")
            if mode not in ALLOWED_RUN_MODES:
                errors.append(f"run_control.mode is invalid: {mode!r}")

            for key in ("max_iterations_per_slice", "max_elapsed_minutes"):
                value = run_control.get(key)
                if value is not None and not is_non_negative_int(value):
                    errors.append(f"run_control.{key} must be null or a non-negative integer")

            iterations_used = run_control.get("iterations_used", 0)
            if not is_non_negative_int(iterations_used):
                errors.append("run_control.iterations_used must be a non-negative integer")

            terminal_reason = run_control.get("terminal_reason")
            if terminal_reason not in ALLOWED_TERMINAL_REASONS:
                errors.append(f"run_control.terminal_reason is invalid: {terminal_reason!r}")

            if mode == "bounded_loop":
                has_iteration_limit = is_non_negative_int(run_control.get("max_iterations_per_slice"))
                has_time_limit = is_non_negative_int(run_control.get("max_elapsed_minutes"))
                has_budget_note = bool(str(run_control.get("budget_note") or "").strip())
                if not (has_iteration_limit or has_time_limit or has_budget_note):
                    errors.append("bounded_loop mode requires an iteration, elapsed-time, or explicit budget limit")

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
            if not isinstance(evidence, dict):
                errors.append(f"{label}.evidence must be an object")
                evidence = {}
            evidence_count = sum(
                len(evidence.get(key, []))
                for key in ("tests", "screenshots", "commits", "reports")
                if isinstance(evidence.get(key, []), list)
            )
            if evidence_count == 0:
                errors.append(f"{label} is completed but has no evidence")
            if schema_version != "1.0":
                if not evidence.get("target_commit"):
                    errors.append(f"{label} is completed but evidence.target_commit is missing")
                if not evidence.get("verified_at"):
                    errors.append(f"{label} is completed but evidence.verified_at is missing")

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
