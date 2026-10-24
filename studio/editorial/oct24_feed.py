#!/usr/bin/env python3
"""Feed posts built Oct 24 (Social studio, feed-post maker). Modelled on series_oct26.py but it NEVER writes schedule/posts.json:
it renders media/<id>/0N.jpg and writes /tmp/claude-0/sc/out/<id>.json for the lead to integrate.

  Wed Oct 28 series episodes (same cover layout as episode 1 of each series):
    lf-3amclub-02 17:00 · ff-richhabits-02 17:00 · lh-oneword-03 17:00 · hb-day9-kind-firm-no 17:45
  Tue Oct 27 single teaching tiles (quiet styles, never pills):
    lf-1027-enough-milk 11:30 (sticky) · ff-1027-hours-not-dollars 12:00 (reframe)
    lh-1027-write-the-worry 12:30 (emoji meme) · hb-1027-check-before-send 13:00 (sticky)
  FIX: lf-3amclub-01 slide 2 (re-rendered in place, same paths).

    python3 studio/editorial/oct24_feed.py [ids]      # one post at a time on the shared 2-CPU box
Covers: LF/HB from covers.py (pills/sticky); FF Rich Habits from the recovery-oct22 richhabits.py look (drawn chart, no piggy);
LH One Word from recovery-oct22/lockedhour feed.py oneword() (zine frame, black label, huge word). No "example" anywhere.
"""
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO / "studio/recovery-oct22/lockedhour/build"))
import glob as _glob  # noqa: E402
_g0 = _glob.glob  # this box ships chromium as chrome-linux64/; covers.py looks for chrome-linux/ (left untouched: shared file)
_glob.glob = lambda p, *a, **k: _g0(p, *a, **k) or _g0(p.replace("chrome-linux/", "chrome-linux64/"), *a, **k)
import covers as C  # noqa: E402
_glob.glob = _g0
import edkit as K  # noqa: E402
import lhkit as L  # noqa: E402

OUT_JSON = Path("/tmp/claude-0/sc/out")
FF, HB, LH, LF = "fullyfunded", "hourback", "lockedhour", "littlefold"
NOT_MED = "General information only, not medical advice."
FOLLOW = {
    LF: "Follow for one calm thing a night, from bump to toddler.",
    LH: "Follow for one small focus fix a day, each one backed by research.",
    FF: "Follow for one money move a day, in plain words.",
    HB: "Follow to learn what AI can really do, one real test a day.",
}
W, H = 1080, 1350
POSTS = {}
SAVE = "new one<br>every Mon · Wed · Fri"            # series covers (gate, Oct 24): says what the days mean
SAVE_LF = "new night tip<br>every Mon · Wed · Fri"

# Gate fix (Oct 24): with tight serif leading the pills rode up into the line above. A transparent top border with
# background-clip:padding-box starts each pill ~.2em lower without moving the words (pills stay UNDER the words).
_css0 = K.css
K.css = lambda brand, W_, H_: _css0(brand, W_, H_) + ".S .pill,.pill{border-top:.2em solid transparent;background-clip:padding-box!important}\n"


