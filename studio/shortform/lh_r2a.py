"""LH round 2 · 'Which one are you?' (3 kinds of 'I'll start soon', comment 1/2/3), then one fix: a 2-minute ugly start."""
from r2 import *  # noqa: F403

YEL, INK, PINK, HL, CREAM, WHITE = (hexc(x) for x in ("FFE27A", "141414", "FF5CA8", "FFD43B", "FFF4E0", "FFFFFF"))
BLUE = hexc("6C8CFF")

S = Script("lh-r2-which-one", skip={"Starting was the hard part.", "So."}, out_name="LH-R2-which-one-are-you")
P = S.p
K1, K2, K3 = S.phrase("The Cleaner"), S.phrase("The Researcher"), S.phrase("The Waiter")
K_SPOT, K_UNT, K_TABS, K_147, K_AT2, K_FIX, K_TIMER, K_UGLY, K_STOP, K_LAST = (
    S.phrase("Desk spotless"), S.phrase("untouched"), S.phrase("Twelve tabs"), S.phrase("1:47"), S.phrase("start at 2"),
    S.phrase("Same fix"), S.phrase("timer"), S.phrase("ugliest"), S.phrase("allowed"), S.phrase("2 or 3"))
TYPES = [("1", "THE CLEANER", "🧽"), ("2", "THE RESEARCHER", "🔎"), ("3", "THE WAITER", "⏰")]


def zine(img, b, fill, r=34, sh=14):
    box(img, b, r, fill, shadow=(sh, sh, INK), outline=INK, width=6)


def big_card(img, t, i):
    """One character card, the gag drawn inside it."""
    num, name, emo = TYPES[i]
    t0 = P([K1, K2, K3][i]) - 0.9
    a = pop(t, t0, 0.35)
    L = layer()
    zine(L, (90, 420, W - 90, 1120), [CREAM, WHITE, CREAM][i])
    d = ImageDraw.Draw(L)
    d.ellipse((130, 455, 230, 555), fill=PINK, outline=INK, width=5)
    T(L, num, 180, 505, 60, INK, key=f"num{num}")
    T(L, name, 600, 505, 70, INK, key=name)
    if i == 0:   # spotless desk, untouched work
        box(L, (190, 820, 890, 860), 12, INK)
        emoji(L, "💻", 420, 740, 170)
        emoji(L, "🧽", 700, 750, 150, rot=-12 + 10 * math.sin(t * 9))
        for k, (x, y) in enumerate([(260, 640), (820, 610), (600, 950), (330, 960)]):
            if t >= P(K_SPOT) - 0.2:
                emoji(L, "✨", x, y, 80 + 14 * math.sin(t * 6 + k))
        if t >= P(K_UNT) - 0.1:
            emoji(L, "🫠", 540, 1010, 120 * min(1, pop(t, P(K_UNT) - 0.1)))
    elif i == 1:  # 12 tabs, no words
        n = 12 if t >= P(K_TABS) + 1.2 else max(1, int(12 * max(0, t - (P(K_TABS) - 0.4)) / 1.6))
        for k in range(n):
            x = 130 + (k % 4) * 205
            y = 640 + (k // 4) * 120
            box(L, (x, y, x + 185, y + 92), 16, [HL, PINK, BLUE, WHITE][k % 4], outline=INK, width=5)
        emoji(L, "🤓", 540, 1040, 120)
    else:  # 1:47 -> "at 2"
        zine(L, (300, 640, 780, 860), INK, r=30, sh=10)
        T(L, "1:47" if t < P(K_AT2) + 0.6 else "1:58", 540, 752, 150, HL, f="black", key="clock", words=1)
        if t >= P(K_AT2):
            emoji(L, "🛋️", 540, 990, 140 * min(1, pop(t, P(K_AT2))))
    return L, a


def frame(t):
    img = dots_bg(YEL, (20, 20, 20, 26), t)
    k = S.at(t) or 0
    if t >= S.end_voice:
        endcard(img, S, t, YEL, "lockedhour.png")
        return img
    if k < K_FIX:
        T(img, "WHICH ONE ARE YOU?", W / 2, 250, 100, INK, key="hook")
        if t < P(K1) - 0.9:   # opening: the three numbered tiles
            for i, (num, name, emo) in enumerate(TYPES):
                x = 90 + i * 310
                a = pop(t, 0.25 * i, 0.3) if t > 0.03 else 1
                L = layer()
                zine(L, (x, 520, x + 280, 900), [CREAM, WHITE, CREAM][i])
                T(L, num, x + 140, 610, 110, PINK, key=f"tile{num}")
                emoji(L, "❓", x + 140, 790, 120)
                put(img, L, 0.8 + 0.2 * min(1, a), x + 140, 710)
        else:
            i = 0 if t < P(K2) - 0.9 else (1 if t < P(K3) - 0.9 else 2)
            L, a = big_card(img, t, i)
            sx, sy = shake(t, P(K_147), 0.3, 14) if i == 2 else (0, 0)
            put(img, L, 0.85 + 0.15 * min(1, a), W / 2, 770, dx=sx + (1 - min(1, a)) * 300)
    else:
        T(img, "THE FIX", W / 2, 250, 110, INK, key="fix")
        # three small tiles stay in a row: the same fix for all three
        for i, (num, name, emo) in enumerate(TYPES):
            x = 90 + i * 310
            zine(img, (x, 360, x + 280, 560), [CREAM, WHITE, CREAM][i], sh=8)
            T(img, num, x + 80, 460, 90, PINK, key=f"row{num}")
            emoji(img, emo, x + 195, 460, 100)
        # the 2-minute timer
        if t >= P(K_TIMER) - 0.1:
            u = max(0.0, t - P(K_TIMER))
            secs = max(0, 120 - int(u))              # real seconds: each value holds 1 s (reading rule, 1 word)
            L = layer()
            zine(L, (240, 640, 840, 1000), INK, r=40)
            T(L, f"{secs // 60}:{secs % 60:02d}", 540, 820, 190, HL, key="timer", words=1)
            put(img, L, 0.85 + 0.15 * min(1, pop(t, P(K_TIMER) - 0.1)), W / 2, 820)
        if t >= P(K_UGLY):
            emoji(img, "✍️", 880, 1010, 140 * min(1, pop(t, P(K_UGLY))), rot=-10)
        if t >= P(K_STOP):
            emoji(img, "✅", 200, 1010, 130 * min(1, pop(t, P(K_STOP))), rot=8)
        if k >= K_LAST:
            emoji(img, "👇", W / 2, 1530 + 14 * math.sin(t * 8), 110)
    captions(img, S, t, y=1300, size=100, fill=WHITE, lit=PINK, stroke=INK)
    return img


cues = ([("sfx-tick-ding", 0.0, -10)] + [("sfx-whoosh-fast", P(kk) - 0.95, -9) for kk in (K1, K2, K3)] +
        [("sfx-paper", P(K_SPOT), -10)] + [("sfx-tick-ding", P(K_TABS) - 0.4 + 0.13 * i, -18) for i in range(12)] +
        [("sfx-record-scratch", P(K_147) - 0.05, -10), ("st-1-soft-rise-el", P(K_FIX) - 0.1, -14), ("sfx-tick-ding", P(K_TIMER), -9),
         ("sfx-whoosh-soft", S.end_voice - 0.15, -10)])

if __name__ == "__main__":
    finish(S, frame, cues)
