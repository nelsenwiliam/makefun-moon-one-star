"""The Moon Gets One Star - make.fun bounty entry.

Writes a single one-star review of the Moon (120 characters or fewer)
to /output/entry.txt. Pure standard library only.

The review: the Moon produces no light of its own - it only reflects
the Sun's and takes the credit. A specific, Moon-only grievance, not
the obvious crater / cheese / brightness jokes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120

REVIEW = (
    "One star. Doesn't even make its own light \u2014 just bounces the Sun's "
    "and takes the credit. Sky's biggest plagiarist."
)


def main() -> None:
    # The sealed scorer requires 1-120 characters of non-blank UTF-8 text.
    assert 1 <= len(REVIEW) <= MAX_CHARS, f"review is {len(REVIEW)} chars"
    assert REVIEW.strip(), "review must not be blank"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file must hold exactly the review text.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
