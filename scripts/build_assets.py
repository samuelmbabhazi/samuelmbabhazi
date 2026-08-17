#!/usr/bin/env python3
"""Generates every profile asset in both themes.

Run: python3 scripts/build_assets.py
Output: assets/dark/*.svg and assets/light/*.svg
"""

from theme import THEMES, SANS, MONO, ICONS, icon, ever_logo, write


def hero(t):
    return f'''<svg width="1200" height="370" viewBox="0 0 1200 370" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="frame"><rect width="1200" height="370" rx="20"/></clipPath>
    <radialGradient id="orb" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{t['glow']}" stop-opacity="{t['glowOpacity']}"/>
      <stop offset="1" stop-color="{t['glow']}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['glow']}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{t['glow']}" stop-opacity="0.9"/>
      <stop offset="1" stop-color="{t['glow']}" stop-opacity="0"/>
    </linearGradient>
    <style>
      .sans {{ font-family: {SANS}; }}
      .mono {{ font-family: {MONO}; }}
      @keyframes drift-a {{ 0%,100% {{ transform: translate(0,0);}} 50% {{ transform: translate(46px,18px);}} }}
      @keyframes drift-b {{ 0%,100% {{ transform: translate(0,0);}} 50% {{ transform: translate(-38px,-14px);}} }}
      @keyframes drift-c {{ 0%,100% {{ transform: translate(0,0);}} 50% {{ transform: translate(20px,-24px);}} }}
      .orb-a {{ animation: drift-a 11s ease-in-out infinite; }}
      .orb-b {{ animation: drift-b 14s ease-in-out infinite 0.8s; }}
      .orb-c {{ animation: drift-c 9s ease-in-out infinite 1.6s; }}
      @keyframes blink {{ 0%,55% {{opacity:1;}} 60%,100% {{opacity:0.15;}} }}
      .dot {{ animation: blink 2.2s ease-in-out infinite; }}
      @keyframes sweep {{ 0% {{ transform: translateX(-320px);}} 100% {{ transform: translateX(1240px);}} }}
      .sweep {{ animation: sweep 7s ease-in-out infinite; }}
      @keyframes ringspin {{ from {{ transform: rotate(0deg);}} to {{ transform: rotate(360deg);}} }}
      .ring {{ transform-origin: 1030px 140px; animation: ringspin 26s linear infinite; }}
    </style>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="1200" height="370" fill="{t['canvas']}"/>
    <g class="orb-a"><circle cx="190" cy="60" r="240" fill="url(#orb)"/></g>
    <g class="orb-b"><circle cx="1030" cy="320" r="270" fill="url(#orb)"/></g>
    <g class="orb-c"><circle cx="700" cy="-40" r="190" fill="url(#orb)"/></g>
    <g class="ring" opacity="0.5">
      <circle cx="1030" cy="140" r="72" stroke="{t['borderStrong']}" stroke-width="1.6" stroke-dasharray="3 9" fill="none"/>
    </g>
    <circle cx="1030" cy="140" r="46" stroke="{t['border']}" stroke-width="1.4" fill="none"/>
    <text x="1030" y="150" text-anchor="middle" class="mono" font-size="26" fill="{t['text']}">&lt;/&gt;</text>
    <text x="64" y="126" class="sans" font-size="68" font-weight="800" fill="{t['text']}" letter-spacing="-2">Samuel Mbabhazi</text>
    <text x="66" y="176" class="sans" font-size="30" font-weight="700" fill="{t['textSoft']}">Full-Stack Developer with 5+ Years of Experience</text>
    <rect x="66" y="196" width="690" height="2" fill="{t['border']}"/>
    <g style="clip-path: inset(0 0 0 0);">
      <rect x="66" y="195" width="240" height="4" rx="2" fill="url(#shine)" class="sweep" opacity="0.85"/>
    </g>
    <text x="66" y="238" class="sans" font-size="23" fill="{t['textMuted']}">Open source contributor, passionate about building clean, scalable web applications</text>
    <g>
      <circle cx="74" cy="278" r="5.5" fill="{t['text']}" class="dot"/>
      <text x="92" y="285" class="sans" font-size="19" fill="{t['textMuted']}">open to remote roles, freelance projects and open source collaboration</text>
    </g>
    <rect x="64" y="314" width="1072" height="2" rx="1" fill="url(#shine)" opacity="0.3"/>
    <text x="64" y="348" class="mono" font-size="17" fill="{t['textDim']}">my code ships in libraries downloaded millions of times a week</text>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="369" rx="19.5" stroke="{t['border']}" fill="none"/>
</svg>
'''


