#!/usr/bin/env python3
"""Hourback Reels built Tue Oct 27 2026 by the Hourback maker (Social studio).

    python3 studio/editorial/oct27_hourback.py menu|chat                  # render mp4 + dedicated cover -> media/studio-oct27/hourback/
    python3 studio/editorial/oct27_hourback.py menu --frame 0 1 2 4 ...   # quick stills sheet for review

menu = hb-reel-1028am-menu-translate (Wed Oct 28, 8:45 am, NO trial). Performance desk order 4 (Oct 27): the Littlefold
       'burp' format ported to Hourback. Frame 0 = ONE felt question (<= 6 words) + ONE drawn object (a Japanese menu on a
       table); a drawn hand slides a phone over it at 0.2 s and the covered part of the menu turns into English, scanned
       live, by ~1.6 s, in ONE illustrated scene (not a screen recording). Real shipped feature: Google Translate app,
       Camera -> point at text, verified Oct 27 2026 on support.google.com/translate/answer/6142483 (Android + iPhone) and
       blog.google (NMT in instant camera translation, Jul 10 2019). The English shown is a correct translation of the drawn
       menu, not a claimed app output ("Drawn for this post").
       Cover = swipe-to-reveal look (style 11, quiet): the menu split down the middle, Japanese | English, with a slider.
chat = hb-reel-1030-group-chat (Fri Oct 30, 7 pm, no trial). A REAL run: studio/editorial/hb-oct27-run-group-chat.txt
       (fresh Claude session via claude -p, Oct 27 2026). Chat made up for this post. Body = sticky-note list (style 13 look):
       the chat bubbles are pulled into a taped note and Claude's reply is written on it line by line, quoted exactly
       (the last suggestion line cut, said on screen). Cover = follow the line (style 9, quiet): names -> dishes, one loose end.

Reuses the Hourback kit (oct25_hb.py -> takereel.py, oct24_hb.py) by import; nothing in them is edited.
"""
import sys
from pathlib import Path

REPO = Path("/home/claude/steadfold-autopost")
sys.path.insert(0, str(REPO / "studio/recovery-oct22/hourback/build"))
sys.path.insert(0, str(REPO / "studio/editorial"))
sys.dont_write_bytecode = True
import json  # noqa: E402
import oct25_hb as O  # noqa: E402
from oct25_hb import T, serif, hand, card, scene, F, INK, ACC, SUN, W, H, FPS, stamp, small, kicker, button  # noqa: E402
from takereel import JS, edkit  # noqa: E402
from oct24_hb import EXTRA_JS  # noqa: E402

O.OUT = REPO / "media/studio-oct27/hourback"
O.SCRATCH = Path("/tmp/claude-0/oct27-hourback/render")
MUSIC = REPO / "media/music/library/v4"
JP = "'Noto Sans CJK JP','Noto Sans CJK SC',sans-serif"
SKIN, SKIN_D = "#F4C9A8", "#E3A982"

