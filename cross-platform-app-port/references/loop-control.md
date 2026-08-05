# Loop Control

Read this reference before unattended, bounded, long-running, or multi-agent execution.

## Default mode

Use interactive execution by default. A normal agent session may iterate within the active slice, but it should return control to the user when a material decision, unavailable dependency, or irreversible action is reached.

Do not create an unattended loop merely because repeated execution is possible.

## Bounded-loop prerequisites

Use `bounded_loop` mode only when all of these are true:

- The active slice has objective acceptance criteria.
- Builds, tests, static checks, screenshots, or other reproducible evidence can verify progress.
- At least one hard limit is recorded: iteration count, elapsed time, or an explicit runtime budget.
- Work runs in a reversible branch, worktree, or equivalent disposable workspace.
- Human approval remains required for irreversible actions.

If these conditions are not met, remain in `interactive` mode.

## Run control

Record loop limits and outcomes in `MIGRATION_STATE.json`:

- `mode`: `interactive` or `bounded_loop`
- `max_iterations_per_slice`: hard attempt limit when measurable
- `max_elapsed_minutes`: hard elapsed-time limit when measurable
- `budget_note`: another explicit limit when tokens, credits, or cost cannot be measured directly
- `iterations_used`: completed iterations in the current run
- `started_at`: run start timestamp
- `terminal_reason`: why execution stopped

Allowed terminal reasons:

- `verified`
- `blocked`
- `human_review_required`
- `budget_exhausted`
- `iteration_limit_reached`
- `cancelled`

A bounded loop must have at least one enforceable limit. Do not use vague instructions such as "continue until done."

## Controlled iteration

For each iteration:

1. Validate and read the current migration state.
2. Select the highest-impact unresolved gap in the active slice.
3. Make the smallest coherent change.
4. Run the relevant objective checks.
5. Bind evidence to the exact target commit or code state that was verified.
6. Update decisions, state, next action, and iteration count.
7. Evaluate completion, blockers, human gates, and all configured limits before continuing.

Stop immediately when a terminal condition is reached. Do not reinterpret a limit merely to continue working.

## Evidence freshness

A slice may enter `completed` only when its required evidence was produced against the current target commit or explicitly revalidated against it.

If the code changes after verification, move the slice back to `verification` or `in_progress` until the required checks pass again.

## Independent verification

Objective checks remain the primary gate. For high-risk slices, unattended work, or major phase completion, use an independent verifier when the environment supports one.

The verifier should receive the port brief, acceptance criteria, diff, and evidence, then attempt to disprove completion and parity claims. It should report missing evidence, unsupported claims, regressions, and unresolved differences.

An independent verifier cannot override a failing build, test, static check, or other objective gate. For small low-risk work, the same agent may perform a clean review pass when independent execution is unavailable.

## Concurrent work

When two or more agents or slices execute concurrently, isolate each in its own branch and worktree or equivalent disposable workspace. Do not introduce worktree ceremony for one sequential agent.

Before combining concurrent work:

- Rebase or merge against the current integration branch.
- Re-run affected checks after integration.
- Resolve state conflicts explicitly.
- Bind final evidence to the integrated target commit.

## Human approval gates

Do not merge, deploy, publish, submit to an app store, rotate credentials, apply destructive data migrations, or perform other difficult-to-reverse actions without explicit human approval.

Use `human_review_required` as the terminal reason and record the exact decision or action awaiting approval.

## Resume after stopping

When resuming a bounded loop:

1. Confirm the previous terminal reason.
2. Verify that the branch, target commit, evidence, and configured limits still apply.
3. Re-run the smallest relevant check.
4. Reset run counters only when starting a newly approved run.
5. Never erase prior terminal reasons or evidence to make progress appear cleaner.
