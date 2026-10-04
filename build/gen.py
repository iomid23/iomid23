"""Generates the profile graphics in light and dark, using the omidamini.de design tokens."""
import base64
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
PORTRAIT = base64.b64encode((Path(__file__).resolve().parent / "portrait.jpg").read_bytes()).decode()
FONT = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
THEMES = {
    "light": dict(bg="#fafaf9", card="#f4f4f2", line="#e7e6e2", text="#111110", muted="#5a5a57", faint="#767672", accent="#1e40af", accent_soft="#1e40af14"),
    "dark": dict(bg="#0c0c0b", card="#141413", line="#262624", text="#e8e8e6", muted="#a8a8a4", faint="#8b8b86", accent="#60a5fa", accent_soft="#60a5fa1f"),
}


def grid(t, w, h, step=32):
    lines = [f'<path d="M{x} 0V{h}" />' for x in range(step, w, step)] + [f'<path d="M0 {y}H{w}" />' for y in range(step, h, step)]
    return f'<g stroke="{t["line"]}" stroke-width="1" opacity="0.55">{"".join(lines)}</g>'


def header(t):
    w, h = 1200, 380
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Omid Amini, EDI and SAP integration and full-stack engineering, Remscheid, Germany">
  <defs>
    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0.45" stop-color="{t["bg"]}" stop-opacity="1"/><stop offset="1" stop-color="{t["bg"]}" stop-opacity="0.35"/></linearGradient>
    <clipPath id="r"><rect width="{w}" height="{h}" rx="20"/></clipPath>
  </defs>
  <g clip-path="url(#r)">
    <rect width="{w}" height="{h}" fill="{t["bg"]}"/>
    {grid(t, w, h)}
    <rect width="{w}" height="{h}" fill="url(#fade)"/>
    <rect x="0" y="0" width="6" height="{h}" fill="{t["accent"]}"/>
  </g>
  <rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="19.5" fill="none" stroke="{t["line"]}"/>
  <g font-family="{FONT}">
    <rect x="64" y="58" width="44" height="44" rx="10" fill="{t["accent"]}"/>
    <text x="86" y="88" text-anchor="middle" font-size="19" font-weight="800" fill="{t["bg"]}" letter-spacing="-0.5">OA</text>
    <text x="124" y="78" font-size="17" font-weight="700" fill="{t["text"]}">Omid Amini</text>
    <text x="124" y="99" font-size="13" fill="{t["faint"]}">Software Engineer · OA IT Solutions</text>
    <text x="64" y="160" font-size="13" font-weight="600" fill="{t["accent"]}" letter-spacing="2.4">REMSCHEID, GERMANY · BUILDING SOFTWARE SINCE 2016</text>
    <text x="64" y="218" font-size="46" font-weight="800" fill="{t["text"]}" letter-spacing="-1.4">EDI and SAP integration</text>
    <text x="64" y="270" font-size="46" font-weight="800" fill="{t["text"]}" letter-spacing="-1.4">for mid-sized companies</text>
    <text x="64" y="310" font-size="18" fill="{t["muted"]}">Order pipelines, enterprise platforms and my own product, Rebar.</text>
    <text x="64" y="342" font-size="15" fill="{t["muted"]}"><tspan font-weight="800" fill="{t["accent"]}">&gt; 92%</tspan> fewer processing errors at <tspan font-weight="700" fill="{t["text"]}">4,000+</tspan> records a day</text>
  </g>
  <defs><clipPath id="photo"><rect x="896" y="70" width="240" height="240" rx="18"/></clipPath></defs>
  <image x="896" y="70" width="240" height="240" preserveAspectRatio="xMidYMid slice" clip-path="url(#photo)" href="data:image/jpeg;base64,{PORTRAIT}"/>
  <rect x="896.5" y="70.5" width="239" height="239" rx="17.5" fill="none" stroke="{t["line"]}"/>
</svg>
'''


def rebar(t):
    w, h = 1200, 250
    tags = ["iOS", "Android", "Web", "NestJS", "PostgreSQL", "React Native", "RevenueCat", "4 languages · RTL"]
    x, chips = 64, []
    for tag in tags:
        cw = 22 + len(tag) * 7.6
        chips.append(f'<rect x="{x}" y="170" width="{cw:.0f}" height="30" rx="7" fill="none" stroke="{t["line"]}"/><text x="{x + cw/2:.0f}" y="190" text-anchor="middle" font-size="13" fill="{t["muted"]}">{tag}</text>')
        x += cw + 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Rebar, my own product: a multilingual Kurdish business platform, live on the App Store, Google Play and the web">
  <rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="19.5" fill="{t["card"]}" stroke="{t["line"]}"/>
  <g font-family="{FONT}">
    <text x="64" y="62" font-size="13" font-weight="600" fill="{t["accent"]}" letter-spacing="2.4">OWN PRODUCT</text>
    <text x="64" y="106" font-size="34" font-weight="800" fill="{t["text"]}" letter-spacing="-0.8">Rebar <tspan font-weight="600" fill="{t["faint"]}">ڕێبەر</tspan></text>
    <text x="64" y="142" font-size="17" fill="{t["muted"]}">Kurdish business platform and a 273,000 word dictionary. Built and run alone, from database to store release.</text>
    {"".join(chips)}
    <text x="1136" y="62" text-anchor="end" font-size="13" font-weight="600" fill="{t["text"]}">Live on App Store, Google Play and web →</text>
  </g>
</svg>
'''


def contact(t):
    w, h = 1200, 170
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Have an integration or platform project? Free first call, fixed price after. omidamini.de">
  <rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="19.5" fill="{t["accent_soft"]}" stroke="{t["line"]}"/>
  <g font-family="{FONT}">
    <text x="64" y="76" font-size="28" font-weight="800" fill="{t["text"]}" letter-spacing="-0.6">Have an integration or platform project?</text>
    <text x="64" y="112" font-size="17" fill="{t["muted"]}">Free first call, then a binding fixed-price offer. You talk to the person who writes the code.</text>
    <rect x="896" y="58" width="240" height="54" rx="12" fill="{t["accent"]}"/>
    <text x="1016" y="92" text-anchor="middle" font-size="17" font-weight="700" fill="{t["bg"]}">omidamini.de  →</text>
  </g>
</svg>
'''


for name, build in {"header": header, "rebar": rebar, "contact": contact}.items():
    for theme, tokens in THEMES.items():
        (OUT / f"{name}-{theme}.svg").write_text(build(tokens), encoding="utf-8")
print("ok")