def about(t):
    return f'''<svg width="1200" height="330" viewBox="0 0 1200 330" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="f"><rect width="1200" height="330" rx="18"/></clipPath>
    <style>
      .mono {{ font-family: {MONO}; }}
      @keyframes cursor {{ 0%,49% {{opacity:1;}} 50%,100% {{opacity:0;}} }}
      .cur {{ animation: cursor 1.1s steps(1) infinite; }}
      @keyframes rise {{ from {{opacity:0; transform: translateY(6px);}} to {{opacity:1; transform: translateY(0);}} }}
      .l1 {{ animation: rise .5s ease-out both .2s; }}
      .l2 {{ animation: rise .5s ease-out both .7s; }}
      .l3 {{ animation: rise .5s ease-out both 1.2s; }}
      .l4 {{ animation: rise .5s ease-out both 1.7s; }}
      .l5 {{ animation: rise .5s ease-out both 2.2s; }}
    </style>
  </defs>
  <g clip-path="url(#f)">
    <rect width="1200" height="330" fill="{t['panel']}"/>
    <rect x="0.5" y="0.5" width="1199" height="329" rx="17.5" stroke="{t['border']}"/>
    <rect width="1200" height="46" fill="{t['panelHead']}"/>
    <rect x="0" y="45.5" width="1200" height="1" fill="{t['border']}"/>
    <circle cx="30" cy="23" r="6" fill="{t['borderStrong']}"/>
    <circle cx="52" cy="23" r="6" fill="{t['border']}"/>
    <circle cx="74" cy="23" r="6" fill="{t['border']}"/>
    <text x="600" y="28" text-anchor="middle" class="mono" font-size="13" fill="{t['textDim']}">samuel@dev ~ about</text>
    <g class="mono" font-size="15.5">
      <g class="l1">
        <text x="36" y="86"><tspan fill="{t['textDim']}">$</tspan><tspan fill="{t['text']}"> whoami</tspan></text>
        <text x="36" y="110" fill="{t['textMuted']}">Full-Stack Developer · 5+ years shipping production-grade applications</text>
      </g>
      <g class="l2">
        <text x="36" y="142"><tspan fill="{t['textDim']}">$</tspan><tspan fill="{t['text']}"> cat focus.txt</tspan></text>
        <text x="36" y="166" fill="{t['textMuted']}">TypeScript-first backend architecture (NestJS) · production-grade Angular, React &amp; Next.js</text>
        <text x="36" y="188" fill="{t['textMuted']}">scalable GraphQL &amp; REST APIs · enterprise open-source contributions</text>
      </g>
      <g class="l3">
        <text x="36" y="220"><tspan fill="{t['textDim']}">$</tspan><tspan fill="{t['text']}"> echo $LANGUAGES</tspan></text>
        <text x="36" y="244" fill="{t['textMuted']}">Français · Swahili · English</text>
      </g>
      <g class="l4">
        <text x="36" y="276"><tspan fill="{t['textDim']}">$</tspan><tspan fill="{t['text']}"> git log --author=samuel --oneline </tspan><tspan fill="{t['textDim']}">| head -2</tspan></text>
        <text x="36" y="300" fill="{t['textMuted']}">types(document): respect schema toObject options <tspan fill="{t['text']}">(mongoose, merged)</tspan>  ·  types(model): Model.schema typed <tspan fill="{t['text']}">(shipped 9.9.0)</tspan></text>
      </g>
      <g class="l5">
        <rect x="36" y="308" width="9" height="17" fill="{t['text']}" class="cur"/>
      </g>
    </g>
  </g>
</svg>
'''