# ---------------------------------------------------------------- shared JS: lens (menu), suck + write (chat)
MY_JS = r"""
function lens(t){
 document.querySelectorAll('[data-lens]').forEach(el=>{
  const a=+el.dataset.lens, still=+(el.dataset.still||0);
  const sw=+el.dataset.sw, sh=+el.dataset.sh, x0=+el.dataset.x0, y1=+el.dataset.y1, y2=+el.dataset.y2;
  const tin=still?1:E((t-a-0.15)/0.75);
  const tm=still?0:(t-a-3.3)/0.9; const k=C(tm), dn=k<.5?4*k*k*k:1-Math.pow(-2*k+2,3)/2;
  const px=x0+760*(1-tin) + (still?0:Math.sin((t-a)*2.1)*4), py=y1+(y2-y1)*dn + (still?0:Math.cos((t-a)*1.7)*4);
  const scan=still?1:C((t-a-0.95)/0.6);
  el.querySelectorAll('.ph').forEach(p=>{p.style.transform=`translate(${px}px,${py}px)`});
  const en=el.querySelector('.en'), W=+el.dataset.mw, H=+el.dataset.mh;
  const L=Math.max(0,px), R=Math.min(W,px+sw), Tp=Math.max(0,py), B=Math.min(H,py+sh*scan);
  if(R<=L||B<=Tp){en.style.clipPath='inset(100% 100% 100% 100%)'} else en.style.clipPath=`inset(${Tp}px ${W-R}px ${H-B}px ${L}px)`;
  const sc=el.querySelector('.scan'); sc.style.opacity=(scan>0&&scan<1)?1:0; sc.style.transform=`translate(${px}px,${py+sh*scan-4}px)`;
 });
}
function suck(t){
 document.querySelectorAll('[data-suck]').forEach(el=>{
  const a=+el.dataset.suck, dx=+el.dataset.dx, dy=+el.dataset.dy; const p=C((t-a)/0.45), q=p*p;
  el.style.transform=`translate(${dx*q}px,${dy*q}px) scale(${1-0.85*q}) rotate(${q*20}deg)`; el.style.opacity=p>=1?0:1;
 });
 document.querySelectorAll('[data-write]').forEach(el=>{
  const a=+el.dataset.write, d=+(el.dataset.wd||0.3); const p=C((t-a)/d);
  el.style.clipPath=`inset(-20px calc(${(1-p)*100}% + ${(1-p)*90}px) -20px -90px)`;
 });
}
const _seek3=seek; seek=function(t){_seek3(t);lens(t);suck(t)};
"""


def page4(scenes, shakes):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{edkit.css('hourback', W, H)}</style></head>
<body><div id="cam" style="position:absolute;inset:0;overflow:hidden">{''.join(scenes)}</div>
<script>window.SHAKES={json.dumps(shakes)};{JS}{EXTRA_JS}{MY_JS}</script></body></html>"""


# ================================================================== A. menu translate (Wed Oct 28, 8:45 am)
ITEMS = [("焼き鳥", "Chicken skewers", "¥680"), ("餃子", "Dumplings", "¥520"),
         ("親子丼", "Chicken and egg<br>rice bowl", "¥950"), ("抹茶アイス", "Green tea<br>ice cream", "¥450")]
MW, MH = 600, 880
ROWS = [210, 370, 530, 690]


def menu_layer(lang):
    """One full menu face. lang 'jp' = the printed card; 'en' = the same card as the camera shows it in English."""
    o = ""
    head = ('<div style="font:900 70px %s;letter-spacing:.2em">メニュー</div>' % JP) if lang == "jp" else \
        '<div style="font:800 58px Inter;letter-spacing:.06em;padding-top:6px">MENU</div>'
    o += f'<div style="position:absolute;left:0;right:0;top:56px;text-align:center;color:{INK}">{head}</div>'
    o += f'<div style="position:absolute;left:150px;right:150px;top:160px;height:5px;background:{ACC};border-radius:3px"></div>'
    for (jp, en, pr), y in zip(ITEMS, ROWS):
        if lang == "jp":
            name = f'<div style="font:700 66px/1.1 {JP};color:{INK};letter-spacing:.04em">{jp}</div>'
        else:
            name = (f'<div style="display:inline-block;background:#FFF1C4;border-radius:12px;padding:4px 12px;margin-left:-12px;'
                    f'font:800 42px/1.12 Inter;color:{INK}">{en}</div>')
        o += (f'<div style="position:absolute;left:62px;right:62px;top:{y}px;height:130px;display:flex;align-items:center;'
              f'justify-content:space-between;border-bottom:3px dashed #D8CDBE">{name}'
              f'<div style="font:700 40px Inter;color:{INK}">{pr}</div></div>')
    bg = "#FFFBF2" if lang == "jp" else "#FFFBF2"
    return f'<div style="position:absolute;inset:0;background:{bg};border-radius:22px">{o}</div>'


def hand_svg():
    """ONE drawn hand (single outline): palm under the phone's bottom-right corner, thumb up the right edge. Phone-screen coords."""
    return (f'<svg width="10" height="10" style="position:absolute;left:0;top:0;overflow:visible">'
            f'<path d="M330 735 Q296 760 300 830 L318 1080 L604 1080 L592 850 Q588 760 572 650 Q562 480 538 458 Q508 452 504 500 '
            f'L512 690 Q470 722 330 735 Z" fill="{SKIN}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>'
            f'<path d="M514 486 Q526 470 540 478" stroke="{SKIN_D}" stroke-width="5" fill="none" stroke-linecap="round"/>'
            f'<path d="M300 880 Q330 884 350 868 M304 950 Q334 954 354 938 M310 1015 Q336 1018 352 1006" stroke="{SKIN_D}" stroke-width="5" fill="none" stroke-linecap="round"/>'
            f'<path d="M360 760 Q380 790 410 768 M420 772 Q440 800 470 776" stroke="{SKIN_D}" stroke-width="5" fill="none" stroke-linecap="round"/>'
            f'<rect x="312" y="1040" width="300" height="70" fill="#8F86E0" stroke="{INK}" stroke-width="7"/></svg>')


