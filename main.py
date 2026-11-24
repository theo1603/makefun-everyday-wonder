"""Everyday Wonder entry: write one sentence to /output/entry.txt.

The sentence is fixed and deterministic: a small everyday moment (a
thermal receipt fading to blank) turned at an angle the reader has not
met before. Python 3 standard library only, no network, no input.

Before writing, the program checks the entry against the scorer's gate
itself (UTF-8 text, 1 to 200 characters, not only white space, a single
sentence) and refuses to write anything that would fail it, so a future
edit to the sentence can never silently produce an invalid entry.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "The thermal receipt in my pocket faded to blank by evening, "
    "as if the day had already decided to forget what I bought."
)


def validate(entry: str) -> None:
    """Raise ValueError unless the entry passes the scorer's gate."""
    if not entry or not entry.strip():
        raise ValueError("entry is empty or only white space")
    if len(entry) > 200:
        raise ValueError(f"entry is {len(entry)} characters, over the 200 limit")
    if entry.strip() != entry:
        raise ValueError("entry has leading or trailing white space")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    # Exactly one sentence: one terminal period, at the end, and no other
    # sentence-ending punctuation inside.
    body = entry[:-1]
    if not entry.endswith("."):
        raise ValueError("entry must end with a period")
    if any(ch in body for ch in ".!?"):
        raise ValueError("entry must be a single sentence")
    entry.encode("utf-8")  # raises if not valid UTF-8 text


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
