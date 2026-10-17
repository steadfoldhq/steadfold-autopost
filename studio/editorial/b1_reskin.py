#!/usr/bin/env python3
"""Re-skin the two Hourback pilot Reels (Oct 20) in the approved editorial look without touching their motion.

Loads studio/b1-hourback-pilots/build_reels.py (its scene timings, words and transitions stay as they are), swaps the
theme CSS for the editorial one (DM Serif Display in ink, peach/butter pills, soft periwinkle/peach fields, white cards),
adds the halftone object + handwritten save-line to the hook scene and the brand stamp to every scene, renders with the
same engine, and uses the frame at 0.75 s (the hook) as the cover.

    python3 studio/editorial/b1_reskin.py hb-reel-1020am-driveway-text hb-reel-1020-three-tabs
"""
import shutil
import subprocess
import sys
import types
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
import edkit as K  # noqa: E402

SRC = REPO / "studio" / "b1-hourback-pilots" / "build_reels.py"
F = K.FIELDS["hourback"]
INK, ACC = F["indi"]["ink"], K.ACCENT["hourback"]

THEME = K.FONTS + f"""
:root{{--bg:{F['indi']['bg']};--hl:{F['indi']['p1']};--hl-dark:{F['indi']['p1']};--prog-bg:transparent;--prog-fg:transparent;--strike:{ACC}}}
.cam{{transform:none!important}}
.pat{{background:url('{K.uri(K.GRAIN)}') 0 0/420px 420px;mix-blend-mode:multiply;opacity:.55}}
.H{{{K.SERIF['hourback']};color:{INK};line-height:1.1!important;padding-top:.06em}}  /* this engine's entrances clip to the line box */
.B b{{color:{ACC}!important}}
.dark .H{{color:{INK}}}
.B{{font-family:'DM Serif Display';font-size:58px;line-height:1.15;letter-spacing:-.02em;color:{INK}}}.dark .B{{color:{INK}}}
.fine{{font:500 36px/1.3 Fraunces;color:{INK};opacity:.75}}.dark .fine{{color:{INK}}}
.kick{{display:inline-block;font-family:'Caveat Brush';font-size:56px;color:{ACC};background:none;padding:0}}
.yl{{background:{F['indi']['p1']};border-radius:.42em;padding:0 .12em .02em;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.dark .yl{{color:{INK};background:{F['indi']['p2']};border-radius:.42em}}
.pc{{background:#fff;border-radius:44px;border-bottom-left-radius:14px;padding:46px 52px;color:{INK};font-family:'DM Serif Display';
 font-size:56px;line-height:1.2;box-shadow:0 24px 50px rgba(40,30,80,.16)}}
.lab{{display:inline-block;font-family:'Caveat Brush';font-size:56px;line-height:1;color:{ACC};background:none;padding:0;margin-bottom:18px}}
.res{{background:#fff;border-radius:36px;padding:26px 44px;box-shadow:0 16px 36px rgba(40,30,80,.14)}}
.r{{display:flex;gap:20px;font:500 42px/1.25 Fraunces;color:{INK};padding:14px 0;border-bottom:3px dashed #E4DDF5}}
.r:last-child{{border:0}}.r b{{flex:none;width:170px;font-family:'DM Serif Display';font-weight:400;color:{INK}}}
.notif{{background:#fff;border-radius:38px;padding:30px 36px;box-shadow:0 18px 40px rgba(40,30,80,.16);font:500 44px/1.34 Fraunces;color:{INK}}}
.notif .hd{{display:flex;justify-content:space-between;font:700 30px/1 Fraunces;color:#6A6080;margin-bottom:14px}}
.mail{{background:#fff;border-radius:36px;padding:40px 44px;box-shadow:0 16px 36px rgba(40,30,80,.14);font:500 46px/1.4 Fraunces;color:{INK}}}
.tab{{display:inline-block;font:600 40px/1 Fraunces;background:#fff;color:{INK};border-radius:18px 18px 0 0;padding:22px 28px;margin-right:10px;box-shadow:0 -4px 14px rgba(40,30,80,.1)}}
#tag{{display:none}}
"""
EXTRA = {  # hook-scene object + save-line, per Reel
    "driveway": dict(obj=K.obj("phone", 800, 1420, 220, 12), save="save this for the next awkward text", sy=1480),
    "blender": dict(obj=K.obj("point", 560, 1150, 420, -40, True), save="save this for your next 11 pm cart", sy=1470),
}
SOFT = {"#FFF8EF": F["indi"]["bg"], "#5E54C9": F["yel"]["bg"], "#EDE8FA": F["plum"]["bg"]}


def load():
    code = SRC.read_text()
    code = code.replace('CHAT = [l.split(": ", 1) for l in open("/home/claude/hb-pilots/runs/chat-costume.txt").read().strip().split("\\n")]',
                        "CHAT = []  # (editorial re-skin: the costume Reel isn't rebuilt here)")
    code = code.replace('OUT = Path("/home/claude/hb-pilots/out/reels"); OUT.mkdir(parents=True, exist_ok=True)',
                        'OUT = Path("/tmp/hb-pilots-ed"); OUT.mkdir(parents=True, exist_ok=True)')
    code = code.split('\nif __name__ == "__main__":')[0]
    mod = types.ModuleType("b1")
    mod.__file__ = str(SRC)
    exec(compile(code, str(SRC), "exec"), mod.__dict__)
    return mod


def reskin(mod, fn_name, key):
    import vlab
    orig = getattr(mod, fn_name)

    def wrapped():
        v = orig()
        v.theme_css = THEME
        ex = EXTRA[key]
        for i, sc in enumerate(v.scenes):
            sc["bg"] = SOFT.get(sc["bg"], sc["bg"])
            sc["cls"] = sc["cls"].replace("dark", "")
            stamp = K.stamp("hourback", 810, 1560, 160, -12)
            add = stamp
            if i == 0:
                add += ex["obj"] + (f'<div style="position:absolute;left:84px;width:700px;top:{ex["sy"]}px;font-family:\'Caveat Brush\';'
                                    f'font-size:68px;line-height:1.05;color:{ACC};transform:rotate(-3deg)">{ex["save"]}</div>')
            sc["inner"] = sc["inner"] + add
        return v
    return wrapped


def main(ids):
    mod = load()
    RL = mod.RL
    fns = {"hb-reel-1020am-driveway-text": ("kin_driveway", "driveway"), "hb-reel-1020-three-tabs": ("kin_blender", "blender")}
    for rid in ids:
        fn, key = fns[rid]
        RL.R[rid]["kinetic"] = reskin(mod, fn, key)
        RL.build(rid)
        mp4 = mod.L.OUT / f"{rid}.mp4"
        dst = REPO / "media" / "reels"
        shutil.copy(mp4, dst / f"{rid}.mp4")
        # cover = the hook frame (editorial composition), 1080x1920
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "0.75", "-i", str(mp4), "-frames:v", "1", "-q:v", "2",
                        str(dst / f"{rid}-cover.jpg")], check=True)
        print("done", rid, flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
