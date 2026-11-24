#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry (program/v1).

Writes one line, at most 120 characters, to /output/entry.txt:
the error message a kitchen toaster shows its owner.
"""

import os

ENTRY = 'FAULT 0xBREAD: "This bread has been toasted 4 times and is now legally charcoal." — Management (me).'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
