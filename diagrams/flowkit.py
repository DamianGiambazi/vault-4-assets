"""flowkit.py: the drawing helpers shared by the Vault data-flow diagrams (from make_flows.py)."""
from html import escape

W, H = 1600, 900
INK, MUTED, EDGE = "#1F2430", "#5B6472", "#8A94A6"
STYLE = {   # fill, stroke, stroke-width, title colour, text colour
    "file":    ("#FFFFFF", EDGE, 2, INK, MUTED),
    "tool":    ("#E3ECFA", "#2F5DA8", 2.5, INK, INK),
    "human":   ("#FFF4EE", "#B4532A", 2.5, INK, MUTED),
    "verdict": ("#1F2430", "#1F2430", 2, "#FFFFFF", "#D7DCE4"),
    "fail":    ("#FCEDED", "#B42A2A", 2, "#8E1F1F", "#8E1F1F"),
    "note":    ("#FFFFFF", EDGE, 1.5, INK, MUTED),
}
LEGEND = [("file", "files and evidence"), ("tool", "a tool runs"), ("human", "you decide or write first"),
          ("verdict", "a verdict word"), ("fail", "fails closed")]


class Svg:
    def __init__(self, title, subtitle, thesis=None):
        self.out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
                    'font-family="Segoe UI, Inter, Helvetica, Arial, sans-serif">',
                    f"<title>{escape(title)}: {escape(subtitle)}</title>",
                    '<defs>'
                    f'<marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{MUTED}"/></marker>'
                    '<marker id="r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#B42A2A"/></marker>'
                    '<marker id="o" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#B4532A"/></marker>'
                    '</defs>',
                    f'<rect width="{W}" height="{H}" fill="#FAF8F4"/>',
                    f'<text x="60" y="62" font-size="32" font-weight="700" fill="{INK}">{escape(title)}</text>',
                    f'<text x="60" y="94" font-size="19" fill="{MUTED}">{escape(subtitle)}</text>']
        if thesis:
            for i, line in enumerate(thesis):
                self.out.append(f'<text x="{W-60}" y="{58 + 26*i}" text-anchor="end" font-size="19" '
                                f'font-style="italic" fill="{INK}">{escape(line)}</text>')

    def box(self, x, y, w, h, title, lines=(), kind="file", size=21, sub=15):
        fill, stroke, sw, tc, lc = STYLE[kind]
        self.out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        n = 1 + len(lines)
        block = size + (len(lines) * (sub + 6))
        top = y + (h - block) / 2 + size - 3
        cx = x + w / 2
        self.out.append(f'<text x="{cx}" y="{top:.0f}" text-anchor="middle" font-size="{size}" font-weight="700" fill="{tc}">{escape(title)}</text>')
        for i, ln in enumerate(lines):
            mono = ln.startswith("`") and ln.endswith("`")
            t = ln.strip("`")
            fam = ' font-family="Cascadia Mono, Consolas, Menlo, monospace"' if mono else ""
            self.out.append(f'<text x="{cx}" y="{top + 8 + (i+1)*(sub+6):.0f}" text-anchor="middle" font-size="{sub - (1 if mono else 0)}"{fam} fill="{lc}">{escape(t)}</text>')

    def arrow(self, pts, colour="grey", dashed=False, both=False):
        stroke, m = {"grey": (MUTED, "a"), "red": ("#B42A2A", "r"), "orange": ("#B4532A", "o")}[colour]
        d = "M" + " L".join(f"{x} {y}" for x, y in pts)
        extra = ' stroke-dasharray="7 6"' if dashed else ""
        start = f' marker-start="url(#{m})"' if both else ""
        self.out.append(f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="2.5"{extra}{start} marker-end="url(#{m})"/>')

    def label(self, x, y, text, anchor="middle", colour=MUTED, size=15, bold=False):
        self.out.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}"{" font-weight=\"600\"" if bold else ""} fill="{colour}">{escape(text)}</text>')

    def band(self, x, y, w, h, text, right=False):
        self.out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#EEF2F7" stroke="{EDGE}" stroke-width="1.5" stroke-dasharray="9 7"/>')
        self.out.append(f'<text x="{x+w-18 if right else x+18}" y="{y+24}" text-anchor="{"end" if right else "start"}" font-size="14" font-weight="600" letter-spacing="1" fill="{MUTED}">{escape(text)}</text>')

    def legend(self, y=H - 34):
        x = 60
        for kind, text in LEGEND:
            fill, stroke, sw, *_ = STYLE[kind]
            self.out.append(f'<rect x="{x}" y="{y-13}" width="22" height="16" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
            self.label(x + 30, y, text, anchor="start", size=14)
            x += 40 + len(text) * 7.6

    def save(self, path):
        self.out.append("</svg>")
        open(path, "w", encoding="utf-8").write("\n".join(self.out))