def menu_object(a, still=False, scale=0.92, phone=True, y2=170):
    """The single drawn object: a menu card on the table; the phone (with hand) slides over it and translates what it covers."""
    sw, sh, x0, y1 = 520, 700, 40, 30
    jp = f'<div style="position:absolute;inset:0">{menu_layer("jp")}</div>'
    en = f'<div class="en" style="position:absolute;inset:0;clip-path:inset(100% 100% 100% 100%)">{menu_layer("en")}</div>'
    card_ = (f'<div style="position:absolute;left:0;top:0;width:{MW}px;height:{MH}px;border:6px solid {INK};border-radius:28px;'
             f'box-shadow:16px 16px 0 rgba(42,29,71,.22);overflow:hidden;background:#FFFBF2">{jp}{en}</div>')
    ph = ""
    if phone:
        bez = 22
        frame = (f'<div style="position:absolute;left:{-bez}px;top:{-bez}px;width:{sw + 2 * bez}px;height:{sh + 2 * bez}px;'
                 f'border:{bez}px solid {INK};border-radius:64px;box-sizing:border-box;box-shadow:12px 14px 0 rgba(42,29,71,.28)"></div>'
                 f'<div style="position:absolute;left:{sw / 2 - 60}px;top:-8px;width:120px;height:28px;border-radius:99px;background:{INK}"></div>'
                 f'<div style="position:absolute;left:0;top:0;width:{sw}px;height:{sh}px;border-radius:44px;background:rgba(201,202,245,.10)"></div>')
        ph = (f'<div class="ph" style="position:absolute;left:0;top:0;width:{sw}px;height:{sh}px">'
              f'{frame}{hand_svg()}</div>')
        scan = (f'<div class="scan" style="position:absolute;left:0;top:0;width:{sw}px;height:8px;border-radius:4px;background:{SUN};'
                f'box-shadow:0 0 22px 6px rgba(255,201,77,.8);opacity:0"></div>')
        ph += scan
    attrs = (f'data-lens="{a}" data-still="{1 if still else 0}" data-sw="{sw}" data-sh="{sh}" data-x0="{x0}" data-y1="{y1}" '
             f'data-y2="{y2}" data-mw="{MW}" data-mh="{MH}"') if phone else ""
    return (f'<div {attrs} style="position:relative;width:{MW}px;height:{MH}px;transform:scale({scale});transform-origin:0 0">'
            f'{card_}{ph}</div>')


def table_bg():
    """Warm table top under the menu: soft wood planks in the page's cream/peach."""
    planks = "".join(f'<div style="position:absolute;left:0;right:0;top:{i * 120}px;height:3px;background:rgba(42,29,71,.07)"></div>' for i in range(17))
    return f'<div style="position:absolute;left:0;right:0;top:590px;bottom:0;background:#FFE3CC">{planks}</div>'


def menu_hook(a, b, first, still=False):
    hf = F["indi"]
    fx = "none" if first or still else "iris"
    inner = (table_bg() +
             T(serif("Menu in another / *language?*", 132, hf), a, b, "none", extra="left:90px;top:300px") +
             T(menu_object(a, still=True, phone=False), a, b, "none", extra="left:280px;top:610px", base="rotate(-2deg)",
               float=0 if still else 3) +
             T(stamp(90, 1240, 130), a, b))
    return scene(hf["bg"], a, b, fx, inner, d=0.45, drift=0 if still else 0.004)


