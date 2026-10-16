"""HB round 2 · 'One of these should never go into an AI chat' (pause, comment 1/2/3). Answer: 3, a bank-app screenshot.
Privacy education; the screenshot on screen is a blurred mock (no real data).
Round 2b (Oct 16 pm): one Eleven v3 take, continuous bed + room tone, floating text, colour scenes with bold cuts."""
from r2 import *  # noqa: F403

PLUM, IND, YEL, ORA, CRM, INK, WHITE = (hexc(x) for x in ("3A2240", "5E54C9", "FFC94D", "FF8A3D", "FFF8EF", "2A2238", "FFFFFF"))
RED, GREEN = hexc("D63A30"), hexc("128A52")

S = Script("hb-r2-never-paste-v3-t2", hold={"1, 2 or 3?": 2.4}, out_name="HB-R2-never-paste")
P = S.p
K_ONE, K_TWO, K_THREE, K_CHARGE, K_GUESS = (S.phrase("One."), S.phrase("Two."), S.phrase("Three."), S.phrase("explain one"),
                                            S.phrase("2 or 3"))
K_A1, K_A2 = S.phrase("One.", K_GUESS), S.phrase("Two.", K_GUESS)
K_ANS = S.phrase("Three.", K_GUESS)
K_THATS, K_SHOW, K_TYPE, K_LAST = S.phrase("That's the one"), S.phrase("show your name"), S.phrase("Type just"), S.phrase("pick three")
ITEMS = [("1", "Recipe to halve", "🍝", K_ONE), ("2", "Email, no names", "✉️", K_TWO), ("3", "Bank app screenshot", "📱", K_THREE)]
T_HOLD = S.words[S.ph[K_GUESS][-1]][2] + 0.1
SCENES = [(0, PLUM, (255, 255, 255, 18)), (P(K_ANS), IND, (255, 255, 255, 22)), (P(K_TYPE), YEL, (42, 34, 56, 26))]
CUTS = [(P(K_ANS), RED, "wipeR"), (P(K_TYPE), ORA, "iris")]


def item(img, i, t, y, dim=False):
    num, label, emo, kk = ITEMS[i]
    a = pop(t, P(kk) - 0.05, 0.3)
    if a <= 0:
        return
    verdict = None
    if i == 0 and t >= P(K_A1) or i == 1 and t >= P(K_A2):
        verdict = "ok"
    L = layer()
    box(L, (80, y, W - 80, y + 190), 34, WHITE, shadow=(0, 12, (0, 0, 0, 90)))
    d = ImageDraw.Draw(L)
    d.ellipse((110, y + 45, 210, y + 145), fill=GREEN if verdict == "ok" else IND)
    T(L, num, 160, y + 95, 60, WHITE, key=f"n{num}")
    emoji(L, emo, 300, y + 95, 110)
    T(L, label, 390, y + 95, 56, INK, f="xbold", anchor="lm", key=label)
    put(img, L, 0.85 + 0.15 * min(1, a), W / 2, y + 95, alpha=min(1, a * 1.6) * (0.3 if dim else 1.0))
    if verdict:
        emoji(img, "✅", W - 110, y + 20, 100 * min(1, pop(t, P(K_A1 if i == 0 else K_A2))))