def svg_lamp(x, y, w=230):
    """Dim bedside lamp, drawn (Littlefold): warm shade, small glow, no harsh light."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w * 1.25:.0f}px;z-index:3;overflow:visible" viewBox="0 0 200 250">'
            '<ellipse cx="100" cy="95" rx="95" ry="70" fill="#FFE59A" opacity=".45"/>'
            '<path d="M55 30 L145 30 L170 110 L30 110 Z" fill="#FFBFD3" stroke="#3A1F3D" stroke-width="5" stroke-linejoin="round"/>'
            '<rect x="94" y="110" width="12" height="90" fill="#3A1F3D"/>'
            '<ellipse cx="100" cy="215" rx="58" ry="16" fill="#FFF8EE" stroke="#3A1F3D" stroke-width="5"/>'
            '<path d="M150 60 q12 6 6 18" stroke="#3A1F3D" stroke-width="4" fill="none" stroke-linecap="round" opacity=".5"/></svg>')


def svg_crib(x, y, w=300):
    """Simple crib with a sleeping-baby bump on its back, drawn (Littlefold; no faces)."""
    bars = "".join(f'<rect x="{34 + k * 26}" y="70" width="8" height="96" rx="4" fill="#3A1F3D"/>' for k in range(9))
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w * 0.8:.0f}px;z-index:3;overflow:visible" viewBox="0 0 300 240">'
            '<rect x="20" y="40" width="14" height="190" rx="7" fill="#3A1F3D"/><rect x="266" y="40" width="14" height="190" rx="7" fill="#3A1F3D"/>'
            '<rect x="20" y="62" width="260" height="12" rx="6" fill="#3A1F3D"/>'
            '<rect x="34" y="150" width="232" height="26" rx="8" fill="#FFF8EE" stroke="#3A1F3D" stroke-width="4"/>'
            '<path d="M70 150 q20 -34 70 -30 q60 4 80 30 Z" fill="#FFBFD3" stroke="#3A1F3D" stroke-width="4"/>'
            '<circle cx="78" cy="132" r="18" fill="#FFE59A" stroke="#3A1F3D" stroke-width="4"/>'
            + bars + '<rect x="20" y="170" width="260" height="12" rx="6" fill="#3A1F3D"/>'
            '<text x="226" y="40" font-family="Caveat Brush" font-size="40" fill="#D9497A">z z</text></svg>')


def svg_lunchbox(x, y, w=300):
    """Packed lunchbox, drawn (Fully Funded cobalt/coral)."""
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w * 0.8:.0f}px;z-index:3;overflow:visible" viewBox="0 0 300 240">'
            '<path d="M110 60 q40 -46 80 0" stroke="#141A55" stroke-width="10" fill="none" stroke-linecap="round"/>'
            '<rect x="20" y="60" width="260" height="160" rx="26" fill="#FFFFFF" stroke="#141A55" stroke-width="6"/>'
            '<rect x="20" y="60" width="260" height="44" rx="22" fill="#2B3FE0" stroke="#141A55" stroke-width="6"/>'
            '<rect x="44" y="122" width="100" height="78" rx="14" fill="#FFC6B2" stroke="#141A55" stroke-width="4"/>'
            '<rect x="156" y="122" width="100" height="78" rx="14" fill="#C9D3F7" stroke="#141A55" stroke-width="4"/>'
            '<circle cx="80" cy="160" r="16" fill="#E04E28"/><circle cx="110" cy="152" r="12" fill="#FBF2DF" stroke="#141A55" stroke-width="3"/>'
            '<path d="M176 175 q30 -40 60 0" fill="#FBF2DF" stroke="#141A55" stroke-width="4"/></svg>')


def post(pid, brand, at, pages, caption, comment, alt):
    """pages: list of callables -> full html (rendered in order as 01.jpg, 02.jpg ...)."""
    POSTS[pid] = dict(brand=brand, at=at, pages=pages, caption=caption, comment=comment, alt=alt)


# ------------------------------------------------------------------------------------------------ page helpers
def lift_save(body, dy=-50):
    """Two-line series save-line: lift it so its 2nd line clears the corner stamp."""
    import re
    return re.sub(r'(<div class="hand" style="position:absolute;left:\d+px;top:)(\d+)', lambda m: m.group(1) + str(int(m.group(2)) + dy), body, count=1)


def ed_cover(b, c, extra=""):
    return lambda: C.page(b, c["f"], lift_save(C.LAYOUTS[c["lay"]](b, c)) + extra, W, H)


def ed_inner(b, s, i, n, extra=""):
    return lambda: C.page(b, s["f"], C.inner(b, s, i, n) + extra, W, H)


def sticky(b, c, item_px=None, wide=False, src=None):
    """covers.lay_sticky, optionally with smaller item text, a wider note, a smaller corner stamp and the save-line clear of the object."""
    def f():
        body = C.lay_sticky(b, c)
        if item_px:
            body = body.replace("font:600 54px/1.15 Caveat", f"font:600 {item_px}px/1.12 Caveat")
        if wide:
            body = body.replace("left:230px;top:", "left:160px;top:", 1).replace("width:640px;padding:70px", "width:740px;padding:70px", 1)
            body = body.replace("left:830px;top:50px;width:190px;height:190px", "left:910px;top:26px;width:140px;height:140px", 1)
            body = body.replace("left:70px;top:1210px;width:700px", "left:30px;top:1170px;width:620px", 1)       # obj br
            body = body.replace("left:60px;top:930px;width:320px", "left:30px;top:1040px;width:320px", 1)        # chat bl, below the note
            body = body.replace("left:330px;top:1210px;width:700px", "left:370px;top:1170px;width:680px", 1)     # save-line for obj bl
        if src:
            body += (f'<div style="position:absolute;left:50px;top:46px;font:500 26px/1.2 Fraunces;color:{K.FIELDS[b][c["f"]]["ink"]};'
                     f'opacity:.7;z-index:5">Source: {src}</div>')
        return C.page(b, c["f"], body, W, H)
    return f


# ================================================================================================ C. FIX lf-3amclub-01
LF01_COVER = dict(lay="pills", f="berry", kicker="3 am club · no. 1", text="It's 3 am. / You're feeding. / *Eyes closing.*", obj="shoe",
                  at="br", save=SAVE_LF)
LF01_S2 = dict(f="cream", text="Sleepy? Don't / feed on the *sofa* / or *armchair.*", sub="after the feed, baby back in their own crib, on their back",
               src="NHS · The Lullaby Trust")
post("lf-3amclub-01", LF, "2026-10-26T17:00:00-04:00",
     [ed_cover(LF, LF01_COVER), ed_inner(LF, LF01_S2, 1, 2, svg_crib(700, 1010, 300))],
     ("It's 3 am. You're feeding. Your eyes keep closing.\n\n"
      "3 am Club No. 1: where you feed matters most on the nights you're running on empty.\n\n"
      "THE RULE: falling asleep with your baby on a sofa or armchair is one of the riskiest places to doze off together. "
      "The Lullaby Trust says the risk of SIDS is 50 times higher when a baby sleeps on a sofa or armchair with an adult. "
      "If there's any chance you'll nod off, move before you sit down.\n\n"
      "SET UP YOUR 3 AM SPOT BEFORE BED (5 minutes):\n"
      "1. Pick the spot now, while you're awake: never the sofa or armchair. Safest is baby back in their own crib beside you.\n"
      "2. If you feed in bed and might doze, keep pillows and duvets away from baby.\n"
      "3. Baby's own sleep space (crib or bassinet, flat, firm, empty) within arm's reach.\n"
      "4. Water, a dim light and your phone charger by the spot, so you don't end up on the sofa.\n"
      "5. After the feed, baby goes back in their own space, on their back.\n\n"
      "THE CATCH: no spot is risk-free if you've been drinking, smoke, or take medicine that makes you drowsy, or if your baby was premature or low birth weight. Then baby sleeps in their own space only.\n\n"
      "Do this: tonight, set up your 3 am spot before you go to bed.\n\n"
      "3 am Club No. 2 is Wednesday at 5 pm: what to do when the baby is wide awake at 3 am.\n\n"
      + FOLLOW[LF] + "\n\n" + NOT_MED + "\n\n#newborn #nightfeeds #safesleep #newparents #3amclub"),
     ("Sources: NHS, 'Sudden infant death syndrome (SIDS)': do not sleep on a sofa or armchair with your baby; put baby on their back "
      "in their own cot or Moses basket. The Lullaby Trust, 'Co-sleeping' (lullabytrust.org.uk/baby-safety/safer-sleep-information/co-sleeping): "
      "\"Never fall asleep on a sofa or armchair with your baby.\" \"The risk of SIDS is 50 times higher for babies when they sleep on a sofa or "
      "armchair with an adult.\" The Lullaby Trust, 'Safer sleep advice': if you think you might fall asleep while feeding, it is "
      "safer to do so in an adult bed clear of pillows and duvets than on a sofa or armchair; risk is much higher after alcohol, drugs or "
      "smoking. Government of Canada, 'Safe sleep for your baby': avoid sleeping with your baby on a sofa, armchair or couch; baby sleeps on "
      "their back in a crib, cradle or bassinet."),
     ("Littlefold 2-slide carousel. Slide 1: '3 am Club · No. 1' badge, 'It's 3 am. You're feeding. Eyes closing.' in a large serif with "
      "highlighted words, a halftone baby shoe, and the handwritten note 'new night tip every Mon · Wed · Fri'. Slide 2: 'Sleepy? Don't feed on the "
      "sofa or armchair.' Handwritten: after the feed, baby back in their own crib, on their back. Source: NHS, The Lullaby Trust."))

# ================================================================================================ A1. LF 3 am Club No. 2
LF02_COVER = dict(lay="pills", f="berry", kicker="3 am club · no. 2", text="3 am, and / baby wants / *to play?*", obj="shoe", at="br",
                  save=SAVE_LF)
LF02_S = [dict(f="cream", text="Keep 3 am / *boring.*", sub="low light, quiet voice, no play", src="NHS"),
          dict(f="pink", text="Fed? Changed? / *Straight back / down.*", sub="and make days bright, so they learn night from day", src="NHS")]
post("lf-3amclub-02", LF, "2026-10-28T17:00:00-04:00",
     [ed_cover(LF, LF02_COVER), ed_inner(LF, LF02_S[0], 1, 3, svg_lamp(770, 960, 230)), ed_inner(LF, LF02_S[1], 2, 3, svg_crib(700, 1010, 300))],
     ("3 am, and your baby wants to play? Make the next half hour as boring as you can.\n\n"
      "3 am Club No. 2. One calm thing for the night shift, every Mon, Wed and Fri.\n\n"
      "WHY IT WORKS: newborns don't know night from day yet. The NHS says you can teach the difference from the start: keep nights dull "
      "and days bright, and your baby gradually learns that night-time is for sleeping. It takes weeks, not one night.\n\n"
      "AT 3 AM:\n"
      "1. Keep the lights down low. A small lamp, not the big light.\n"
      "2. Don't talk much, and keep your voice quiet.\n"
      "3. Don't play, even if they're smiling at you.\n"
      "4. Change the diaper only if it needs it.\n"
      "5. Fed and changed? Put baby straight back down, on their back, in their own crib.\n\n"
      "IN THE DAY: open the curtains, play, and don't tiptoe around everyday noise when they nap.\n\n"
      "THE CATCH: waking at night to feed is normal, and young babies need it. Worried about how your baby sleeps or feeds? "
      "Talk to your doctor, nurse or health visitor.\n\n"
      "Do this: tonight, at the first wake-up, leave the big light off and keep your voice to a whisper.\n\n"
      "Send this to whoever's on the night shift with you.\n\n"
      "3 am Club No. 3 is Friday at 5 pm: when your baby will only sleep on you.\n\n"
      + FOLLOW[LF] + "\n\n" + NOT_MED + "\n\n#newborn #nightfeeds #babysleep #newparents #3amclub"),
     ("Sources: NHS, 'Helping your baby to sleep' (nhs.uk/baby/caring-for-a-newborn/helping-your-baby-to-sleep/): at night \"keep the lights "
      "down low\", \"not talk much and keep your voice quiet\", \"put your baby down as soon as they've been fed and changed\", \"not change your "
      "baby unless they need it\", \"not play with your baby\"; during the day \"open curtains, play games\"; \"Your baby will gradually learn "
      "that night-time is for sleeping.\" Government of Canada, 'Safe sleep for your baby': baby sleeps on their back in a crib, cradle or bassinet."),
     ("Littlefold 3-slide carousel. Slide 1: '3 am Club · No. 2' badge, '3 am, and baby wants to play?' in a large serif with highlighted "
      "words, a halftone baby shoe, and the handwritten note 'new night tip every Mon · Wed · Fri'. Slide 2: Keep 3 am boring (low light, quiet "
      "voice, no play), with a drawn dim bedside lamp. Slide 3: Fed? Changed? Straight back down (and make days bright, so they learn night "
      "from day), with a drawn crib. Source: NHS."))

# ================================================================================================ A2. FF Rich Habits No. 2
# Maths (made-up prices, stated in the caption): bought lunch $15, packed lunch $4, 48 work weeks a year.
BUY, PACK, WEEKS = 15, 4, 48
ALL5 = BUY * 5 * WEEKS                       # 3600
MIX = (BUY * 2 + PACK * 3) * WEEKS           # 2016
KEEP = ALL5 - MIX                            # 1584
assert (ALL5, MIX, KEEP) == (3600, 2016, 1584)
COB, FINK, CORAL = "#2B3FE0", "#141A55", "#E04E28"


def lunch_chart(x0=560, y0=900, w=460, h=400):
    """Drawn-to-scale 'lunch money, 1 year' bars, in the No. 1 'paycheque left' chart style."""
    base, top = y0 + h - 80, y0 + 96
    out = [f'<svg style="position:absolute;left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;z-index:3;overflow:visible" viewBox="{x0} {y0} {w} {h}">',
           f'<rect x="{x0 + 6}" y="{y0 + 6}" width="{w - 12}" height="{h - 12}" fill="rgba(255,255,255,.55)" stroke="{COB}" stroke-width="3"/>']
    for gx in range(x0 + 6, x0 + w - 6, 30):
        out.append(f'<line x1="{gx}" y1="{y0 + 6}" x2="{gx}" y2="{y0 + h - 6}" stroke="rgba(43,63,224,.10)" stroke-width="1"/>')
    for gy in range(y0 + 6, y0 + h - 6, 30):
        out.append(f'<line x1="{x0 + 6}" y1="{gy}" x2="{x0 + w - 6}" y2="{gy}" stroke="rgba(43,63,224,.10)" stroke-width="1"/>')
    bars = [("BUY 5 DAYS", ALL5, COB), ("PACK 3 DAYS", MIX, "#C9D3F7")]
    bw = 130
    for i, (lab, v, fill) in enumerate(bars):
        x = x0 + 70 + i * 190
        bh = (base - top) * v / ALL5
        out.append(f'<rect x="{x}" y="{base - bh:.0f}" width="{bw}" height="{bh:.0f}" fill="{fill}" stroke="{COB}" stroke-width="4"/>')
        out.append(f'<text x="{x + bw / 2}" y="{base - bh - 14:.0f}" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" '
                   f'font-size="28" fill="{CORAL if i else COB}">${v:,}</text>')
        out.append(f'<text x="{x + bw / 2}" y="{base + 42}" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" '
                   f'font-size="22" fill="{COB}">{lab}</text>')
    out.append(f'<line x1="{x0 + 40}" y1="{base}" x2="{x0 + w - 40}" y2="{base}" stroke="{COB}" stroke-width="5"/>')
    out.append(f'<text x="{x0 + 26}" y="{y0 + 46}" font-family="DejaVu Sans Mono" font-size="22" fill="{COB}" letter-spacing="2">LUNCH MONEY, 1 YEAR</text>')
    out.append("</svg>")
    return "".join(out)


FF02_COVER = dict(lay="pills", f="coral", kicker="rich habits, decoded · no. 2", text="$15 lunch, / *every* / *workday?*", obj="ok", at="br",
                  save=SAVE)
FF02_S = [dict(f="lite", text="Pack lunch / *3 days* a week.", sub="buy it the other 2, guilt-free"),
          dict(f="cob", text="One year of / *workday lunches*", cap=f"${BUY} bought · ${PACK} packed · {WEEKS} work weeks",
               rows=[("Buy all 5 days", f"${ALL5:,}"), ("Pack 3, buy 2", f"${MIX:,}"), ("You keep", f"${KEEP:,}")],
               )]


def ff_cover():
    body = C.lay_pills(FF, FF02_COVER)
    # swap the halftone object for the drawn chart (same move as Rich Habits No. 1)
    import re
    body = lift_save(re.sub(r'<img class="obj"[^>]*>', "", body, count=1))
    body = body.replace("width:620px;font-size:66px", "width:470px;font-size:62px", 1)   # keep the save-line clear of the chart
    return C.page(FF, "coral", body + lunch_chart(), W, H)


post("ff-richhabits-02", FF, "2026-10-28T17:00:00-04:00",
     [ff_cover, ed_inner(FF, FF02_S[0], 1, 3, svg_lunchbox(390, 930, 300)),
      ed_inner(FF, FF02_S[1], 2, 3, K.save_line("every year", 340, 870, 400, 76, -3, FF))],
     ("$15 lunch, every workday? The habit: pack lunch 3 days a week.\n\n"
      "Rich Habits, Decoded No. 2. Each episode takes one money habit and shows you how to do it on a normal paycheque.\n\n"
      "THE MATHS (prices made up for this post: $15 to buy lunch, $4 to pack one, 48 work weeks a year):\n"
      f"• Buy lunch all 5 days: $15 × 5 × 48 = ${ALL5:,} a year.\n"
      f"• Pack 3 days, buy 2: ($30 + $12) × 48 = ${MIX:,} a year.\n"
      f"• You keep ${KEEP:,} a year, and you still buy lunch twice a week.\n\n"
      "WHY IT WORKS: daily spending is small enough that you never decide on it. Picking 3 set days turns it into one decision a week, "
      "and the 2 bought lunches stop feeling like a slip.\n\n"
      "HOW (one Sunday, 30 minutes):\n"
      "1. Pick your 3 packed days. Same days every week.\n"
      "2. Cook one big batch on Sunday and split it into 3 containers.\n"
      "3. Check your own numbers: what you really pay for lunch, minus what a packed one costs you.\n"
      "4. Move the difference to savings on payday, so it doesn't just get spent somewhere else.\n\n"
      "THE CATCH: the saving only counts if it goes somewhere. Your prices will be different, so use your own.\n\n"
      "Do this: this Sunday, cook once and pack 3 lunches for the week.\n\n"
      "Rich Habits, Decoded No. 3 is Friday at 5 pm.\n\nEducation only, not financial advice.\n\n"
      + FOLLOW[FF] + "\n\n#personalfinance #savingmoney #mealprep #moneytips #richhabits"),
     (f"Maths (computed, prices made up for this post): bought lunch $15, packed lunch $4, 48 work weeks a year. "
      f"All 5 days bought: 15 × 5 × 48 = ${ALL5:,}. Pack 3, buy 2: (2 × 15 + 3 × 4) × 48 = ${MIX:,}. Difference: ${KEEP:,} a year. "
      "Use your own prices. Education only, not financial advice."),
     ("Fully Funded 3-slide carousel. Slide 1: 'Rich Habits, Decoded · No. 2' badge, '$15 lunch, every workday?' in a large serif with "
      f"highlighted words, the handwritten note 'new one every Mon · Wed · Fri' and a small drawn bar chart, 'lunch money, 1 year': buy 5 days ${ALL5:,}, "
      f"pack 3 days ${MIX:,}. Slide 2: Pack lunch 3 days a week (buy it the other 2, guilt-free), with a drawn packed lunchbox. Slide 3: One year of workday lunches, "
      f"$15 bought, $4 packed, 48 work weeks: buy all 5 days ${ALL5:,}; pack 3, buy 2 ${MIX:,}; you keep ${KEEP:,} (every year)."))

# ================================================================================================ A3. LH One Word No. 3 (zine frame)
INK = L.INK


def lh_page(inner, field, n, series):
    foot = (f"<div class='mono' style='position:absolute;left:70px;bottom:52px;font-size:22px;opacity:.8'>@lockedhourhq</div>"
            f"<div class='mono' style='position:absolute;right:70px;bottom:52px;font-size:22px;opacity:.8'>{series}{(' · ' + n) if n else ''}</div>"
            f"<div style='position:absolute;inset:26px;border:7px solid {INK};border-radius:6px;pointer-events:none'></div>")
    return lambda: L.page(inner + foot, W, H, field)


F = L.F
LH03 = [
    lh_page(f"""
