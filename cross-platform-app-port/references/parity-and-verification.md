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
