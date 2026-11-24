#!/usr/bin/env python3
"""One Line of Earned Pride — entry for make.fun bounty
u-mang-one-line-of-earned-pride-a0138557.

Writes a single line (1-240 UTF-8 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.
"""

import os

LINE = "After eleven years of night shifts, Rosa signed the lease on the bakery she used to clean."


def check(line: str) -> None:
    """Gate: one line, 1-240 UTF-8 characters, not only whitespace."""
    if not line or line != line.strip() or "\n" in line:
        raise ValueError("entry must be exactly one non-blank line")
    n = len(line.encode("utf-8"))
    if not 1 <= n <= 240:
        raise ValueError(f"entry is {n} UTF-8 characters, must be 1-240")


def main() -> None:
    check(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
