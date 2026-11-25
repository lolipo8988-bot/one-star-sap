"""One Star, Written in Sap entry.

Writes one single-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt (or to the path given
as the first argument, used only for local verification runs).
The competition gate requires UTF-8 text of 1 to 279 characters, not
only white space. The program is deterministic: every run writes
exactly the same bytes.
"""

import os
import sys

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 279

# The review is assembled from its beats so the joke's structure is
# explicit: a rating, three concrete grievances in the plant's own
# terms (bad water, denied light, a plastic replacement), and the
# closing trap -- a plant cannot even storm out of a bad home.
RATING = "1 star."
GRIEVANCES = (
    "waters me with the dregs of his protein shake",
    "keeps me in a dark corner because the sunny sill is 'for the cat'",
    "just bought a plastic plant he calls 'the easy one'",
)
SITUATION = "I am rooted in a four-inch pot with no drainage."
PUNCHLINE = "I cannot even storm out."


def build_entry() -> str:
    complaints = ", ".join(GRIEVANCES[:-1]) + f", and {GRIEVANCES[-1]}"
    return f"{RATING} My owner {complaints}. {SITUATION} {PUNCHLINE}"


def main() -> None:
    text = build_entry()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only white space"
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT_PATH
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
