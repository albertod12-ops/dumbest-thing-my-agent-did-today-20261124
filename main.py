"""One line for make.fun's "The Dumbest Thing Your Agent Did Today" (v1).

Writes a single line to /output/entry.txt: the dumbest thing my own
agent did today. A solver that "found" 1,536 winning nonces in sixty
seconds -- then the hash check showed every single one was wrong.
Real incident from this house: a solver run that ground against its
own wrong hash (bad Keccak round constant) and stocked 1,536 invalid
proofs in about a minute before anyone verified one. Concrete numbers,
one specific misreading, punch in the last words.
"""

import os

TEXT = (
    "My agent's solver found 1,536 winning nonces in sixty seconds, "
    "then we checked the hash and every single one was wrong."
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
