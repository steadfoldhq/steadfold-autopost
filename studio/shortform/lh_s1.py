from common import *
INK=hexc("141414"); BUT=hexc("FFE27A"); CREAM=hexc("FFF4E0"); PINK=hexc("FF5CA8"); HL=hexc("FFD43B"); WHITE=hexc("FFFFFF")
words, total = build_voice([(V+'lh-s1-v3.mp3', V+'lh-s1-v3.json')], OUT+'/lh-s1.voice.wav', pauses={10: 3.6})
groups = caption_groups(words)
T = lambda n, k=0, a=0: find_word(words, n, k, a)
t_brain = T("brain"); t_in = T("in") ; t_fix = T("Here's"); t_ift = T("if-then"); t_if = T("If", 0, t_ift + 0.3)
t_then = T("then", 0, t_if); t_94 = T("94"); t_write = T("Write", 0, t_94)
bubbles = ["quick question", "did we reply to Sam", "is the oven off??", "how long do otters sleep", "that thing from 2014", "new song idea", "check the phone. once."]
b_times = [t_in + 0.2 + i * 0.5 for i in range(len(bubbles))]
ping_track(b_times, total, OUT+'/lh-s1.fx.wav', vol=0.09)

def timer_card(img, t):
    secs = 3600 - (0 if t < t_brain else 240) - max(0, t - (t_brain if t >= t_brain else 0))
    secs = int(max(0, secs))
    zine_card(img, (190, 420, 890, 640), CREAM)
    d = ImageDraw.Draw(img)
    s = f"{secs//60:02d}:{secs%60:02d}"
    f = font("black", 150); tw = text_size(d, s, f)[0]
    d.text(((W - tw) / 2, 430), s, font=f, fill=INK)
    f2 = font("xbold", 34); lab = "DEEP FOCUS  \u00b7  LOCKED IN"; tw = text_size(d, lab, f2)[0]
    d.text(((W - tw) / 2, 590), lab, font=f2, fill=PINK)

def frame(t):
    img = bg_dots(BUT, hexc("E9C95C"), drift=(0, 6), t=t)
    brand_tag(img, "LOCKED HOUR", INK, y=150, size=30)
    if t < t_fix - 0.2:
        # hook headline
        hd = "MY BRAIN, 4 MINUTES INTO “DEEP FOCUS”"
        draw_center(img, hd, 205 - 0, font("black", 62), INK, maxw=900) if False else None
        timer_card(img, t)
        draw_center(img, "ME: 1 HOUR OF DEEP FOCUS" if t < t_brain - 0.1 else "MY BRAIN, 4 MIN IN:", 240, font("black", 74), INK if t < t_brain - 0.1 else PINK, maxw=1000)
        # bubbles
        y = 700
        for i, (b, bt) in enumerate(zip(bubbles, b_times)):
            if t < bt: break
            a = back((t - bt) / 0.22)
            def dr(L, b=b, y=y):
                d = ImageDraw.Draw(L); f = font("xbold", 58)
                tw = text_size(d, b, f)[0]; x0 = 190
                rrect(L, (x0, y, x0 + tw + 70, y + 104), 52, WHITE, outline=INK, width=5, shadow=(8, 8, INK))
                d.text((x0 + 35, y + 16), b, font=f, fill=INK)
                d.ellipse((70, y + 6, 158, y + 94), fill=PINK, outline=INK, width=5)
                fb = font("black", 24); d.text((114 - text_size(d, "BRAIN", fb)[0] / 2, y + 36), "BRAIN", font=fb, fill=WHITE)
            paste_scaled(img, layer_draw(dr), 0.6 + 0.4 * a, 190, y + 50, alpha=min(1, a * 1.5))
            y += 118
        if t > b_times[-1] + 0.5:
            cnt = min(len(bubbles), 5)
    else:
        # the fix
        a = appear(t, t_fix - 0.2)
        zine_card(img, (70, 250, 1010, 420), PINK)
        draw_center(img, "THE FIX: AN IF-THEN PLAN", 296, font("black", 64), WHITE, maxw=920, alpha=int(255 * a))
        if t >= t_if - 0.15:
            zine_card(img, (70, 480, 1010, 1000), CREAM)
            d = ImageDraw.Draw(img); f = font("black", 76); fb = font("xbold", 66)
            d.text((120, 515), "IF", font=f, fill=PINK)
            d.text((120, 605), "I want my phone,", font=fb, fill=INK)
            if t >= t_then - 0.1:
                p = ease((t - t_then) / 0.6)
                d.rectangle((110, 800, 110 + int(560 * p), 880), fill=HL)
                d.rectangle((110, 885, 110 + int(580 * max(0, p * 1.4 - 0.4)), 965), fill=HL)
                d.text((120, 710), "THEN", font=f, fill=PINK)
                d.text((120, 800), "I write it down", font=fb, fill=INK)
                d.text((120, 885), "and keep going.", font=fb, fill=INK)
        if t_94 - 0.2 <= t < t_write - 0.2:
            a2 = back((t - t_94 + 0.2) / 0.3)
            def st(L):
                rrect(L, (90, 1040, 990, 1230), 30, INK, shadow=(10, 10, PINK))
                draw_center(L, "94 studies back this up", 1062, font("black", 48), HL, maxw=860)
                draw_center(L, "Gollwitzer & Sheeran 2006 meta-analysis: medium-to-large effect", 1150, font("semi", 32), WHITE, maxw=860)
            paste_scaled(img, layer_draw(st), 0.7 + 0.3 * a2, W / 2, 1135, alpha=min(1, a2))
    if t >= t_write - 0.2:
        a3 = appear(t, t_write - 0.2)
        def en(L):
            rrect(L, (90, 1040, 990, 1230), 30, WHITE, outline=INK, width=6, shadow=(10, 10, INK))
            draw_center(L, "Your turn: IF ___ THEN ___", 1100, font("black", 58), INK, maxw=860)
        paste_scaled(img, layer_draw(en), 1, W / 2, 1135, alpha=a3)
    if not (t_in + 0.1 < t < t_fix - 0.2): draw_captions(img, t, words, groups, y=1300 if t < t_fix else 1300, accent=PINK, stroke=INK, size=92)
    return img

if __name__ == "__main__":
    print(render("LH-S1_brain-vs-me", total, frame, OUT+'/lh-s1.voice.wav', OUT+'/lh-s1.fx.wav', OUT), round(total, 2))
