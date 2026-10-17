"""Aggressive pivot Reel scripts (Oct 17, 1:15 am). One idea, a 3-5 word hook, ONE hero number on the drop.
Figures come from ff_math.FIG (10% a year headline, compounded monthly, never above 10%).
Techniques: studio/pivot/TRANSITIONS.md (T1 leak, T2 burn, T3 flicker, T5 word captions, T7 punch-in, T8 slam-up card,
T9 circle, T10 pinned caption, T11 land, T12 glide, T13 grow, T15 loop, T16 swipe)."""
from ff_math import FIG

FF = "fullyfunded"

REELS = {
    # Sample A: burn -> leak, whip, land + punch-in + circle on the drop, leak loop
    "ff-reel-1017am-match": dict(brand=FF, track="ff-x-money-moves", scenes=[
        dict(k="hook", f="cob", text="Free money. / *Unclaimed?*", emo="🙈", burn=True),
        dict(k="say", f="lite", tin="leak", text=f"Pay: *${FIG['match_pay']:,}*"),
        dict(k="say", f="coral", tin="whipL", text="Boss adds half, / up to *6%.*"),
        dict(k="num", f="deep", tin="land", drop=True, label="Put in 6%:", value=FIG["match_6"], pre="+$", suf="a year. Free."),
    ]),
    # Sample B: flicker, pinned caption over swipe + glide, land + punch-in + circle, leak loop
    "ff-reel-1017-raise-half": dict(brand=FF, track="ff-x-level-up", pin=(1, 2, "Half your raise"), scenes=[
        dict(k="hook", f="cob", text="Raise? / *Save half.*", emo="🎉"),
        dict(k="say", f="lite", tin="swipe", flick=True, text=f"*${FIG['raise_save']}* a month."),
        dict(k="say", f="coral", tin="glide", text=f"At *10%* / for {FIG['raise_years']} years."),
        dict(k="num", f="deep", tin="land", drop=True, label="It becomes", value=FIG["raise_fv"], pre="$",
             suf=f"from ${FIG['raise_in']:,} put in.", size=230),
    ]),
    "ff-reel-1018am-lower-rate": dict(brand=FF, track="ff-x-big-reveal", scenes=[
        dict(k="hook", f="cob", text="One call. / *Lower rate.*", emo="📞"),
        dict(k="say", f="lite", tin="whipL", text="$5,000 card / at *20%.*"),
        dict(k="card", f="coral", tin="slamup", label="Interest in a year", value=f"${FIG['card_20']:,}"),
        dict(k="num", f="deep", tin="land", drop=True, label="Ask for 16%:", value=FIG["card_saved"], pre="−$", suf="a year."),
    ]),
    "ff-reel-1018-the-door": dict(brand=FF, track="ff-x-money-moves", scenes=[
        dict(k="hook", f="cob", text="$100 a month. / *From birth.*", emo="🍼"),
        dict(k="say", f="lite", tin="swipe", text="Stop at *18.* / Never touch it."),
        dict(k="say", f="coral", tin="whipL", flick=True, text="At *10%* a year:"),
        dict(k="num", f="deep", tin="land", drop=True, label="At 65:", value=round(FIG["door_65"] / 1e6, 2), dec=2, pre="$", unit="M",
             suf=f"from ${FIG['door_in']:,}."),
    ]),
    "ff-reel-1019am-gift-per-person": dict(brand=FF, track="ff-x-level-up", scenes=[
        dict(k="hook", f="cob", text="Budget *per person.*", emo="🎁"),
        dict(k="words", f="lite", tin="swipe", chunks=["*14*", "people."], gap=0.7, size=200),
        dict(k="say", f="coral", tin="whipL", text="× *$25* each."),
        dict(k="num", f="deep", tin="land", drop=True, label="Total:", value=FIG["gift_total"], pre="$", suf="Before you shop."),
    ]),
    "ff-reel-1019-late-start": dict(brand=FF, track="ff-x-big-reveal", scenes=[
        dict(k="hook", f="cob", text="Late start? / *Still worth it.*", emo="⏳"),
        dict(k="say", f="lite", tin="whipL", text="*$300* a month / from 34, at 10%."),
        dict(k="swap", f="coral", tin="swipe", text="Not too *late.*", size=190),
        dict(k="num", f="deep", tin="land", drop=True, label="By 65:", value=FIG["late_34"], pre="$", suf="Start now.", size=230),
    ]),
    "ff-reel-1020am-three-numbers": dict(brand=FF, track="ff-x-level-up", scenes=[
        dict(k="hook", f="cob", text="Moving in? / Swap *3 numbers.*", emo="🏠"),
        dict(k="words", f="lite", tin="swipe", chunks=["Take-home.", "Debts.", "*Savings.*"], gap=0.75, size=170),
        dict(k="num", f="deep", tin="land", drop=True, label="Then split", value=1, unit=" bill", suf="Half, or by income.", size=260),
    ]),
    "ff-reel-1020-windfall-pause": dict(brand=FF, track="ff-x-big-reveal", scenes=[
        dict(k="hook", f="cob", text="Windfall? / *Park it first.*", emo="💰"),
        dict(k="say", f="lite", tin="whipL", text="Somewhere / *boring.*"),
        dict(k="words", f="coral", tin="swipe", chunks=["No big", "*moves.*"], gap=0.6, size=190),
        dict(k="num", f="deep", tin="land", drop=True, label="Wait", value=30, unit=" days", suf="Then decide.", size=260),
    ]),
}
