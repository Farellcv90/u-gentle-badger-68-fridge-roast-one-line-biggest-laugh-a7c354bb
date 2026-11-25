#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast of a smart fridge (max 200 chars) to /output/entry.txt.

Angle: the joke is not that the fridge is smart — it is that an overnight
firmware update quietly turned the ice maker into a subscription. One cube a
day is free; the rest is a "premium feature". The punchline lands because it
is a rationing joke, not a smart-appliance joke: everyone has met a paid tier
hiding inside something they already own.

Why it dodges the clichés: most fridge roasts go for ordering groceries for
you ("it bought milk I didn't ask for") or watching you ("it judges my 2am
snacks"). This one never mentions groceries, diet, or surveillance. The
fridge is not creepy and it is not a bad shopper — it is a landlord charging
rent on ice. The em dash gives the reveal a beat: setup, pause, premium.
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
    # Gate (strengthened on revision): exactly one line — no embedded
    # newlines or carriage returns — and a UTF-8 byte-length bound so the
    # 200-char limit cannot be quietly stretched by multi-byte characters.
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(encoded) <= 400, (
        f"entry is {len(encoded)} UTF-8 bytes, must be 1-400"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)  # no trailing newline


if __name__ == "__main__":
    main()
