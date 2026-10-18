"""Fully Funded money maths for the aggressive pivot (Oct 17). Every on-screen and caption figure is computed here.
Headline growth rate is 10% a year (S&P 500 long-run average, before inflation); never above 10%. Compounded monthly.
Run it to print the table: python3 studio/pivot/ff_math.py"""
RATE = 0.10
assert RATE <= 0.10


def fv_monthly(pmt, years, rate=RATE):
    """Value of `pmt` paid at the end of every month for `years`, compounded monthly."""
    r, n = rate / 12, round(years * 12)
    return pmt * n if r == 0 else pmt * ((1 + r) ** n - 1) / r


def grow(pv, years, rate=RATE):
    return pv * (1 + rate / 12) ** round(years * 12)


def card_interest(bal, apr, years=1):
    return grow(bal, years, apr) - bal


def r(x, to=1):
    return int(round(x / to) * to)


FIG = {}
FIG["match_pay"], FIG["match_3"], FIG["match_6"] = 50000, r(50000 * 0.03 * 0.5), r(50000 * 0.06 * 0.5)
FIG["raise_save"], FIG["raise_years"] = 100, 20
FIG["raise_fv"] = r(fv_monthly(100, 20))
FIG["raise_in"] = 100 * 12 * 20
FIG["card_20"], FIG["card_16"] = r(card_interest(5000, 0.20)), r(card_interest(5000, 0.16))
FIG["card_saved"] = FIG["card_20"] - FIG["card_16"]
FIG["door_18"] = fv_monthly(100, 18)
FIG["door_65"] = r(grow(FIG["door_18"], 65 - 18), 1000)
FIG["door_in"] = 100 * 12 * 18
FIG["gift_total"] = 14 * 25
FIG["late_24"] = r(fv_monthly(300, 65 - 24), 1000)
FIG["late_34"] = r(fv_monthly(300, 65 - 34), 1000)
FIG["late_in_34"] = 300 * 12 * (65 - 34)
FIG["home_0"], FIG["home_3"], FIG["home_10"] = 10000, r(grow(10000, 20, 0.03), 100), r(grow(10000, 20, 0.10), 100)
FIG["coat_a"], FIG["coat_b"] = 240 // 120, 60 // 6
savers = [1200, 2500, 3400, 4800, 88100]
FIG["avg"], FIG["median"] = sum(savers) // len(savers), sorted(savers)[2]
FIG["hundred_65_from_25"] = r(fv_monthly(100, 40), 1000)

# ---- §13 (Oct 17 pm): 8-10% only, viewer late 20s-mid 30s, horizons to 55-65 -------------------------------------
FIG["card_bal"] = 5000
FIG["card14"] = r(card_interest(5000, 0.14))                       # avg cut 6.3 pts (LendingTree 2026) -> 20% to 14%
FIG["card_cut"] = FIG["card_20"] - FIG["card14"]
FIG["mo_20"] = r(5000 * 0.20 / 12)                                  # first month's interest at 20%
FIG["mo_14"] = r(5000 * 0.14 / 12)
FIG["s28_60"] = r(fv_monthly(300, 60 - 28), 100)                    # $300/mo, 28 -> 60, 10%
FIG["s33_60"] = r(fv_monthly(300, 60 - 33), 100)                    # $300/mo, 33 -> 60, 10%
FIG["s_gap"] = FIG["s28_60"] - FIG["s33_60"]
FIG["s_in_extra"] = 300 * 12 * 5                                    # 5 more years of $300
FIG["catch_pmt"] = r(300 * fv_monthly(1, 60 - 28) / fv_monthly(1, 60 - 33))  # monthly from 33 that matches $300 from 28
FIG["k10_0"] = 10000
FIG["k10_8"] = r(grow(10000, 30, 0.08), 100)                        # $10,000 at 30, left to 60
FIG["k10_10"] = r(grow(10000, 30, 0.10), 100)
FIG["k10_steps"] = [r(grow(10000, y, 0.10), 1000) for y in (0, 10, 20, 30)]
FIG["split_a"], FIG["split_b"], FIG["split_rent"] = 6000, 4000, 2000
FIG["split_ra"] = r(2000 * 6000 / 10000)
FIG["split_rb"] = 2000 - FIG["split_ra"]
FIG["gift_n"], FIG["gift_each"] = 14, 25


if __name__ == "__main__":
    for k, v in FIG.items():
        print(f"{k:22s} {v:>14,.0f}" if isinstance(v, (int, float)) else (k, v))
