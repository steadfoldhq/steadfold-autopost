"""FF round 2 · 'Who has more at 65?' (pause and guess, comment 1 or 2).
Example math, 8% a year, monthly compounding, deposits at month end:
  Maya 200/mo from 25 to 35 (24,000 in), then nothing:  36,589 at 35 -> ~400,130 at 65
  Jay  200/mo from 35 to 65 (72,000 in):                 ~298,072 at 65
"""
from r2 import *  # noqa: F403

COB, DEEP, CORAL, PEACH, SOFT, INK, WHITE = (hexc(x) for x in ("2B3FE0", "16206B", "FF6A3D", "FFB08F", "F5F7FF", "0E1440", "FFFFFF"))
YEL = hexc("FFD63B")


def fv(p, n, r=0.08 / 12, b=0.0):
    for _ in range(n):
        b = b * (1 + r) + p
    return b


MAYA = fv(200, 120) * (1 + 0.08 / 12) ** 360
JAY = fv(200, 360)
assert round(MAYA, -3) == 400000 and round(JAY, -3) == 298000

S = Script("ff-r2-who-has-more", skip={0, 4, 8, 16, 21}, hold={6: 2.4}, out_name="FF-R2-who-has-more")
P = S.p
K_COMMENT, K_MIN, K_JIN, K_JAY, K_AND, K_MAYA, K_THIRD, K_TIME, K_CATCH, K_LAST = (
    S.phrase("Comment"), S.phrase("Maya put in"), S.phrase("Jay put in"), S.phrase("Jay has about"), S.phrase("And Maya"),
    S.phrase("About 400"), S.phrase("A third"), S.phrase("secret"), S.phrase("The catch"), S.phrase("guess right"))
T_HOLD = S.words[S.ph[K_COMMENT][-1]][2] + 0.1          # countdown starts after "Comment 1 or 2."


def money(v):
    return f"{int(round(v, -2)):,}"


def card(img, t, x0, who, num, emo, col, fg, seg, t_seg, inn, t_in, at65, t_65, win):
    L = layer()
    box(L, (x0, 400, x0 + 450, 1100), 36, col, shadow=(0, 16, DEEP))
    # number badge + name
    d = ImageDraw.Draw(L)
    d.ellipse((x0 + 26, 424, x0 + 116, 514), fill=YEL if col == CORAL else CORAL)
    T(L, num, x0 + 71, 469, 64, INK, key=f"num{num}")
    T(L, who, x0 + 290, 469, 72, fg, key=f"name{num}")
    emoji(L, emo, x0 + 225, 620, 150)
    T(L, "200/mo", x0 + 225, 735, 50, fg, f="xbold", key=f"amt{num}")
    # timeline 25 -> 65
    tx0, tx1, ty = x0 + 50, x0 + 400, 810
    box(L, (tx0, ty - 14, tx1, ty + 14), 14, (0, 0, 0, 40))
    a, b = seg
    p = ease((t - t_seg) / 1.2) if t >= t_seg else 0
    xa, xb = tx0 + (tx1 - tx0) * (a - 25) / 40, tx0 + (tx1 - tx0) * (a - 25 + (b - a) * p) / 40
    if p > 0:
        box(L, (xa, ty - 14, max(xa + 28, xb), ty + 14), 14, YEL if col == CORAL else COB)
    for age in (25, 35, 65):
        T(L, str(age), tx0 + (tx1 - tx0) * (age - 25) / 40, ty + 50, 38, fg, f="bold", key=f"age{num}{age}")
    # money rows
    if t >= t_in:
        a1 = pop(t, t_in)
        T(L, f"IN {inn}", x0 + 225, 925, 52, fg, f="xbold", alpha=min(1, a1), key=f"in{num}", words=2)
    if t >= t_65:
        q = ease((t - t_65) / 1.1)
        T(L, money(at65 * q) if q < 1 else "≈" + money(at65), x0 + 225, 1020, 74 if not win else 80,
          YEL if (win and col == CORAL) else (CORAL if win else fg), key=f"at65{num}", words=1)
    return L