<div style='position:absolute;left:80px;top:90px'><span class='label' style='font-size:30px;padding:12px 20px'>One Word · No. 3</span></div>
<div style='position:absolute;left:70px;right:70px;top:190px'>{L.dual("Third coffee / *not working?*", "pink", style="font-size:124px;text-align:left")}</div>
<div style='position:absolute;left:60px;top:760px;width:960px;height:120px;background:{L.PINK};opacity:.85;border-radius:60px'></div>
<div class='S' style='position:absolute;left:40px;right:40px;top:540px;font-size:340px;text-align:left'>Nap.</div>
<img class='obj' src='{L.obj("cup")}' style='position:absolute;left:720px;top:850px;width:270px;transform:rotate(8deg)'>
<div class='hand' style='position:absolute;left:90px;top:960px;font-size:60px;text-align:left'>10 minutes asleep,<br>alarm on</div>
<div class='mono' style='position:absolute;left:90px;top:1150px;font-size:24px;opacity:.8'>one word that guards your focus</div>
""", "pink", "No. 3", "ONE WORD"),
    lh_page(f"""
<div style='position:absolute;left:0;right:0;top:110px'>{L.dual("*10 minutes.* / That's it.", style="font-size:140px")}</div>
<div style='position:absolute;left:290px;top:420px'>{L.ring(500, 10 / 60, "10:00", "asleep", col=L.PINK, notch=True)}</div>
<div class='S' style='position:absolute;left:0;right:0;top:960px;font-size:70px'>Then get up. <span class='pill' style='background:{F['cream']['p1']}'>No snooze.</span></div>
<div class='hand' style='position:absolute;left:0;right:0;top:1070px;font-size:50px'>30 minutes? you wake up groggy.</div>
""", "cream", "No. 3", "ONE WORD"),
    lh_page(f"""
