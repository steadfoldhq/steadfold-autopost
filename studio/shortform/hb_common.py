from common import *
IND=hexc("5E54C9"); YEL=hexc("FFC94D"); ORA=hexc("FF8A3D"); CRM=hexc("FFF8EF"); CRM2=hexc("FFEEDC"); INK=hexc("2A2238"); WHITE=hexc("FFFFFF"); GREY=(120, 112, 140, 255)

def prompt_card(L, box, lead, chips, t=None, t0=0):
    rrect(L, box, 30, CRM, shadow=(0, 14, (0, 0, 0, 90)))
    d = ImageDraw.Draw(L); x0, y0, x1, y1 = box
    d.text((x0 + 36, y0 + 28), "PROMPT", font=font("black", 30), fill=IND)
    d.text((x0 + 36, y0 + 76), lead, font=font("xbold", 44), fill=INK)
    y = y0 + 150
    for i, c in enumerate(chips):
        if t is not None and t < t0 + i * 0.45: break
        f = font("xbold", 42); tw = text_size(d, c, f)[0]
        rrect(L, (x0 + 30, y, x0 + 30 + tw + 50, y + 74), 18, YEL)
        d.text((x0 + 55, y + 12), c, font=f, fill=INK)
        y += 90

def footer(img, s, y=1520):
    draw_center(img, s, y, font("semi", 30), CRM, maxw=900)
