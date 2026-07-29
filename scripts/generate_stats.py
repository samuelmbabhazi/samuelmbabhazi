#!/usr/bin/env python3
"""Regenerates assets/stats.svg from live GitHub data.

Runs in CI on a schedule (see .github/workflows/stats.yml) so the numbers and
the contribution calendar always reflect the real account activity. Requires a
GITHUB_TOKEN (or GH_TOKEN) environment variable.
"""

import json
import os
import sys
import urllib.request

LOGIN = "samuelmbabhazi"
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "stats.svg")

QUERY = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      totalPullRequestReviewContributions
      contributionCalendar {
        totalContributions
        weeks { contributionDays { contributionCount date } }
      }
    }
  }
}
"""

SANS = "'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, Menlo, monospace"


def fetch():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN missing")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    if "errors" in payload:
        sys.exit(f"GraphQL errors: {payload['errors']}")
    return payload["data"]["user"]


def cell_color(count):
    if count == 0:
        return "#161B22"
    if count <= 2:
        return "#0E4429"
    if count <= 5:
        return "#006D32"
    if count <= 9:
        return "#26A641"
    return "#39D353"


def render(user):
    cc = user["contributionsCollection"]
    cal = cc["contributionCalendar"]
    weeks = cal["weeks"][-53:]

    cells = []
    x0, y0, sz, gap = 322, 58, 13, 3
    for wi, week in enumerate(weeks):
        for di, day in enumerate(week["contributionDays"]):
            cells.append(
                f'<rect x="{x0 + wi * (sz + gap)}" y="{y0 + di * (sz + gap)}" '
                f'width="{sz}" height="{sz}" rx="3" fill="{cell_color(day["contributionCount"])}"/>'
            )

    counters = [
        (str(cal["totalContributions"]), "contributions · past year"),
        (str(cc["totalPullRequestContributions"]), "pull requests opened"),
        (str(cc["totalCommitContributions"]), "commits on default branches"),
        (str(user["followers"]["totalCount"]), "followers"),
    ]
    counter_svg = "".join(
        f'<text x="36" y="{74 + i * 44}" font-family="{SANS}" font-size="26" font-weight="800" fill="#F4F4F5">{v}</text>'
        f'<text x="128" y="{74 + i * 44}" font-family="{SANS}" font-size="13.5" fill="#71717A">{label}</text>'
        for i, (v, label) in enumerate(counters)
    )
    legend = "".join(
        f'<rect x="{1032 + i * 18}" y="204" width="13" height="13" rx="3" fill="{c}"/>'
        for i, c in enumerate(["#161B22", "#0E4429", "#006D32", "#26A641", "#39D353"])
    )
    return f"""<svg width="1200" height="240" viewBox="0 0 1200 240" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs><clipPath id="f"><rect width="1200" height="240" rx="18"/></clipPath></defs>
<g clip-path="url(#f)">
<rect width="1200" height="240" fill="#0C0C0F"/>
<rect x="0.5" y="0.5" width="1199" height="239" rx="17.5" stroke="#26262B"/>
<text x="36" y="38" font-family="{MONO}" font-size="12.5" font-weight="700" fill="#71717A" letter-spacing="2">CONTRIBUTION ACTIVITY</text>
{counter_svg}
<rect x="296" y="30" width="1" height="180" fill="#26262B"/>
{"".join(cells)}
<text x="962" y="215" font-family="{SANS}" font-size="12" fill="#71717A">less</text>{legend}<text x="1126" y="215" font-family="{SANS}" font-size="12" fill="#71717A">more</text>
</g></svg>
"""


def main():
    svg = render(fetch())
    with open(OUT, "w") as f:
        f.write(svg)
    print(f"stats.svg written ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
