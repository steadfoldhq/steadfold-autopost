"""HB round 2 · 'Three words make any AI way better. Guess them before the end.' The three words stay hidden
(redaction bars) until the last beat: 'Ask me first.' The AI replies on screen are illustrations.
Round 2b (Oct 16 pm): one Eleven v3 take, continuous bed + room tone, floating text, colour scenes with bold cuts."""
from r2 import *  # noqa: F403

PLUM, IND, YEL, ORA, CRM, INK, WHITE = (hexc(x) for x in ("3A2240", "5E54C9", "FFC94D", "FF8A3D", "FFF8EF", "2A2238", "FFFFFF"))
GREY = (200, 192, 214, 255)

S = Script("hb-r2-three-words-v3-t2", out_name="HB-R2-three-words")
P = S.p
K_PLAN, K_GET, K_GEN, K_ADD, K_ASKS, K_Q1, K_Q2, K_Q3, K_FITS, K_THE3, K_REVEAL, K_LAST = (
    S.phrase("'Plan my week.'"), S.phrase("You get this"), S.phrase("Generic"), S.phrase("Now add"), S.phrase("Now it asks"),
    S.phrase("packed"), S.phrase("must get done"), S.phrase("gym"), S.phrase("fits"), S.phrase("The three words?"),
    S.phrase("Ask me first"), S.phrase("have it plan"))
SCENES = [(0, PLUM, (255, 255, 255, 18)), (P(K_ADD), IND, (255, 255, 255, 22)), (P(K_FITS), PLUM, (255, 255, 255, 18)),
          (P(K_REVEAL), YEL, (42, 34, 56, 26))]
CUTS = [(P(K_ADD), YEL, "wipeR"), (P(K_FITS), ORA, "wipeU"), (P(K_REVEAL), IND, "iris")]


def bubble(img, x0, y, w, h, me, t0, t, txt=None, bars=None, hidden=None, key=None):
    a = pop(t, t0, 0.3)
    if a <= 0:
        return
    L = layer()
    box(L, (x0, y, x0 + w, y + h), 34, ORA if me else WHITE, shadow=(0, 10, (0, 0, 0, 70)))
    if txt:
        T(L, txt, x0 + 40, y + 62, 54, INK, f="xbold", anchor="lm", key=key or txt)
    if bars:
        for j, bw in enumerate(bars):
            box(L, (x0 + 40, y + 40 + j * 46, x0 + 40 + bw, y + 66 + j * 46), 13, GREY)
    if hidden == "bars":
        for j, (bx, bw) in enumerate([(0, 90), (110, 70), (200, 130)]):
            box(L, (x0 + 40 + bx, y + 112, x0 + 40 + bx + bw, y + 160), 12, INK)
    put(img, L, 0.85 + 0.15 * min(1, a), x0 + w / 2, y + h / 2, alpha=min(1, a * 1.6))


