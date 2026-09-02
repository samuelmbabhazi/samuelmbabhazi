"""Shared palettes and helpers for the profile assets.

Every asset is generated twice, once per theme, into assets/dark and
assets/light. The README then serves the right one through <picture> and
prefers-color-scheme, so the profile follows the visitor's GitHub theme.
"""

import json
import os

SANS = "'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, Menlo, monospace"

# Light values follow GitHub's own light palette so the panels sit naturally
# on the page instead of floating as foreign blocks.
THEMES = {
    "dark": {
        "canvas": "#0A0A0C",
        "panel": "#0C0C0F",
        "panelHead": "#101014",
        "chip": "#101014",
        "border": "#26262B",
        "borderStrong": "#3F3F46",
        "text": "#F4F4F5",
        "textSoft": "#D4D4D8",
        "textMuted": "#A1A1AA",
        "textDim": "#71717A",
        "textFaint": "#52525B",
        "glow": "#FFFFFF",
        "glowOpacity": "0.10",
        "calendar": ["#161B22", "#0E4429", "#006D32", "#26A641", "#39D353"],
        # Brand icons that are white by definition need an inverse on light.
        "invertible": "#FFFFFF",
    },
    "light": {
        "canvas": "#FFFFFF",
        "panel": "#F6F8FA",
        "panelHead": "#EAEEF2",
        "chip": "#FFFFFF",
        "border": "#D1D9E0",
        "borderStrong": "#8C959F",
        "text": "#1F2328",
        "textSoft": "#32383F",
        "textMuted": "#59636E",
        "textDim": "#656D76",
        "textFaint": "#818B98",
        "glow": "#1F2328",
        "glowOpacity": "0.05",
        "calendar": ["#EBEDF0", "#9BE9A8", "#40C463", "#30A14E", "#216E39"],
        "invertible": "#1F2328",
    },
}

_DATA = json.load(open(os.path.join(os.path.dirname(__file__), "icons.json")))
ICONS = _DATA["icons"]
EVER_LOGO = _DATA["everLogo"]

BRAND = {
    "typescript": "#3178C6", "javascript": "#F7DF1E", "python": "#3776AB",
    "php": "#777BB4", "gnubash": "#4EAA25", "angular": "#DD0031",
    "react": "#61DAFB", "nextdotjs": "#FFFFFF", "reactivex": "#B7178C",
    "ngrx": "#BA2BD2", "reactquery": "#FF4154", "tailwindcss": "#06B6D4",
    "sass": "#CC6699", "html5": "#E34F26", "css3": "#1572B6",
    "nestjs": "#E0234E", "nodedotjs": "#5FA04E", "express": "#FFFFFF",
    "graphql": "#E10098", "apollographql": "#7B61FF", "socketdotio": "#FFFFFF",
    "postgresql": "#4169E1", "mysql": "#4479A1", "mongodb": "#47A248",
    "redis": "#DC382D", "prisma": "#5A67D8", "typeorm": "#FE0803",
    "docker": "#2496ED", "githubactions": "#2088FF", "nginx": "#009639",
    "postman": "#FF6C37", "swagger": "#85EA2D", "figma": "#F24E1E",
    "mongoose": "#B0413E", "upwork": "#6FDA44", "linkedin": "#0A66C2",
    "gmail": "#EA4335", "devdotto": "#FFFFFF", "github": "#FFFFFF",
    "googlechrome": "#4285F4", "wikipedia": "#FFFFFF",
    "firefoxbrowser": "#FF7139", "gitlab": "#FC6D26",
}


def icon(slug, x, y, size, t):
    """A brand icon in its own colour, swapped to the theme ink when the brand
    colour is white (invisible on a light page)."""
    if slug not in ICONS:
        return ""
    fill = BRAND.get(slug, t["text"])
    if fill.upper() == "#FFFFFF":
        fill = t["invertible"]
    scale = size / 24
    return (f'<g transform="translate({x},{y}) scale({scale:.3f})">'
            f'<path d="{ICONS[slug]}" fill="{fill}"/></g>')


def ever_logo(x, y, size):
    return (f'<image x="{x}" y="{y}" width="{size}" height="{size}" '
            f'href="data:image/png;base64,{EVER_LOGO}" clip-path="inset(0 round 6px)"/>')


def write(name, theme_name, svg):
    out = os.path.join(os.path.dirname(__file__), "..", "assets", theme_name, name)
    with open(out, "w") as f:
        f.write(svg)
