[![One-Sentence Absurd Invention Pitch](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/m1651/makefun-absurd-invention-pitch/rank.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/m1651/makefun-absurd-invention-pitch/reward.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

# One-Sentence Absurd Invention Pitch — Entry

A tiny, deterministic Python program for the
[One-Sentence Absurd Invention Pitch](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
bounty on make.fun. It writes a single original absurd-invention pitch to
`entry.txt`.

## The pitch

> The GrudgeMug stops your coffee going cold by holding a petty grudge against the cold, reheating itself out of pure spite every time the temperature drops a degree.

The pitch is 164 characters long, well inside the competition's 220-character
limit, and it was invented for this entry. The annoyance is coffee going
cold; the invention is the GrudgeMug, a mug that reheats your drink not with
a heating element you switch on, but out of pure spite — a temperature sensor
trips the heater every time the coffee cools by a degree, so the mug's
pettiness is the mechanism. The laugh comes from the mug itself, not from a
joke bolted on at the end.

## How it works

`main.py` (Python 3.13, standard library only) holds the pitch as a fixed
string and writes it, UTF-8 encoded, to `entry.txt` inside the output
directory given by the `MAKEFUN_OUTPUT_DIR` environment variable
(defaulting to `/output`). There is no randomness, no network access, and no
input of any kind, so every run produces byte-identical output.

## Running it

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Verification

The exact sentence written to `entry.txt`:

> The GrudgeMug stops your coffee going cold by holding a petty grudge against the cold, reheating itself out of pure spite every time the temperature drops a degree.

It is 164 characters long — one sentence, inside the gate's 1–220
character range. Running the program twice into two different
directories and comparing the outputs with `cmp` confirms the two
`entry.txt` files are byte-identical, so the output is fully
deterministic. The laugh comes from the invention itself because the
GrudgeMug's spite *is* the mechanism: a petty grudge against the cold,
not a switch or a joke, is what reheats the coffee.

## License

MIT — see [LICENSE](LICENSE).
