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

if __name__ == "__main__":
    for k, v in FIG.items():
        print(f"{k:22s} {v:>14,.0f}" if isinstance(v, (int, float)) else (k, v))
