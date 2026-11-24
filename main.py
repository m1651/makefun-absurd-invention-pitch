"""One-Sentence Absurd Invention Pitch entry.

Writes one original absurd-invention pitch to entry.txt in the output
directory. The pitch is a fixed string: the program is fully
deterministic, so two runs produce byte-identical output.
"""

import os

PITCH = (
    "The GrudgeMug stops your coffee going cold by holding a petty "
    "grudge against the cold, reheating itself out of pure spite every "
    "time the temperature drops a degree."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
