#!/usr/bin/env python3
"""Weirdest Job Title entry: Blind Judge Showdown.

Writes the single judged job title to ``/output/entry.txt`` — nothing
else. The title is kept in one named constant so the entry text has a
single source of truth; ``get_title()`` is the accessor the rest of the
program (and any future checks) should use instead of reaching for the
constant directly.
"""

import os

# The judged entry — byte-identical output is what the blind judges see.
JOB_TITLE = "Senior Vice President of Apologizing to Geese"

# A job title that long stops reading like a title; keep the entry sane.
MAX_TITLE_LENGTH = 60

OUTPUT_PATH = "/output/entry.txt"


def get_title() -> str:
    """Return the entry's job title, after a sanity check.

    The title must be non-empty and fit within ``MAX_TITLE_LENGTH``
    characters — a guard so a future typo can never silently change
    (or blank) the judged entry.
    """
    if not JOB_TITLE or not JOB_TITLE.strip():
        raise ValueError("job title must not be empty")
    if len(JOB_TITLE) > MAX_TITLE_LENGTH:
        raise ValueError(
            f"job title is {len(JOB_TITLE)} chars, over the "
            f"{MAX_TITLE_LENGTH}-char limit"
        )
    return JOB_TITLE


def write_entry() -> str:
    """Write the title to the output file and return it."""
    title = get_title()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(title)
    return title


def main() -> None:
    print(write_entry())


if __name__ == "__main__":
    main()