def menu_reel():
    dur = 13.0
    hf = F["indi"]
    # 0-6.2: ONE illustrated scene. Hook line on frame 0; the phone slides in at 0.15 s, scans 0.95-1.55 s, English by ~1.6 s;
    # 1.9 s the headline becomes the payoff; 3.3-4.2 s the phone glides down to the dessert line, ring drawn on it.
    ring = (f'<svg width="500" height="170" viewBox="0 0 560 190" style="overflow:visible"><path data-draw=1 data-t0="4.3" data-t1="4.9" '
            f'd="M300 14 C520 10 560 80 530 130 C490 186 60 186 22 120 C-4 70 70 18 330 16" fill="none" stroke="{ACC}" stroke-width="9" stroke-linecap="round"/></svg>')
    s1 = (table_bg() +
          T(serif("Menu in another / *language?*", 132, hf), 0, 1.9, "none", extra="left:90px;top:300px", hard=1) +
          T(serif("Point your camera. / *See it in English.*", 96, hf), 1.9, 6.2, "slam", 0.22, "left:90px;top:320px") +
          T(menu_object(0), 0, 6.2, "none", extra="left:280px;top:610px", base="rotate(-2deg)") +
          T(ring, 0, 6.2, "none", extra="left:305px;top:1215px", base="rotate(-2deg)") +
          T(hand("Japanese<br>→ English,<br>live", 62, ACC, -6, width=230), 2.3, 6.2, "pop", 0.25, "left:40px;top:700px") +
          T(small("Google Translate app · Camera", 38, INK, w=900, weight=800), 2.0, 6.2, "up", 0.25, "left:90px;top:497px") +
          T(small("Drawn for this post. Real Google feature.", 30, INK, w=900, weight=600), 2.0, 6.2, "none", extra="left:90px;top:545px") +
          T(stamp(90, 1240, 130), 0, 1.9, "none", hard=1))
    s = [scene(hf["bg"], 0, 6.2, "none", s1, d=0.3, drift=0.004)]
    # 6.2-9.8 Do this: the exact taps, with the translated menu + phone kept in frame (the same drawn object)
    yf = F["yel"]
    arrow = f'<div style="font:800 46px Inter;color:{INK};width:900px;text-align:center">↓</div>'
    chain = ""
    for i, lab in enumerate(["Open Google Translate", "Tap Camera", "Point at the words"]):
        t0 = 6.45 + i * 0.45
        chain += T(f'<div style="width:900px;text-align:center">{button(lab, 54, SUN if i == 2 else "#FFFDF8")}</div>', t0, 9.8, "pop", 0.25,
                   f"left:90px;top:{440 + i * 150}px")
        if i:
            chain += T(arrow, t0 - 0.12, 9.8, "up", 0.2, f"left:90px;top:{440 + i * 150 - 58}px")
    do = ('<div style="position:absolute;left:0;right:0;top:880px;bottom:0;background:#FFE3CC"></div>' +
          T('<div class="hand" style="font-size:110px;color:%s">Do this:</div>' % ACC, 6.2, 9.8, "slam", 0.2, "left:90px;top:300px;width:900px") +
          chain +
          T(menu_object(0, still=True, scale=0.56), 6.2, 9.8, "up", 0.35, "left:560px;top:900px", base="rotate(-3deg)") +
          T(card(small("Going abroad? Download the language in the app first, so it works offline.", 36, INK, 380, weight=700),
                 w=430, pad=24, bg="#FFF0C2"), 7.9, 9.8, "drop", 0.3, "left:70px;top:960px", base="rotate(-1.5deg)") +
          T(small("Free on Android and iPhone.", 34, INK, w=430, weight=700), 7.4, 9.8, "up", 0.25, "left:70px;top:1260px"))
    s.append(scene(yf["bg"], 6.2, 9.8, "wipe", do, d=0.28))
    # 9.8-12.4 follow (2.6 s on screen), periwinkle surface + the menu/phone object
    nf = F["indi"]
    end = ('<div style="position:absolute;left:0;right:0;top:880px;bottom:0;background:#FFE3CC"></div>' +
           T(serif("Follow to learn / one real AI trick / *a day.*", 118, nf), 9.8, 12.4, "up", 0.25, "left:90px;top:300px") +
           T(hand("one you can try tonight", 70, ACC, -3), 10.3, 12.4, "pop", 0.25, "left:90px;top:660px") +
           T(menu_object(0, still=True, scale=0.56), 9.8, 12.4, "up", 0.35, "left:330px;top:830px", base="rotate(2deg)") +
           T(stamp(90, 1180, 130), 9.8, 12.4))
    s.append(scene(nf["bg"], 9.8, 12.4, "wipeD", end, d=0.26))
    s.append(menu_hook(12.4, 99, False))
    return dur, page4(s, [1.9, 6.2, 9.8]), page4([menu_cover()], []), MUSIC / "hb-x-future-easy.mp3"


