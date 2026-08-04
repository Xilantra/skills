# Example Port Brief: iOS to Android

## Product Goal

Create an Android version that preserves the existing app's information architecture, user journeys, calculations, and calm visual identity while using appropriate Android conventions and a maintainable Android implementation.

## Required Parity

- Core layouts and information hierarchy should remain recognizably the same.
- Business rules and calculation outputs must remain equivalent for the same inputs.
- Existing supported locales and content must be preserved.

## Requested Target Improvements

| ID | Improvement | Observable acceptance criteria | Priority |
|---|---|---|---|
| IMP-001 | Configurable text casing | Representative labels can render normal case. Lowercase is not globally hardcoded in components or content processing. | Must |
| IMP-002 | Stronger theme system | Every supported color family defines semantic light and dark tokens, and core screens pass contrast checks in both appearances. | Must |
| IMP-003 | Lower bloat | Dependencies and assets are audited. App size, startup, and memory are measured and material regressions are justified. | Must |
| IMP-004 | Calculation-engine optimization | Existing outputs are protected by fixtures. Any optimization is benchmarked and documented for possible adoption by the source app. | Should |

## Accepted Target-Native Adaptations

| ID | Source behavior or UI | Allowed target adaptation | Product intent that must remain |
|---|---|---|---|
| ADAPT-001 | iOS-styled controls and transitions | Use suitable Android-native controls, navigation, back behavior, sheets, and system surfaces. | Same task flow, hierarchy, content, and product identity. |

## Deferred for This Phase

| ID | Capability | Status | Reason | Revisit phase |
|---|---|---|---|---|
| DEF-001 | Home-screen widgets | Deferred | Focus this phase on the main application. | Phase 2 |
| DEF-002 | System quick controls or source-platform Control Center equivalents | Deferred | Requires separate platform integration design. | Phase 2 |

## Source Feedback Requested

When the Android port reveals a safer, simpler, faster, or more testable calculation or architecture, record evidence and a suggested source-side improvement instead of changing the source silently.
