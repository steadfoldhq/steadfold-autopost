from hb_common import *
words, total = build_voice([(V+'hb-s1.mp3', V+'hb-s1.json')], OUT+'/hb-s1.voice.wav', maxgap=0.38, pauses={15: 1.4})
groups = caption_groups(words)
T = lambda n, k=0, a=0: find_word(words, n, k, a)
tWhat = T("What"); tWhat2 = T("What", 1); tOne = T("One"); tMake = T("make"); tThen = T("Then"); tRead = T("read")
ping_track([tWhat2, tThen], total, OUT+'/hb-s1.fx.wav', vol=0.07, kind="pop")
TYPED = "As I already said TWICE, the file is in the folder. Please read my emails."
SENT = "Quick resend in case it got buried: the file is in the shared folder. Happy to walk you through it if that's easier!"

def mail(L, box, label, body, lab_col, body_col, strike=0.0):
    rrect(L, box, 30, WHITE, shadow=(0, 14, (0, 0, 0, 90)))
    d = ImageDraw.Draw(L); x0, y0, x1, y1 = box
    rrect(L, (x0 + 30, y0 + 26, x0 + 30 + text_size(d, label, font("black", 32))[0] + 40, y0 + 80), 16, lab_col)
    d.text((x0 + 50, y0 + 34), label, font=font("black", 32), fill=WHITE)
    f = font("xbold", 52); lines = wrap(d, body, f, x1 - x0 - 80); y = y0 + 106
    for ln in lines:
        d.text((x0 + 40, y), ln, font=f, fill=body_col)
        if strike > 0:
            tw = text_size(d, ln, f)[0]; d.line((x0 + 40, y + 28, x0 + 40 + tw * min(1, strike), y + 28), fill=ORA, width=6)
        y += 64

def frame(t):
    img = Image.new("RGBA", (W, H), IND)
    brand_tag(img, "HOURBACK", CRM, y=150, size=30)
    if t < tWhat - 0.1:
        draw_center(img, "POV: you need to say “per my last email”", 240, font("black", 80), WHITE, maxw=980)
        draw_center(img, "without starting a war", 440, font("brush", 84), YEL, maxw=980)
        # compose window with cursor
        def cmp(L):
            rrect(L, (110, 620, 970, 990), 30, WHITE, shadow=(0, 14, (0, 0, 0, 90)))
            d = ImageDraw.Draw(L); d.text((150, 650), "To: Jordan", font=font("bold", 36), fill=GREY)
            d.line((150, 705, 930, 705), fill=(230, 226, 240, 255), width=3)
            s = "Per my last email,"; n = int(min(len(s), 7 + max(0, t * 12)))
            d.text((150, 740), s[:n] + ("|" if int(t * 3) % 2 == 0 else ""), font=font("xbold", 54), fill=INK)
        img.alpha_composite(layer_draw(cmp))
    else:
        top = "TYPED vs SENT"
        draw_center(img, top, 230, font("black", 84), WHITE, maxw=980)
        if t < tOne - 0.15:
            a = back((t - tWhat + 0.1) / 0.3)
            sp = ease((t - tWhat - 1.1) / 0.6) if t >= tWhat + 1.1 else 0
            paste_scaled(img, layer_draw(lambda L: mail(L, (60, 340, 1020, 720), "TYPED", TYPED, ORA, INK, strike=sp)), 0.7 + 0.3 * a, W / 2, 530, alpha=min(1, a))
        else:
            a = back((t - tOne + 0.15) / 0.3)
            paste_scaled(img, layer_draw(lambda L: prompt_card(L, (60, 340, 1020, 720), "Make this kind but clear.", ["[keep it short]"], t, tMake)), 0.7 + 0.3 * a, W / 2, 560, alpha=min(1, a))
        if t >= tWhat2 - 0.1:
            a = back((t - tWhat2 + 0.1) / 0.3)
            y0 = 750
            paste_scaled(img, layer_draw(lambda L: mail(L, (60, y0, 1020, y0 + 440), "SEND", SENT, hexc("1FA971"), INK)), 0.7 + 0.3 * a, W / 2, y0 + 220, alpha=min(1, a))
        if t >= tRead - 0.1:
            a = back((t - tRead + 0.1) / 0.3)
            def st(L):
                rrect(L, (580, 1130, 1020, 1230), 20, YEL, outline=INK, width=5)
                draw_center(L, "READ IT FIRST", 1152, font("black", 50), INK, x=800)
            L = layer_draw(st).rotate(5, center=(800, 1180), resample=Image.BICUBIC)
            paste_scaled(img, L, 1.5 - 0.5 * a, 800, 1180, alpha=min(1, a))
    draw_captions(img, t, words, groups, y=1300, accent=YEL, stroke=INK, size=92)
    footer(img, "Example made up · written with AI", 1450)
    return img

if __name__ == "__main__":
    print(render("HB-S1_per-my-last-email", total, frame, OUT+'/hb-s1.voice.wav', OUT+'/hb-s1.fx.wav', OUT), round(total, 2))
