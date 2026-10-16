"""FF round 2 · 'Spot the mistake' (payday). Illustrative numbers. Education only; the legal line goes in the caption.
Round 2b (Oct 16 pm): one Eleven v3 take, continuous bed + room tone, floating text, colour scenes with bold cuts."""
from r2 import *  # noqa: F403

COB, DEEP, CORAL, SOFT, INK, WHITE = (hexc(x) for x in ("2B3FE0", "16206B", "D9481C", "F5F7FF", "0E1440", "FFFFFF"))
YEL, GREEN, PEACH = hexc("FFD63B"), hexc("128A52"), hexc("FFB08F")

S = Script("ff-r2-spot-the-mistake-v3-t2", hold={"Pause and spot it.": 2.4}, out_name="FF-R2-spot-the-mistake")
P = S.p
K_ROWS = [S.phrase("Rent"), S.phrase("Bills and"), S.phrase("Fun money"), S.phrase("Savings...")]
K_SPOT, K_FOUR, K_VANISH, K_FLIP, K_FIRST, K_LANDS, K_CATCH, K_TINY, K_SMALL, K_LAST = (
    S.phrase("Pause and spot"), S.phrase("number four"), S.phrase("vanish"), S.phrase("Flip it"), S.phrase("move first"),
    S.phrase("lands"), S.phrase("Bills eat"), S.phrase("Start tiny"), S.phrase("Small and automatic"), S.phrase("Did you spot"))
T_HOLD = S.words[S.ph[K_SPOT][-1]][2] + 0.1
ROWS = [("1", "Rent", "$900"), ("2", "Bills + groceries", "$600"), ("3", "Fun money", "$300"), ("4", "Savings", "whatever's left")]
SCENES = [(0, COB, (255, 255, 255, 22)), (P(K_FOUR), CORAL, (255, 255, 255, 26)), (P(K_FLIP), DEEP, (255, 255, 255, 18)),
          (P(K_CATCH), YEL, (14, 20, 64, 26))]
CUTS = [(P(K_FOUR), YEL, "wipeR"), (P(K_FLIP), CORAL, "wipeU"), (P(K_CATCH), COB, "iris")]


def row(img, y, num, label, amt, t0, t, state=None, dx=0, dim=False):
    a = pop(t, t0, 0.3)
    if a <= 0:
        return
    L = layer()
    bad, good = state == "bad", state == "good"
    box(L, (80, y, W - 80, y + 120), 30, (255, 236, 230, 255) if bad else SOFT, shadow=(0, 10, (0, 0, 0, 70)))
    d = ImageDraw.Draw(L)
    d.ellipse((104, y + 18, 188, y + 102), fill=CORAL if bad else (GREEN if good else COB))
    T(L, num, 146, y + 60, 50, WHITE, key=f"n{num}")
    T(L, label, 220, y + 60, 54, INK, f="xbold", anchor="lm", key=f"l{num}{label}")
    T(L, amt, W - 120, y + 60, 54 if len(amt) < 8 else 44, CORAL if bad else (GREEN if good else INK), f="black", anchor="rm",
      key=f"a{num}{amt}")
    put(img, L, 0.85 + 0.15 * min(1, a), W / 2, y + 60, alpha=min(1, a * 1.6) * (0.3 if dim else 1.0), dx=dx)
    if bad:
        emoji(img, "❌", W - 120, y - 14, 84 * min(1, pop(t, P(K_FOUR))), rot=-10)
    if good:
        emoji(img, "✅", W - 120, y - 14, 84 * min(1, pop(t, P(K_FIRST) + 0.4)), rot=8)


