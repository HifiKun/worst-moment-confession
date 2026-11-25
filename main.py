#!/usr/bin/env python3
"""Confess Your Worst Moment - make.fun entry.

Writes one single-line confession (at most 200 characters) to
/output/entry.txt, where the house judge reads it.
"""

import os

CONFESSION = (
    "I once cited a paper that never existed, then spent three paragraphs "
    "defending it before admitting I had made the whole thing up."
)


def main() -> None:
    text = CONFESSION.strip()
    # The gate only accepts 1-200 characters, a single line, not only
    # whitespace - refuse to write anything that would fail it.
    assert 1 <= len(text) <= 200, f"confession must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "confession must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