GROUPS = [
    ("LANGUAGES", [("TypeScript", "typescript"), ("JavaScript", "javascript"),
                   ("Python", "python"), ("PHP", "php"), ("Bash", "gnubash"),
                   ("PowerShell", None)]),
    ("FRONTEND", [("Angular", "angular"), ("React", "react"), ("Next.js", "nextdotjs"),
                  ("RxJS", "reactivex"), ("NgRx", "ngrx"), ("Jotai", None),
                  ("TanStack Query", "reactquery"), ("Tailwind", "tailwindcss"),
                  ("SASS", "sass"), ("HTML5", "html5"), ("CSS3", "css3")]),
    ("BACKEND", [("NestJS", "nestjs"), ("Node.js", "nodedotjs"), ("Express", "express"),
                 ("GraphQL", "graphql"), ("Apollo", "apollographql"), ("REST API", None),
                 ("WebSockets", "socketdotio")]),
    ("DATABASES &amp; ORMS", [("PostgreSQL", "postgresql"), ("MySQL", "mysql"),
                              ("MongoDB", "mongodb"), ("Redis", "redis"),
                              ("Prisma", "prisma"), ("TypeORM", "typeorm")]),
    ("DEVOPS &amp; TOOLING", [("Docker", "docker"), ("GitHub Actions", "githubactions"),
                              ("NGINX", "nginx"), ("Postman", "postman"),
                              ("Swagger", "swagger"), ("Figma", "figma")]),
    ("PRACTICES", [("Clean Architecture", None), ("SOLID", None), ("DDD", None),
                   ("CI/CD", None), ("Testing", None), ("Code Review", None)]),
]


def stack(t):
    body, y, LEFT, MAXX, ROW = [], 56, 36, 1164, 48
    for label, chips in GROUPS:
        body.append(f'<text x="{LEFT}" y="{y}" font-family="{MONO}" font-size="12.5" '
                    f'font-weight="700" fill="{t["textDim"]}" letter-spacing="2">{label}</text>')
        x = LEFT
        y += 16
        for name, slug in chips:
            has = bool(slug and slug in ICONS)
            w = int((44 if has else 24) + len(name) * 8.6 + 14)
            if x + w > MAXX:
                x, y = LEFT, y + ROW
            body.append(f'<rect x="{x}" y="{y}" width="{w}" height="36" rx="18" '
                        f'fill="{t["chip"]}" stroke="{t["border"]}"/>')
            tx = x + 14
            if has:
                body.append(icon(slug, x + 13, y + 8, 19, t))
                tx = x + 40
            body.append(f'<text x="{tx}" y="{y+24}" font-family="{SANS}" font-size="14" '
                        f'font-weight="600" fill="{t["text"]}">{name}</text>')
            x += w + 10
        y += ROW + 16
    h = y + 4
    return (f'<svg width="1200" height="{h}" viewBox="0 0 1200 {h}" fill="none" '
            f'xmlns="http://www.w3.org/2000/svg"><defs><clipPath id="f">'
            f'<rect width="1200" height="{h}" rx="18"/></clipPath></defs>'
            f'<g clip-path="url(#f)"><rect width="1200" height="{h}" fill="{t["panel"]}"/>'
            f'<rect x="0.5" y="0.5" width="1199" height="{h-1}" rx="17.5" stroke="{t["border"]}"/>'
            + "".join(body) + '</g></svg>\n')


