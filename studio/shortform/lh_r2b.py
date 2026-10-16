"""LH round 2 · POV mini-scene: 'you sat down to study at 7' -> 7:43. Fix: phone in another room.
Evidence: Ward, Duke, Gneezy & Bos (2017), 'Brain Drain', J. Assoc. Consumer Research 2(2): with phones silenced,
people with the phone in another room did better on working-memory and fluid-intelligence tasks than people with it
on the desk. Later replications are mixed (said on screen and in the caption)."""
from r2 import *  # noqa: F403

YEL, INK, PINK, HL, CREAM, WHITE = (hexc(x) for x in ("FFE27A", "141414", "FF5CA8", "FFD43B", "FFF4E0", "FFFFFF"))
NIGHT, NIGHT2 = hexc("1B1830"), hexc("2A2450")

S = Script("lh-r2-pov-7pm", skip={"Wait.", "Try this."}, out_name="LH-R2-pov-7pm")
P = S.p
K_OKAY, K_701, K_CHECK, K_743, K_HOW, K_PHONE, K_FACE, K_ANOTHER, K_STUDY, K_DESK, K_SCORED, K_SILENT, K_MIXED, K_HALL, K_LAST = (
    S.phrase("Okay"), S.phrase("7:01"), S.phrase("checking"), S.phrase("7:43."), S.phrase("How is it"), S.phrase("Phone in another"),
    S.phrase("face down"), S.phrase("Another room."), S.phrase("2017"), S.phrase("on the desk"), S.phrase("scored better"),
    S.phrase("silent"), S.phrase("mixed"), S.phrase("hallway"), S.phrase("did your 7"))


def zine(img, b, fill, r=34, sh=14, ink=INK):
    box(img, b, r, fill, shadow=(sh, sh, ink), outline=ink, width=6)


def clock_txt(t):
    if t < P(K_701):
        return "7:00"
    if t < P(K_743):
        return "7:01"
    return "7:43"


def frame(t):
    k = S.at(t) or 0
    night = k < K_PHONE
    img = dots_bg(NIGHT if night else YEL, (255, 255, 255, 18) if night else (20, 20, 20, 26), t)
    if t >= S.end_voice:
        endcard(img, S, t, YEL, "lockedhour.png")
        return img
    if night:
        # lamp glow
        g = layer()
        ImageDraw.Draw(g).ellipse((560, 260, 1160, 860), fill=(255, 212, 59, 40))
        put(img, g)
        T(img, "WHERE DID THE HOUR GO?", W / 2, 230, 84, HL, key="hook")
        sx, sy = shake(t, P(K_743), 0.4, 26)
        L = layer()
        zine(L, (250, 360, 830, 600), INK, r=36, ink=HL)
        T(L, clock_txt(t), 540, 482, 180, PINK if t >= P(K_743) else HL, key="clock", words=1)
        put(img, L, 1.0 + 0.08 * max(0, 1 - (t - P(K_743)) / 0.3) * (t >= P(K_743)), W / 2, 480, dx=sx, dy=sy)
        # desk + book + phone
        box(img, (90, 1000, W - 90, 1050), 14, (90, 70, 50, 255))
        emoji(img, "📖", 360, 900, 200)
        buzz = 10 * math.sin(t * 60) if P(K_CHECK) - 0.4 <= t < P(K_CHECK) + 0.6 else 0
        if t < P(K_CHECK):
            emoji(img, "📱", 720 + buzz, 900, 170, rot=-8)
        else:
            # doom-scroll: the phone fills the middle, coloured posts scroll (no words)
            a = min(1, pop(t, P(K_CHECK), 0.3))
            L = layer()
            zine(L, (310, 640, 770, 1160), (245, 245, 250, 255), r=50, sh=10, ink=INK)
            off = (t - P(K_CHECK)) * 420
            cols = [PINK, HL, (108, 140, 255, 255), (120, 220, 170, 255)]
            for j in range(-1, 6):
                y = 690 + ((j * 150 - off) % 900) - 150
                if 650 < y < 1100:
                    box(L, (340, y, 740, min(y + 120, 1140)), 20, cols[j % 4])
            put(img, L, 0.6 + 0.4 * a, W / 2, 900, alpha=a)
        if t >= P(K_HOW):
            emoji(img, "😱", 860, 640, 150 * min(1, pop(t, P(K_HOW))))
    else:
        T(img, "TRY THIS", W / 2, 230, 104, INK, key="try")
        if k < K_STUDY:
            # two rooms: desk (crossed out) vs other room
            zine(img, (90, 360, 510, 1080), CREAM)
            zine(img, (570, 360, 990, 1080), WHITE)
            T(img, "DESK", 300, 430, 64, INK, key="desk")
            T(img, "OTHER ROOM", 780, 430, 64, INK, key="other")
            emoji(img, "📱", 300, 700, 170, rot=8 if t >= P(K_FACE) else 0)
            if t >= P(K_FACE):
                emoji(img, "❌", 300, 900, 150 * min(1, pop(t, P(K_FACE))))
            emoji(img, "🚪", 780, 700, 190)
            if t >= P(K_ANOTHER):
                emoji(img, "✅", 780, 900, 150 * min(1, pop(t, P(K_ANOTHER))))
        else:
            a = pop(t, P(K_STUDY), 0.35)
            L = layer()
            zine(L, (90, 360, W - 90, 1090), WHITE)
            box(L, (250, 400, 830, 490), 45, PINK)
            T(L, "ONE 2017 STUDY", W / 2, 445, 52, WHITE, key="study")
            if t >= P(K_DESK):
                T(L, "Desk vs other room", W / 2, 590, 66, INK, key="vs")
            if t >= P(K_SCORED):
                T(L, "Other room did better", W / 2, 720, 66, PINK, key="better")
            if t >= P(K_SILENT):
                T(L, "(phones on silent)", W / 2, 820, 50, INK, f="xbold", key="silent")
            if t >= P(K_MIXED):
                T(L, "Later studies: mixed", W / 2, 960, 56, INK, f="xbold", key="mixed")
            put(img, L, 0.8 + 0.2 * min(1, a), W / 2, 720, alpha=min(1, a * 1.5))
            if t >= P(K_HALL):
                emoji(img, "🚪", 930, 1070, 130 * min(1, pop(t, P(K_HALL))), rot=-8)
        if k >= K_LAST:
            emoji(img, "👇", W / 2, 1530 + 14 * math.sin(t * 8), 110)
    captions(img, S, t, y=1300, size=100, fill=WHITE, lit=PINK if not night else HL, stroke=INK)
    return img


cues = [("sfx-tick-ding", 0.0, -12), ("sfx-tick-ding", P(K_701), -10), ("sfx-phone-buzz", P(K_CHECK) - 0.45, -8),
        ("sfx-record-scratch", P(K_743) - 0.05, -6), ("sfx-door-open", P(K_PHONE) - 0.2, -9), ("sfx-whoosh-soft", P(K_STUDY) - 0.1, -10),
        ("sfx-paper", P(K_SCORED), -10), ("sfx-whoosh-soft", S.end_voice - 0.15, -10)]

if __name__ == "__main__":
    finish(S, frame, cues)