def frame(t):
    img = scene_bg(t, SCENES)
    k = S.at(t) or 0
    if t >= S.end_voice:
        endcard(img, S, t, COB, "fullyfunded.png")
        return img
    if t < P(K_CATCH):
        T(img, "SPOT THE MISTAKE", W / 2, 230, 104, WHITE, key="hook")
        a = pop(t, 0.0, 0.35) if t > 0.05 else 1.0
        T(img, "PAYDAY  +$2,000", W / 2, 410, 92, YEL, key="payday", scale=0.9 + 0.1 * min(1, a))
        emoji(img, "💸", 960, 330, 100, rot=14)
        sx, sy = shake(t, P(K_FOUR), 0.3, 18)
        ys = [560, 700, 840, 980]
        if t < P(K_FIRST):
            G = layer()   # frame 0 is never empty: four ghost slots wait to be filled
            gd = ImageDraw.Draw(G)
            for i in range(4):
                if t < P(K_ROWS[i]) - 0.5:
                    gd.rounded_rectangle((80, ys[i], W - 80, ys[i] + 120), 30, outline=(255, 255, 255, 120), width=5)
                    gd.ellipse((104, ys[i] + 18, 188, ys[i] + 102), outline=(255, 255, 255, 120), width=5)
            put(img, G)
            dim = T_HOLD <= t < P(K_FOUR) - 0.05
            for i, (num, lab, amt) in enumerate(ROWS):
                st = "bad" if (i == 3 and t >= P(K_FOUR)) else None
                row(img, ys[i], num, lab, amt, P(K_ROWS[i]) - 0.5, t, st, dx=sx if i == 3 else 0, dim=dim)
            if dim:   # pause-and-spot: a draining ring under the list, no words
                u = (t - T_HOLD) / (P(K_FOUR) - 0.05 - T_HOLD)
                L = layer()
                ImageDraw.Draw(L).arc((370, 610, 710, 950), -90, -90 + 360 * (1 - u), fill=YEL, width=28)
                put(img, L, 1.0 + 0.06 * math.sin(t * 9))
                emoji(img, "⏳", W / 2, 780, 140, rot=180 * u)
        else:
            u = ease((t - P(K_FIRST)) / 0.6)
            new = {3: 0, 0: 1, 1: 2, 2: 3}
            for i, (num, lab, amt) in enumerate(ROWS):
                y = ys[i] + (ys[new[i]] - ys[i]) * u
                if i == 3:
                    row(img, y, "1", "Savings", "FIRST", -1, t, "good")
                else:
                    row(img, y, str(new[i] + 1), lab, amt, -1, t)
    else:
        q = pop(t, P(K_CATCH) + 0.05, 0.35)
        T(img, "Bills eat it all?", W / 2, 360, 92, INK, key="c1")
        if t >= P(K_TINY):
            T(img, "START TINY.", W / 2, 560, 150, COB, key="c2", scale=0.8 + 0.2 * min(1, pop(t, P(K_TINY), 0.3)))
        if t >= P(K_SMALL):
            T(img, "Small + automatic", W / 2, 760, 80, INK, key="c3", words=3)
            T(img, "beats big + skipped.", W / 2, 870, 80, CORAL, key="c4", words=4)
        emoji(img, "🌱", W / 2, 1060, 160 * min(1, q))
        if k >= K_LAST:
            emoji(img, "👇", W / 2, 1560 + 14 * math.sin(t * 8), 110)
    if t >= P(K_CATCH):
        captions(img, S, t, y=1300, size=100, fill=INK, lit=COB)
    elif P(K_FOUR) <= t < P(K_FLIP):
        captions(img, S, t, y=1300, size=100, fill=WHITE, lit=INK)
    else:
        captions(img, S, t, y=1300, size=100, fill=WHITE, lit=YEL)
    img = transition(img, t, CUTS)
    return img


cues = ([("sfx-cash", 0.05, -10)] + [("sfx-paper", P(K_ROWS[i]) - 0.5, -8) for i in range(4)] +
        [("sfx-tick-ding", T_HOLD + 0.8 * i, -8) for i in range(3)] +
        [("sfx-record-scratch", P(K_FOUR) - 0.05, -9), ("sfx-whoosh-fast", P(K_FLIP) - 0.17, -9), ("st-2-ta-da-el", P(K_FIRST) + 0.4, -12),
         ("sfx-whoosh-soft", P(K_CATCH) - 0.17, -9)])

if __name__ == "__main__":
    finish(S, frame, cues, bed="v3/ff-d-question-marimba-el.mp3")
