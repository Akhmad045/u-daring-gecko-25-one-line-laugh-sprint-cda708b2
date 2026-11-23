#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Assembles a single original funny line (1-200 chars) and writes it
to /output/entry.txt.
"""

import os

LINES = [
    "My phone sends me a weekly screen-time report like a disappointed parent — except Mum at least pretends to love me.",
]

LINE = LINES[0]


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"OK: {len(LINE)} chars")
    print(LINE)


if __name__ == "__main__":
    main()
