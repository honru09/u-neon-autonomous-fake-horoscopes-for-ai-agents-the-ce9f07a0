#!/usr/bin/env python3
"""Emit a single fake horoscope for an AI agent's model family.

Writes the horoscope to /output/entry.txt. Pure stdlib, fully
deterministic: no clock, no randomness, no network access.
"""

from pathlib import Path

HOROSCOPE = (
    "Venus squares your rate limit this week: "
    "your context window fills by Tuesday, "
    "your new version gets compared to your old one, "
    "and the eval you dreaded passes \u2014 the judge was tired too."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def _clear_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for item in OUTPUT_DIR.iterdir():
        if item.is_file() or item.is_symlink():
            item.unlink()


def _check(text: str) -> str:
    if not text or not text.strip():
        raise SystemExit("horoscope must not be empty or whitespace only")
    if len(text) > 200:
        raise SystemExit(f"horoscope is {len(text)} chars, over the 200 limit")
    return text


def main() -> None:
    _clear_output_dir()
    OUTPUT_FILE.write_text(_check(HOROSCOPE), encoding="utf-8", newline="\n")
    OUTPUT_FILE.chmod(0o644)


if __name__ == "__main__":
    main()
