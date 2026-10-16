"""LH round 2 · POV mini-scene: 'you sat down to study at 7' -> 7:43. Fix: phone in another room.
Evidence: Ward, Duke, Gneezy & Bos (2017), 'Brain Drain', J. Assoc. Consumer Research 2(2): with phones silenced,
people with the phone in another room did better on working-memory and fluid-intelligence tasks than people with it
on the desk. Later replications are mixed (said in the voice and on screen).

Round 2b (Oct 16 pm): one continuous Eleven v3 take (house voice), continuous rain-and-room ambience and music under
everything (no dead air), floating text with a soft shadow (no dark boxes), Locked Hour colour scenes with bold cuts."""
from r2 import *  # noqa: F403

YEL, INK, PINK, HL, CREAM, WHITE = (hexc(x) for x in ("FFE27A", "141414", "E83E8C", "FFD43B", "FFF4E0", "FFFFFF"))
MAG, NIGHT, SKY = hexc("B0105A"), hexc("1B1830"), hexc("6C8CFF")

S = Script("lh-r2-pov-7pm-v3-t2", out_name="LH-R2-pov-7pm")
P = S.p
K_OKAY, K_701, K_CHECK, K_743, K_HOW, K_TRY, K_PHONE, K_FACE, K_ANOTHER, K_STUDY, K_DESK, K_SCORED, K_SILENT, K_MIXED, K_HALL, K_LAST = (
    S.phrase("Okay"), S.phrase("7:01"), S.phrase("checking"), S.phrase("7:43?!"), S.phrase("How is it"), S.phrase("Try this"),
    S.phrase("Phone in another"), S.phrase("face down"), S.phrase("Another room."), S.phrase("2017"), S.phrase("on the desk"),
    S.phrase("scored better"), S.phrase("silent"), S.phrase("mixed"), S.phrase("hallway"), S.phrase("did your 7"))

