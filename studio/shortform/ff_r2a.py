"""FF round 2 · 'Who has more at 65?' (pause and guess, comment 1 or 2).
Maths stated directly (8% a year, monthly compounding, deposits at month end), computed below:
  Maya $200/mo from 25 to 35 ($24,000 in), then nothing:  36,589 at 35 -> ~$400,130 at 65
  Jay  $200/mo from 35 to 65 ($72,000 in):                 ~$298,072 at 65
'Not guaranteed. Returns vary. Education, not advice.' goes in the post caption only.
Round 2b (Oct 16 pm): one Eleven v3 take, continuous bed + room tone, floating text, colour scenes with bold cuts."""
from r2 import *  # noqa: F403

COB, DEEP, CORAL, SOFT, INK, WHITE = (hexc(x) for x in ("2B3FE0", "16206B", "D9481C", "F5F7FF", "0E1440", "FFFFFF"))
YEL = hexc("FFD63B")


def fv(p, n, r=0.08 / 12, b=0.0):
    for _ in range(n):
        b = b * (1 + r) + p
    return b


MAYA = fv(200, 120) * (1 + 0.08 / 12) ** 360
JAY = fv(200, 360)
assert round(MAYA, -3) == 400000 and round(JAY, -3) == 298000

S = Script("ff-r2-who-has-more-v3-t2", hold={"comment 1 or 2.": 2.4}, out_name="FF-R2-who-has-more")
P = S.p
K_STOP, K_JAYST, K_Q, K_COMMENT, K_MIN, K_JIN, K_JAY, K_AND, K_MAYA, K_THIRD, K_TIME, K_RATE, K_EARLY, K_LAST = (
    S.phrase("She stops"), S.phrase("Jay starts"), S.phrase("Who has more"), S.phrase("Pause and guess"), S.phrase("Maya put in"),
    S.phrase("Jay put in"), S.phrase("Jay has about"), S.phrase("And Maya"), S.phrase("About $400"), S.phrase("A third"),
    S.phrase("secret"), S.phrase("8% a year"), S.phrase("Ten years early"), S.phrase("guess right"))
T_HOLD = S.words[S.ph[K_COMMENT][-1]][2] + 0.1          # countdown starts after "comment 1 or 2."
SCENES = [(0, COB, (255, 255, 255, 22)), (P(K_MIN), DEEP, (255, 255, 255, 18)), (P(K_TIME), YEL, (14, 20, 64, 26))]
CUTS = [(P(K_MIN), YEL, "wipeR"), (P(K_TIME), CORAL, "iris")]


def money(v):
    return "$" + f"{int(round(v, -2)):,}"


def card(t, x0, who, num, emo, col, fg, seg, t_seg, inn, t_in, at65, t_65, win):
    L = layer()
    box(L, (x0, 400, x0 + 450, 1110), 36, col, shadow=(0, 16, (0, 0, 0, 70)))
    d = ImageDraw.Draw(L)
    d.ellipse((x0 + 26, 424, x0 + 116, 514), fill=YEL if col == CORAL else COB)
    T(L, num, x0 + 71, 469, 64, INK if col == CORAL else WHITE, key=f"num{num}")
    T(L, who, x0 + 290, 469, 72, fg, key=f"name{num}")
    emoji(L, emo, x0 + 225, 620, 150)
    T(L, "$200/mo", x0 + 225, 735, 54, fg, f="xbold", key=f"amt{num}")
    tx0, tx1, ty = x0 + 50, x0 + 400, 810
    box(L, (tx0, ty - 14, tx1, ty + 14), 14, (0, 0, 0, 40))
    a, b = seg
    p = ease((t - t_seg) / 1.2) if t >= t_seg else 0
    xa, xb = tx0 + (tx1 - tx0) * (a - 25) / 40, tx0 + (tx1 - tx0) * (a - 25 + (b - a) * p) / 40
    if p > 0:
        box(L, (xa, ty - 14, max(xa + 28, xb), ty + 14), 14, YEL if col == CORAL else COB)
    for age in (25, 35, 65):
        T(L, str(age), tx0 + (tx1 - tx0) * (age - 25) / 40, ty + 50, 40, fg, f="bold", key=f"age{num}{age}")
    if t >= t_in:
        a1 = pop(t, t_in)
        T(L, f"IN {inn}", x0 + 225, 935, 54, fg, f="xbold", alpha=min(1, a1), key=f"in{num}", words=2)
    if t >= t_65:
        q = ease((t - t_65) / 1.1)
        T(L, money(at65 * q) if q < 1 else "≈" + money(at65), x0 + 225, 1035, 80 if win else 72, fg, key=f"at65{num}", words=1)
    return L


