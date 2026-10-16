"""LH round 2 · 'Which one are you?' (3 kinds of 'I'll start soon', comment 1/2/3), then one fix: a 2-minute ugly start.
Round 2b (Oct 16 pm): one Eleven v3 take, continuous bed + room tone, floating text (no dark boxes), a colour scene per
character with a bold cut on the spoken number."""
from r2 import *  # noqa: F403

YEL, INK, PINK, HL, CREAM, WHITE = (hexc(x) for x in ("FFE27A", "141414", "E83E8C", "FFD43B", "FFF4E0", "FFFFFF"))
MAG, SKY, LAV = hexc("B0105A"), hexc("6C8CFF"), hexc("C9D3FF")

S = Script("lh-r2-which-one-v3-t2", out_name="LH-R2-which-one-are-you")
P = S.p
K1, K2, K3 = S.phrase("One..."), S.phrase("Two..."), S.phrase("Three...")
K_SPOT, K_UNT, K_TABS, K_147, K_AT2, K_FIX, K_TIMER, K_UGLY, K_STOP, K_HARD, K_LAST = (
    S.phrase("Desk spotless"), S.phrase("untouched"), S.phrase("Twelve tabs"), S.phrase("1:47"), S.phrase("start at 2"),
    S.phrase("Same fix"), S.phrase("timer"), S.phrase("ugliest"), S.phrase("allowed"), S.phrase("hard part"), S.phrase("2 or 3"))
TYPES = [("1", "THE CLEANER", "🧽"), ("2", "THE RESEARCHER", "🔎"), ("3", "THE WAITER", "⏰")]
SCENES = [(0, YEL, (20, 20, 20, 24)), (P(K1), CREAM, (20, 20, 20, 20)), (P(K2), PINK, (255, 255, 255, 30)),
          (P(K3), LAV, (20, 20, 20, 22)), (P(K_FIX), YEL, (20, 20, 20, 24))]
CUTS = [(P(K1), PINK, "wipeR"), (P(K2), INK, "wipeU"), (P(K3), YEL, "wipeL"), (P(K_FIX), PINK, "iris")]


def zine(img, b, fill, r=34, sh=14):
    box(img, b, r, fill, shadow=(sh, sh, INK), outline=INK, width=6)


def scene_of(t):
    return 0 if t < P(K1) else 1 if t < P(K2) else 2 if t < P(K3) else 3 if t < P(K_FIX) else 4


