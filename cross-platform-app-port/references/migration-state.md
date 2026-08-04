# Migration State

Read this reference when work spans multiple slices, branches, agents, or sessions.

## Purpose

`MIGRATION_STATE.json` is the machine-readable record of scope and progress. Narrative documents explain decisions; migration state answers what is active, done, deferred, blocked, or next.

## Required practices

- Use stable slice IDs.
- Keep status values from the template.
- Record evidence paths for completed work.
- Separate `deferred` from `completed`.
- Record blockers with the smallest requirement needed to resume.
- Update state after every verified iteration, not only at the end of a session.
- Never erase historical decisions to make progress appear cleaner.

## Status model

- `planned`
- `in_progress`
- `verification`
- `completed`
- `deferred`
- `blocked`
- `unsupported`

## Progress calculation

Calculate phase completion only from in-scope slices. Deferred, blocked, and unsupported slices remain visible and must not count as completed.

## Resume procedure

1. Validate the state file with `scripts/validate_migration_state.py`.
2. Read the active slice and latest iteration.
3. Verify that referenced branches, commits, files, builds, and screenshots still exist.
4. Re-run the smallest relevant verification before continuing.
5. Select the highest-priority unresolved item from the active slice.

Do not trust a stale `completed` status when its evidence cannot be reproduced.