def frame(t):
    img = scene_bg(t, SCENES)
    k = S.at(t) or 0
    if t >= S.end_voice:
        endcard(img, S, t, PLUM, "hourback.png")
        return img
    if t < P(K_REVEAL):
        T(img, "3 WORDS.", W / 2, 230, 120, WHITE, key="hook1")
        T(img, "GUESS THEM.", W / 2, 360, 104, YEL, key="hook2")
    if k < K_PLAN:   # intro: three big locked tiles (frame 0 is never empty)
        for j in range(3):
            a = pop(t, 0.12 * j, 0.3) if t > 0.03 else 1.0
            L = layer()
            x = 90 + j * 310
            box(L, (x, 560, x + 280, 900), 40, YEL, shadow=(0, 16, (0, 0, 0, 110)))
            T(L, "?", x + 140, 680, 150, INK, key="q", words=0)
            emoji(L, "🔒", x + 140, 830, 90, rot=6 * math.sin(t * 5 + j))
            put(img, L, 0.8 + 0.2 * min(1, a), x + 140, 730)
    elif t < P(K_ADD):
        bubble(img, 380, 520, 600, 124, True, P(K_PLAN) - 0.1, t, txt="Plan my week.")
        bubble(img, 100, 690, 700, 300, False, P(K_GET) - 0.1, t, bars=[560, 600, 520, 610, 480])
        if t >= P(K_GEN):
            emoji(img, "😐", 860, 830, 160 * min(1, pop(t, P(K_GEN))))
    elif t < P(K_FITS):
        bubble(img, 300, 470, 680, 200, True, P(K_ADD) + 0.05, t, txt="Plan my week.", hidden="bars", key="Plan my week. (2)")
        if t >= P(K_ADD) + 0.4:
            emoji(img, "🤫", 930, 470, 110)
        qs = [(K_Q1, "Which days are packed?"), (K_Q2, "What must get done?"), (K_Q3, "Any gym days?")]
        if t >= P(K_ASKS):
            for j, (kk, q) in enumerate(qs):
                bubble(img, 100, 720 + j * 150, 760, 124, False, min(P(kk) - 0.15, P(K_FITS) - 2.1), t, txt=q)  # each holds >= 1.8 s
    elif t < P(K_REVEAL):
        a = pop(t, P(K_FITS) + 0.05, 0.35)
        L = layer()
        box(L, (120, 520, W - 120, 1100), 40, WHITE, shadow=(0, 14, (0, 0, 0, 80)))
        cols = [YEL, IND, ORA, YEL, IND]
        for d in range(5):
            x = 170 + d * 150
            box(L, (x, 580, x + 120, 1040), 18, CRM)
            for j in range(3):
                if (d + j) % 2 == 0:
                    box(L, (x + 10, 620 + j * 130, x + 110, 720 + j * 130), 14, cols[(d + j) % 5])
        put(img, L, 0.8 + 0.2 * min(1, a), W / 2, 810, alpha=min(1, a * 1.5))
        emoji(img, "✅", 940, 540, 130 * min(1, pop(t, P(K_FITS) + 0.3)))
    else:
        a = pop(t, P(K_REVEAL) + 0.05, 0.3)
        sx, sy = shake(t, P(K_REVEAL) + 0.1, 0.3, 16)
        T(img, "ASK", W / 2 + sx, 420 + sy, 240, INK, key="ans1", scale=0.7 + 0.3 * min(1, a), words=1)
        T(img, "ME", W / 2 + sx, 640 + sy, 240, IND, key="ans2", scale=0.7 + 0.3 * min(1, pop(t, P(K_REVEAL) + 0.2, 0.3)), words=1)
        T(img, "FIRST.", W / 2 + sx, 860 + sy, 240, INK, key="ans3", scale=0.7 + 0.3 * min(1, pop(t, P(K_REVEAL) + 0.4, 0.3)), words=1)
        emoji(img, "🔓", 900, 230, 140 * min(1, a), rot=12)
        if k >= K_LAST:
            emoji(img, "👇", W / 2, 1560 + 14 * math.sin(t * 8), 110)
    if t >= P(K_REVEAL):
        captions(img, S, t, y=1300, size=100, fill=INK, lit=IND)
    else:
        captions(img, S, t, y=1300, size=100, fill=WHITE, lit=YEL)
    img = transition(img, t, CUTS)
    return img


cues = [("sfx-tick-ding", 0.05, -10), ("sfx-whoosh-soft", P(K_PLAN) - 0.15, -10), ("sfx-paper", P(K_GET) - 0.1, -10),
        ("sfx-whoosh-fast", P(K_ADD) - 0.17, -9)] + [("sfx-tick-ding", P(kk) - 0.15, -14) for kk in (K_Q1, K_Q2, K_Q3)] + \
       [("sfx-whoosh-soft", P(K_FITS) - 0.17, -10), ("st-3-wait-for-it-el", P(K_THE3) - 0.1, -16),
        ("st-2-ta-da-el", P(K_REVEAL) - 0.05, -9)]

if __name__ == "__main__":
    finish(S, frame, cues, bed="v3/hb-c-clever-celesta-el.mp3")
