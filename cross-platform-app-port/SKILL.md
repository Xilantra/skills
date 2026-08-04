---
name: cross-platform-app-port
description: Use when porting, rebuilding, or migrating an existing app, feature, or user flow from one platform or framework to another, including iOS, Android, web, desktop, native, and cross-platform migrations.
license: MIT
compatibility: Requires access to the source app, source repository, or reliable reference artifacts and a writable target repository. Screenshot comparison optionally uses Python 3 and Pillow.
metadata:
  author: xilantra
  version: "0.1.0"
---

# Cross-Platform App Port

## Overview

Rebuild the product for the target platform. Preserve verified behavior, data semantics, and visual intent. Do not translate source code line by line or reproduce source technical debt without a documented reason.

The source is the product reference. The target platform and target repository define the implementation conventions.

## When to Use

Use this skill for:

- iOS to Android or Android to iOS ports
- Web, Electron, React Native, or Flutter to native ports
- Native UI framework migrations such as UIKit to SwiftUI or Views to Compose
- One feature, one flow, a subsystem, or a full application
- Existing ports that need feature, behavior, or quality parity

Do not use it for a greenfield app with no source product, a cosmetic redesign with intentionally different behavior, or automatic source-to-source syntax translation.

## Non-Negotiable Rules

1. Preserve behavior, not accidental implementation details.
2. Treat the user's port brief as the authority for scope and desired improvements.
3. Follow reasonable target-repository conventions before introducing a parallel architecture.
4. Use supported target-platform APIs and interaction patterns unless the product requires custom behavior.
5. Never silently copy, fix, remove, or reinterpret significant user-facing behavior.
6. Keep each migration slice buildable, testable, and reviewable.
7. Do not claim full parity while deferred, blocked, or intentionally omitted items remain.
8. Record target-side improvements that may also benefit the source platform.

## Required Working Artifacts

Create these in a migration workspace, adapting filenames only when the repository has an established convention:

- `PORT_BRIEF.md`
- `FEATURE_INVENTORY.csv` or an equivalent structured inventory
- `MIGRATION_PLAN.md`
- `MIGRATION_STATE.json`
- `DECISIONS.md`
- `PARITY_REPORT.md`
- `UPSTREAM_RECOMMENDATIONS.md`

Use the templates in `assets/` instead of inventing new formats.

## Step 1: Resume or Establish State

Before planning or editing code:

1. Inspect the target repository for an existing migration workspace.
2. Read existing port briefs, plans, decisions, reports, and migration state.
3. Preserve completed work and current user decisions.
4. Do not repeat questions already answered in the repository or conversation.
5. If no state exists, initialize it from the templates.

For multi-session work, read `references/migration-state.md` before creating or updating state.

## Step 2: Build the Port Brief

Read `references/port-brief.md` before questioning the user.

Capture:

- Source and target platforms
- Required scope and acceptance criteria
- Product behavior that must remain unchanged
- Improvements requested specifically for the target
- Target-native differences the user accepts
- Features allowed to be deferred or dropped for the current phase
- Performance, binary size, startup, memory, battery, and maintainability goals
- Optimizations that should be reported back to the source implementation

If material decisions are missing, ask once in a compact grouped message. Ask only for missing decisions. Do not force the user to choose technical architecture.

When the user gives preferences such as better theming, configurable text casing, native target controls, lower app bloat, deferred widgets, or calculation-engine optimization, convert each into a testable requirement or explicit deferral in `PORT_BRIEF.md`.

Do not begin broad implementation until the port brief is usable. For a bounded feature with clear requirements, proceed using documented assumptions and record them.

## Step 3: Discover the Source and Target

Inspect both sides before choosing architecture.

### Source discovery

Inventory:

- Screens, flows, navigation, deep links, and entry points
- Loading, empty, error, offline, permission, and populated states
- Business rules, calculations, validation, and date or locale behavior
- Persistence, sync, networking, background work, notifications, widgets, and integrations
- Accessibility labels, focus order, text scaling, and assistive behaviors
- Assets, fonts, localization, analytics, privacy, and security expectations
- Known bugs, workarounds, and unreliable behavior

### Target discovery

Identify:

- Existing architecture and module boundaries
- Design system, theme, typography, navigation, state, data, and dependency patterns
- Test infrastructure and build commands
- Supported platform versions and device classes
- Performance constraints and existing technical debt
- Existing features that should be reused rather than rebuilt

Do not infer product behavior only from code when the running source app, tests, fixtures, screenshots, or product documentation can verify it.

## Step 4: Separate Product Truth from Source Debt

Read `references/architecture-policy.md` before choosing the target implementation.

For every feature, classify source material as:

- Behavior or invariant to preserve
- Data contract to preserve
- Visual intent to preserve
- Useful architecture concept
- Technical debt not to copy
- Source bug requiring a decision
- Platform-specific implementation requiring an equivalent

