#!/usr/bin/env python3
"""Small structural validator for an Agent Skill package.

This is not a replacement for the official `skills-ref validate` command.
It checks the most important local constraints without external dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LOCAL_LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter is not closed")
    raw = text[4:end]
    body = text[end + 5 :]
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, body


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    skill_md = root / "SKILL.md"
    errors = 0
    warnings = 0

    if not skill_md.is_file():
        fail(f"Missing {skill_md}")
        return 1

    text = skill_md.read_text(encoding="utf-8")
    try:
        fields, body = parse_frontmatter(text)
    except ValueError as exc:
        fail(str(exc))
        return 1

    name = fields.get("name", "")
    description = fields.get("description", "")

    if not name:
        fail("Frontmatter requires `name`")
        errors += 1
    elif not NAME_RE.fullmatch(name):
        fail("`name` must use lowercase letters, numbers, and single hyphens")
        errors += 1
    elif len(name) > 64:
        fail("`name` exceeds 64 characters")
        errors += 1

    if name and root.name != name:
        fail(f"Directory name `{root.name}` does not match skill name `{name}`")
        errors += 1

    if not description:
        fail("Frontmatter requires `description`")
        errors += 1
    elif len(description) > 1024:
        fail("`description` exceeds 1024 characters")
        errors += 1

    line_count = len(text.splitlines())
    if line_count > 500:
        print(f"WARNING: SKILL.md has {line_count} lines; recommended maximum is 500")
        warnings += 1

    word_count = len(re.findall(r"\b\w+\b", body))
    if word_count > 4000:
        print(f"WARNING: SKILL.md body has about {word_count} words; review context cost")
        warnings += 1

    for match in LOCAL_LINK_RE.finditer(text):
        target = match.group(1).split("#", 1)[0]
        if not target:
            continue
        path = (root / target).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            fail(f"Local link escapes skill directory: {target}")
            errors += 1
            continue
        if not path.exists():
            fail(f"Broken local link: {target}")
            errors += 1

    for directory in ("references", "assets", "scripts"):
        path = root / directory
        if path.exists() and not path.is_dir():
            fail(f"{directory} must be a directory")
            errors += 1

    print(
        f"Checked {root}: {errors} error(s), {warnings} warning(s), "
        f"{line_count} SKILL.md lines."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