def menu_cover():
    """Dedicated cover, swipe-to-reveal look (style 11): one menu with a slider; above it Japanese, below it the same lines in English."""
    pf = F["plum"]
    cut = 515
    top = f'<div style="position:absolute;inset:0;clip-path:inset(0 0 {MH - cut}px 0)">{menu_layer("jp")}</div>'
    bot = f'<div style="position:absolute;inset:0;clip-path:inset({cut}px 0 0 0)">{menu_layer("en")}</div>'
    slider = (f'<div style="position:absolute;left:-30px;top:{cut - 4}px;width:{MW + 60}px;height:8px;background:{INK};border-radius:4px"></div>'
              f'<div style="position:absolute;left:{MW - 70}px;top:{cut - 56}px;width:112px;height:112px;border-radius:50%;background:{SUN};'
              f'border:6px solid {INK};display:flex;align-items:center;justify-content:center;font:800 58px Inter;color:{INK}">⇅</div>')
    menu = (f'<div style="position:relative;width:{MW}px;height:{MH}px;transform:scale(.78);transform-origin:0 0">'
            f'<div style="position:absolute;inset:0;border:6px solid {INK};border-radius:28px;overflow:hidden;background:#FFFBF2;'
            f'box-shadow:16px 16px 0 rgba(42,29,71,.22)">{top}{bot}</div>{slider}</div>')
    inner = (T(serif("Can't read / *the menu?*", 150, pf), 0, 99, "none", extra="left:90px;top:300px") +
             T(menu, 0, 99, "none", extra="left:290px;top:650px", base="rotate(-1.5deg)") +
             T(hand("point your camera, see English", 62, ACC, -3, width=900), 0, 99, "none", extra="left:90px;top:1340px") +
             T(stamp(90, 1150, 140), 0, 99))
    return scene(pf["bg"], 0, 99, "none", inner, d=0.1, drift=0)


# ================================================================== B. group chat (Fri Oct 30, 7 pm) - real run
CHAT = [("Mom", "I'll do the roast chicken"), ("Sam", "I can bring a salad!"), ("Jo", "Drinks are on me"),
        ("Mom", "Has anyone got dessert?"), ("Sam", "Can someone bring chairs? We only have 6"),
        ("Jo", "Also who's picking up Grandpa?"), ("Mom", "Priya, can you still come at 4 to help set up?")]
# Claude's reply, verbatim (studio/editorial/hb-oct27-run-group-chat.txt); markdown ** and "- " shown as headings and bullets.
REPLY = [("h", "Covered"), ("i", "Mom: roast chicken"), ("i", "Sam: salad"), ("i", "Jo: drinks"),
         ("h", "Still missing"), ("m", "Dessert"), ("m", "Extra chairs (they only have 6)"), ("m", "Someone to pick up Grandpa"),
         ("h", "You need to reply to"), ("r", "Mom: whether you can still come at 4 to help set up")]
NAMECOL = {"Mom": "#5E54C9", "Sam": ACC, "Jo": "#2E8A6E"}


