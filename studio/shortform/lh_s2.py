from common import *
INK=hexc("141414"); BUT=hexc("FFE27A"); CREAM=hexc("FFF4E0"); PINK=hexc("FF5CA8"); HL=hexc("FFD43B"); WHITE=hexc("FFFFFF"); DPINK=hexc("E8336F")
words, total = build_voice([(V+'lh-s2.mp3', V+'lh-s2.json')], OUT+'/lh-s2.voice.wav')
groups = caption_groups(words)
T = lambda n, k=0, a=0: find_word(words, n, k, a)
tC = T("colour-coding"); tB = T("quick"); tA = T("building"); tS = T("rewriting"); tReal = T("Real"); tWhich = T("Which")
tPretty = T("pretty"); tNever = T("never"); tForty = T("forty"); tAgain = T("Again")
ping_track([tC, tB, tA, tS], total, OUT+'/lh-s2.fx.wav', vol=0.10, kind="pop")
rows = [("S", PINK, tS, "Rewriting your to-do list", tAgain, "beautifully. again."),
        ("A", HL, tA, "The perfect focus playlist", tForty, "40 minutes in"),
        ("B", CREAM, tB, "A “quick” inbox check", tNever, "never quick"),
        ("C", WHITE, tC, "Colour-coding your notes", tPretty, "0 words written")]
Y0, RH = 430, 212

def frame(t):
    img = bg_dots(BUT, hexc("E9C95C"), drift=(0, 6), t=t)
    brand_tag(img, "LOCKED HOUR", INK, y=150, size=30)
    draw_center(img, "FAKE PRODUCTIVITY, RANKED", 230, font("black", 84), INK, maxw=960)
    for i, (lab, col, ti, item, tn, note) in enumerate(rows):
        y = Y0 + i * RH
        zine_card(img, (60, y, 220, y + RH - 26), col, r=18, sh=8, width=5)
        draw_center(img, lab, y + 22, font("black", 104), INK, maxw=150, x=140)
        rrect(img, (240, y, 1000, y + RH - 26), 18, (255, 255, 255, 110), outline=INK, width=4)
        if t >= ti - 0.1:
            a = back((t - ti + 0.1) / 0.3)
            def dr(L, y=y, item=item):
                rrect(L, (262, y + 18, 980, y + RH - 46), 16, WHITE, outline=INK, width=4, shadow=(6, 6, INK))
                f = font("xbold", 46); d = ImageDraw.Draw(L)
                d.text((290, y + 34), item, font=f, fill=INK)
            dy = int((1 - a) * -120)
            L = layer_draw(dr)
            if dy: L = L.transform(L.size, Image.AFFINE, (1, 0, 0, 0, 1, -dy))
            img.alpha_composite(L)
        if t >= tn - 0.05:
            a2 = appear(t, tn - 0.05, 0.2)
            d = ImageDraw.Draw(img); f = font("brush", 50)
            txt = note; tw = 0
            col2 = DPINK[:3] + (int(255 * a2),)
            d.text((292, y + 92), "- " + txt, font=f, fill=col2)
    if t >= tReal - 0.15:
        a = back((t - tReal + 0.15) / 0.3)
        img.alpha_composite(Image.new("RGBA", (W, H), BUT[:3] + (int(200 * min(1, a)),)))
        def st(L):
            rrect(L, (70, 600, 1010, 940), 34, PINK, outline=INK, width=8, shadow=(16, 16, INK))
            draw_center(L, "REAL WORK:", 640, font("black", 100), WHITE, maxw=900)
            draw_center(L, "the next ugly 25 minutes", 770, font("black", 72), INK, maxw=900)
        L = layer_draw(st); paste_scaled(img, L, 0.6 + 0.4 * a, W / 2, 770, alpha=min(1, a))
    draw_captions(img, t, words, groups, y=1300, accent=PINK, stroke=INK, size=92)
    if t >= tWhich - 0.1:
        draw_center(img, "Which one's yours? ↓", 1010, font("black", 66), INK, maxw=900, alpha=int(255 * appear(t, tWhich - 0.1)))
    return img

if __name__ == "__main__":
    print(render("LH-S2_fake-productivity-tier-list", total, frame, OUT+'/lh-s2.voice.wav', OUT+'/lh-s2.fx.wav', OUT), round(total, 2))
