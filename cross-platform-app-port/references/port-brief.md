# Port Brief Guidance

Read this reference before asking the user for migration preferences.

## Purpose

The port brief separates six things that agents often mix together:

1. Required product parity
2. Requested target improvements
3. Accepted target-native differences
4. Deferred or omitted scope
5. Quality and performance goals
6. Findings to feed back to the source platform

Without this separation, an agent may copy unwanted limitations, remove features without agreement, or polish architecture while missing what the user actually cares about.

## Question policy

First inspect the conversation and repository for existing decisions. Ask only for missing decisions that materially change the plan.

Prefer one compact message such as:

> Before I plan the port, what should remain exact, what should improve on the target, which target-native differences are acceptable, and what can be deferred for this phase? Also mention any performance or architecture improvements you want reported back to the source app.

Do not ask the user to select patterns such as MVVM, Clean Architecture, Redux, coordinators, repositories, or dependency-injection frameworks unless they have an established technical preference. The agent should inspect the target repository and recommend the simplest justified design.

## Convert wishes into verifiable requirements

A user wish is not complete until it has an observable outcome.

| User wish | Better requirement |
|---|---|
| "Allow normal case" | Text casing is controlled by content or a documented style token, not globally hardcoded to lowercase. Verify representative labels in relevant locales. |
| "Better themes" | Every supported brand or accent color defines tested light and dark semantic tokens with sufficient contrast. |
| "Use Android style where suitable" | Preserve information architecture and task flow, but use documented Android-native controls and navigation where product behavior remains equivalent. |
| "Do not bloat the app" | Record baseline and target app size, startup, memory, and dependency changes. Justify regressions and remove unused assets or libraries. |
| "Drop widgets for this phase" | Mark widget and system-control integrations as deferred, exclude them from phase completion, and keep them visible in the roadmap. |
| "Optimize the engine" | Protect current outputs with fixtures or characterization tests, measure the improvement, and record an upstream recommendation for the source app. |

## Conflict rules

When preferences conflict, use this order unless the user states otherwise:

1. Data integrity and safety
2. Explicit user requirements
3. Verified product behavior
4. Accessibility
5. Target-platform support and maintainability
6. Performance and resource use
7. Visual fidelity
8. Optional polish

Surface any material trade-off instead of deciding silently.

## Default assumptions

When the user has not specified a preference and the decision is reversible:

- Preserve behavior and visual hierarchy
- Use target-native components where they do not change product intent
- Keep source feature scope unless it is impossible or clearly platform-specific
- Avoid new dependencies unless they provide clear value
- Measure before optimizing
- Record assumptions in the port brief
