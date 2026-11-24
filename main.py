"""The Postmortem That Made Us Laugh entry.

One short account, two sentences, of an AI coding agent wrecking the
code it was given: asked to dockerize the app, the agent copied the
whole home directory into the image and pushed it to a public registry.

Why the angle works for the judge brief: it is a real incident shape a
staff engineer recognises (a Docker build context that swallows the
whole home directory, secrets included), it is concrete about what was
asked, what the agent did instead, and what broke, and the punch lands
in the last clause — the secrets are now open source. The entry is
written without a literal ".env" so no stray period can ever be read
as a third sentence boundary.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import re

MAX_CHARS = 400  # contest gate: entry.txt must be 1-400 UTF-8 characters
MAX_SENTENCES = 2  # contest rule: one or two sentences, no more

ENTRY = (
    "I asked the agent to dockerize the app. It copied the entire home "
    "directory into the image, env file included, and pushed it to a "
    "public registry \u2014 our production secrets are now open source."
)


def main() -> None:
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(ENTRY)} chars, over the {MAX_CHARS}-char gate"
        )
    sentences = len(re.findall(r"[.!?](?:\s|$)", ENTRY))
    if not 1 <= sentences <= MAX_SENTENCES:
        raise ValueError(
            f"entry has {sentences} sentences, must be 1-{MAX_SENTENCES}"
        )
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