def frame(t):
    img = scene_bg(t, SCENES)
    k = S.at(t) or 0
    if t >= S.end_voice:
        endcard(img, S, t, PLUM, "hourback.png")
        return img
    if t < P(K_ANS):
        T(img, "NEVER PASTE THIS", W / 2, 230, 104, WHITE, key="hook")
        T(img, "1, 2 OR 3?", W / 2, 345, 80, YEL, key="hook2")
        G = layer()  # frame 0 is never empty: three numbered ghost slots wait to be filled
        gd = ImageDraw.Draw(G)
        for i in range(3):
            y = 450 + i * 230
            if t < P(ITEMS[i][3]) + 0.1:
                gd.rounded_rectangle((80, y, W - 80, y + 190), 34, outline=(255, 255, 255, 110), width=5)
                gd.ellipse((110, y + 45, 210, y + 145), outline=(255, 255, 255, 140), width=5)
                emoji(G, "❔", 540, y + 95, 90, alpha=0.6)
        put(img, G)
        guessing = T_HOLD <= t < P(K_A1) - 0.05
        for i in range(3):
            item(img, i, t, 450 + i * 230, dim=guessing)
        if guessing:
            u = (t - T_HOLD) / (P(K_A1) - 0.05 - T_HOLD)
            L = layer()
            ImageDraw.Draw(L).arc((370, 620, 710, 960), -90, -90 + 360 * (1 - u), fill=YEL, width=28)
            put(img, L, 1.0 + 0.06 * math.sin(t * 9))
            emoji(img, "⏳", W / 2, 790, 140, rot=180 * u)
    elif t < P(K_TYPE):
        sx, sy = shake(t, P(K_ANS) + 0.05, 0.35, 18)
        T(img, "NUMBER 3", W / 2 + sx, 240 + sy, 130, YEL, key="ans")
        a = pop(t, P(K_ANS) + 0.05, 0.35)
        L = layer()   # mock bank screenshot, blurred lines (no real data)
        box(L, (150, 400, 640, 1060), 50, WHITE, shadow=(0, 16, (0, 0, 0, 90)))
        box(L, (150, 400, 640, 500), 50, (120, 110, 200, 255))
        for j in range(5):
            box(L, (200, 560 + j * 95, 200 + [380, 260, 400, 320, 360][j], 596 + j * 95), 16, (220, 214, 232, 255))
        put(img, L, 0.8 + 0.2 * min(1, a), 335, 730, alpha=min(1, a * 1.5), dx=sx)
        emoji(img, "🚫", 540, 420, 150 * min(1, pop(t, P(K_ANS) + 0.2)), rot=-10)
        flags = [("NAME", 600, 0.0), ("BALANCE", 760, 0.5), ("ACCOUNT #", 920, 1.0)]
        for lab, y, dt in flags:
            t0 = P(K_SHOW) + dt
            if t >= t0:
                q = min(1, pop(t, t0, 0.3))
                T(img, lab, 880, y, 56, YEL, key=lab, scale=0.7 + 0.3 * q, words=1)   # centred right of the pointer, clear of it
                emoji(img, "👈", 625, y, 70 * q)
    else:
        q = pop(t, P(K_TYPE) + 0.05, 0.35)
        T(img, "TYPE JUST", W / 2, 330, 120, INK, key="type1")
        T(img, "THE CHARGE:", W / 2, 470, 120, INK, key="type2")
        T(img, "“STORE  $34.99?”", W / 2, 700, 110, IND, key="typeit", scale=0.8 + 0.2 * min(1, q), words=2)
        emoji(img, "⌨️", W / 2, 950, 180 * min(1, q))
        if k >= K_LAST:
            emoji(img, "👇", W / 2, 1560 + 14 * math.sin(t * 8), 110)
    if t >= P(K_TYPE):
        captions(img, S, t, y=1300, size=100, fill=INK, lit=IND)
    else:
        captions(img, S, t, y=1300, size=100, fill=WHITE, lit=YEL)
    img = transition(img, t, CUTS)
    return img


cues = ([("sfx-tick-ding", 0.05, -10)] + [("sfx-whoosh-soft", P(kk) - 0.1, -11) for kk in (K_ONE, K_TWO, K_THREE)] +
        [("sfx-tick-ding", T_HOLD + 0.8 * i, -8) for i in range(3)] +
        [("sfx-record-scratch", P(K_ANS) - 0.05, -8), ("sfx-paper", P(K_SHOW), -10), ("sfx-whoosh-fast", P(K_TYPE) - 0.17, -10)])

if __name__ == "__main__":
    finish(S, frame, cues, bed="v3/hb-a-ta-da-el.mp3")