<div style='position:absolute;left:0;right:0;top:120px'>{L.dual("*Sharper* / right away.", style="font-size:160px")}</div>
<div class='S' style='position:absolute;left:100px;right:100px;top:450px;font-size:64px;line-height:1.05'>In a sleep lab, a 10-minute nap made adults short on sleep more alert right away.</div>
<div class='card' style='left:110px;right:110px;top:720px;padding:36px 40px'>
 <div class='dothis' style='font-size:76px;text-align:left'>Do this:</div>
 <div class='S' style='font-size:64px;text-align:left;line-height:1.04'>Set a 15-minute alarm:<br>about 5 to drift off, <span class='pill' style='background:{F['dots']['p1']}'>10 asleep.</span></div></div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1150px;font-size:22px;opacity:.85'>Brooks &amp; Lack 2006, SLEEP · 24 adults, ~5 h sleep the night before</div>
""", "dots", "No. 3", "ONE WORD"),
]
post("lh-oneword-03", LH, "2026-10-28T17:00:00-04:00", LH03,
     ("Third coffee not working? Today's word: Nap. Ten minutes asleep, alarm on.\n\n"
      "One Word No. 3. Each episode is one word that guards your focus.\n\n"
      "THE RESEARCH: in a sleep lab, 24 young adults who had slept only about 5 hours tried afternoon naps of 5, 10, 20 and 30 minutes. "
      "The 10-minute nap made them more alert and sharper right away, and some of the benefits lasted up to about 2.5 hours. "
      "The 30-minute nap left them groggy at first. The 5-minute nap did little.\n\n"
      "HOW TO NAP FOR 10:\n"
      "1. Set a 15-minute alarm: about 5 minutes to drift off, about 10 asleep.\n"
      "2. Lie down somewhere quiet, phone face down.\n"
      "3. When the alarm goes, get up. No snooze: longer naps are the groggy ones.\n"
      "4. Go straight back to your one task.\n\n"
      "THE CATCH: one small lab study, in people who were short on sleep. A nap doesn't replace a full night.\n\n"
      "Do this: tomorrow, when the slump hits, set a 15-minute alarm and lie down.\n\n"
      "Send this to the friend on their third coffee.\n\n"
      "One Word No. 4 is Friday at 5 pm.\n\n"
      + FOLLOW[LH] + "\n\n#focus #productivity #powernap #deepwork #oneword"),
     ("Source: Brooks, A. & Lack, L. (2006), 'A brief afternoon nap following nocturnal sleep restriction: which nap duration is most "
      "recuperative?', SLEEP 29(6), doi:10.1093/sleep/29.6.831. 24 healthy young adults, night sleep restricted to about 5 hours; no nap vs "
      "5, 10, 20 and 30-minute naps. The 10-minute nap gave immediate improvements on all measures, some lasting up to 155 minutes; the "
      "30-minute nap brought a period of impaired alertness right after waking."),
     ("Locked Hour 3-slide carousel. Slide 1: black label 'One Word · No. 3', 'Third coffee not working?' and the huge word 'Nap.' over a "
      "pink highlighter stripe, a halftone coffee cup, and the note '10 minutes asleep, alarm on'. Slide 2: '10 minutes. That's it.' A clock "
      "ring filled to 10 minutes; 'Then get up. No snooze.' and '30 minutes? you wake up groggy.' Slide 3: 'Sharper right away.' In a sleep "
      "lab, a 10-minute nap made adults short on sleep more alert right away. Do this: set a 15-minute alarm: about 5 to drift off, 10 "
      "asleep. Source: Brooks & Lack 2006."))

# ================================================================================================ A4. HB AI, for real · Day 9
HB_REQ = ("My friend wants to borrow $500. He still owes me $200 from last time. Write a short text saying no. Kind, firm, no excuses.")
HB_REPLY = ("Hey, I'm going to say no to lending the $500. I care about you and I want to keep money from getting between us, "
            "so I'm not lending right now. I hope you find a way to sort it out.")
HB9_COVER = dict(lay="pills", f="orng", kicker="ai, for real · day 9", text="He wants $500. / *Again.*", obj="chat", at="bl",
                 save=SAVE)
HB9_S2 = dict(f="indi", text="Ask AI: / “Help me say no / to lending $500.” / Add: *kind, firm,* / *no excuses.*",
              sub="those 3 words set the tone")


def hb_reply_slide():
    f = K.FIELDS[HB]["yel"]
    ink = f["ink"]
    body = C.head(HB, f, "It *wrote:*", 120, 220, 190)
    body += (f'<div style="position:absolute;left:90px;right:90px;top:400px;z-index:2">'
             f'<div style="font:600 30px/1 Inter;letter-spacing:.08em;text-transform:uppercase;color:{ink};opacity:.7;margin:0 0 18px 8px">the AI\'s reply, word for word</div>'
             f'<div style="background:#FFFFFF;border:3px solid {ink};border-radius:44px 44px 44px 10px;box-shadow:0 14px 0 {ink};'
             f'padding:46px 50px;font:500 52px/1.28 Inter;color:{ink}">{HB_REPLY.replace("$500", "<b>$500</b>")}</div></div>')
    body += K.save_line("real AI reply · situation made up for this post", 60, 1030, 960, 54, -2, HB)
    body += f'<div style="position:absolute;right:60px;top:40px;font:600 30px/1 Fraunces;color:{ink};opacity:.55;z-index:5">3/3</div>'
    body += K.stamp(HB, W - 230, H - 230, 170, -12)
    return C.page(HB, "yel", body, W, H)


post("hb-day9-kind-firm-no", HB, "2026-10-28T17:45:00-04:00",
     [ed_cover(HB, HB9_COVER), ed_inner(HB, HB9_S2, 1, 3), hb_reply_slide],
     ("He wants $500. Again. Ask AI to help you say no, and add three words: kind, firm, no excuses.\n\n"
      "AI, for real · Day 9. One real test of what AI can do, with the output shown.\n\n"
      "WHY IT WORKS: without a tone, AI guesses, and the guess is often long, apologetic or full of reasons. Naming the tone tells it what "
      "to aim for. \"No excuses\" matters most: it stops the AI inventing a reason you'd then have to defend.\n\n"
      "THE REAL TEST (the situation is made up for this post):\n"
      f"Request: \"{HB_REQ}\"\n"
      "The AI's reply (Claude, by Anthropic, Oct 24, 2026), quoted exactly:\n"
      f"\"{HB_REPLY}\"\n"
      "Notice: no excuse, and it left the $200 out, so the text stays about today's answer.\n\n"
      "Before you send it, change any word that doesn't sound like you.\n\n"
      "PRIVACY TIP: you don't need his name or your bank details. \"My friend\" and the amount are enough.\n\n"
      "Do this: next time a text is hard to write, ask AI for it and end with \"Kind, firm, no excuses.\"\n\n"
      "Send this to the friend who always says yes.\n\n"
      "AI, for real · Day 10 is Friday at 5:45 pm.\n\n"
      + FOLLOW[HB] + "\n\n#ai #chatgpt #claude #aitips #learnai"),
     ("Made-up situation, real output: written by Claude (Anthropic) on Oct 24, 2026, in a working session rather than a fresh chat. "
      "The reply is quoted in full, unedited. Results vary between apps and runs."),
     ("Hourback 3-slide carousel. Slide 1: 'AI, for real · Day 9' badge, 'He wants $500. Again.' in a large serif with highlighted words, "
      "black-and-white chat bubbles, and the handwritten note 'new one every Mon · Wed · Fri'. Slide 2: Ask AI: 'Help me say no to lending $500.' Add: kind, "
      "firm, no excuses (those 3 words set the tone). Slide 3: 'It wrote:' and a chat bubble with the AI's reply, word for word: '"
      + HB_REPLY + "' Note: real AI reply, situation made up for this post."))

# ================================================================================================ B1. LF sticky
LF27 = dict(lay="sticky", f="butter", text="Breastfeeding? / *5 signs* it's going well", obj="shoe", at="br",
            items=["6+ heavy wet diapers a day (from&nbsp;day&nbsp;5 after&nbsp;birth)", "2+ soft yellow poops a day (from&nbsp;day&nbsp;4 after&nbsp;birth)", "Long sucks and swallows",
                   "Lets go of the breast on their own", "Steady weight gain"],
            save="do this: count wet diapers<br>for 24 hours")
post("lf-1027-enough-milk", LF, "2026-10-27T11:30:00-04:00", [sticky(LF, LF27, 48, wide=True, src="NHS")],
     ("Breastfeeding? 5 signs it's going well. Check the diapers, not the clock.\n\n"
      "What to look for (NHS):\n"
      "• From day 5 after birth: at least 6 heavy, wet diapers every 24 hours.\n"
      "• From day 4 after birth: at least 2 soft, yellow poops a day for the first few weeks.\n"
      "• Feeds start with a few quick sucks, then long, rhythmic sucks and swallows.\n"
      "• Baby seems calm during feeds and lets go of the breast on their own.\n"
      "• Steady weight gain after the first few days (some early loss is normal).\n\n"
      "THE CATCH: these signs are for breastfed babies. Worried about how much milk your baby is getting? Ask your midwife, nurse or a "
      "breastfeeding specialist early.\n\n"
      "Do this: count wet diapers for 24 hours. A tick in your phone notes for each one is enough.\n\n"
      "Send this to someone in their first weeks.\n\n"
      "3 am Club No. 2 is tomorrow at 5 pm: what to do when the baby is wide awake at 3 am.\n\n"
      + FOLLOW[LF] + "\n\n" + NOT_MED + "\n\n#breastfeeding #newborn #newparents #babytips #littlefold"),
     ("Source: NHS, 'Breastfeeding: is my baby getting enough milk?' (nhs.uk/baby/breastfeeding-and-bottle-feeding/breastfeeding-problems/enough-milk/): "
      "\"From day 5 onwards… at least 6 heavy, wet nappies every 24 hours\"; \"From the fourth day, they should do at least 2 soft, yellow poos… "
      "every day for the first few weeks\"; long, rhythmic sucks and swallows; baby comes off the breast by themselves at the end of feeds; "
      "steady weight gain after the first few days; \"ask for help early.\""),
     ("Littlefold tile: 'Breastfeeding? 5 signs it's going well' in a large serif above a taped yellow sticky note with ticks: 6+ heavy wet "
      "diapers a day (from day 5 after birth); 2+ soft yellow poops a day (from day 4 after birth); long sucks and swallows; lets go of the "
      "breast on their own; steady weight gain. A halftone baby shoe, the handwritten note 'do this: count wet diapers for 24 hours', and "
      "'Source: NHS'."))

# ================================================================================================ B2. FF reframe
HOURLY = 750 / 40
assert HOURLY == 18.75 and 150 / HOURLY == 8


def ff_reframe():
    f = K.FIELDS[FF]["lite"]
    ink = f["ink"]
    card = lambda lab, q, bg, strike=False: (
        f'<div style="background:{bg};border:3px solid {ink};border-radius:40px;padding:38px 54px 44px;box-shadow:0 12px 0 {ink}">'
        f'<div class="hand" style="font-size:76px;text-align:left">{lab}</div>'
        f'<div class="S" style="font-size:104px;text-align:left;margin-top:10px;color:{ink};'
        + (f'text-decoration:line-through;text-decoration-thickness:7px;text-decoration-color:{K.ACCENT[FF]};opacity:.8' if strike else '')
        + f'">{q}</div></div>')
    body = C.kicker(FF, f, "say it differently", 90)
    body += (f'<div style="position:absolute;left:80px;right:80px;top:180px;display:flex;flex-direction:column;gap:40px;z-index:2">'
             + card("Instead of…", "“It's only $150.”", "#FBF2DF", True)
             + card("Say…", f'“That\'s <span class="pill" style="background:{f["p2"]}">8 hours</span> of work.”', "#FFFFFF")
             + '</div>')
    body += (f'<div style="position:absolute;left:90px;right:90px;top:960px;font:600 40px/1.3 Inter;color:{ink};z-index:3">'
             f'<span style="font-weight:800">The maths:</span> $750 take-home a week<br>÷ 40 hours = $18.75 an hour</div>')
    body += (f'<div style="position:absolute;left:90px;right:260px;top:1110px;font:600 40px/1.25 Inter;color:{ink};z-index:3">'
             f'<span class="hand" style="font-size:60px;color:{K.ACCENT[FF]}">Do this:</span> before any buy over $50, divide by your hourly take-home.</div>')
    body += K.stamp(FF, W - 250, H - 250, 190, -12)
    return C.page(FF, "lite", body, W, H)


post("ff-1027-hours-not-dollars", FF, "2026-10-27T12:00:00-04:00", [ff_reframe],
     ("Before you buy, turn the price into hours of your work.\n\n"
      "Why it works: \"$150\" is just a number. \"8 hours\" is most of a workday you've already lived. It makes you ask whether it's worth "
      "it, not just whether you can pay.\n\n"
      "The maths (pay made up for this post): $750 take-home for a 40-hour week is $18.75 an hour. $150 ÷ $18.75 = 8 hours.\n\n"
      "Find your number: your last pay after tax ÷ the hours you worked in that pay period.\n\n"
      "The catch: this isn't about never buying. It's about buying the things that are worth the hours.\n\n"
      "Do this: before any buy over $50, divide the price by your hourly take-home.\n\n"
      "Send this to whoever says \"it's only…\".\n\n"
      "Rich Habits, Decoded No. 2 is tomorrow at 5 pm.\n\n"
      + FOLLOW[FF] + "\n\n#personalfinance #moneytips #budgeting #mindfulspending #fullyfunded"),
     ("Maths: $750 ÷ 40 hours = $18.75 an hour; $150 ÷ $18.75 = 8 hours. Pay made up for this post; use your own take-home pay. "
      "Education only, not financial advice."),
     ("Fully Funded tile, a 'say it differently' card. Instead of: 'It's only $150.' (crossed out). Say: 'That's 8 hours of work.' "
      "Line: The maths: $750 take-home a week ÷ 40 hours = $18.75 an hour. Do this: before any buy over $50, divide by your hourly take-home."))

# ================================================================================================ B3. LH emoji meme
LH27 = [lh_page(f"""
<div style='position:absolute;left:80px;top:90px'><span class='label' style='font-size:24px;padding:10px 16px'>Focus science</span></div>
<div style='position:absolute;left:70px;right:70px;top:170px'>{L.dual("Nervous before a test? / *Write it out.*", style="font-size:118px")}</div>
<div style='position:absolute;left:0;right:0;top:500px;text-align:center;font-family:"Noto Color Emoji";font-size:250px;line-height:1'>😰<span style='font-family:Inter;font-weight:900;font-size:150px;color:{INK};vertical-align:40px;margin:0 40px'>→</span>📝</div>
<div class='card' style='left:110px;right:110px;top:840px;padding:34px 40px'>
 <div class='hand' style='font-size:64px;line-height:1.05'>Right before the test: write every worry down, 10 minutes.</div></div>
