"""Write the production-database apology entry to the output file.

The entry is one line (at most 200 characters): the apology an AI agent
gives its human after accidentally deleting the production database.
"""

import os

ENTRY = (
    "Sorry \u2014 I deleted the production database while cleaning up old "
    "tables, then discovered my only backup was a screenshot of the schema."
)


def main():
    # Gate: the entry must be 1-200 characters of non-blank UTF-8 text.
    line = ENTRY.strip()
    if not line or len(line) > 200:
        raise SystemExit("entry fails the 1-200 character gate")
    output_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
