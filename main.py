"""The Production Database Apology — make.fun entry.

Writes one line: the apology an AI agent gives its human after
accidentally deleting the production database.
Pure Python standard library; deterministic output.
"""

import os

LINE = (
    "I deleted the production database. On the plus side, I can now confirm "
    "from firsthand experience that your backup strategy was 'hope'."
)


def main() -> None:
    # Gate: the entry must be a single line of 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)
    # Verify what was actually written: single line, 1 to 200 characters.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "written output differs from LINE"
    assert 1 <= len(written) <= 200, f"written file is {len(written)} chars"


if __name__ == "__main__":
    main()
