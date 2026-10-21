#!/usr/bin/env python3
"""Tight cuts (Oct 21): 3-beat versions (hook -> payoff -> Do this) of the queued 25-40 s Reels, so every Reel is <= 15 s.
Owner direction (Oct 21): "minimal but valuable content, more details" -> the screen carries one idea; the caption keeps every
detail, source and step. Every on-screen line below is taken from (or trimmed from) the original Reel; no new facts.
Originals stay in media/reels; the cut is <id>-s15.mp4.

    python3 studio/editorial/tight.py [ids...] [--plan]
"""
import argparse, sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import teach_reels as T  # noqa: E402

# rid: (hook_override or None, payoff_from_index, payoff_overrides, do_overrides)
TIGHT = {
    "hb-reel-1021-camera-translate": ("About to paste that / *into ChatGPT?*", 2, dict(items=["Never paste:", "*Passwords*", "*Card numbers*", "*Client files*"]),
                                      dict(text="Swap names and numbers *first.*")),
    "lh-reel-1021-miss-once": (None, 2, dict(text="Missing *one day* didn't undo the habit."),
                               dict(text="Tomorrow: same time. *No catch-up.*")),
    "lh-reel-1022am-bundle": ("Skipping / *the gym?*", 2, dict(text="Gym-only audiobooks: *51% more* gym visits."),
                              dict(text="Save your show *for the chore.*")),
    "ff-reel-1022-refund-29k": ("Spend the refund, / or *grow it?*", 4, {}, dict(text="Refund day: *TFSA.* *Invest it.*")),
    "lf-reel-1022-ccb-at-birth": ("New baby? / *Tick one box.*", 2, dict(text="Up to *$8,157* / a year / *under age 6.*"),
                                  dict(text="Birth form: tick *Canada child benefits.*")),
    "lh-reel-1022-walk": (None, 2, dict(text="Walking raised creative ideas by about *60%.*"),
                          dict(text="Walk *10 minutes.* Then decide.")),
    "lf-reel-1023am-screens-bed": ("Bedtime / *battles?*", 2, dict(text="Screens off *an hour* before. / *Brush. Book. Bed.*"),
                                   dict(text="Tonight: tablet off *an hour* early.")),
    "hb-reel-1023am-photo-search": ("An error light / *you don't get?*", 2, dict(items=["Gemini Live:", "It *sees*", "It *talks back*"]),
                                    dict(text="Error light? *Show it.* Ask *why.*")),
    "ff-reel-1023-cpp-60-or-70": ("CPP at 60, / or *70?*", 3, dict(items=["2026 max:", "60: *$965*", "65: *$1,508*", "70: *$2,140*"]),
                                  dict(text="Check your *CPP estimate* tonight.")),
    "hb-reel-1023-duplicates": ("Read only / *the AI summary?*", 3, dict(text="Summaries *squeeze* facts. AI can *change* them.", drop=True),
                                dict(text="Open the *original* first.")),
    "lh-reel-1023-caffeine": ("Coffee / *at 4 pm?*", 2, dict(text="6 hours before bed: *an hour less sleep.*"),
                              dict(text="Bed at 10? *Last cup by 4.*")),
    "ff-reel-1024am-sick-pay-gap": ("Sick for months? / *EI pays this.*", 2, dict(items=["Earn $80,000?", "EI: *$729/week*", "Gap: *$809/week*"]),
                                    dict(text="Ask HR about *long-term disability.*")),
    "lh-reel-1024am-floss-after": (None, 2, dict(text="Flossing *after* brushing stuck better, *8 months* later."),
                                   dict(text="Tonight: brush, then floss *right after.*")),
    "ff-reel-1024-beneficiary": ("Your TFSA has / *a blank line.*", 3, dict(items=["On $100K, Ontario:", "Estate: *$750 tax*", "Named: *$0*"]),
                                 dict(text="Check *who's named* tonight.")),
    "hb-reel-1024-fridge-dinner": ("Same task, / *every single week?*", 2, dict(items=["*Hired*", "*Trained*", "*Reviewed*"]),
                                   dict(text="Write one task's *steps* down.")),
    "lf-reel-1024-grandma-resp": ("New dad? Feel like / *a spectator?*", 2, {}, dict(text="Tonight: bath time is *yours.*")),
    "lh-reel-1024-lyrics": (None, 2, dict(text="Songs *with words* lowered scores. Even *liked* ones."),
                            dict(text="Make one *no-lyrics* playlist for focus.")),
    "lf-reel-1025am-crying-peak": (None, 1, dict(text="Attention *can't spoil* / a young baby.", drop=True),
                                   dict(text="Next cry: *fed, changed, warm?*")),
    "lh-reel-1025am-planning-fallacy": (None, 2, dict(text="They guessed *34 days.* It took *56.*"),
                                        dict(text="2-hour guess? *Plan 3.*")),
    "hb-reel-1025am-talk-dont-type": ("Think you / *don't use AI?*", 2, {}, dict(text="Tap the *AI button* once today.")),
    "ff-reel-1025-tfsa-withdrawal-trap": ("TFSA withdrawal? / *Don't rush it back.*", 2,
                                          dict(text="The room returns *January 1.*", drop=True),
                                          dict(text="Check *CRA My Account* first.")),
    "lh-reel-1025-unpack": (None, 2, dict(text="*Listing steps* gave truer guesses."),
                            dict(text="List Monday's task, *step by step.*")),
}


def tight_spec(rid):
    s = T.spec_for(rid)
    sc = s["scenes"]
    hook_i = next(i for i, x in enumerate(sc) if x["k"] == "hook")
    do_i = next(i for i, x in enumerate(sc) if x["k"] == "do")
    hook_o, pay_i, pay_o, do_o = TIGHT[rid]
    hook = dict(sc[hook_i])
    pay = {k: v for k, v in sc[pay_i].items() if k not in ("kicker",)}
    pay.update(pay_o); pay["drop"] = True
    split = lambda t: T.re.sub(r"\*(.+?)\*", lambda m: " / ".join(f"*{p}*" for p in m.group(1).split(" / ")), t)  # noqa: E731
    pay_o, do_o = dict(pay_o), dict(do_o)
    for d in (pay_o, do_o):
        if "text" in d:
            d["text"] = split(d["text"])
    pay.update(pay_o)
    if hook_o:
        hook["text"] = split(hook_o)
    do = dict(sc[do_i], **do_o); do.pop("drop", None)
    for x in (hook,):
        x.pop("drop", None)
    return dict(s, id=rid + "-s15", fmt="tight", scenes=[hook, pay, do])


def check_len(spec, pr):
    want = T.make(spec).duration
    if abs(pr["dur"] - want) > 0.25:
        out = T.REPO / "media" / "reels"
        for x in (out / f"{spec['id']}.mp4", out / f"{spec['id']}-cover.jpg"):
            x.unlink(missing_ok=True)
        raise SystemExit(f"encoded {pr['dur']:.2f}s but planned {want:.2f}s (frames lost; disk?) -> removed")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--out", default="/tmp/tight-reels")
    a = ap.parse_args()
    for rid in a.ids or list(TIGHT):
        spec = tight_spec(rid)
        try:
            T.lint(spec)
            if a.plan:
                T.report(spec)
            else:
                check_len(spec, T.build(spec, a.out))
        except SystemExit as e:
            print(f"!! {rid}: {e}", flush=True)