C1, C2, C3 = P(K_TRY), P(K_STUDY), P(K_HALL)          # scene cuts land exactly on the spoken line
SCENES = [(0, NIGHT, (255, 255, 255, 16)), (C1, YEL, (20, 20, 20, 24)), (C2, PINK, (255, 255, 255, 30)), (C3, YEL, (20, 20, 20, 24))]
CUTS = [(C1, PINK, "wipeR"), (C2, INK, "wipeU"), (C3, PINK, "iris")]


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
    img = scene_bg(t, SCENES)
    if t >= S.end_voice:
        endcard(img, S, t, YEL, "lockedhour.png")
        return img
    if t < C1:
        T(img, "WHERE DID THE HOUR GO?", W / 2, 230, 84, HL, key="hook")
        # the clock floats: huge digits, no box
        sx, sy = shake(t, P(K_743), 0.45, 30)
        L = layer()
        late = t >= P(K_743)
        T(L, clock_txt(t), 540, 500, 250, (255, 120, 180, 255) if late else HL, key="clock", words=1)
        punch = 1.0 + 0.14 * max(0.0, 1 - (t - P(K_743)) / 0.35) * late
        put(img, L, punch, W / 2, 500, dx=sx, dy=sy)
        box(img, (90, 1000, W - 90, 1050), 14, (90, 70, 50, 255))
        emoji(img, "📖", 360, 900, 200)
        buzz = 10 * math.sin(t * 60) if P(K_CHECK) - 0.4 <= t < P(K_CHECK) + 0.6 else 0
        if t < P(K_CHECK):
            emoji(img, "📱", 720 + buzz, 900, 170, rot=-8)
        else:  # doom-scroll: the phone grows and colourful posts fly past (no words)
            a = min(1, pop(t, P(K_CHECK), 0.3))
            L = layer()
            zine(L, (310, 640, 770, 1110), (245, 245, 250, 255), r=50, sh=10, ink=INK)
            off = (t - P(K_CHECK)) * 520
            cols = [PINK, HL, SKY, (120, 220, 170, 255)]
            for j in range(-1, 6):
                y = 690 + ((j * 150 - off) % 900) - 150
                if 650 < y < 1050:
                    box(L, (340, y, 740, min(y + 120, 1090)), 20, cols[j % 4])
            put(img, L, 0.6 + 0.4 * a, W / 2, 875, alpha=a)
        if t >= P(K_HOW):
            emoji(img, "😱", 870, 400, 170 * min(1, pop(t, P(K_HOW))), rot=-8)
    elif t < C2:
        T(img, "TRY THIS", W / 2, 230, 120, INK, key="try")
        a = pop(t, C1 + 0.05, 0.35)
        L = layer()
        zine(L, (90, 360, 510, 1080), CREAM)
        zine(L, (570, 360, 990, 1080), WHITE)
        T(L, "DESK", 300, 440, 60, INK, key="desk")
        T(L, "OTHER ROOM", 780, 440, 56, INK, key="other")
        emoji(L, "📱", 300, 700, 170, rot=8 if t >= P(K_FACE) else 0)
        if t >= P(K_FACE):
            emoji(L, "❌", 300, 920, 150 * min(1, pop(t, P(K_FACE))))
        emoji(L, "🚪", 780, 700, 190)
        if t >= P(K_ANOTHER):
            emoji(L, "✅", 780, 920, 150 * min(1, pop(t, P(K_ANOTHER))))
        put(img, L, 0.75 + 0.25 * min(1, a), W / 2, 720, dy=(1 - min(1, a)) * 120)
    elif t < C3:
        T(img, "ONE 2017 STUDY", W / 2, 230, 96, WHITE, key="study")
        a = pop(t, C2 + 0.05, 0.35)
        L = layer()
        zine(L, (90, 360, W - 90, 1090), WHITE)
        if t < P(K_SCORED):   # the mini vote: phone on the desk, or behind the door?
            emoji(L, "📱", 360, 800, 200, rot=-6 + 4 * math.sin(t * 7))
            emoji(L, "🚪", 720, 800, 220)
            if t >= P(K_DESK):
                emoji(L, "❓", W / 2, 800, 120, rot=8 * math.sin(t * 5))
        if t >= P(K_DESK):
            T(L, "Desk vs other room", W / 2, 470, 66, INK, key="vs")
        if t >= P(K_SCORED):
            q = min(1, pop(t, P(K_SCORED), 0.3))
            T(L, "Other room", W / 2, 640, 110, MAG, key="better1", scale=0.8 + 0.2 * q, words=2)
            T(L, "did better", W / 2, 760, 110, MAG, key="better2", scale=0.8 + 0.2 * q, words=2)
        if t >= P(K_SILENT):
            T(L, "(phones on silent)", W / 2, 880, 54, INK, f="xbold", key="silent")
        if t >= P(K_MIXED):
            T(L, "Later studies: mixed", W / 2, 990, 58, INK, f="xbold", key="mixed")
        put(img, L, 0.8 + 0.2 * min(1, a), W / 2, 720, alpha=min(1, a * 1.5))
    else:
        T(img, "THE HALLWAY", W / 2, 260, 120, INK, key="hall1")
        T(img, "IS FREE.", W / 2, 390, 120, MAG, key="hall2")
        a = pop(t, C3 + 0.05, 0.4)
        emoji(img, "🚪", W / 2 - 120, 780, 340 * min(1, a), rot=-4)
        emoji(img, "📱", W / 2 + 190, 860, 150 * min(1, pop(t, C3 + 0.35)), rot=14)
        if k >= K_LAST:
            emoji(img, "👇", W / 2, 1560 + 14 * math.sin(t * 8), 110)
    if t < C1:
        cap = dict(fill=WHITE, lit=HL)
    elif C2 <= t < C3:
        cap = dict(fill=WHITE, lit=INK)
    else:
        cap = dict(fill=INK, lit=MAG)
    captions(img, S, t, y=1300, size=100, **cap)
    img = transition(img, t, CUTS)
    return img


cues = [("sfx-tick-ding", 0.05, -12), ("sfx-tick-ding", P(K_701), -10), ("sfx-phone-buzz", P(K_CHECK) - 0.45, -8),
        ("sfx-record-scratch", P(K_743) - 0.05, -6), ("sfx-whoosh-fast", C1 - 0.17, -8), ("sfx-door-open", P(K_PHONE) - 0.2, -10),
        ("sfx-whoosh-fast", C2 - 0.17, -8), ("sfx-paper", P(K_SCORED), -10), ("sfx-whoosh-soft", C3 - 0.17, -8),
        ("st-1-soft-rise-el", S.end_voice - 0.6, -14)]

if __name__ == "__main__":
    finish(S, frame, cues, bed="v3/lh-a-focus-pulse-el.mp3", amb="amb-night-rain.mp3")
