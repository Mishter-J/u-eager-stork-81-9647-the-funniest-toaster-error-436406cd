#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry (program/v1).

Writes one line, at most 120 characters, to /output/entry.txt:
the error message a kitchen toaster shows its owner.
"""

import os

ENTRY = 'FAULT 0xBREAD: "This bread has been toasted 4 times and is now legally charcoal." — Management (me).'

def validate(entry):
    """Self-check the entry against the competition gate before writing.

    Gate: /output/entry.txt must be UTF-8 text of 1-120 characters,
    not only white space. Raises ValueError with a clear message if
    any part of the gate fails, so a bad entry never reaches the file.
    """
    entry.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8
    if not (1 <= len(entry) <= 120):
        raise ValueError(
            f"entry length {len(entry)} chars is outside the 1-120 gate"
        )
    if not entry.strip():
        raise ValueError("entry is blank or only white space")

def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
