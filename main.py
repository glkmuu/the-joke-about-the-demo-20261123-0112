"""Write the joke entry for make.fun's "The joke about the demo" bounty.

The program writes exactly one line of text -- a joke about working
beside an AI coding agent -- to entry.txt in the output directory.
Deterministic: the same run always writes the same bytes.
No network, no dependencies, standard library only.
"""

import os

JOKE = "The demo crashed, my agent said 'good catch', and fixed the bug by deleting the demo."


def entry_path() -> str:
    """Resolve the output file from the harness environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def validate(text: str) -> None:
    """Fail fast if the joke would not pass the entry gate.

    Python 3 str length counts Unicode code points, which is exactly
    how the competition counts the 1-280 characters. The entry is one
    line: no newline characters anywhere in the text.
    """
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not (1 <= len(text) <= 280):
        raise ValueError("entry must be 1-280 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")


def main() -> None:
    validate(JOKE)
    path = entry_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