def frame(t):
    img = scene_bg(t, SCENES)
    k = S.at(t) or 0
    if t >= S.end_voice:
        endcard(img, S, t, YEL, "lockedhour.png")
        return img
    sc = scene_of(t)
    if sc == 0:
        T(img, "WHICH ONE", W / 2, 250, 130, INK, key="hook1")
        T(img, "ARE YOU?", W / 2, 390, 130, MAG, key="hook2")
        for i, (num, name, emo) in enumerate(TYPES):
            x = 90 + i * 310
            a = pop(t, 0.2 * i, 0.3) if t > 0.03 else 1
            L = layer()
            zine(L, (x, 560, x + 280, 940), [CREAM, WHITE, CREAM][i])
            T(L, num, x + 140, 650, 120, MAG, key=f"tile{num}")
            emoji(L, emo, x + 140, 830, 120, rot=8 * math.sin(t * 4 + i))
            put(img, L, 0.8 + 0.2 * min(1, a), x + 140, 750, dy=8 * math.sin(t * 3 + i))
    elif sc in (1, 2, 3):
        i = sc - 1
        num, name, emo = TYPES[i]
        light = sc != 2
        T(img, num, W / 2, 300, 220, MAG if light else WHITE, key=f"big{num}", words=1)
        T(img, name, W / 2, 470, 96, INK, key=name)
        a = pop(t, P([K1, K2, K3][i]) + 0.05, 0.35)
        L = layer()
        if i == 0:   # spotless desk, untouched work
            box(L, (190, 880, 890, 920), 12, INK)
            emoji(L, "💻", 420, 790, 190)
            emoji(L, "🧽", 700, 800, 160, rot=-12 + 10 * math.sin(t * 9))
            if t >= P(K_SPOT) - 0.2:
                for kk, (x, y) in enumerate([(240, 640), (840, 610), (620, 1010), (300, 1020)]):
                    emoji(L, "✨", x, y, 84 + 14 * math.sin(t * 6 + kk))
            if t >= P(K_UNT) - 0.1:
                emoji(L, "🫠", 860, 1040, 140 * min(1, pop(t, P(K_UNT) - 0.1)))
        elif i == 1:  # 12 tabs pile up, no words
            n = 12 if t >= P(K_TABS) + 1.2 else max(1, int(12 * max(0, t - (P(K_TABS) - 0.4)) / 1.6))
            for kk in range(n):
                x = 130 + (kk % 4) * 205
                y = 620 + (kk // 4) * 120
                box(L, (x, y, x + 185, y + 92), 16, [HL, WHITE, SKY, CREAM][kk % 4], outline=INK, width=5)
            emoji(L, "🤓", 540, 1050, 140)
        else:  # 1:47 -> "at 2": the digits float, huge
            late = t >= P(K_AT2) + 0.6
            sx, sy = shake(t, P(K_147), 0.3, 14)
            T(L, "1:58" if late else "1:47", 540 + sx, 760 + sy, 250, INK, key="clock", words=1)
            if t >= P(K_AT2):
                emoji(L, "🛋️", 540, 1010, 170 * min(1, pop(t, P(K_AT2))))
        put(img, L, 0.8 + 0.2 * min(1, a), W / 2, 800, dx=(1 - min(1, a)) * 260)
    else:
        T(img, "THE FIX", W / 2, 250, 130, INK, key="fix")
        for i, (num, name, emo) in enumerate(TYPES):   # same fix for all three
            x = 150 + i * 290
            T(img, num, x + 40, 420, 90, MAG, key=f"row{num}", words=0)
            emoji(img, emo, x + 140, 420, 90)
        if t >= P(K_TIMER) - 0.1:
            u = max(0.0, t - P(K_TIMER))
            secs = max(0, 120 - int(u))              # real seconds: each value holds 1 s (reading rule, 1 word)
            q = min(1, pop(t, P(K_TIMER) - 0.1))
            T(img, f"{secs // 60}:{secs % 60:02d}", 540, 760, 280, INK, key="timer", words=1, scale=0.85 + 0.15 * q)
        if t >= P(K_UGLY):
            emoji(img, "✍️", 880, 1010, 150 * min(1, pop(t, P(K_UGLY))), rot=-10)
        if t >= P(K_STOP):
            emoji(img, "✅", 200, 1010, 140 * min(1, pop(t, P(K_STOP))), rot=8)
        if k >= K_LAST:
            emoji(img, "👇", W / 2, 1560 + 14 * math.sin(t * 8), 110)
    cap = dict(fill=WHITE, lit=INK) if sc == 2 else dict(fill=INK, lit=MAG)
    captions(img, S, t, y=1300, size=100, **cap)
    img = transition(img, t, CUTS)
    return img


cues = ([("sfx-tick-ding", 0.05, -10)] + [("sfx-whoosh-fast", P(kk) - 0.17, -8) for kk in (K1, K2, K3)] +
        [("sfx-paper", P(K_SPOT), -10)] + [("sfx-tick-ding", P(K_TABS) - 0.4 + 0.13 * i, -18) for i in range(12)] +
        [("sfx-record-scratch", P(K_147) - 0.05, -10), ("sfx-whoosh-soft", P(K_FIX) - 0.17, -8), ("sfx-tick-ding", P(K_TIMER), -9),
         ("st-2-ta-da-el", P(K_HARD) - 0.05, -14)])

if __name__ == "__main__":
    finish(S, frame, cues, bed="v3/lh-c-morning-drive-el.mp3")