def chat_bubble(name, text, size=34, w=520):
    return (f'<div style="max-width:{w}px;background:#FFFFFF;border:4px solid {INK};border-radius:28px 28px 28px 8px;'
            f'box-shadow:6px 6px 0 rgba(42,29,71,.25);padding:12px 20px;font:500 {size}px/1.25 Inter;color:{INK}">'
            f'<b style="color:{NAMECOL[name]}">{name}</b><br>{text}</div>')


def chat_heap(a, b, still=False, suck_at=None):
    """The frame-0 object: a messy heap of the 7 chat bubbles (all text from the made-up prompt)."""
    pos = [(90, 590, -3), (570, 610, 3), (120, 740, 2), (550, 750, -3), (90, 895, -2), (560, 965, 2), (190, 1125, -1)]
    o = ""
    for i, ((n, tx), (x, y, r)) in enumerate(zip(CHAT, pos)):
        pop_t = a + (0.25 if (i == 6 and not still) else 0)
        b_html = chat_bubble(n, tx, w=430 if i != 6 else 640)
        suck = f'data-suck="{suck_at + i * 0.03}" data-dx="{540 - x - 230}" data-dy="{900 - y}"' if suck_at else ""
        o += T(f'<div {suck}>{b_html}</div>', pop_t, b, "none" if (still or i != 6) else "pop", 0.25,
               f"left:{x}px;top:{y}px", base=f"rotate({r}deg)", float=0 if still else 3 + i % 3, **({"hard": 1} if suck_at else {}))
    return o


def chat_hook(a, b, first, still=False):
    hf = F["orng"]
    fx = "none" if first or still else "iris"
    inner = (T(serif("Group chat chaos? / *Get the list.*", 104, hf), a, b, "none", extra="left:90px;top:300px") +
             chat_heap(a, b, still) +
             T(small("Chat made up for this post.", 32, INK, w=600, align="left", weight=700), a, b, "none", extra="left:90px;top:1305px") +
             T(stamp(870, 1280, 120), a, b))
    return scene(hf["bg"], a, b, fx, inner, d=0.45, drift=0 if still else 0.005)


def note_card(a, write=True, h=780, you=True):
    LH = 66
    lines = "".join(f'<div style="position:absolute;left:0;right:0;top:{52 + i * LH}px;height:2px;background:#BFD3EE"></div>' for i in range(11))
    rows, y = "", 52 - LH + 6
    for i, (k, tx) in enumerate(REPLY):
        t0 = a + 0.25 + i * 0.22
        y += LH
        if k == "h":
            el = f'<div style="font:400 56px/{LH}px \'Caveat Brush\';color:{ACC}">{tx}</div>'
        else:
            mark = {"i": "✓", "m": "○", "r": "→"}[k]
            col = {"i": "#2E8A6E", "m": ACC, "r": "#5E54C9"}[k]
            el = (f'<div style="font:700 54px/{LH}px Caveat;color:{INK};width:760px;padding-left:50px;text-indent:-50px"><span style="color:{col};font-family:Inter;'
                  f'font-weight:800;font-size:34px;display:inline-block;width:46px">{mark}</span>{tx}</div>')
        wr = f'data-write="{t0}" data-wd="0.3"' if write else ""
        rows += f'<div {wr} style="position:absolute;left:{70 if k == "h" else 92}px;top:{y - LH + 4}px">{el}</div>'
        if k == "r":
            y += LH
    if you:
        yy = 52 + 10 * LH - 8
        rows += (f'<div {f"data-write=\"{a + 0.25 + 10 * 0.22}\" data-wd=\"0.3\"" if write else ""} style="position:absolute;left:520px;top:{yy}px;'
                 f'font:400 46px \'Caveat Brush\';color:{ACC};transform:rotate(-4deg)">← that\'s you, Priya</div>')
    tape = (f'<div style="position:absolute;left:330px;top:-26px;width:240px;height:60px;background:rgba(255,201,77,.75);'
            f'transform:rotate(-3deg);border:2px solid rgba(42,29,71,.15)"></div>')
    return (f'<div style="position:relative;width:900px;height:{h}px;background:#FFFDF6;border:5px solid {INK};border-radius:16px;'
            f'box-shadow:12px 12px 0 rgba(42,29,71,.3)">{lines}'
            f'<div style="position:absolute;top:0;bottom:0;left:56px;width:3px;background:#F08A8A"></div>{rows}{tape}</div>')


