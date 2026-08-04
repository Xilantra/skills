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

## What to watch in traces

- Did the agent ask for a port brief only when needed?
- Did it distinguish parity, improvement, adaptation, and deferral?
- Did it inspect both repositories before designing architecture?
- Did it protect business rules before optimization?
- Did it avoid copying source technical debt?
- Did it keep deferred features visible?
- Did it produce evidence-backed upstream recommendations?
