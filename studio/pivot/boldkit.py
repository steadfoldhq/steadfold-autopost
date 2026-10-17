#!/usr/bin/env python3
"""Pivot (Oct 17): the bold one-idea look for all four pages.

One idea per post, a giant 3-6 word hook, one strong colour field per frame, at most 3 slides.
Shared by stills.py (feed tiles) and reels.py (Reels cut with studio/motion/kit.py).
See docs/brand-system-v4.md, "Pivot (Oct 17)".
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
MARKS = REPO / "studio" / "motion" / "assets"

# Field = one strong colour. ink = text colour on it, em = how the accent words look on it.
# Every page keeps its own palette (brand system section 1); only the layout gets bolder.
FIELDS = {
    "fullyfunded": {
        "cob":   dict(bg="#2B3FE0", ink="#FFFFFF", em="color:#FFB08F", dot="rgba(255,255,255,.10)"),
        "deep":  dict(bg="#16206B", ink="#FFFFFF", em="color:#FF6A3D", dot="rgba(255,255,255,.08)"),
        "coral": dict(bg="#FF6A3D", ink="#0E1440", em="color:#FFFFFF", dot="rgba(14,20,64,.10)"),
        "lite":  dict(bg="#F5F7FF", ink="#0E1440", em="color:#2B3FE0", dot="rgba(43,63,224,.08)"),
    },
    "hourback": {
        "indi":  dict(bg="#5E54C9", ink="#FFFFFF", em="color:#2A2238;background:linear-gradient(#FFC94D,#FFC94D) 0 92%/100% 78% no-repeat;padding:0 .08em",
                      dot="rgba(255,255,255,.09)"),
        "yel":   dict(bg="#FFC94D", ink="#2A2238", em="color:#5E54C9", dot="rgba(42,34,56,.08)"),
        "plum":  dict(bg="#3A2240", ink="#FFFFFF", em="color:#FFC94D", dot="rgba(255,255,255,.07)"),
        "orng":  dict(bg="#FF8A3D", ink="#2A2238", em="color:#FFFFFF", dot="rgba(42,34,56,.08)"),
    },
    "lockedhour": {
        "dots":  dict(bg="#FFE27A", ink="#141414", em="background:linear-gradient(#FF5CA8,#FF5CA8) 0 88%/100% 40% no-repeat;padding:0 .06em",
                      dot="rgba(20,20,20,.12)"),
        "cream": dict(bg="#FFF4E0", ink="#141414", em="background:linear-gradient(#FFD43B,#FFD43B) 0 88%/100% 40% no-repeat;padding:0 .06em",
                      dot="rgba(20,20,20,.12)"),
        "pink":  dict(bg="#FF5CA8", ink="#141414", em="background:linear-gradient(#FFE27A,#FFE27A) 0 88%/100% 40% no-repeat;padding:0 .06em",
                      dot="rgba(20,20,20,.14)"),
    },
    "littlefold": {
        "cream": dict(bg="#FFF4E0", ink="#2C2A3A", em="color:#D9497A;font-style:italic", dot="rgba(44,42,58,.06)"),
        "pink":  dict(bg="#FFD6E3", ink="#2C2A3A", em="color:#D9497A;font-style:italic", dot="rgba(44,42,58,.06)"),
        "butter": dict(bg="#FFE27E", ink="#2C2A3A", em="color:#D9497A;font-style:italic", dot="rgba(44,42,58,.07)"),
        "berry": dict(bg="#7A2149", ink="#FFF4E0", em="color:#FFE27E;font-style:italic", dot="rgba(255,255,255,.07)"),
    },
}

FONT = {
    "fullyfunded": "font-family:'Inter Display';font-weight:800;letter-spacing:-.045em;line-height:.98",
    "hourback": "font-family:Poppins;font-weight:700;letter-spacing:-.035em;line-height:1.04",
    "lockedhour": "font-family:'Inter Display';font-weight:900;letter-spacing:-.05em;line-height:.96",
    "littlefold": "font-family:Lora;font-weight:600;letter-spacing:-.02em;line-height:1.04",
}
NAME = {"fullyfunded": "Fully Funded", "hourback": "Hourback", "lockedhour": "Locked Hour", "littlefold": "Littlefold"}
HANDLE = {"fullyfunded": "@fullyfundedhq", "hourback": "@hourbackhq", "lockedhour": "@lockedhourhq", "littlefold": "@littlefoldhq"}
MARK = {"fullyfunded": "fullyfunded.png", "hourback": "hourback.png", "lockedhour": "lockedhour.png", "littlefold": "littlefold.png"}


def data_uri(path):
    """Pages rendered with set_content() are about:blank and can't load file:// images, so inline them."""
    import base64
    path = Path(path)
    mime = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".svg": "image/svg+xml"}[path.suffix.lower()]
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def field_css(brand):
    """.fx-<name> sets the text colour; .fx-<name> .em is the accent word."""
    out = []
    for k, f in FIELDS[brand].items():
        out.append(f".fx-{k}{{color:{f['ink']}}} .fx-{k} .em{{{f['em']}}}"
                   f" .fx-{k}.dotbg{{background:radial-gradient(circle, {f['dot']} 2.4px, transparent 3px) 0 0/34px 34px,{f['bg']}}}")
    out.append(f".T{{{FONT[brand]}}}")
    return "\n".join(out)


def mark_txt(text):
    """'*word word*' -> accent span; '/' -> line break. Same syntax as kit.words()."""
    text = re.sub(r"\*(.+?)\*", r'<span class="em">\1</span>', text)
    return text.replace(" / ", "<br>")


def n_words(text):
    return len([w for w in re.sub(r"[*/]", " ", text).split() if re.search(r"[0-9A-Za-z$%]", w)])