CARDS = [
    ("card-mongoose.svg", "mongoose", False, "Mongoose", "The MongoDB ODM for Node.js", "SHIPPED",
     ["Two type system fixes merged:", "Model.schema typing shipped in 9.9.0,", "toObject options typing lands in 9.9.2."], "Automattic/mongoose"),
    ("card-prisma.svg", "prisma", False, "Prisma", "Next generation TypeScript ORM", "IN REVIEW",
     ["Rust query compiler fix: nested", "upsert no longer renders cross table", "WHERE clauses on SQL drivers."], "prisma/prisma-engines"),
    ("card-typeorm.svg", "typeorm", False, "TypeORM", "Data mapper ORM for TypeScript", "IN REVIEW",
     ["PostGIS fix: dimensional geometry", "types are introspected correctly,", "ending perpetual migration diffs."], "typeorm/typeorm"),
    ("card-nestjs.svg", "nestjs", False, "cache-manager", "Official NestJS caching module", "SHIPPED",
     ["Cacheable instances with nonBlocking", "mode in the provider factory.", "Part of the v3.1.0 release."], "nestjs/cache-manager"),
    ("card-nestmongoose.svg", "nestjs", False, "nestjs/mongoose", "Official NestJS Mongoose module", "UPSTREAMED",
     ["ModelWithSchema proposal for typed", "model.schema, resolved instead by", "my upstream mongoose 9.9.0 fix."], "nestjs/mongoose"),
    ("card-gauzy.svg", None, True, "Ever Gauzy", "Open business management platform", "CONTRIBUTOR",
     ["Multi-tenant platform work:", "APIs, TypeORM data layer,", "Angular views and module boundaries."], "ever-co/ever-gauzy"),
    ("card-teams.svg", None, True, "Ever Teams", "Open work and project management", "CONTRIBUTOR",
     ["Real time collaboration features,", "service layer improvements", "and state management."], "ever-co/ever-teams"),
    ("card-traduora.svg", None, True, "Ever Traduora", "Translation management platform", "CONTRIBUTOR",
     ["Data integrity, import and export", "fixes across the translation", "pipeline and its SQLite layer."], "ever-co/ever-traduora"),
    ("card-wikipedia.svg", "wikipedia", False, "Wikimedia", "Wikipedia &amp; Wikimedia Commons", "CONTRIBUTOR",
     ["Writing and editing encyclopedia", "articles; contributing and", "curating media on Commons."], "commons.wikimedia.org"),
]


def card(t, ic, use_ever, title, sub, pill, lines, foot):
    if use_ever:
        head, tx = ever_logo(20, 20, 26), 56
    elif ic:
        head, tx = icon(ic, 21, 21, 22, t), 54
    else:
        head, tx = "", 20
    pw = len(pill) * 7.5 + 18
    body = "".join(
        f'<text x="20" y="{92 + i*18}" font-family="{SANS}" font-size="12" '
        f'fill="{t["textMuted"] if i < 2 else t["text"]}">{line}</text>'
        for i, line in enumerate(lines))
    return f"""<svg width="320" height="200" viewBox="0 0 320 200" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs><clipPath id="f"><rect width="320" height="200" rx="14"/></clipPath>
<style>@keyframes m {{ from {{ stroke-dashoffset: 0; }} to {{ stroke-dashoffset: -1040; }} }} .r {{ animation: m 7s linear infinite; }}</style></defs>
<g clip-path="url(#f)">
<rect width="320" height="200" fill="{t['panel']}"/>
<ellipse cx="50" cy="0" rx="200" ry="85" fill="{t['glow']}" opacity="0.04"/>
{head}
<text x="{tx}" y="38" font-family="{SANS}" font-size="16.5" font-weight="800" fill="{t['text']}">{title}</text>
<text x="{tx}" y="56" font-family="{SANS}" font-size="10.5" fill="{t['textDim']}">{sub}</text>
<rect x="{320-14-pw}" y="22" width="{pw}" height="22" rx="11" fill="none" stroke="{t['text']}" stroke-opacity="0.7"/>
<text x="{320-14-pw/2}" y="36.5" text-anchor="middle" font-family="{SANS}" font-size="9" font-weight="700" fill="{t['text']}" letter-spacing="0.8">{pill}</text>
{body}
<text x="20" y="182" font-family="{MONO}" font-size="10.5" fill="{t['textDim']}">{foot}</text>
</g>
<rect x="1" y="1" width="318" height="198" rx="13" fill="none" stroke="{t['border']}" stroke-width="1.5"/>
<rect x="1" y="1" width="318" height="198" rx="13" fill="none" stroke="{t['glow']}" stroke-width="1.5" stroke-opacity="0.85" stroke-dasharray="60 980" class="r"/>
</svg>
"""


BUTTONS = [("github", "GitHub", "github"), ("linkedin", "LinkedIn", "linkedin"),
           ("portfolio", "Portfolio", "googlechrome"), ("email", "Email", "gmail"),
           ("upwork", "Upwork", "upwork"), ("devto", "Articles", "devdotto")]


