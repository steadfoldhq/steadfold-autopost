"""HB round 2 · 'Three words make any AI way better. Guess them before the end.' The three words stay hidden
(redaction bars) until the last beat: 'Ask me first.' AI replies are made up and labelled."""
from r2 import *  # noqa: F403

PLUM, IND, YEL, ORA, CRM, INK, WHITE = (hexc(x) for x in ("3A2240", "5E54C9", "FFC94D", "FF8A3D", "FFF8EF", "2A2238", "FFFFFF"))
GREY = (200, 192, 214, 255)

S = Script("hb-r2-three-words", skip={"Watch.", "You get this.", "'Plan my week.", "Ask me first.'", "You answer."},
           out_name="HB-R2-three-words")
P = S.p
K_PLAN, K_GEN, K_ADD, K_ASKS, K_Q1, K_Q2, K_Q3, K_FITS, K_THE3, K_REVEAL, K_LAST = (
    S.phrase("'Plan my week.'"), S.phrase("Generic"), S.phrase("Now add"), S.phrase("Now it asks"), S.phrase("packed"),
    S.phrase("must get done"), S.phrase("gym"), S.phrase("fits"), S.phrase("The three words?"), S.phrase("Ask me first"),
    S.phrase("have it plan"))


def bubble(img, x0, y, w, h, me, t0, t, txt=None, bars=None, hidden=None, key=None):
    a = pop(t, t0, 0.3)
    if a <= 0:
        return
    L = layer()
    box(L, (x0, y, x0 + w, y + h), 34, IND if me else WHITE, shadow=(0, 10, (0, 0, 0, 70)))
    if txt:
        T(L, txt, x0 + 40, y + 62, 54, WHITE if me else INK, f="xbold", anchor="lm", key=key or txt)
    if bars:
        for j, bw in enumerate(bars):
            box(L, (x0 + 40, y + 40 + j * 46, x0 + 40 + bw, y + 66 + j * 46), 13, GREY)
    if hidden is not None:
        if hidden == "bars":
            for j, (bx, bw) in enumerate([(0, 90), (110, 70), (200, 130)]):
                box(L, (x0 + 40 + bx, y + 112, x0 + 40 + bx + bw, y + 160), 12, YEL)
        else:
            T(L, hidden, x0 + 40, y + 138, 60, YEL, f="black", anchor="lm", key="reveal3")
    put(img, L, 0.85 + 0.15 * min(1, a), x0 + w / 2, y + h / 2, alpha=min(1, a * 1.6))


def frame(t):
    img = dots_bg(PLUM, (255, 255, 255, 18), t)
    k = S.at(t) or 0
    if t >= S.end_voice:
        endcard(img, S, t, PLUM, "hourback.png")
        return img
    if k < K_REVEAL:
        T(img, "3 WORDS. GUESS THEM.", W / 2, 240, 92, WHITE, key="hook")
        # three locked slots under the hook (the gap)
        for j in range(3):
            x = 250 + j * 200
            box(img, (x, 320, x + 170, 400), 18, YEL if (j == 0 or t > 0.3) else YEL)
            emoji(img, "🔒", x + 85, 360, 50)
    else:
        a = pop(t, P(K_REVEAL), 0.3)
        L = layer()
        box(L, (110, 170, W - 110, 420), 40, YEL, shadow=(0, 14, (0, 0, 0, 90)))
        T(L, "ASK ME FIRST.", W / 2, 295, 104, INK, key="answer")
        put(img, L, 0.6 + 0.4 * min(1, a), W / 2, 295)
        sx, sy = shake(t, P(K_REVEAL), 0.3, 16)
    # intro: three big locked tiles fill the frame until the demo starts (frame 0 is never empty)
    if k < K_PLAN:
        for j in range(3):
            a = pop(t, 0.12 * j, 0.3) if t > 0.03 else 1.0
            L = layer()
            x = 90 + j * 310
            box(L, (x, 560, x + 280, 900), 40, YEL, shadow=(0, 16, (0, 0, 0, 110)))
            T(L, "?", x + 140, 680, 150, INK, key="q", words=0)
            emoji(L, "🔒", x + 140, 830, 90, rot=6 * math.sin(t * 5 + j))
            put(img, L, 0.8 + 0.2 * min(1, a), x + 140, 730)
    # chat column
    if K_PLAN <= k < K_ADD:
        bubble(img, 380, 520, 600, 124, True, P(K_PLAN) - 0.1, t, txt="Plan my week.")
        bubble(img, 100, 690, 700, 300, False, P(K_GEN) - 0.2, t, bars=[560, 600, 520, 610, 480])
        if t >= P(K_GEN):
            emoji(img, "😐", 860, 830, 140 * min(1, pop(t, P(K_GEN))))
    elif K_ADD <= k < K_FITS:
        bubble(img, 300, 470, 680, 200, True, P(K_ADD) - 0.1, t, txt="Plan my week.", hidden="bars", key="Plan my week. (2)")
        if t >= P(K_ADD) + 0.4:
            emoji(img, "🤫", 930, 470, 100)
        qs = [(K_Q1, "Which days are packed?"), (K_Q2, "What must get done?"), (K_Q3, "Any gym days?")]
        if t >= P(K_ASKS):
            for j, (kk, q) in enumerate(qs):
                bubble(img, 100, 720 + j * 150, 760, 124, False, P(kk) - 0.15, t, txt=q)
    elif k >= K_FITS:
        a = pop(t, P(K_FITS), 0.35)
        L = layer()
        box(L, (120, 520, W - 120, 1100), 40, WHITE, shadow=(0, 14, (0, 0, 0, 80)))
        cols = [YEL, IND, ORA, YEL, IND]
        for d in range(5):
            x = 170 + d * 150
            box(L, (x, 600, x + 120, 1040), 18, CRM)
            for j in range(3):
                if (d + j) % 2 == 0:
                    box(L, (x + 10, 640 + j * 130, x + 110, 740 + j * 130), 14, cols[(d + j) % 5])
        T(L, "EXAMPLE · MADE UP", W / 2, 1072, 32, IND, f="xbold", key="example2")
        put(img, L, 0.8 + 0.2 * min(1, a), W / 2, 810, alpha=min(1, a * 1.5))
        emoji(img, "✅", 940, 540, 120 * min(1, pop(t, P(K_FITS) + 0.3)))
        if k >= K_LAST:
            emoji(img, "👇", W / 2, 1530 + 14 * math.sin(t * 8), 110)
    if K_PLAN <= k < K_FITS:
        T(img, "EXAMPLE · MADE UP", W / 2, 1160, 38, YEL, f="xbold", key="example")
    captions(img, S, t, y=1300, size=100, fill=WHITE, lit=YEL, stroke=INK)
    return img


cues = [("sfx-tick-ding", 0.0, -10), ("sfx-whoosh-soft", P(K_PLAN) - 0.15, -10), ("sfx-paper", P(K_GEN) - 0.2, -10),
        ("sfx-whoosh-fast", P(K_ADD) - 0.15, -9)] + [("sfx-tick-ding", P(kk) - 0.15, -14) for kk in (K_Q1, K_Q2, K_Q3)] + \
       [("sfx-whoosh-soft", P(K_FITS) - 0.1, -10), ("st-3-wait-for-it-el", P(K_THE3) - 0.1, -16), ("st-2-ta-da-el", P(K_REVEAL) - 0.05, -9),
        ("sfx-whoosh-soft", S.end_voice - 0.15, -10)]

if __name__ == "__main__":
    finish(S, frame, cues)
