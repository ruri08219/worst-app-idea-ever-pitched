"""BlinkSync -- the worst app idea ever pitched.

Writes the one-sentence pitch to /output/entry.txt.
Gate: UTF-8 text, 1-240 characters, not only whitespace.
Standard library only.
"""

import os

ENTRY = (
    "BlinkSync is the app that texts your houseplants goodnight every "
    "evening and charges $4.99 a month to read their replies, which arrive "
    "as photos of themselves, slightly wilted, captioned 'thriving'."
)

MAX_CHARS = 240


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Revision: read the file back and prove the written bytes are the
    # entry exactly -- a silent truncation must fail loudly, not ship.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("entry.txt does not match ENTRY after write")


if __name__ == "__main__":
    main()
