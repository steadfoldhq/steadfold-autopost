from hb_common import *
words, total = build_voice([(V+'hb-s2.mp3', V+'hb-s2.json')], OUT+'/hb-s2.voice.wav', maxgap=0.38)
groups = caption_groups(words)
T = lambda n, k=0, a=0: find_word(words, n, k, a)
tYou = T("You"); tPaste = T("Paste"); tWhat = T("what", 0, tPaste); tThree = T("Three"); tUncle = T("Uncle")
MSGS = [("Mum", "who is bringing the rice"), ("Priya", "not me I did it last time \U0001F643"), ("Uncle Dev", "I will bring dessert"),
        ("Arjun", "what time are we eating"), ("Mum", "6. or 6:30. depends"), ("Priya", "depends on what??"),
        ("Uncle Dev", "dessert might be store bought"), ("Nani", "\U0001F44D"), ("Arjun", "so 6 or 6:30"),
        ("Mum", "6:30. FINAL"), ("Priya", "can someone bring chairs"), ("Uncle Dev", "dessert update: tbc"),
        ("Arjun", "who has the salad"), ("Mum", "YOU have the salad"), ("Nani", "6:30 at mine ❤"), ("Priya", "reply by Fri for headcount")]
MSGS = [(n, m.replace("\U0001F643", "").replace("\U0001F44D", "ok").replace("❤", "")) for n, m in MSGS]
COLS = {"Mum": ORA, "Priya": hexc("1FA971"), "Uncle Dev": IND, "Arjun": hexc("E25A86"), "Nani": hexc("2B7BE0")}
ping_track([0.05 + i * 0.22 for i in range(12)], total, OUT+'/hb-s2.fx.wav', vol=0.035)
RESULT = [("Decided:", "Sunday 6:30 pm at Nani's"), ("Bringing:", "you: salad · Uncle Dev: dessert"), ("Reply:", "headcount to Priya by Friday")]

def chat(L, t):
    rrect(L, (90, 330, 990, 1180), 40, CRM2, shadow=(0, 14, (0, 0, 0, 90)))
    d = ImageDraw.Draw(L)
    rrect(L, (90, 330, 990, 430), 40, WHITE)
    d.text((140, 358), "Family ❤", font=font("black", 40), fill=INK) if False else d.text((140, 358), "Family (12)", font=font("black", 40), fill=INK)
    cnt = 214
    rrect(L, (720, 352, 960, 410), 29, ORA); draw_center(L, f"{cnt} unread", 358, font("black", 36), WHITE, x=840)
    # scrolling messages
    sc = t * 260
    clip = Image.new("RGBA", (W, H), (0, 0, 0, 0)); cd = ImageDraw.Draw(clip)
    y = 1150 - sc
    for i in range(60):
        n, m = MSGS[i % len(MSGS)]
        y_i = 450 + i * 116 - sc
        if y_i < 420 or y_i > 1160: continue
        f = font("bold", 46); tw = text_size(cd, m, f)[0]
        rrect(clip, (120, y_i, 120 + max(tw, 200) + 50, y_i + 100), 26, WHITE)
        cd.text((145, y_i + 6), n, font=font("black", 28), fill=COLS[n])
        cd.text((145, y_i + 38), m, font=f, fill=INK)
    mask = Image.new("L", (W, H), 0); ImageDraw.Draw(mask).rectangle((90, 430, 990, 1170), fill=255)
    L.paste(clip, (0, 0), Image.composite(clip, Image.new("RGBA", (W, H)), mask).split()[3])

def frame(t):
    img = Image.new("RGBA", (W, H), IND)
    brand_tag(img, "HOURBACK", CRM, y=150, size=30)
    if t < tPaste - 0.15:
        draw_center(img, "214 UNREAD.", 196, font("black", 84), WHITE, maxw=1000)
        draw_center(img, "what time is dinner?", 278, font("brush", 0 or 70), YEL, maxw=1000) if False else None
        img.alpha_composite(layer_draw(lambda L: chat(L, min(t, 6.0))))
    elif t < tThree - 0.15:
        draw_center(img, "PASTE IT IN. ASK 3 THINGS.", 210, font("black", 70), WHITE, maxw=1000)
        a = back((t - tPaste + 0.15) / 0.3)
        paste_scaled(img, layer_draw(lambda L: prompt_card(L, (90, 360, 990, 830), "From this chat, give me:", ["[what got decided]", "[who's bringing what]", "[what I need to reply to]"], t, tWhat)), 0.7 + 0.3 * a, W / 2, 600, alpha=min(1, a))
        draw_center(img, "Remove names + numbers you don't want to share first.", 900, font("bold", 36), CRM, maxw=900)
    else:
        draw_center(img, "THREE LINES.", 210, font("black", 84), WHITE, maxw=1000)
        def res(L):
            rrect(L, (70, 360, 1010, 1060), 34, WHITE, shadow=(0, 14, (0, 0, 0, 90)))
            d = ImageDraw.Draw(L); y = 400
            for i, (k, v) in enumerate(RESULT):
                if t < tThree - 0.15 + i * 0.35: break
                if i == 1 and t >= tUncle - 0.1:
                    p = ease((t - tUncle) / 0.6)
                    d.rectangle((100, y + 70, 100 + int(860 * p), y + 140), fill=YEL)
                d.text((110, y), k, font=font("black", 44), fill=ORA)
                for j, ln in enumerate(wrap(d, v, font("xbold", 48), 860)):
                    d.text((110, y + 70 + j * 64), ln, font=font("xbold", 48), fill=INK)
                y += 215
        a = back((t - tThree + 0.15) / 0.3)
        paste_scaled(img, layer_draw(res), 0.8 + 0.2 * a, W / 2, 700, alpha=min(1, a))
        if t >= tUncle + 1.0:
            draw_center(img, "(still owes everyone)", 1090, font("brush", 64), YEL)
    draw_captions(img, t, words, groups, y=1260, accent=YEL, stroke=INK, size=92)
    footer(img, "Example made up · summary written with AI", 1420)
    return img

if __name__ == "__main__":
    print(render("HB-S2_family-group-chat", total, frame, OUT+'/hb-s2.voice.wav', OUT+'/hb-s2.fx.wav', OUT), round(total, 2))
