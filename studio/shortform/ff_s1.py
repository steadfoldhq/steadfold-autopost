from common import *
COB=hexc("2B3FE0"); DCOB=hexc("16206B"); WHITE=hexc("FFFFFF"); SOFT=hexc("F5F7FF"); INK=hexc("0E1440"); CORAL=hexc("FF6A3D"); SCOR=hexc("FFB08F")
words, total = build_voice([(V+'ff-s1a-v3.mp3', V+'ff-s1a-v3.json'), (V+'ff-s1b-v3.mp3', V+'ff-s1b-v3.json')], OUT+'/ff-s1.voice.wav', pauses={14: 1.45})
groups = caption_groups(words)
T = lambda n, k=0, a=0: find_word(words, n, k, a)
tGap = T("gap"); tLate = T("Start"); t54 = T("54,000"); t150 = T("150,000"); tEarly = T("Start", 1); t18 = T("18,000"); t299 = T("299,000")
tAbout = T("About"); tCatch = T("Example"); tWhat = T("What", 0, tCatch)
cd = [tGap + 0.45 + i * 0.42 for i in range(3)]
ping_track(cd, total, OUT+'/ff-s1.fx.wav', vol=0.07, kind="tick")
LATE_FV, EARLY_FV = 150677, 298724

def money(v): return f"{int(round(v)):,}"

def card(img, x0, title, sub, col, put, fv, t_put, t_fv, t):
    rrect(img, (x0, 480, x0 + 450, 1120), 30, SOFT, shadow=(0, 14, DCOB))
    rrect(img, (x0, 480, x0 + 450, 590), 30, col)
    img_d = ImageDraw.Draw(img)
    draw_center(img, title, 500, font("black", 56), WHITE if col == CORAL else INK, maxw=420, x=x0 + 225)
    draw_center(img, sub, 606, font("semi", 34), INK, maxw=420, x=x0 + 225)
    if t < t_put - 0.1:
        draw_center(img, "?", 720, font("black", 230), COB, x=x0 + 225)
        return
    draw_center(img, "puts in " + money(put), 660, font("xbold", 42), INK, x=x0 + 225)
    p = ease((t - t_fv + 0.1) / 0.9) if t >= t_fv - 0.1 else 0
    v = put + (fv - put) * p
    draw_center(img, money(v) if p > 0 else "...", 730, font("black", 88), CORAL if col == CORAL else COB, x=x0 + 225, maxw=440)
    # bar
    full = 250; h = max(8, int(full * (v / EARLY_FV)))
    rrect(img, (x0 + 60, 1095 - h, x0 + 390, 1095), 12, col if col == CORAL else COB)

def frame(t):
    img = Image.new("RGBA", (W, H), COB)
    # subtle grain of rings
    brand_tag(img, "FULLY FUNDED", SOFT, y=150, size=30)
    draw_center(img, "SAME 150 A MONTH.", 205, font("black", 76), WHITE, maxw=1000)
    draw_center(img, "10 YEARS APART.", 290, font("black", 76), WHITE, maxw=1000)
    draw_center(img, "GUESS THE GAP.", 375, font("black", 76), SCOR, maxw=1000)
    card(img, 75, "START 25", "saves 150/mo to 65", CORAL, 72000, EARLY_FV, tEarly, t299, t)
    card(img, 555, "START 35", "saves 150/mo to 65", WHITE, 54000, LATE_FV, tLate, t150, t)
    if cd[0] - 0.1 <= t < tLate - 0.1:
        k = min(2, int((t - cd[0] + 0.1) / 0.42)); n = 3 - k
        a = back(((t - cd[0] + 0.1) % 0.42) / 0.2)
        def dr(L):
            d = ImageDraw.Draw(L); d.ellipse((400, 1160, 680, 1440), fill=CORAL, outline=WHITE, width=10)
            draw_center(L, str(n), 1180, font("black", 190), WHITE)
        paste_scaled(img, layer_draw(dr), 0.7 + 0.3 * a, W / 2, 1300)
        draw_center(img, "guess in your head", 1460, font("brush", 70), WHITE)
        return img
    if tAbout - 0.15 <= t < tCatch - 0.1:
        a = back((t - tAbout + 0.15) / 0.3)
        def dr(L):
            rrect(L, (90, 1160, 990, 1320), 34, CORAL, shadow=(0, 12, DCOB))
            draw_center(L, "≈148,000 apart", 1188, font("black", 92), WHITE, maxw=880)
        paste_scaled(img, layer_draw(dr), 0.6 + 0.4 * a, W / 2, 1240, alpha=min(1, a))
    if t >= tCatch - 0.1:
        a = appear(t, tCatch - 0.1)
        def dr(L):
            rrect(L, (70, 1150, 1010, 1340), 30, SOFT, outline=CORAL, width=6)
            draw_center(L, "THE CATCH", 1166, font("black", 46), CORAL)
            draw_center(L, "Example math at 6% a year. Real returns change, and can fall.", 1224, font("bold", 38), INK, maxw=880)
        paste_scaled(img, layer_draw(dr), 1, W / 2, 1245, alpha=a)
    if t >= t150:
        draw_center(img, "example math · 6% a year, monthly · not a promise", 1050 - 0, font("semi", 26), SOFT, maxw=960) if False else None
    draw_captions(img, t, words, groups, y=1380, accent=SCOR, stroke=INK, size=92)
    if t >= tWhat - 0.1:
        draw_center(img, "Your guess? ↓", 1500, font("brush", 76), WHITE, alpha=int(255 * appear(t, tWhat - 0.1)))
    return img

if __name__ == "__main__":
    print(render("FF-S1_guess-the-gap", total, frame, OUT+'/ff-s1.voice.wav', OUT+'/ff-s1.fx.wav', OUT), round(total, 2))
