# Skill Evals

The official Agent Skills guidance recommends realistic test cases with a prompt, expected output, optional input files, and observable assertions.

## Initial evaluation loop

For each case in `evals.json`:

1. Run once in a clean session without the skill.
2. Run once in a clean session with this skill.
3. Save outputs separately.
4. Grade every assertion using concrete evidence.
5. Compare missed requirements, unnecessary work, token use, and execution time.
6. Update the skill only for observed failures or waste.

The current package defines three realistic cases. They have not yet been executed, so no pass rate is claimed.

## Record every run

Create a dated result file such as `results/2026-08-04-codex.md` containing:

- Date and time zone
- Agent and model
- Skill commit SHA
- Tool and environment constraints
- Whether the run used the skill
- Prompt or eval case identifier
- Output location
- Pass or fail for every assertion
- Evidence for each judgment
- Token use and elapsed time when available
- Observed waste, ambiguity, or failure
- Changes made after the run

Do not average results across different models or materially different environments without showing the individual runs.

## Suggested result format

```markdown
# Eval Run: [agent/model] — [date]

- Skill commit:
- Environment:
- With skill: Yes / No
- Case:

## Assertions

| Assertion | Result | Evidence |
| --- | --- | --- |
| [Assertion text] | Pass / Fail / Partial | [Concrete output or trace reference] |

## Efficiency

- Tokens:
- Elapsed time:
- Unnecessary work:

## Findings

- [Observed strength or failure]

## Follow-up

- [Skill change, test change, or no change]
```

## What to watch in traces

- Did the agent scale artifacts to the job instead of generating unnecessary paperwork?
- Did it ask for a port brief only when needed?
- Did it distinguish parity, improvement, adaptation, and deferral?
- Did it inspect both repositories before designing architecture?
- Did it protect business rules before optimization?
- Did it avoid copying source technical debt?
- Did it keep deferred features visible?
- Did it produce evidence-backed upstream recommendations?
