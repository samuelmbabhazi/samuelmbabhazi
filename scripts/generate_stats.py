#!/usr/bin/env python3
"""Regenerates assets/{light,dark}/stats.svg from live GitHub data, in the README style.
Runs in CI (.github/workflows/stats.yml). Needs GITHUB_TOKEN or GH_TOKEN."""

import base64, json, os, re, sys, urllib.parse, urllib.request

LOGIN = "samuelmbabhazi"
THEMES = {
    "light": {"muted": "#6B6B6B", "faint": "#A1A1A1", "c1": "#FFFFFF", "c2": "#FAFAFA", "bd": "#E4E4E7", "cal": ["#EFEFF1", "#F7D3CA", "#EFA08C", "#E0573E", "#B8321D"]},
    "dark": {"muted": "#8F8F8F", "faint": "#5E5E5E", "c1": "#050505", "c2": "#000000", "bd": "#1C1C1C", "cal": ["#111111", "#3A2A27", "#6B342A", "#B24530", "#FF6A50"]},
}
QUERY = """query($login: String!) { user(login: $login) { contributionsCollection {
  contributionCalendar { totalContributions weeks { contributionDays { contributionCount weekday } } } } } }"""


def fetch():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN missing")
    req = urllib.request.Request("https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    if "errors" in payload:
        sys.exit(f"GraphQL errors: {payload['errors']}")
    return payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def font(text):
    url = "https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400&text=" + urllib.parse.quote(text)
    css = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 Chrome/120"}), timeout=30).read().decode()
    src = re.search(r"url\(([^)]+)\)", css).group(1)
    data = base64.b64encode(urllib.request.urlopen(src, timeout=30).read()).decode()
    return f"@font-face{{font-family:'J';src:url(data:font/woff2;base64,{data}) format('woff2')}}"


def level(n):
    return 0 if n == 0 else 1 if n <= 2 else 2 if n <= 5 else 3 if n <= 9 else 4


def render(cal, t, style):
    weeks = cal["weeks"][-53:]
    step = 1136 / len(weeks)
    size = step - 4
    y = round(32 + 7 * step + 30)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="250" viewBox="0 0 1200 250" fill="none"><style>{style}</style>',
           f'<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{t["c1"]}"/><stop offset="1" stop-color="{t["c2"]}"/></linearGradient></defs>',
           f'<rect x="0.5" y="0.5" width="1199" height="249" rx="22" fill="url(#g)" stroke="{t["bd"]}"/>']
    for c, week in enumerate(weeks):
        for day in week["contributionDays"]:
            out.append(f'<rect x="{32 + c * step:.1f}" y="{32 + day["weekday"] * step:.1f}" width="{size:.1f}" height="{size:.1f}" rx="3.5" fill="{t["cal"][level(day["contributionCount"])]}"/>')
    out.append(f'<text x="32" y="{y}" font-family="J" font-size="13" fill="{t["muted"]}">{cal["totalContributions"]:,} contributions in the past year</text>')
    x = 1168 - 31
    out.append(f'<text x="{x}" y="{y}" font-family="J" font-size="13" fill="{t["faint"]}">More</text>')
    x -= 10
    for i in range(4, -1, -1):
        x -= 14
        out.append(f'<rect x="{x}" y="{y - 10}" width="11" height="11" rx="3" fill="{t["cal"][i]}"/>')
        x -= 3
    out.append(f'<text x="{x - 6}" y="{y}" font-family="J" font-size="13" fill="{t["faint"]}" text-anchor="end">Less</text></svg>')
    return "".join(out)


def main():
    cal = fetch()
    style = font("0123456789, contributionsthepasyrLeMo")
    root = os.path.join(os.path.dirname(__file__), "..", "assets")
    for name, t in THEMES.items():
        with open(os.path.join(root, name, "stats.svg"), "w") as f:
            f.write(render(cal, t, style))
    print("stats.svg written for light and dark")


if __name__ == "__main__":
    main()
