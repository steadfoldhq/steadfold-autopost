"""FF round 2 · 'Spot the mistake' (payday). Example numbers, made up and labelled. Education only."""
from r2 import *  # noqa: F403

COB, DEEP, CORAL, PEACH, SOFT, INK, WHITE = (hexc(x) for x in ("2B3FE0", "16206B", "FF6A3D", "FFB08F", "F5F7FF", "0E1440", "FFFFFF"))
YEL, GREEN = hexc("FFD63B"), hexc("1FAF6B")

S = Script("ff-r2-spot-the-mistake", skip={"Pause and spot it.", "Flip it.", "Small and automatic.", "Beats big and skipped."}, hold={"whatever's left.": 2.4}, out_name="FF-R2-spot-the-mistake")
P = S.p
K_ROWS = [S.phrase("Rent"), S.phrase("Bills and"), S.phrase("Fun money"), S.phrase("Savings:")]
K_LEFT, K_FOUR, K_VANISH, K_FIRST, K_LANDS, K_CATCH, K_LAST = (
    S.phrase("whatever's left."), S.phrase("number four"), S.phrase("vanish"), S.phrase("move first"), S.phrase("lands"),
    S.phrase("The catch"), S.phrase("spot it"))
T_HOLD = S.words[S.ph[K_LEFT][-1]][2] + 0.1
ROWS = [("1", "Rent", "900"), ("2", "Bills + groceries", "600"), ("3", "Fun money", "300"), ("4", "Savings", "whatever's left")]


def row(img, y, num, label, amt, t0, t, state=None, dx=0):
    a = pop(t, t0, 0.3)
    if a <= 0:
        return
    L = layer()
    bad = state == "bad"
    good = state == "good"
    box(L, (80, y, W - 80, y + 120), 30, (255, 236, 230, 255) if bad else SOFT, shadow=(0, 10, DEEP))
    d = ImageDraw.Draw(L)
    d.ellipse((104, y + 18, 188, y + 102), fill=CORAL if bad else (GREEN if good else COB))
    T(L, num, 146, y + 60, 50, WHITE, key=f"n{num}")
    T(L, label, 220, y + 60, 54, INK, f="xbold", anchor="lm", key=f"l{num}{label}")
    T(L, amt, W - 120, y + 60, 54 if len(amt) < 8 else 44, CORAL if bad else INK, f="black", anchor="rm", key=f"a{num}{amt}")
    put(img, L, 0.85 + 0.15 * min(1, a), W / 2, y + 60, alpha=min(1, a * 1.6), dx=dx)
    if bad:
        emoji(img, "❌", W - 70, y + 10, 90 * min(1, pop(t, P(K_FOUR))), rot=-10)
    if good:
        emoji(img, "✅", W - 70, y + 10, 90 * min(1, pop(t, P(K_FIRST) + 0.4)), rot=8)


def frame(t):
    img = dots_bg(COB, (255, 255, 255, 22), t)
    k = S.at(t) or 0
    if t >= S.end_voice:
        endcard(img, S, t, COB, "fullyfunded.png")
        return img
    if k < K_CATCH:
        T(img, "SPOT THE MISTAKE", W / 2, 240, 104, WHITE, key="hook")
        # payday card
        a = pop(t, 0.0, 0.35) if t > 0.05 else 1.0
        L = layer()
        box(L, (160, 340, W - 160, 500), 40, YEL, shadow=(0, 14, DEEP))
        T(L, "PAYDAY +2,000", W / 2, 420, 76, INK, key="payday")
        put(img, L, 0.9 + 0.1 * min(1, a), W / 2, 420)
        emoji(img, "💸", 175, 350, 110, rot=-14)
        sx, sy = shake(t, P(K_FOUR), 0.3, 18)
        ys = [560, 700, 840, 980]
        if t < P(K_FIRST):
            order = [0, 1, 2, 3]
            for i, (num, lab, amt) in enumerate(ROWS):
                st = "bad" if (i == 3 and t >= P(K_FOUR)) else None
                row(img, ys[i], num, lab, amt, P(K_ROWS[i]) - 0.6 if i < 3 else P(K_ROWS[i]) - 0.6, t, st, dx=sx if i == 3 else 0)
        else:
            u = ease((t - P(K_FIRST)) / 0.6)
            new = {3: 0, 0: 1, 1: 2, 2: 3}
            for i, (num, lab, amt) in enumerate(ROWS):
                y = ys[i] + (ys[new[i]] - ys[i]) * u
                if i == 3:
                    row(img, y, "1", "Savings", "FIRST", -1, t, "good")
                else:
                    row(img, y, str(new[i] + 1), lab, amt, -1, t)
        if t >= 0.3:
            T(img, "EXAMPLE NUMBERS", W / 2, 1150, 40, PEACH, f="xbold", key="example")
    if T_HOLD <= t < P(K_FOUR) - 0.05:
        u = (t - T_HOLD) / (P(K_FOUR) - 0.05 - T_HOLD)
        L = layer()
        d = ImageDraw.Draw(L)
        d.arc((440, 1120 - 230, 640, 1120 - 30), -90, -90 + 360 * (1 - u), fill=YEL, width=22)
        put(img, L)
        emoji(img, "⏳", W / 2, 990, 100, rot=180 * u)
    if k >= K_CATCH:
        a = pop(t, P(K_CATCH), 0.35)
        L = layer()
        box(L, (80, 380, W - 80, 1060), 40, SOFT, shadow=(0, 18, DEEP))
        box(L, (300, 430, 780, 520), 45, CORAL)
        T(L, "THE CATCH", W / 2, 475, 54, WHITE, key="catch")
        T(L, "Bills eat it all?", W / 2, 640, 76, INK, key="c1")
        T(L, "Start tiny.", W / 2, 760, 96, CORAL, key="c2")
        T(L, "Automatic beats big.", W / 2, 900, 60, INK, f="xbold", key="c3")
        put(img, L, 0.7 + 0.3 * min(1.0, a), W / 2, 720, alpha=min(1, a * 1.5))
        if k >= K_LAST:
            emoji(img, "👇", W / 2, 1520 + 14 * math.sin(t * 8), 110)
    captions(img, S, t, y=1300, size=100, lit=YEL, stroke=INK)
    return img


cues = ([("sfx-cash", 0.05, -10)] + [("sfx-paper", P(K_ROWS[i]) - 0.6, -8) for i in range(4)] +
        [("sfx-tick-ding", T_HOLD + 0.8 * i, -8) for i in range(3)] +
        [("sfx-record-scratch", P(K_FOUR) - 0.05, -9), ("sfx-whoosh-fast", P(K_FIRST), -9), ("st-2-ta-da-el", P(K_FIRST) + 0.4, -12),
         ("sfx-whoosh-soft", P(K_CATCH) - 0.1, -9), ("sfx-whoosh-soft", S.end_voice - 0.15, -10)])

if __name__ == "__main__":
    finish(S, frame, cues)
