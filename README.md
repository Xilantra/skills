# xilantra/skills

Reusable Agent Skills by Afiq Xilantra Azmi.

## Included skill

### `cross-platform-app-port`

Ports an existing app, feature, or user flow from one platform or framework to another while preserving verified product behavior and producing a maintainable, target-native implementation.

The skill supports workflows such as:

- iOS to Android
- Android to iOS
- Web to native mobile
- Electron to native desktop
- UIKit to SwiftUI
- Views to Jetpack Compose
- React Native or Flutter to native platforms

## Install this skill

```bash
npx skills add https://github.com/Xilantra/skills --skill cross-platform-app-port
```

## Install all Xilantra skills

```bash
npx skills add xilantra/skills
```

The Skills CLI installation pattern is documented by [skills.sh](https://skills.sh/).

## Validate

Run the bundled structural validator:

```bash
python cross-platform-app-port/scripts/validate_skill.py cross-platform-app-port
```

Then run the official Agent Skills reference validator when available:

```bash
skills-ref validate ./cross-platform-app-port
```

## Development status

Version `0.1.0` is an initial, source-backed release candidate. It includes realistic eval cases, but those agent evals must still be run with and without the skill against clean sessions before calling the skill proven.

## License

MIT. See [LICENSE](LICENSE).
