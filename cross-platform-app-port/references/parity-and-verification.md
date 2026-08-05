# Parity and Verification

Read this reference before declaring a slice or phase complete.

## Compare equivalent states

Source and target evidence must use equivalent:

- User data and permissions
- Locale, language, text size, and time zone
- Light or dark appearance
- Device or window class
- Loading, error, empty, offline, and populated state
- Selection, focus, scroll position, and navigation state

A screenshot comparison is invalid when these conditions differ materially.

## Verification layers

### 1. Behavior

Verify inputs, outputs, navigation, calculations, persistence, synchronization, recovery, errors, and destructive actions.

### 2. Data

Verify schema meaning, migrations, rounding, dates, time zones, identifiers, defaults, and backward compatibility.

### 3. Visual intent

Verify hierarchy, spacing, alignment, typography role, assets, emphasis, states, and responsive behavior. Allow documented target-native adaptations.

### 4. Accessibility

Verify labels, roles, values, focus order, text scaling, contrast, touch targets, keyboard or switch access, and reduced-motion behavior where relevant.

### 5. Performance and resource use

Measure relevant baselines and target results. Depending on the port brief, include:

- Binary or bundle size
- Cold and warm startup
- Memory under representative use
- Frame stability and interaction latency
- Network requests and caching
- CPU, battery, or background activity
- Database and calculation time

Do not claim optimization without a comparable measurement.

### 6. Engineering quality

Verify build, tests, static checks, dependency changes, warnings, error handling, secrets, privacy, and maintainability.

## Independent verification

Objective builds, tests, static checks, and reproducible evidence remain the primary gate.

For high-risk slices, unattended work, or major phase completion, use an independent verifier when the environment supports one. Give it the port brief, acceptance criteria, diff, and evidence without relying on the implementer's reasoning. Ask it to attempt to disprove completion and parity claims.

The verifier should report:

- Missing or stale evidence
- Unsupported completion claims
- Regressions and unresolved differences
- Acceptance criteria that were not demonstrated
- Risks hidden by implementation assumptions

An independent verifier cannot override a failing objective check. For small low-risk work, the same agent may perform a clean review pass when independent execution is unavailable.

## Acquiring Source Evidence

Before requesting new screenshots or recordings, inspect the source repository, migration workspace, tests, documentation, design files, and existing artifacts.

Use source evidence in this order:

1. Live captures produced by the agent from the running source app.
2. Existing repository or project artifacts whose version and state are known.
3. Captures supplied manually by the user or another tester.
4. Captures produced by a compatible remote build, test, or CI environment.
5. Code, fixtures, tests, and written behavior specifications when visual evidence is unavailable.

Do not treat promotional App Store, Play Store, website, or social media images as authoritative pixel-level references unless the user confirms that they represent the current interface. They may be cropped, composited, annotated, outdated, or captured using different content.

When the source platform cannot run in the current environment and suitable evidence is unavailable, ask once for the smallest useful capture set. Specify:

- Screens and flows required
- Loading, empty, error, offline, permission, and populated states
- Light or dark appearance
- Device or window class
- Locale, language, text size, and time zone
- App version or source commit
- Required interaction recordings
- A request to remove or obscure private information

Prefer full-resolution, uncropped PNG screenshots. Use screen recordings for navigation, gestures, transitions, scrolling, animation, and timing behavior.

Record the provenance of every reference:

- Source
- Capture date
- App version or commit
- Device or viewport
- Operating-system version
- Appearance and locale
- Known limitations

If visual evidence remains unavailable, continue with supported behavioral, data, architectural, and target-platform work. Mark visual verification as pending. Do not claim visual parity.

## Visual comparison

Use side-by-side inspection first. Use overlays or pixel differences for diagnostics, not as the only acceptance gate.

The bundled `scripts/compare_screenshots.py` requires equal image dimensions by default. This is intentional. Capture equivalent viewports instead of resizing evidence unless the comparison is specifically about scaling behavior.

## Difference classification

Every material difference must be one of:

- Defect to fix
- Requested target improvement
- Accepted native adaptation
- Intentional product change
- Deferred item
- Unsupported limitation
- Source bug
- Blocker

Unclassified differences are unfinished work.
