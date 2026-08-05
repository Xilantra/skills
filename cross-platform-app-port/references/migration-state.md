# Migration State

Read this reference when work spans multiple slices, branches, agents, sessions, or bounded execution loops.

## Purpose

`MIGRATION_STATE.json` is the machine-readable record of scope and progress. Narrative documents explain decisions; migration state answers what is active, done, deferred, blocked, next, and why execution stopped.

## Required practices

- Use stable slice IDs.
- Keep status values from the template.
- Record evidence paths for completed work.
- Bind completed evidence to the exact target commit and verification timestamp.
- Separate `deferred` from `completed`.
- Record blockers with the smallest requirement needed to resume.
- Update state after every verified iteration, not only at the end of a session.
- Never erase historical decisions or terminal reasons to make progress appear cleaner.

## Run control

The optional `run_control` object distinguishes ordinary interactive work from explicitly bounded autonomous execution.

### Modes

- `interactive`: default; return control when material decisions, unavailable dependencies, or human gates are reached.
- `bounded_loop`: continue independently only within recorded hard limits and objective verification gates.

A bounded loop must record at least one limit:

- `max_iterations_per_slice`
- `max_elapsed_minutes`
- `budget_note` describing another enforceable runtime, token, credit, or cost limit

Track `iterations_used`, `started_at`, and the final `terminal_reason`.

Allowed terminal reasons:

- `verified`
- `blocked`
- `human_review_required`
- `budget_exhausted`
- `iteration_limit_reached`
- `cancelled`

Read `loop-control.md` before starting unattended or multi-agent execution.

## Status model

- `planned`
- `in_progress`
- `verification`
- `completed`
- `deferred`
- `blocked`
- `unsupported`

## Completion evidence

A completed slice must have reproducible evidence and identify:

- `target_commit`: the exact target code state verified
- `verified_at`: when verification completed
- `source_commit`: the source reference when one is available
- Relevant tests, screenshots, commits, or reports

If the target changes after verification, move the slice back to `verification` or `in_progress` until the required checks pass again.

## Progress calculation

Calculate phase completion only from in-scope slices. Deferred, blocked, and unsupported slices remain visible and must not count as completed.

## Resume procedure

1. Validate the state file with `scripts/validate_migration_state.py`.
2. Read the active slice, latest iteration, run controls, and terminal reason.
3. Verify that referenced branches, commits, files, builds, and screenshots still exist.
4. Confirm that configured limits still apply before resetting counters or starting another bounded run.
5. Re-run the smallest relevant verification before continuing.
6. Select the highest-priority unresolved item from the active slice.

Do not trust a stale `completed` status when its evidence cannot be reproduced against the recorded target commit.