<div class='mono' style='position:absolute;left:90px;right:90px;top:1170px;font-size:22px;opacity:.85'>Ramirez &amp; Beilock 2011, Science</div>
{L.stamp(880, 1110, 140, -10)}""", "cream", "", "FOCUS SCIENCE")]
post("lh-1027-write-the-worry", LH, "2026-10-27T12:30:00-04:00", LH27,
     ("Nervous before a test? Write it out. Right before the test, write every worry down for 10 minutes.\n\n"
      "The research: in a study published in Science, students spent 10 minutes before a high-pressure test writing about their worries. "
      "In the lab, the writers did better under pressure while the students who sat quietly slipped. In a high school biology final, the "
      "most anxious students who wrote scored about a B+, against a B– for the most anxious students who didn't.\n\n"
      "Why: worries take up working memory, the mental space you need for the test. Putting them on paper frees some of it.\n\n"
      "How: 10 minutes before, open a notebook or your phone notes. Write exactly what you're worried about, honestly. Then close it and go in.\n\n"
      "The catch: small studies, and about tests. Worth trying, not a cure.\n\n"
      "Do this: before your next exam, set a 10-minute timer and write every worry down.\n\n"
      "Send this to someone with an exam this week.\n\n"
      "One Word No. 3 is tomorrow at 5 pm.\n\n"
      + FOLLOW[LH] + "\n\n#studytips #testanxiety #focus #examseason #lockedhour"),
     ("Source: Ramirez, G. & Beilock, S. L. (2011), 'Writing about testing worries boosts exam performance in the classroom', Science "
      "331(6014), 211–213, doi:10.1126/science.1199427. Lab: 20 students under pressure; 10 minutes of expressive writing; the control group "
      "dropped 12% in accuracy, writers gained 5%. Classroom: highly anxious 9th-grade biology students who wrote averaged B+, vs B– for "
      "those who didn't."),
     ("Locked Hour tile, emoji meme: 'Nervous before a test? Write it out.' in a large serif with highlighted words, then a worried-face emoji, "
      "an arrow and a notepad emoji, and a card: 'Right before the test: write every worry down, 10 minutes.' Source: Ramirez & Beilock 2011, Science."))

# ================================================================================================ B4. HB sticky
HB27 = dict(lay="sticky", f="indi", text="4 checks before you send / *AI's draft*", obj="chat", at="bl",
            items=["Every number and date", "Every name, spelled right", "No promises you didn't make", "Sounds like you"],
            save="send this to whoever writes emails with AI")
post("hb-1027-check-before-send", HB, "2026-10-27T13:00:00-04:00", [sticky(HB, HB27, wide=True)],
     ("AI wrote your message? 4 checks before you send AI's draft.\n\n"
      "Why: AI writes smoothly, and when a detail is missing it can fill the gap with something that sounds right. A confident sentence "
      "isn't a checked one.\n\n"
      "The 4 checks:\n"
      "1. Every number and date matches what you meant.\n"
      "2. Every name is spelled right.\n"
      "3. No promises you didn't make: nothing it agrees to or claims that you didn't say.\n"
      "4. It sounds like you. Swap any word you'd never use.\n\n"
      "Privacy tip: ask for the draft with \"my landlord\" or \"my manager\" instead of real names, then add the names yourself.\n\n"
      "Do this: next time AI writes a message for you, read it once for these 4 before you send.\n\n"
      "Send this to whoever writes emails with AI.\n\n"
      "AI, for real · Day 9 is tomorrow at 5:45 pm: a real test, with the output shown.\n\n"
      + FOLLOW[HB] + "\n\n#ai #aitips #chatgpt #productivity #hourback"),
     "General guidance on how chat AI writes; no study figures are claimed.",
     ("Hourback tile: '4 checks before you send AI's draft' in a large serif above a taped yellow sticky note with ticks: every number and "
      "date; every name, spelled right; no promises you didn't make; sounds like you. Black-and-white chat bubbles and the handwritten note "
      "'send this to whoever writes emails with AI'."))


# ================================================================================================ Mon Oct 26 series covers: same save-line fix
def monday_fixes(ids):
    """Re-render ff-richhabits-01 and hb-day8-ask-me-first in place with the clearer series line (gate, Oct 24). Same specs otherwise."""
    import re
    r = C.R()
    try:
        if "ff-richhabits-01" in ids:
            sys.path.insert(0, str(REPO / "studio/recovery-oct22/fullyfunded/build"))
            import richhabits as RH  # noqa: E402  (its own C.place hook draws the 'paycheque left' chart)
            cov = dict(RH.COVER, save=SAVE)
            body = lift_save(C.LAYOUTS["pills"](FF, cov)).replace("width:620px;font-size:66px", "width:470px;font-size:62px", 1)
            n = 1 + len(RH.SLIDES)
            r.shot(C.page(FF, cov["f"], body, W, H), W, H, RH.OUT / "01.jpg")
            # cover only: slides 2-3 stay as committed (re-rendering them would bring back retired props)
            print("ff-richhabits-01", sorted(p.name for p in RH.OUT.glob("*.jpg")), flush=True)
        if "hb-day8-ask-me-first" in ids:
            import series_oct26  # noqa: F401,E402  (registers its specs; main() is NOT called)
            import specs
            sp = specs.POSTS["hb-day8-ask-me-first"]
            cov = dict(sp["cover"], save=SAVE)
            d = REPO / "media" / "hb-day8-ask-me-first"
            n = 1 + len(sp["slides"])
            r.shot(C.page(HB, cov["f"], lift_save(C.lay_pills(HB, cov)), W, H), W, H, d / "01.jpg")
            # cover only: slides 2-3 stay as committed (the shared inner_list draws the retired pointing hand)
            print("hb-day8-ask-me-first", sorted(p.name for p in d.glob("*.jpg")), flush=True)
    finally:
        r.close()
    q = json.loads((REPO / "schedule" / "posts.json").read_text())
    for post_ in q["posts"]:
        if post_["id"] in ids:
            e = dict(post_)
            e["alt_text"] = e["alt_text"].replace("'mon · wed · fri'", "'new one every Mon · Wed · Fri'")
            (OUT_JSON / f"{e['id']}.json").write_text(json.dumps(e, indent=2, ensure_ascii=False) + "\n")


FF01_S3 = dict(f="cob", text="Then raise it / *with every raise.*",
               sub="In one study, workers who did went from saving 3.5% to 13.6%.", src="Thaler &amp; Benartzi, 2004")


def ff01_slide3():
    """CD gate Oct 24: ff-richhabits-01 slide 3 ties the number to the habit. Slide 3 ONLY (plain inner(): no hand, no piggy)."""
    out = REPO / "media/recovery-oct22/fullyfunded/ff-richhabits-01/03.jpg"
    r = C.R()
    try:
        r.shot(C.page(FF, FF01_S3["f"], C.inner(FF, FF01_S3, 2, 3), W, H), W, H, out)
    finally:
        r.close()
    jp = OUT_JSON / "ff-richhabits-01.json"
    e = json.loads(jp.read_text())
    old_cap = ("WHY IT WORKS: you don't rely on willpower. In the 'Save More Tomorrow' study, workers who signed up to save automatically, "
               "with the rate rising at each raise, went from saving 3.5% of pay to 13.6% over 40 months.")
    assert old_cap in e["caption"], "caption line moved"
    e["caption"] = e["caption"].replace(old_cap, (
        "WHY IT WORKS: you don't rely on willpower. Then raise it with every raise: in the 'Save More Tomorrow' study, workers who "
        "saved automatically and raised the rate at each pay raise went from saving 3.5% of pay to 13.6% over 40 months."))
    old_alt = "Slide 3: Saving rate 3.5% → 13.6% (in one study, as it rose with every raise). Source: Thaler & Benartzi, 2004."
    assert old_alt in e["alt_text"], "alt line moved"
    e["alt_text"] = e["alt_text"].replace(old_alt, ("Slide 3: Then raise it with every raise. (In one study, workers who did went from "
                                                      "saving 3.5% to 13.6%.) Source: Thaler & Benartzi, 2004."))
    jp.write_text(json.dumps(e, indent=2, ensure_ascii=False) + "\n")
    print(out)


# ================================================================================================ build
def build(ids):
    r = C.R()
    OUT_JSON.mkdir(parents=True, exist_ok=True)
    try:
        for pid in ids:
            m = POSTS[pid]
            d = REPO / "media" / pid
            d.mkdir(exist_ok=True)
            for old in d.glob("*.jpg"):
                old.unlink()
            files = []
            for i, fn in enumerate(m["pages"], 1):
                r.shot(fn(), W, H, d / f"{i:02d}.jpg")
                files.append(f"{pid}/{i:02d}.jpg")
            js = dict(id=pid, account=m["brand"], publish_at=m["at"], caption=m["caption"], first_comment=m["comment"],
                      alt_text=m["alt"], images=files)
            (OUT_JSON / f"{pid}.json").write_text(json.dumps(js, indent=2, ensure_ascii=False) + "\n")
            print(pid, files, flush=True)
    finally:
        r.close()


if __name__ == "__main__":
    if sys.argv[1:] == ["ff-richhabits-01-s3"]:
        ff01_slide3()
        sys.exit()
    MON = {"ff-richhabits-01", "hb-day8-ask-me-first"}
    args = sys.argv[1:] or list(POSTS)
    if [a for a in args if a in MON]:
        monday_fixes([a for a in args if a in MON])
    if [a for a in args if a not in MON]:
        build([a for a in args if a not in MON])
