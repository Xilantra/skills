# Platform Equivalence

Read this reference when source behavior depends on platform APIs or conventions.

## Equivalence levels

| Level | Meaning |
|---|---|
| Direct equivalent | The target offers a supported capability with substantially equivalent behavior. |
| Native adaptation | Product intent remains, but target interaction or presentation follows target conventions. |
| Custom implementation | No sufficient native equivalent exists and the feature is important enough to build. |
| Deferred | The user intentionally excludes it from the current phase. |
| Unsupported fallback | The target cannot provide full capability, so a documented reduced experience is used. |
| Decision required | Product intent is unclear or trade-offs are material. |

## Mapping checklist

For each platform-specific capability, record:

- User need being served
- Source API or convention
- Target equivalent or adaptation
- Lifecycle and background limitations
- Permission model
- Privacy and data implications
- Accessibility behavior
- Offline behavior
- Test strategy
- Phase status

## Common categories

Review these categories instead of focusing only on visible screens:

- Navigation, back behavior, sheets, dialogs, and menus
- App lifecycle and state restoration
- Background work, alarms, scheduled work, and push notifications
- Widgets, live surfaces, quick controls, and lock-screen experiences
- Health, location, media, contacts, files, and system accounts
- Secure storage, cloud sync, backups, and cross-device state
- Typography, system icons, haptics, motion, and gestures
- VoiceOver, TalkBack, keyboard, pointer, switch, and text scaling
- Deep links, app links, universal links, and share extensions

## Native adaptation rule

A native adaptation is acceptable when it:

- Preserves the user's task and information hierarchy
- Does not weaken required behavior or privacy
- Is documented in the port brief or decisions log
- Is validated with target-platform users or conventions when feasible
- Does not become an excuse to omit difficult behavior

Layout similarity does not require forcing source-platform controls onto the target. Product identity does not require reproducing every source-platform convention.