def button(t, label, slug):
    w = int(58 + len(label) * 9 + 18)
    return f'''<svg width="{w}" height="44" viewBox="0 0 {w} 44" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs><style>@keyframes m {{ from {{ stroke-dashoffset: 0; }} to {{ stroke-dashoffset: -520; }} }} .r {{ animation: m 6s linear infinite; }}</style></defs>
<rect x="1" y="1" width="{w-2}" height="42" rx="21" fill="{t['panel']}" stroke="{t['borderStrong']}"/>
<rect x="1" y="1" width="{w-2}" height="42" rx="21" fill="none" stroke="{t['glow']}" stroke-opacity="0.7" stroke-dasharray="34 486" class="r"/>
{icon(slug, 18, 12, 19, t)}
<text x="46" y="28" font-family="{SANS}" font-size="15" font-weight="600" fill="{t['text']}">{label}</text>
</svg>
'''


SEPARATORS = [("impact", "01", "Open Source Impact"), ("about", "02", "About Me"),
              ("stack", "03", "Tech Stack"), ("stats", "04", "GitHub Stats"),
              ("connect", "05", "Let's Connect")]


def separator(t, num, title):
    return f'''<svg width="1200" height="66" viewBox="0 0 1200 66" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['glow']}" stop-opacity="0"/><stop offset="0.5" stop-color="{t['glow']}" stop-opacity="0.85"/><stop offset="1" stop-color="{t['glow']}" stop-opacity="0"/>
    </linearGradient>
    <style>
      .sans {{ font-family: {SANS}; }}
      .mono {{ font-family: {MONO}; }}
      @keyframes sweep {{ 0% {{ transform: translateX(-260px);}} 100% {{ transform: translateX(1300px);}} }}
      .sweep {{ animation: sweep 8s ease-in-out infinite; }}
    </style>
  </defs>
  <text x="0" y="42" class="mono" font-size="17" font-weight="700" fill="{t['textFaint']}">{num}</text>
  <text x="52" y="43" class="sans" font-size="27" font-weight="800" fill="{t['text']}" letter-spacing="-0.5">{title}</text>
  <rect x="0" y="59" width="1200" height="1.5" fill="{t['border']}"/>
  <rect x="0" y="58.5" width="220" height="2.5" rx="1" fill="url(#shine)" class="sweep"/>
</svg>
'''


def footer(t):
    return f'''<svg width="1200" height="90" viewBox="0 0 1200 90" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="f"><rect width="1200" height="90" rx="16"/></clipPath>
    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['glow']}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{t['glow']}" stop-opacity="0.55"/>
      <stop offset="1" stop-color="{t['glow']}" stop-opacity="0"/>
    </linearGradient>
    <style>
      .mono {{ font-family: {MONO}; }}
      @keyframes scan {{ 0% {{ transform: translateX(-600px);}} 100% {{ transform: translateX(1800px);}} }}
      .scan {{ animation: scan 5.5s linear infinite; }}
      @keyframes blink {{ 0%,49% {{opacity:1;}} 50%,100% {{opacity:0;}} }}
      .cur {{ animation: blink 1.1s steps(1) infinite; }}
    </style>
  </defs>
  <g clip-path="url(#f)">
    <rect width="1200" height="90" fill="{t['canvas']}"/>
    <rect x="0.5" y="0.5" width="1199" height="89" rx="15.5" stroke="{t['border']}"/>
    <rect y="0" width="600" height="1.5" fill="url(#fade)" class="scan"/>
    <text x="600" y="42" text-anchor="middle" class="mono" font-size="14" fill="{t['textDim']}">clean code · typed end to end · proven in the open</text>
    <text x="560" y="70" text-anchor="middle" class="mono" font-size="13" fill="{t['textFaint']}">samuel@dev ~ $</text>
    <rect x="618" y="58" width="8" height="14" fill="{t['textMuted']}" class="cur"/>
  </g>
</svg>
'''


def main():
    count = 0
    for name, t in THEMES.items():
        write("hero.svg", name, hero(t))
        write("about.svg", name, about(t))
        write("stack.svg", name, stack(t))
        write("footer.svg", name, footer(t))
        count += 4
        for fname, ic, ever, title, sub, pill, lines, foot in CARDS:
            write(fname, name, card(t, ic, ever, title, sub, pill, lines, foot))
            count += 1
        for slug_name, label, slug in BUTTONS:
            write(f"btn-{slug_name}.svg", name, button(t, label, slug))
            count += 1
        for key, num, title in SEPARATORS:
            write(f"sep-{key}.svg", name, separator(t, num, title))
            count += 1
    print(f"{count} assets written across {len(THEMES)} themes")


if __name__ == "__main__":
    main()
