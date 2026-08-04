#!/usr/bin/env python3
"""Compare two screenshots and write an amplified visual diff plus JSON metrics.

Dependency: Pillow
Install with: python -m pip install Pillow
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageEnhance
except ImportError:
    print(
        "ERROR: Pillow is required. Install it with `python -m pip install Pillow`.",
        file=sys.stderr,
    )
    raise SystemExit(2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path)
    parser.add_argument("target", type=Path)
    parser.add_argument("--output", type=Path, default=Path("screenshot-diff.png"))
    parser.add_argument("--report", type=Path, default=Path("screenshot-diff.json"))
    parser.add_argument(
        "--threshold",
        type=int,
        default=0,
        choices=range(0, 256),
        metavar="0-255",
        help="Ignore per-channel differences at or below this value.",
    )
    parser.add_argument(
        "--amplify",
        type=float,
        default=4.0,
        help="Contrast multiplier for the saved diagnostic diff.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        reference = Image.open(args.reference).convert("RGBA")
        target = Image.open(args.target).convert("RGBA")
    except FileNotFoundError as exc:
        print(f"ERROR: File not found: {exc.filename}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"ERROR: Could not read image: {exc}", file=sys.stderr)
        return 1

    if reference.size != target.size:
        print(
            "ERROR: Image dimensions differ. Capture equivalent viewports instead of "
            f"resizing evidence: reference={reference.size}, target={target.size}",
            file=sys.stderr,
        )
        return 1

    raw_diff = ImageChops.difference(reference, target)
    if args.threshold:
        diff = raw_diff.point(lambda value: 0 if value <= args.threshold else value)
    else:
        diff = raw_diff

    width, height = diff.size
    total_pixels = width * height
    changed_pixels = 0
    max_channel_delta = 0

    pixels = diff.load()
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            if any(pixel):
                changed_pixels += 1
                max_channel_delta = max(max_channel_delta, *pixel)

    absolute_sum = 0
    channel_samples = total_pixels * 4
    for band in diff.split():
        histogram = band.histogram()
        absolute_sum += sum(value * count for value, count in enumerate(histogram))

    mean_absolute_error = absolute_sum / channel_samples if channel_samples else 0.0
    changed_ratio = changed_pixels / total_pixels if total_pixels else 0.0
    bbox = diff.getbbox()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    diagnostic = ImageEnhance.Contrast(diff).enhance(args.amplify)
    diagnostic.save(args.output)

    report = {
        "reference": str(args.reference),
        "target": str(args.target),
        "dimensions": {"width": width, "height": height},
        "threshold": args.threshold,
        "changed_pixels": changed_pixels,
        "total_pixels": total_pixels,
        "changed_pixel_ratio": changed_ratio,
        "mean_absolute_channel_error": mean_absolute_error,
        "max_channel_delta": max_channel_delta,
        "difference_bounding_box": list(bbox) if bbox else None,
        "diagnostic_diff": str(args.output),
        "note": "Use these metrics as diagnostics alongside behavioral and human visual review.",
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
