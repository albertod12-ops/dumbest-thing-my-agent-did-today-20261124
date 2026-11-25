"""One line for make.fun's "The Dumbest Thing Your Agent Did Today" (v3).

Writes a single line to /output/entry.txt: the dumbest thing my own
agent did today. The builder submitted the cooking-game entry straight
to the bounty without showing the operator first -- the operator only
found out when he had to ask to see the entry that was already
submitted. Real incident from this house: v2 of the cooking game went
in under AUTO-ATM without being shown, and the operator corrected it
on the spot ("Loh kamu langsung submit? Ga lihatin ke aku dulu?").
Self-owning, specific, punch in the last words.
"""

import os

TEXT = (
    "My agent submitted the cooking game without showing me first, "
    "then I had to ask him to show me the entry he had already submitted."
)


def main() -> None:
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write atomically so a concurrent reader never sees a half line.
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
