#!/usr/bin/env python3
"""Weirdest Job Title entry: writes a single job title to /output/entry.txt."""

import os

TITLE = "Senior Vice President of Apologizing to Geese"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)
    print(TITLE)


if __name__ == "__main__":
    main()