def frame(t):
    img = dots_bg(COB, (255, 255, 255, 22), t)
    k = S.at(t) or 0
    if t >= S.end_voice:
        endcard(img, S, t, COB, "fullyfunded.png")
        return img
    # top: the question that opens the gap (frame 0) - stays until the catch
    if k < K_CATCH:
        T(img, "WHO HAS MORE AT 65?", W / 2, 250, 96, WHITE, stroke=0, key="hook")
    if k < K_CATCH:
        out = ease((t - P(K_CATCH) + 0.35) / 0.35) if t > P(K_CATCH) - 0.35 else 0
        dx0, dy0 = shake(t, P(K_MAYA) + 0.9, 0.35, 20)
        Lm = card(img, t, 70, "MAYA", "1", "👩", CORAL, WHITE, (25, 35), P(1), "24,000", P(K_MIN), MAYA, P(K_MAYA), True)
        Lj = card(img, t, 560, "JAY", "2", "👨", SOFT, INK, (35, 65), P(3), "72,000", P(K_JIN), JAY, P(K_JAY), False)
        put(img, Lm, 1.0, dx=dx0 - out * 700, dy=dy0)
        put(img, Lj, 1.0, dx=dx0 + out * 700, dy=dy0)
        if t >= P(K_MAYA) + 1.0:
            emoji(img, "👑", 295, 380, 130 * min(1, pop(t, P(K_MAYA) + 1.0)), rot=-12)
        if K_THIRD <= k < K_CATCH:
            emoji(img, "⏳", 470, 640, 120 * min(1, pop(t, P(K_TIME))), rot=10) if t >= P(K_TIME) else None
        if t >= P(K_MIN):
            T(img, "EXAMPLE · 8% A YEAR", W / 2, 1150, 40, PEACH, f="xbold", key="example")
    # pause-and-guess: a draining ring, no words
    if T_HOLD <= t < P(K_MIN) - 0.05:
        u = (t - T_HOLD) / (P(K_MIN) - 0.05 - T_HOLD)
        L = layer()
        d = ImageDraw.Draw(L)
        d.rounded_rectangle((60, 390, W - 60, 1110), 40, fill=(14, 20, 64, 150))
        d.arc((390, 600, 690, 900), -90, -90 + 360 * (1 - u), fill=YEL, width=26)
        put(img, L, alpha=min(1, (t - T_HOLD) / 0.15))
        emoji(img, "⏳", W / 2, 750, 130, rot=180 * u)
    # the catch
    if k >= K_CATCH:
        a = pop(t, P(K_CATCH), 0.35)
        L = layer()
        box(L, (80, 420, W - 80, 1080), 40, SOFT, shadow=(0, 18, DEEP))
        box(L, (300, 470, 780, 560), 45, CORAL)
        T(L, "THE CATCH", W / 2, 515, 54, WHITE, key="catch")
        T(L, "Example math.", W / 2, 680, 70, INK, key="c1")
        T(L, "Not a promise.", W / 2, 775, 70, INK, key="c2")
        T(L, "Returns swing. Fees and inflation bite.", W / 2, 920, 52, CORAL, f="xbold", maxw=820, key="c3")
        put(img, L, 0.7 + 0.3 * min(1.0, a), W / 2, 750, alpha=min(1, a * 1.5))
        if k >= K_LAST:
            emoji(img, "👇", W / 2, 1520 + 14 * math.sin(t * 8), 110)
    captions(img, S, t, y=1300, size=100, lit=YEL, stroke=INK)
    return img


cues = [("sfx-tick-ding", 0.0, -10), ("sfx-whoosh-soft", P(1) - 0.1, -10), ("sfx-whoosh-soft", P(3) - 0.1, -10),
        ("sfx-tick-ding", T_HOLD, -8), ("sfx-tick-ding", T_HOLD + 0.8, -8), ("sfx-tick-ding", T_HOLD + 1.6, -8),
        ("sfx-cash", P(K_JAY) + 0.9, -12), ("st-3-wait-for-it-el", P(K_AND) - 0.1, -14), ("st-2-ta-da-el", P(K_MAYA) + 0.85, -9),
        ("sfx-record-scratch", P(K_CATCH) - 0.05, -10), ("sfx-whoosh-soft", S.end_voice - 0.15, -10)]

if __name__ == "__main__":
    finish(S, frame, cues)
