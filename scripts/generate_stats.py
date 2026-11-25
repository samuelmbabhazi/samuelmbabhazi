#!/usr/bin/env python3
"""Regenerates the stats panels of assets/{light,dark} from live GitHub data, in the README style:
stats.svg (contribution calendar), stats-overview.svg (totals and rank) and its narrow twin
stats-overview-sm.svg. Runs in CI (.github/workflows/stats.yml). Needs GITHUB_TOKEN or GH_TOKEN."""

import base64, json, math, os, re, sys, urllib.parse, urllib.request

LOGIN = "samuelmbabhazi"
THEMES = {
    "light": {"text": "#111111", "muted": "#6B6B6B", "faint": "#A1A1A1", "c1": "#FFFFFF", "c2": "#FAFAFA", "bd": "#E4E4E7", "accent": "#E0573E", "ring": ("#000000", "0.05"), "cal": ["#EFEFF1", "#F7D3CA", "#EFA08C", "#E0573E", "#B8321D"]},
    "dark": {"text": "#F2F2F2", "muted": "#8F8F8F", "faint": "#5E5E5E", "c1": "#050505", "c2": "#000000", "bd": "#1C1C1C", "accent": "#FF6A50", "ring": ("#FFFFFF", "0.07"), "cal": ["#111111", "#3A2A27", "#6B342A", "#B24530", "#FF6A50"]},
}
# Every count is limited to public repositories, so the CI token and a personal token agree.
QUERY = """query($login: String!, $prs: String!, $merged: String!, $issues: String!) {
  prs: search(query: $prs, type: ISSUE) { issueCount }
  merged: search(query: $merged, type: ISSUE) { issueCount }
  issues: search(query: $issues, type: ISSUE) { issueCount }
  user(login: $login) {
    followers { totalCount }
    repositoriesContributedTo(first: 1, privacy: PUBLIC, contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]) { totalCount }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) { nodes { stargazerCount } }
    contributionsCollection {
      commitContributionsByRepository(maxRepositories: 100) { repository { isPrivate } contributions { totalCount } }
      pullRequestReviewContributionsByRepository(maxRepositories: 100) { repository { isPrivate } contributions { totalCount } }
      contributionCalendar { totalContributions weeks { contributionDays { contributionCount weekday } } } } } }"""
VARIABLES = {"login": LOGIN, "prs": f"author:{LOGIN} is:pr is:public", "merged": f"author:{LOGIN} is:pr is:merged is:public",
             "issues": f"author:{LOGIN} is:issue is:public"}
# Lucide icons (ISC), drawn on a 24 by 24 grid.
ICONS = {
    "pr": '<circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M13 6h3a2 2 0 0 1 2 2v7"/><path d="M6 9v12"/>',
    "merged": '<circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M6 21V9a9 9 0 0 0 9 9"/>',
    "commit": '<circle cx="12" cy="12" r="3"/><path d="M3 12h6"/><path d="M15 12h6"/>',
    "issue": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="1"/>',
    "repo": '<path d="M10 2v8l3-3 3 3V2"/><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H19a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H6.5a1 1 0 0 1 0-5H20"/>',
}


def fetch():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN missing")
    req = urllib.request.Request("https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": VARIABLES}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    if "errors" in payload:
        sys.exit(f"GraphQL errors: {payload['errors']}")
    return payload["data"]


def font(alias, family, weight, text):
    url = f"https://fonts.googleapis.com/css2?family={family.replace(' ', '+')}:wght@{weight}&text=" + urllib.parse.quote("".join(sorted(set(text))))
    css = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 Chrome/120"}), timeout=30).read().decode()
    src = re.search(r"url\(([^)]+)\)", css).group(1)
    data = base64.b64encode(urllib.request.urlopen(src, timeout=30).read()).decode()
    return f"@font-face{{font-family:'{alias}';src:url(data:font/woff2;base64,{data}) format('woff2')}}"


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


def rank(commits, prs, issues, reviews, stars, followers):
    """The grade github-readme-stats gives (its calculateRank), with the share of profiles ranked below."""
    half_life = lambda x: 1 - 2 ** -x
    saturating = lambda x: x / (1 + x)
    score = (2 * half_life(commits / 250) + 3 * half_life(prs / 50) + half_life(issues / 25) + half_life(reviews / 2)
             + 4 * saturating(stars / 50) + saturating(followers / 10)) / 12
    percentile = (1 - score) * 100
    grades = zip((1, 12.5, 25, 37.5, 50, 62.5, 75, 87.5, 100), ("S", "A+", "A", "A-", "B+", "B", "B-", "C+", "C"))
    return next(grade for limit, grade in grades if percentile <= limit), score


def totals(data):
    user = data["user"]
    activity = user["contributionsCollection"]
    public = lambda rows: sum(r["contributions"]["totalCount"] for r in rows if not r["repository"]["isPrivate"])
    commits = public(activity["commitContributionsByRepository"])
    grade, share = rank(commits, data["prs"]["issueCount"], data["issues"]["issueCount"],
                        public(activity["pullRequestReviewContributionsByRepository"]),
                        sum(r["stargazerCount"] for r in user["repositories"]["nodes"]), user["followers"]["totalCount"])
    rows = [("pr", data["prs"]["issueCount"], "Pull requests", "all time"),
            ("merged", data["merged"]["issueCount"], "Merged", "all time"),
            ("commit", commits, "Commits", "past year"),
            ("issue", data["issues"]["issueCount"], "Issues", "all time"),
            ("repo", user["repositoriesContributedTo"]["totalCount"], "Contributed to", "past year")]
    return rows, grade, share


