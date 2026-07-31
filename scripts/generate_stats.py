#!/usr/bin/env python3
"""Regenerates the contribution panel from live GitHub data, in both themes.

Runs in CI on a schedule (see .github/workflows/stats.yml) so the numbers and
the calendar always reflect real activity. Requires GITHUB_TOKEN or GH_TOKEN.
Output: assets/dark/stats.svg and assets/light/stats.svg
"""

import json
import os
import sys
import urllib.request

from theme import THEMES, SANS, MONO, write

LOGIN = "samuelmbabhazi"

QUERY = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      contributionCalendar {
        totalContributions
        weeks { contributionDays { contributionCount date } }
      }
    }
  }
}
"""


def fetch():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN missing")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        payload = json.load(response)
    if "errors" in payload:
        sys.exit(f"GraphQL errors: {payload['errors']}")
    return payload["data"]["user"]


def level(count):
    if count == 0:
        return 0
    if count <= 2:
        return 1
    if count <= 5:
        return 2
    if count <= 9:
        return 3
    return 4


def render(user, t):
    cc = user["contributionsCollection"]
    cal = cc["contributionCalendar"]
    weeks = cal["weeks"][-53:]

    x0, y0, sz, gap = 322, 58, 13, 3
    cells = "".join(
        f'<rect x="{x0 + wi * (sz + gap)}" y="{y0 + di * (sz + gap)}" width="{sz}" '
        f'height="{sz}" rx="3" fill="{t["calendar"][level(day["contributionCount"])]}"/>'
        for wi, week in enumerate(weeks)
        for di, day in enumerate(week["contributionDays"])
    )
    counters = [
        (str(cal["totalContributions"]), "contributions · past year"),
        (str(cc["totalPullRequestContributions"]), "pull requests opened"),
        (str(cc["totalCommitContributions"]), "commits on default branches"),
        (str(user["followers"]["totalCount"]), "followers"),
    ]
    counter_svg = "".join(
        f'<text x="36" y="{74 + i * 44}" font-family="{SANS}" font-size="26" '
        f'font-weight="800" fill="{t["text"]}">{value}</text>'
        f'<text x="128" y="{74 + i * 44}" font-family="{SANS}" font-size="13.5" '
        f'fill="{t["textDim"]}">{label}</text>'
        for i, (value, label) in enumerate(counters)
    )
    legend = "".join(
        f'<rect x="{1032 + i * 18}" y="204" width="13" height="13" rx="3" fill="{c}"/>'
        for i, c in enumerate(t["calendar"])
    )
    return f'''<svg width="1200" height="240" viewBox="0 0 1200 240" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs><clipPath id="f"><rect width="1200" height="240" rx="18"/></clipPath></defs>
<g clip-path="url(#f)">
<rect width="1200" height="240" fill="{t['panel']}"/>
<rect x="0.5" y="0.5" width="1199" height="239" rx="17.5" stroke="{t['border']}"/>
<text x="36" y="38" font-family="{MONO}" font-size="12.5" font-weight="700" fill="{t['textDim']}" letter-spacing="2">CONTRIBUTION ACTIVITY</text>
{counter_svg}
<rect x="296" y="30" width="1" height="180" fill="{t['border']}"/>
{cells}
<text x="962" y="215" font-family="{SANS}" font-size="12" fill="{t['textDim']}">less</text>{legend}<text x="1126" y="215" font-family="{SANS}" font-size="12" fill="{t['textDim']}">more</text>
</g></svg>
'''


def main():
    user = fetch()
    for name, t in THEMES.items():
        write("stats.svg", name, render(user, t))
    print(f"stats.svg written for {', '.join(THEMES)}")


if __name__ == "__main__":
    main()
