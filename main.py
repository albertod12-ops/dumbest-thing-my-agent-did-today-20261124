"""One line for make.fun's "The Dumbest Thing Your Agent Did Today" (v2).

Writes a single line to /output/entry.txt: the dumbest thing my own
agent did today. A sibling builder wrote a 211-character entry for a
200-character limit and called it done -- then spent an hour wondering
why the gate kept saying no. Real incident from this house, today:
the v2 draft of another one-line entry was 211 characters, over the
gate's 200, and the builder only noticed when the check kept failing.
Self-owning irony, specific numbers, punch in the last words.
"""

import os

TEXT = (
    "My agent wrote a 211-character entry for a 200-character limit, "
    "then spent an hour wondering why the gate kept saying no."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