def chat_reel():
    dur = 14.2
    hf, pf = F["orng"], F["plum"]
    # 0-2.2 hook; 2.2 the bubbles are pulled into the note; 2.3-8.0 Claude's reply written on the note, line by line
    s1 = (T(serif("Group chat chaos? / *Get the list.*", 104, hf), 0, 2.27, "none", extra="left:90px;top:300px", hard=1) +
          chat_heap(0, 2.2, suck_at=1.65) +
          T(small("Chat made up for this post.", 32, INK, w=600, align="left", weight=700), 0, 1.7, "none", extra="left:90px;top:1305px", hard=1) +
          T(serif("Paste the chat. / *Get the list.*", 100, pf), 2.25, 8.0, "slam", 0.22, "left:90px;top:300px") +
          T(kicker("Claude's real reply, word for word", 35), 2.3, 8.0, "none", extra="left:90px;top:497px") +
          T(small("last line cut · chat made up for this post", 28, "#7E7896", weight=700), 2.3, 8.0, "none", extra="left:90px;top:542px") +
          T(note_card(2.3), 2.3, 8.0, "drop", 0.3, "left:90px;top:600px", base="rotate(-0.8deg)") +
          T(stamp(870, 1280, 120), 0, 2.27, "none", hard=1))
    s = [scene(hf["bg"], 0, 8.0, "none", s1, d=0.3, drift=0.003)]
    # 8.0-11.3 Do this + privacy
    yf = F["yel"]
    do = (T('<div class="hand" style="font-size:120px;color:%s">Do this:</div>' % ACC, 8.0, 11.3, "slam", 0.2, "left:90px;top:300px;width:900px") +
          T(card(serif("Paste the chat. / Ask: *who's / bringing what?*", 104, F["plum"], width=820), w=900, pad=40), 8.12, 11.3, "pop", 0.3,
            "left:90px;top:450px", float=3) +
          T(card(small("Copy just the messages. Leave out phone numbers and addresses.", 42, INK, 820, weight=700), w=900, pad=28, bg="#FFF0C2"),
            9.0, 11.3, "drop", 0.3, "left:90px;top:900px", base="rotate(1.2deg)") +
          T(small("Works in ChatGPT, Claude or Gemini.", 34, INK, w=430, align="left", weight=700), 9.4, 11.3, "up", 0.25, "left:90px;top:1160px"))
    do = (T(f'<div style="transform:scale(.46);transform-origin:0 0">{note_card(0, write=False)}</div>', 8.0, 11.3, "up", 0.35,
            "left:560px;top:1050px", base="rotate(4deg)") + do)
    s.append(scene(yf["bg"], 8.0, 11.3, "wipe", do, d=0.28))
    # 11.3-13.6 follow (2.3 s)
    nf = F["indi"]
    end = (T(serif("Follow to learn / one real AI trick / *a day.*", 118, nf), 11.3, 13.6, "up", 0.25, "left:90px;top:300px") +
           T(hand("real AI replies, made-up chats", 66, ACC, -3), 11.7, 13.6, "pop", 0.25, "left:90px;top:660px") +
           T(f'<div style="position:relative;width:1080px;height:700px;transform:scale(.8);transform-origin:50% 0">{lines_obj()}</div>',
             11.3, 13.6, "up", 0.35, "left:0;top:780px") +
           T(stamp(870, 1290, 110), 11.3, 13.6))
    s.append(scene(nf["bg"], 11.3, 13.6, "wipeD", end, d=0.26))
    s.append(chat_hook(13.6, 99, False))
    return dur, page4(s, [2.2, 8.0, 11.3]), page4([chat_cover()], []), MUSIC / "hb-x-ta-da-funk.mp3"


