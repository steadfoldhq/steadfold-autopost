from common import *
DCOB=hexc("16206B"); COB=hexc("2B3FE0"); CREAM=hexc("F7F1E5"); WHITE=hexc("FFFFFF"); INK=hexc("0E1440"); CORAL=hexc("FF6A3D"); SCOR=hexc("FFB08F"); GRN=hexc("1FA971")
words, total = build_voice([(V+'ff-s2-v3.mp3', V+'ff-s2-v3.json')], OUT+'/ff-s2.voice.wav')
groups = caption_groups(words)
T = lambda n, k=0, a=0: find_word(words, n, k, a)
tAll = T("All"); tFirst = T("First"); tCl = T("clients"); tNob = T("nobody"); tThen = T("Then"); tOwe = T("owe", 0, tThen)
tNow = T("Now"); tFix = T("fix"); tMove = T("move"); tCatch = T("catch")
pays = [("+ 2,400.00", tCl + 0.1), ("+ 1,150.00", tCl + 0.5), ("+ 3,800.00", tCl + 0.9)]
ping_track([p[1] for p in pays] + [0.05], total, OUT+'/ff-s2.fx.wav', vol=0.08)

def notif(L, y, amt):
    rrect(L, (110, y, 970, y + 130), 34, WHITE, shadow=(0, 10, (0, 0, 0, 90)))
    d = ImageDraw.Draw(L)
    d.ellipse((140, y + 25, 220, y + 105), fill=GRN)
    d.text((165, y + 33), "$", font=font("black", 56), fill=WHITE)
    d.text((250, y + 22), "Payment received", font=font("bold", 34), fill=(90, 96, 130, 255))
    d.text((250, y + 62), amt, font=font("black", 52), fill=INK)

def scene_card(img, t, t0, box, fill, draw_fn, pop=True):
    a = back((t - t0) / 0.3) if pop else appear(t, t0)
    def dr(L):
        rrect(L, box, 34, fill, shadow=(0, 14, (0, 0, 0, 110))); draw_fn(L)
    paste_scaled(img, layer_draw(dr), 0.7 + 0.3 * a, (box[0] + box[2]) / 2, (box[1] + box[3]) / 2, alpha=min(1, a * 1.4))

def calendar(L, cy=430, sc=1.0):
    rrect(L, (300, cy - 180, 780, cy + 170), 30, CREAM, shadow=(0, 14, (0, 0, 0, 110)))
    rrect(L, (300, cy - 180, 780, cy - 80), 30, CORAL)
    draw_center(L, "APRIL", cy - 168, font("black", 70), WHITE)
    draw_center(L, "30", cy - 60, font("black", 190), INK)

def frame(t):
    img = Image.new("RGBA", (W, H), DCOB)
    brand_tag(img, "FULLY FUNDED  \u00b7  CANADA SERIES", SCOR, y=150, size=30)
    if t < tFirst - 0.15:
        draw_center(img, "YOU OWE THE CRA.", 220, font("black", 88), WHITE, maxw=1000)
        img.alpha_composite(layer_draw(lambda L: calendar(L, 560)))
        if t >= tAll - 0.15:
            scene_card(img, t, tAll - 0.15, (110, 790, 970, 1060), WHITE, lambda L: (
                draw_center(L, "CRA \u00b7 balance owing", 815, font("bold", 40), (90, 96, 130, 255)),
                draw_center(L, "All of it. At once.", 880, font("black", 76), CORAL, maxw=820)))
    elif t < tThen - 0.1:
        draw_center(img, "POV: FIRST YEAR FREELANCING IN CANADA", 220, font("black", 76), WHITE, maxw=1000)
        for i, (amt, ti) in enumerate(pays):
            if t >= ti:
                a = back((t - ti) / 0.25)
                L = layer_draw(lambda L, i=i, amt=amt: notif(L, 520 + i * 160, amt))
                paste_scaled(img, L, 0.7 + 0.3 * a, W / 2, 585 + i * 160, alpha=min(1, a * 1.5))
        if t >= tCl:
            draw_center(img, "example amounts", 1010, font("semi", 28), SCOR)
        if t >= tNob - 0.1:
            a = back((t - tNob + 0.1) / 0.3)
            def st(L):
                rrect(L, (200, 1080, 880, 1200), 20, (0, 0, 0, 0), outline=CORAL, width=8)
                draw_center(L, "TAX TAKEN OFF: 0.00", 1106, font("black", 58), CORAL)
            L = layer_draw(st).rotate(-4, center=(540, 1140), resample=Image.BICUBIC)
            paste_scaled(img, L, 1.6 - 0.6 * a, W / 2, 1140, alpha=min(1, a))
    elif t < tFix - 0.15:
        draw_center(img, "THEN APRIL. AND IF\u2026", 220, font("black", 80), WHITE, maxw=1000)
        if t >= tOwe - 0.15:
            scene_card(img, t, tOwe - 0.15, (70, 400, 1010, 720), SCOR, lambda L: (
                draw_center(L, "you owe over $3,000 this year AND in 1 of the last 2 years", 430, font("black", 58), INK, maxw=880),
                draw_center(L, "($1,800 in Qu\u00e9bec)", 650, font("bold", 34), INK)))
        if t >= tNow - 0.15:
            scene_card(img, t, tNow - 0.15, (70, 770, 1010, 1130), WHITE, lambda L: (
                draw_center(L, "\u2026you pay every quarter too", 800, font("black", 58), CORAL, maxw=880),
                draw_center(L, "Mar 15 \u00b7 Jun 15 \u00b7 Sep 15 \u00b7 Dec 15", 900, font("xbold", 48), INK, maxw=900),
                draw_center(L, "source: canada.ca", 1060, font("semi", 28), (90, 96, 130, 255))))
    else:
        draw_center(img, "THE FIX", 220, font("black", 90), SCOR)
        p = ease((t - tMove) / 0.9) if t >= tMove else 0
        img.alpha_composite(layer_draw(lambda L: notif(L, 380, "+ 2,400.00")))
        if p > 0:
            y = 540 + int(260 * p)
            rrect(img, (110, 540, 580, 540 + int(260 * min(1, p * 1.2))), 30, CREAM)
            if p > 0.6: draw_center(img, "Yours to spend", 580, font("xbold", 40), INK, x=345)
            rrect(img, (610, 540, 970, y), 30, CORAL, shadow=(0, 10, (0, 0, 0, 80)))
            if p > 0.6:
                draw_center(img, "Tax pot", 580, font("black", 46), WHITE, x=790)
                draw_center(img, "the day it lands", 650, font("brush", 50), WHITE, x=790)
        if t >= tCatch - 0.1:
            scene_card(img, t, tCatch - 0.1, (70, 870, 1010, 1180), CREAM, lambda L: (
                draw_center(L, "THE CATCH", 895, font("black", 48), CORAL),
                draw_center(L, "Your slice depends on your province and income.", 965, font("black", 52), INK, maxw=860)), pop=False)
        if t >= tCatch + 2.2:
            draw_center(img, "Our Canadian Freelancer tracker does the math \u00b7 link in bio", 1440, font("xbold", 38), SCOR, maxw=900, alpha=int(255 * appear(t, tCatch + 2.2)))
    draw_captions(img, t, words, groups, y=1310, accent=SCOR, stroke=INK, size=90)
    return img

if __name__ == "__main__":
    print(render("FF-S2_pov-freelancer-april", total, frame, OUT+'/ff-s2.voice.wav', OUT+'/ff-s2.fx.wav', OUT), round(total, 2))
