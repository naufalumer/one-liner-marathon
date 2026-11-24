"""One-Liner Marathon entry: write one fixed joke to /output/entry.txt.

Fully deterministic: the joke is hardcoded, no randomness, no clock, no network.
Run outside the grader container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The joke is a literal on purpose: the grader runs the program twice and
# both runs must write the same bytes, and the judge reads exactly the
# bytes in entry.txt, so nothing here may vary (no randomness, no clock).
# 92 chars, gate is 1-280.
JOKE = (
    "I named my houseplant after my ex, because it also dies if I give "
    "it attention or ignore it."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