def lines_obj(top=0):
    """Follow-the-line object: names -> dishes with coloured lines; '?' -> dessert left loose. Positioned in a 1080-wide box."""
    names = [("Mom", 0), ("Sam", 160), ("Jo", 320), ("?", 480)]
    things = [("salad", 0), ("drinks", 160), ("roast chicken", 320), ("dessert", 480)]
    pairs = [(0, 2, "#5E54C9"), (1, 0, ACC), (2, 1, "#2E8A6E")]
    paths = ""
    for ni, ti, col in pairs:
        y0, y1 = names[ni][1] + 40 + top, things[ti][1] + 40 + top
        paths += (f'<path d="M330 {y0} C520 {y0 - 120} 460 {y1 + 120} 640 {y1}" fill="none" stroke="{col}" stroke-width="12" stroke-linecap="round"/>')
    paths += f'<path d="M330 {520 + top} C420 {480 + top} 470 {560 + top} 520 {510 + top}" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round" stroke-dasharray="4 18"/>'
    svg = f'<svg width="1080" height="{700 + top}" viewBox="0 0 1080 {700 + top}" style="position:absolute;left:0;top:0;overflow:visible">{paths}</svg>'

    def pill(t, x, y, bg, w):
        return (f'<div style="position:absolute;left:{x}px;top:{y + top}px;width:{w}px;text-align:center;background:{bg};border:5px solid {INK};'
                f'border-radius:99px;box-shadow:6px 6px 0 {INK};padding:10px 0 8px;font:700 44px Poppins;color:{INK}">{t}</div>')
    pl = "".join(pill(n, 90, y, "#FFFDF8" if n != "?" else SUN, 240) for n, y in names)
    pr = "".join(pill(t, 640, y, "#FFFDF8" if t != "dessert" else SUN, 350) for t, y in things)
    return svg + pl + pr


def chat_cover():
    """Dedicated cover, follow-the-line (style 9): names on the left, dishes on the right, coloured lines; dessert has no line."""
    yf = F["indi"]
    inner = (T(serif("Who's bringing / *what, again?*", 140, yf), 0, 99, "none", extra="left:90px;top:300px") +
             lines_obj(700) +
             T(hand("let AI untangle the chat", 66, ACC, -3), 0, 99, "none", extra="left:90px;top:580px") +
             T(stamp(860, 1310, 110), 0, 99))
    return scene(yf["bg"], 0, 99, "none", inner, d=0.1, drift=0)


REELS = {"menu": ("hb-reel-1028am-menu-translate", menu_reel), "chat": ("hb-reel-1030-group-chat", chat_reel)}

if __name__ == "__main__":
    key = sys.argv[1]
    name, fn = REELS[key]
    dur, html, cov, track = fn()
    if "--frame" in sys.argv:
        from playwright.sync_api import sync_playwright
        from PIL import Image
        ts = [float(x) for x in sys.argv[sys.argv.index("--frame") + 1:]]
        p = O.SCRATCH / "prev"; p.mkdir(parents=True, exist_ok=True)
        (p / f"{key}.html").write_text(html); (p / f"{key}-c.html").write_text(cov)
        with sync_playwright() as pw:
            br = pw.chromium.launch(); pg = br.new_page(viewport={"width": W, "height": H})
            ims = []
            pg.goto((p / f"{key}-c.html").as_uri()); pg.wait_for_timeout(800); pg.evaluate("seek(50)")
            pg.screenshot(path=str(p / f"{key}-cover.png")); ims.append(Image.open(p / f"{key}-cover.png").convert("RGB").resize((360, 640)))
            pg.goto((p / f"{key}.html").as_uri()); pg.wait_for_timeout(800)
            for t in ts:
                f = p / f"{key}-{t}.png"; pg.evaluate(f"seek({t})"); pg.screenshot(path=str(f))
                ims.append(Image.open(f).convert("RGB").resize((360, 640)))
            br.close()
        sh = Image.new("RGB", (370 * len(ims), 640), "white")
        for i, im in enumerate(ims): sh.paste(im, (i * 370, 0))
        sh.save(p / f"{key}-sheet.jpg", quality=85); print(p / f"{key}-sheet.jpg")
    else:
        print(O.render(name, html, dur, track, cov))
