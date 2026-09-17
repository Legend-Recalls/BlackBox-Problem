# BlackBox Shipping Quote — Reverse Engineering

Black-box pricing engine (`oracle.py`). All rules were found by calling `quote()` and observing outputs — no implementation reading.

## Check my work on Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Legend-Recalls/BlackBox-Problem/blob/master/Blackbox_Problem.ipynb)

1. Click the badge above (or open `Blackbox_Problem.ipynb` in this repo via Colab).
2. Run cells top to bottom: `weight → distance → category → express → coupon → replica check`.
3. Key cells: weight stairs (Cell 3), distance notch (Cells 8–10), breakpoint disproof (Cells 12–18), category grid (Cell 22), express grid (Cells 27–29), oracle-vs-replica overlay (Cell 36).

Note: `oracle.py` crashes on Python 3.14 (marshal blob segfault). Use Python 3.12 or Colab's default runtime — `quote(2.0, 100, "standard")` should print `330.0`.

## Files

* `oracle.py` — the black box (do not read the blob; query it).
* `Blackbox_Problem.ipynb` — full probe journal with plots.
* `my_quote.py` — exact replica (`my_quote()` + `quote()` alias).
* `SPEC.md` — every rule in plain English with example queries + notebook screenshots.
* `Black Box Reverse Engineering Assignment.pdf` — original brief.

## Result in one line

```python
rounded = math.ceil(weight / 0.5) * 0.5
price = 40 * rounded + 2.5 * distance
if category == "electronics": price *= 1.3
elif category == "fragile": price += 150
if price > 800: price *= 0.9
if coupon == "WELCOME10": price -= 100
return round(price, 2)  # express ignored
```

See `SPEC.md` for proofs and rejected hypotheses.
