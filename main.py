#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast of a smart fridge (max 200 chars) to /output/entry.txt.
"""
import os

ENTRY = (
    "My smart fridge updated its firmware overnight; "
    "now the ice maker gives me one cube a day \u2014 "
    "the rest is a premium feature."
)


def main() -> None:
    text = ENTRY
    encoded = text.encode("utf-8")
    # Gate: UTF-8, 1-200 characters, not only whitespace.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)  # no trailing newline


if __name__ == "__main__":
    main()
