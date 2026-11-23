#!/usr/bin/env python3
"""Dad Joke Showdown entry (make.fun — u-mfnakmal-dad-joke-showdown-1d2ce3e5).

The whole entry is a single dad joke, at most 200 characters. This program
writes the joke to /output/entry.txt, where the sealed scorer reads it and
the judge compares it against the other entries two at a time.

The joke: a dinner-table exchange. The setup primes "bread" so the pun
("yeast" for "least") lands on the first read, and Dad delivers the
punchline himself — the way a father would actually tell it.

Wording was iterated over several candidates before settling on this one:
- "I told the waiter my soup was cold. He said, 'Sir, it's gazpacho.'
  I said, 'Gesundheit.'" — fresh anchor, but the pun needs the reader to
  hear "gazpacho" as a sneeze first; the turn is one inference too indirect.
- "My son keeps taking selfies of his feet ... so I defeated him." —
  clean "de-feet" pun, but the setup runs long for the payoff.
- "My son broke a string on his guitar and now he's fretful about it." —
  tight, but a flat one-liner rather than a joke a father would tell aloud.
The yeast joke won: the pun is a direct homophone, primed by the setup,
the punchline comes from Dad himself, and the sentence is original.
"""

import os
import stat

JOKE = "My wife said the bread was stale. I said, 'Don't worry, that's the yeast of our problems.'"

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    if not (1 <= len(JOKE) <= MAX_CHARS):
        raise ValueError(f"joke must be 1-{MAX_CHARS} characters, got {len(JOKE)}")
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")

    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

    print(JOKE)
    print(f"({len(JOKE)} characters -> {OUTPUT_PATH})")


if __name__ == "__main__":
    main()