def frame(t):
    img = scene_bg(t, SCENES)
    k = S.at(t) or 0
    if t >= S.end_voice:
        endcard(img, S, t, COB, "fullyfunded.png")
        return img
    if t < P(K_TIME):
        T(img, "WHO HAS MORE AT 65?", W / 2, 250, 96, WHITE, key="hook")
        guessing = T_HOLD <= t < P(K_MIN) - 0.05
        dx0, dy0 = shake(t, P(K_MAYA) + 0.9, 0.35, 20)
        Lm = card(t, 70, "MAYA", "1", "👩", CORAL, WHITE, (25, 35), P(1), "$24,000", P(K_MIN), MAYA, P(K_MAYA), True)
        Lj = card(t, 560, "JAY", "2", "👨", SOFT, INK, (35, 65), P(K_JAYST), "$72,000", P(K_JIN), JAY, P(K_JAY), False)
        a0 = 0.25 if guessing else 1.0
        intro = pop(t, 0.0, 0.35) if t > 0.03 else 1.0
        put(img, Lm, 1.0, alpha=a0, dx=dx0 - (1 - min(1, intro)) * 500, dy=dy0)
        put(img, Lj, 1.0, alpha=a0, dx=dx0 + (1 - min(1, intro)) * 500, dy=dy0)
        if t >= P(K_MAYA) + 1.0:
            emoji(img, "👑", 505, 425, 96 * min(1, pop(t, P(K_MAYA) + 1.0)), rot=14)   # card corner, clear of the rate line
        if guessing:   # pause-and-guess: a draining ring floats over the dimmed cards, no words
            u = (t - T_HOLD) / (P(K_MIN) - 0.05 - T_HOLD)
            L = layer()
            ImageDraw.Draw(L).arc((370, 590, 710, 930), -90, -90 + 360 * (1 - u), fill=YEL, width=28)
            put(img, L, 1.0 + 0.06 * math.sin(t * 9))
            emoji(img, "⏳", W / 2, 760, 140, rot=180 * u)
        if t >= P(K_MIN):
            T(img, "$200/MO · 8% A YEAR", W / 2, 345, 46, YEL, f="xbold", key="rate")
    else:
        q = pop(t, P(K_TIME) + 0.05, 0.35)
        T(img, "TIME", W / 2, 420, 300, INK, key="time", scale=0.8 + 0.2 * min(1, q))
        T(img, "beat money.", W / 2, 600, 110, COB, key="beat")
        if t >= P(K_RATE):
            T(img, "$200 a month at 8% a year", W / 2, 760, 58, INK, f="xbold", key="rate2")
        if t >= P(K_EARLY):
            T(img, "10 years early", W / 2, 900, 84, COB, key="early", words=3)
            T(img, "beat 30 years late.", W / 2, 1010, 84, INK, key="late", words=4)
        emoji(img, "⏳", 860, 300, 130 * min(1, q), rot=12)
        if k >= K_LAST:
            emoji(img, "👇", W / 2, 1560 + 14 * math.sin(t * 8), 110)
    if t >= P(K_TIME):
        captions(img, S, t, y=1300, size=100, fill=INK, lit=COB)
    else:
        captions(img, S, t, y=1300, size=100, fill=WHITE, lit=YEL)
    img = transition(img, t, CUTS)
    return img


cues = [("sfx-tick-ding", 0.05, -10), ("sfx-whoosh-soft", P(1) - 0.1, -10), ("sfx-whoosh-soft", P(K_JAYST) - 0.1, -10),
        ("sfx-tick-ding", T_HOLD, -8), ("sfx-tick-ding", T_HOLD + 0.8, -8), ("sfx-tick-ding", T_HOLD + 1.6, -8),
        ("sfx-whoosh-fast", P(K_MIN) - 0.17, -9), ("sfx-cash", P(K_JAY) + 0.9, -12), ("st-3-wait-for-it-el", P(K_AND) - 0.1, -14),
        ("st-2-ta-da-el", P(K_MAYA) + 0.85, -9), ("sfx-whoosh-soft", P(K_TIME) - 0.17, -8)]

if __name__ == "__main__":
    finish(S, frame, cues, bed="v3/ff-c-confident-build-el.mp3")