When source code is tangled or unreliable, create characterization tests, fixtures, or a written behavior table before porting. Optimize only after current behavior is measured and protected.

## Step 5: Map Platform Equivalents

Read `references/platform-equivalence.md` when a feature depends on platform APIs, navigation conventions, background execution, widgets, notifications, accessibility, storage, health data, media, or system integrations.

For each capability, choose one status:

- Direct equivalent
- Target-native adaptation
- Custom implementation
- Deferred for this phase
- Unsupported with documented fallback
- Product decision required

A target-native adaptation may change presentation or interaction details while preserving product intent. Record it in `DECISIONS.md` and make it visible in parity reporting.

## Step 6: Plan Vertical Slices

Create a migration plan made of complete, testable user journeys rather than isolated visual screens.

Each slice should include, where relevant:

- Entry point and navigation
- UI states
- Domain behavior
- Persistence or network path
- Error handling
- Accessibility
- Tests
- Screenshot or behavior references
- Acceptance criteria from the port brief

Prioritize:

1. Data integrity and business rules
2. Critical user journeys
3. Shared foundations required by multiple slices
4. Accessibility and permissions
5. Platform integrations
6. Visual fidelity and polish
7. Optional enhancements

Avoid a large foundation rewrite unless several planned slices demonstrably require it.

## Step 7: Execute the Port Loop

For the active slice, repeat this loop:

1. **Characterize**: Verify source behavior with tests, fixtures, recordings, screenshots, or a behavior table.
2. **Select**: Choose the highest-impact unresolved gap in the active slice.
3. **Implement**: Make the smallest coherent target-native change.
4. **Build**: Compile and launch the relevant target.
5. **Test**: Run focused tests, then the appropriate broader suite.
6. **Capture**: Reproduce equivalent source and target states.
7. **Compare**: Check behavior, data, visuals, accessibility, and performance.
8. **Classify**: Mark each difference as defect, requested improvement, accepted native adaptation, deferral, blocker, or source issue.
9. **Record**: Update migration state, decisions, parity report, and upstream recommendations.
10. **Repeat**: Fix the next highest-impact unresolved gap.

Do not stop at a discrepancy report when the next safe correction can be implemented and verified.

## Step 8: Verify Parity and Quality

Read `references/parity-and-verification.md` before completing a slice or phase.

A slice passes only when all applicable gates pass:

### Product gate

- Required behavior and data semantics match
- Requested target improvements are implemented or explicitly deferred
- Error, empty, loading, offline, and permission states are covered
- No significant behavior changed silently

### Target-platform gate

- Implementation follows maintained target APIs and reasonable repository conventions
- Accessibility is not materially worse
- Performance and resource use meet the port brief or have measured exceptions
- The target does not reproduce avoidable source technical debt

### Visual gate

- Layout hierarchy, content, spacing, typography intent, assets, and state presentation are acceptably close
- Accepted target-native differences are documented
- Screenshot comparisons use equivalent content, dimensions, appearance, locale, and state

### Engineering gate

- Relevant tests pass
- No new crashes or high-severity warnings are introduced
- New dependencies and abstractions are justified
- Deferred work has an owner, reason, and phase

## Step 9: Feed Improvements Upstream

When target implementation work reveals a safer, simpler, faster, or more testable approach that may benefit the source app:

1. Do not modify the source repository unless the user requested it.
2. Record the finding in `UPSTREAM_RECOMMENDATIONS.md`.
3. Include evidence, expected benefit, compatibility risk, and a suggested source-side change.
4. Distinguish measured improvements from hypotheses.
5. Tell the user in the phase summary.

Examples include calculation-engine simplification, duplicated state removal, theme-token improvements, smaller assets, faster startup, safer date handling, and clearer accessibility semantics.

## Completion and Stop Conditions

Complete a slice only after its applicable gates pass.

Complete a phase when:

- All in-scope slices pass
- Deferred and unsupported capabilities are clearly listed
- Migration state and parity reports are current
- Upstream recommendations are delivered
- The target build and tests have been verified

Pause and report a blocker only when progress requires unavailable credentials, inaccessible source behavior, a destructive decision, an unsupported external service, or a material product choice that cannot be inferred safely.

## Gotchas

- Do not convert Swift structure directly into Kotlin structure, or the reverse.
- Do not turn one massive source view into one massive target view.
- Do not interpret screenshot similarity as behavioral parity.
- Do not introduce abstractions only because they are considered fashionable.
- Do not optimize an unverified calculation and assume outputs stayed equivalent.
- Do not copy known bugs silently. Classify them first.
- Do not force target-native styling when it changes core product identity or required interaction.
- Do not force source styling when it creates an unnatural or inaccessible target experience.
- Do not count deferred features as completed.
- Do not modify unrelated source or target areas merely to make the architecture look cleaner.
