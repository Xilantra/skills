# Architecture Policy

Read this reference before choosing or changing target architecture.

## Principle

The source application defines product behavior, not the required internal structure. The target implementation should use the simplest architecture that preserves verified behavior, fits the target repository, supports testing, and uses maintained platform APIs.

## Assessment

For each slice, document:

- Source responsibilities and dependencies
- Behavior and invariants that must remain
- Source coupling, duplication, obsolete APIs, and platform workarounds
- Existing target conventions and reusable foundations
- Proposed target boundaries
- Why each new abstraction is necessary now
- Migration and rollback risk

Use `assets/ARCHITECTURE_DECISION.template.md` for material decisions.

## When to improve architecture

Improve the design during the port when at least one is true:

- Literal translation would reproduce a known defect or dangerous coupling
- Business rules cannot be tested in their current shape
- Target-platform lifecycle or concurrency rules require separation
- Several planned slices need the same stable boundary
- The current target code would create a clear maintenance or performance problem

## When not to rewrite

Do not launch a broad rewrite merely because:

- A different pattern is more fashionable
- The source is untidy but behavior is stable and isolated
- The current slice does not need the proposed foundation
- The change cannot be validated incrementally
- The user asked for a port, not a general cleanup project

## Characterization before optimization

Before changing calculations, state machines, synchronization, date handling, or other business logic:

1. Collect representative inputs and outputs.
2. Add fixtures or characterization tests.
3. Include boundary, locale, time-zone, offline, and invalid-data cases where relevant.
4. Run the baseline and preserve evidence.
5. Implement the target version.
6. Compare outputs.
7. Optimize only after equivalence is established.
8. Record differences and upstream recommendations.

## Source bugs

Classify every discovered source bug:

- `compatibility-required`: Users or stored data depend on it for now
- `safe-to-fix`: The intended behavior is clear and risk is bounded
- `product-decision`: Several reasonable outcomes exist
- `uncertain`: Evidence is insufficient

Do not silently preserve or silently fix a significant bug.
