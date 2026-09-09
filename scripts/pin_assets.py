#!/usr/bin/env python3
"""Points every README image at the CDN, pinned to one commit.

A relative image path makes GitHub serve the file from raw.githubusercontent.com,
which answers 503 often enough that a README holding thirty of them shows broken
images. An absolute URL is fetched once by GitHub's image proxy and served from
its own cache instead. Pinning the URL to a commit means that cache can never
hand back a stale asset.

Run it after committing changed assets, then commit the README:
    python3 scripts/build_assets.py
    git commit -am "..."
    python3 scripts/pin_assets.py
    git commit -am "..."
"""

import re
import subprocess
import sys

REPO = "samuelmbabhazi/samuelmbabhazi"
README = "README.md"
CDN = f"https://cdn.jsdelivr.net/gh/{REPO}@"

PINNED = re.compile(re.escape(CDN) + r"[0-9a-zA-Z._-]+/(assets/[\w./-]+)")
RELATIVE = re.compile(r"(?<=[\"'])\./(assets/[\w./-]+)")


def main() -> int:
    ref = sys.argv[1] if len(sys.argv) > 1 else subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True
    ).stdout.strip()

    known = subprocess.run(["git", "branch", "-r", "--contains", ref],
                           capture_output=True, text=True).stdout
    if "origin/" not in known:
        print(f"{ref[:9]} is not on origin yet; push it first, the CDN reads "
              "the published commit.", file=sys.stderr)
        return 1

    text = open(README).read()
    text = PINNED.sub(lambda m: f"./{m.group(1)}", text)
    text, count = RELATIVE.subn(lambda m: f"{CDN}{ref}/{m.group(1)}", text)
    open(README, "w").write(text)

    print(f"{count} asset URLs pinned to {ref[:9]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