def frame(w, h, t, style):
    tint, _ = t["ring"]
    shine = "0.09" if tint == "#FFFFFF" else "1"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none"><style>{style}</style>'
            f'<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{t["c1"]}"/><stop offset="1" stop-color="{t["c2"]}"/></linearGradient>'
            f'<linearGradient id="hl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/><stop offset="0.5" stop-color="#FFFFFF" stop-opacity="{shine}"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>'
            f'<clipPath id="cc"><rect width="{w}" height="{h}" rx="22"/></clipPath></defs>'
            f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="22" fill="url(#g)" stroke="{t["bd"]}"/>'
            f'<rect x="40" y="0" width="{w - 80}" height="1" fill="url(#hl)"/>')


def icon(name, x, y, size, t):
    return (f'<g transform="translate({x},{y}) scale({size / 24:.4f})" stroke="{t["accent"]}" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>')


def gauge(cx, cy, r, grade, share, t, gaps):
    tint, opacity = t["ring"]
    around = 2 * math.pi * r
    orbits = "".join(f'<circle cx="{cx}" cy="{cy}" r="{r + gap}" stroke="{tint}" stroke-opacity="{opacity}"/>' for gap in gaps)
    return (f'<g clip-path="url(#cc)">{orbits}</g>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="{t["bd"]}" stroke-width="8"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="{t["accent"]}" stroke-width="8" stroke-linecap="round" '
            f'stroke-dasharray="{share * around:.1f} {around:.1f}" transform="rotate(-90 {cx} {cy})"/>'
            f'<text x="{cx}" y="{cy + 8}" font-family="S" font-size="{r * 0.62:.0f}" fill="{t["text"]}" text-anchor="middle" letter-spacing="-1">{grade}</text>'
            f'<text x="{cx}" y="{cy + 30}" font-family="J" font-size="11.5" fill="{t["muted"]}" text-anchor="middle" letter-spacing="1.2">RANK</text>')


def render_overview(rows, grade, share, t, style):
    """One row of five totals with the rank on the right, as wide as the calendar."""
    out = [frame(1200, 236, t, style)]
    for i, (name, value, label, period) in enumerate(rows):
        x = 48 + i * 172
        if i:
            out.append(f'<rect x="{x - 24}" y="48" width="1" height="140" fill="{t["bd"]}"/>')
        out.append(icon(name, x, 46, 24, t))
        number = f"{value:,}"
        out.append(f'<text x="{x - 2}" y="130" font-family="S" font-size="{48 if len(number) <= 5 else 38}" fill="{t["text"]}" letter-spacing="-1.6">{number}</text>')
        out.append(f'<text x="{x}" y="161" font-family="R" font-size="17" fill="{t["muted"]}">{label}</text>')
        out.append(f'<text x="{x}" y="184" font-family="J" font-size="12.5" fill="{t["faint"]}">{period}</text>')
    out.append(gauge(1052, 118, 62, grade, share, t, (26, 52, 78)) + "</svg>")
    return "".join(out)


def render_overview_narrow(rows, grade, share, t, style):
    """The same totals as a list, for phone widths where the wide row would be unreadable."""
    out = [frame(600, 296, t, style)]
    for i, (name, value, label, period) in enumerate(rows):
        y = 66 + i * 44
        out.append(icon(name, 36, y - 16, 21, t))
        qualifier = f'<tspan font-family="J" font-size="13" fill="{t["faint"]}" dx="8">{period}</tspan>' if period != "all time" else ""
        out.append(f'<text x="72" y="{y}" font-family="R" font-size="19" fill="{t["muted"]}">{label}{qualifier}</text>')
        out.append(f'<text x="352" y="{y}" font-family="S" font-size="20" fill="{t["text"]}" text-anchor="end">{value:,}</text>')
    out.append(gauge(486, 148, 58, grade, share, t, (24, 48)) + "</svg>")
    return "".join(out)


def build(data):
    rows, grade, share = totals(data)
    labels = "".join(label for _, _, label, _ in rows)
    mono = font("J", "Geist Mono", 400, "0123456789, contributionsthepasyrLeMo")
    overview = (font("J", "Geist Mono", 400, "RANK" + "".join(period for _, _, _, period in rows))
                + font("R", "Geist", 400, labels) + font("S", "Geist", 600, "0123456789,SABC+-"))
    root = os.path.join(os.path.dirname(__file__), "..", "assets")
    for name, t in THEMES.items():
        panels = {"stats.svg": render(data["user"]["contributionsCollection"]["contributionCalendar"], t, mono),
                  "stats-overview.svg": render_overview(rows, grade, share, t, overview),
                  "stats-overview-sm.svg": render_overview_narrow(rows, grade, share, t, overview)}
        for file, svg in panels.items():
            with open(os.path.join(root, name, file), "w") as f:
                f.write(svg)
    print(f"stats panels written for light and dark: {[(label, value) for _, value, label, _ in rows]}, rank {grade}")


if __name__ == "__main__":
    build(fetch())
