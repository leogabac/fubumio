# fubumio

Tiny matplotlib utilities for plots that should look like someone made a
decision before clicking export. Shocking concept, I know.

`fubumio` is a small, opinionated pile of colors, rcParams, and axes helpers.
The name is doing exactly what it says: adding a bit of weeb personality to
every side-project I have because apparently I simply cannot contain myself.
The palette starts with Fubuki cyan and Mio red, then leaves room for whatever
other colors eventually wander in and demand tenure. The goal is still the same:
give figures a visual identity instead of the default matplotlib emotional
support blue.

## What is in here

- `colors` for named color tokens.
- `palettes` for ordered color recipes and matplotlib property cycles.
- `apply_style()` when you want global plotting defaults.
- `rc_context()` when you want the style temporarily, like a responsible adult.
- `clean_axes()`, `percent_axis()`, and `label_panel()` for the boring cleanup
  that every notebook somehow pretends is new work.

That is it. This is not a plotting framework. It is a small drawer of good
knives. Please do not build a cathedral in the drawer.

## Install

```bash
pip install git+https://github.com/leogabac/fubumio.git
```

For local work:

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
import matplotlib.pyplot as plt
import fubumio as fm

with fm.rc_context():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [0.2, 0.6, 0.9], label="Fubuki-coded competence")
    ax.plot([1, 2, 3], [0.1, 0.4, 0.7], label="Mio-coded consequences")

    fm.percent_axis(ax)
    fm.clean_axes(ax)
    ax.set(title="A plot with standards", xlabel="episode", ylabel="vibes")
    ax.legend()

    fig.savefig("plot.png")
```

## Color Tokens

```python
from fubumio import colors as c
from fubumio import palettes as p

c.fubuki.base       # "#58BFCB"
c.mio.base          # "#D35C7F"
c.ina.purple        # "#594967"
c.ina.gold          # "#eaa36d"
c.suisei.blue       # "#76a7e8"
c.named["fubuki"]   # compatibility mapping, for dictionary enjoyers

p.paper                 # useful default cycle for actual work
p.ina_contrast          # purple/gold for two-variable contrast
```

The `colors` namespace is the intended lazy-person import. One import, then
autocomplete your way through `c.ina.purple` like a civilized menace. Palettes
live next door in `palettes`, because raw colors and ordered plot recipes are
not the same thing, despite every one-off notebook trying very hard to pretend
otherwise.

For matplotlib cycles:

```python
ax.plot(x, y, color=c.ina.gold)
ax.set_prop_cycle(p.cycle(p.ina_contrast))

# The old helper still works when you want hex strings by name.
fm.palette("ina_contrast")
```

Available palettes:

- `duo`: Fubuki, Mio, and a couple of supporting colors.
- `paper`: darker colors that behave better on reports and papers.
- `soft`: lighter colors for fills, bands, and other non-yelling marks.
- `contrast`: stronger lines when the figure needs to survive a projector.
- `basic`: the old pfnumerics red/blue emergency kit.
- `ina`: Ina purple, gold, and pink tokens in one cycle.
- `ina_contrast`: Ina purple/gold for comparing two variables.
- `ina_dark_contrast`: darker Ina purple/gold when the plot needs more drama.
- `suisei`: the two Suisei blues.

## API

```python
fm.apply_style()
```

Applies the style globally. Good for scripts. Dangerous in notebooks if you
forgot which cell did what, which of course you did.

The default style assumes you have a working LaTeX setup and uses serif text,
`pdflatex`, PGF-compatible fonts, and an `amsfonts` preamble. Beautiful labels,
with the usual TeX tax because apparently plots needed a build system too.

```python
with fm.rc_context({"figure.figsize": (5, 3)}):
    ...
```

Applies the style only inside the block, with optional rcParam overrides.

```python
fm.clean_axes(ax)
fm.percent_axis(ax, axis="y", decimals=0, xmax=1.0)
fm.label_panel(ax, "A")
```

Small axes helpers. They return the axes so you can chain them if you are into
that sort of thing.

## Development

```bash
pip install -e ".[dev]"
pytest
ruff check .
```

The project is intentionally tiny. If a helper needs a flowchart, it probably
belongs in your analysis code, not here.
