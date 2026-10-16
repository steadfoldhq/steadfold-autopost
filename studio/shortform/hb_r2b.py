"""HB round 2 · 'One of these should never go into an AI chat' (pause, comment 1/2/3). Answer: 3, a bank-app screenshot.
Privacy education; the screenshot on screen is a blurred mock (no real data)."""
from r2 import *  # noqa: F403

PLUM, IND, YEL, ORA, CRM, INK, WHITE = (hexc(x) for x in ("3A2240", "5E54C9", "FFC94D", "FF8A3D", "FFF8EF", "2A2238", "FFFFFF"))
RED, GREEN = hexc("E8443A"), hexc("1FAF6B")

S = Script("hb-r2-never-paste", skip={9, 11, 12, 13, 14}, hold={"1, 2 or 3?": 2.4}, out_name="HB-R2-never-paste")
P = S.p
K_ONE, K_TWO, K_THREE, K_CHARGE, K_GUESS, K_ANS, K_THATS, K_SHOW, K_BAL, K_TYPE, K_LAST = (
    S.phrase("One."), S.phrase("Two."), S.phrase("Three."), S.phrase("explain one"), S.phrase("2 or 3"), S.phrase("Three.", S.phrase("2 or 3")),
    S.phrase("That's the one"), S.phrase("show your name"), S.phrase("balance and"), S.phrase("Type just"), S.phrase("pick three"))
ITEMS = [("1", "Recipe to halve", "🍝", K_ONE), ("2", "Email, no names", "✉️", K_TWO), ("3", "Bank app screenshot", "📱", K_THREE)]
T_HOLD = S.words[S.ph[K_GUESS][-1]][2] + 0.1


def item(img, i, t, y):
    num, label, emo, kk = ITEMS[i]
    a = pop(t, P(kk) - 0.05, 0.3)
    if a <= 0:
        return
    verdict = None
    if t >= P(K_ANS):
        verdict = "bad" if i == 2 else "ok"
    L = layer()
    box(L, (80, y, W - 80, y + 190), 34, (255, 232, 228, 255) if verdict == "bad" else WHITE, shadow=(0, 12, (0, 0, 0, 90)))
    d = ImageDraw.Draw(L)
    d.ellipse((110, y + 45, 210, y + 145), fill=RED if verdict == "bad" else (GREEN if verdict == "ok" else IND))
    T(L, num, 160, y + 95, 60, WHITE, key=f"n{num}")
    emoji(L, emo, 300, y + 95, 110)
    T(L, label, 390, y + 95, 56, INK, f="xbold", anchor="lm", key=label)
    sx, sy = shake(t, P(K_ANS), 0.3, 16) if i == 2 else (0, 0)
    put(img, L, 0.85 + 0.15 * min(1, a), W / 2, y + 95, alpha=min(1, a * 1.6), dx=sx)
    if verdict:
        emoji(img, "🚫" if verdict == "bad" else "✅", W - 110, y + 20, 100 * min(1, pop(t, P(K_ANS) + (0.0 if i == 2 else 0.3 * i))))


def frame(t):
    img = dots_bg(PLUM, (255, 255, 255, 18), t)
    k = S.at(t) or 0
    if t >= S.end_voice:
        endcard(img, S, t, PLUM, "hourback.png")
        return img
    if k < K_THATS:
        T(img, "NEVER PASTE THIS", W / 2, 230, 104, WHITE, key="hook")
        T(img, "1, 2 OR 3?", W / 2, 345, 76, YEL, key="hook2")
        G = layer()  # frame 0 is never empty: three numbered ghost slots wait to be filled
        gd = ImageDraw.Draw(G)
        for i in range(3):
            y = 450 + i * 230
            if t < P(ITEMS[i][3]) + 0.1:
                gd.rounded_rectangle((80, y, W - 80, y + 190), 34, outline=(255, 255, 255, 110), width=5)
                gd.ellipse((110, y + 45, 210, y + 145), outline=(255, 255, 255, 140), width=5)
                T(G, str(i + 1), 160, y + 95, 60, (255, 255, 255, 170), key="ghostn", words=0)
                emoji(G, "❔", 540, y + 95, 90, alpha=0.6)
        put(img, G)
        for i in range(3):
            item(img, i, t, 450 + i * 230)
    else:
        T(img, "NUMBER 3", W / 2, 240, 110, YEL, key="ans")
        # mock bank screenshot, blurred lines (no real data), with the risky parts circled
        a = pop(t, P(K_THATS), 0.35)
        L = layer()
        box(L, (230, 360, 850, 960), 50, WHITE, shadow=(0, 16, (0, 0, 0, 90)))
        box(L, (230, 360, 850, 470), 50, IND)
        for j in range(4):
            box(L, (280, 520 + j * 90, 280 + [420, 300, 460, 380, 440, 260][j], 556 + j * 90), 16, (220, 214, 232, 255))
        put(img, L, 0.8 + 0.2 * min(1, a), W / 2, 740, alpha=min(1, a * 1.5))
        flags = [(K_SHOW, "NAME", 560), (K_BAL, "BALANCE", 700), (K_BAL, "ACCOUNT #", 840)]
        for kk, lab, y in flags:
            if t >= P(kk) + (0.5 if lab == "ACCOUNT #" else 0):
                q = min(1, pop(t, P(kk) + (0.5 if lab == "ACCOUNT #" else 0)))
                box(img, (560, y - 46, 1000, y + 46), 46, RED)
                T(img, lab, 780, y, 52, WHITE, alpha=q, key=lab)
        if t >= P(K_TYPE):
            a2 = pop(t, P(K_TYPE), 0.3)
            L = layer()
            box(L, (110, 975, W - 110, 1100), 36, YEL, shadow=(0, 10, (0, 0, 0, 90)))
            T(L, "Type: “STORE 34.99?”", W / 2, 1037, 58, INK, key="typeit")
            put(img, L, 0.85 + 0.15 * min(1, a2), W / 2, 1037, alpha=min(1, a2 * 1.5))
        if k >= K_LAST:
            emoji(img, "👇", W / 2, 1530 + 14 * math.sin(t * 8), 110)
    if T_HOLD <= t < P(K_ANS) - 0.05:
        u = (t - T_HOLD) / (P(K_ANS) - 0.05 - T_HOLD)
        L = layer()
        ImageDraw.Draw(L).arc((900, 120, 1040, 260), -90, -90 + 360 * (1 - u), fill=YEL, width=16)
        put(img, L)
        emoji(img, "⏳", 970, 190, 70, rot=180 * u)
    captions(img, S, t, y=1300, size=100, fill=WHITE, lit=YEL, stroke=INK)
    return img


cues = ([("sfx-tick-ding", 0.0, -10)] + [("sfx-whoosh-soft", P(kk) - 0.1, -11) for kk in (K_ONE, K_TWO, K_THREE)] +
        [("sfx-tick-ding", T_HOLD + 0.8 * i, -8) for i in range(3)] +
        [("sfx-record-scratch", P(K_ANS) - 0.05, -8), ("sfx-paper", P(K_SHOW), -10), ("sfx-whoosh-fast", P(K_TYPE) - 0.1, -10),
         ("sfx-whoosh-soft", S.end_voice - 0.15, -10)])

if __name__ == "__main__":
    finish(S, frame, cues)
