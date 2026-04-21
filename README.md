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
- `options` for common matplotlib keyword presets.
- `layouts` for PRL-sized figures without manually converting points to inches.
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
from fubumio import colors as c
from fubumio import export
from fubumio import layouts as layout
from fubumio import options as o

with fm.rc_context():
    fig, ax = layout.subplots(width="single")
    ax.plot(
        [1, 2, 3],
        [0.2, 0.6, 0.9],
        label="Fubuki-coded competence",
        **o.line(c.fubuki.base),
    )
    ax.plot(
        [1, 2, 3],
        [0.1, 0.4, 0.7],
        label="Mio-coded consequences",
        **o.markers(c.mio.base, markersize=5),
    )

    fm.percent_axis(ax)
    fm.clean_axes(ax)
    ax.set(title="A plot with standards", xlabel="episode", ylabel="vibes")
    ax.legend()

    export.savefig(fig, "plot")
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

## Plot Options

```python
from fubumio import colors as c
from fubumio import options as o

ax.plot(x, y, **o.line(c.ina.gold))
ax.plot(x, y, **o.markers(c.ina.purple, markersize=3))
ax.scatter(x, y, **o.scatter(c.suisei.blue, s=12, alpha=0.8))
ax.errorbar(x, y, yerr, **o.errorbar(c.mio.base, capsize=4))
ax.fill_between(x, lo, hi, **o.fill(c.ina.gold, alpha=0.2))
ax.hist(samples, **o.hist(c.ina.purple, bins=24))
fig.savefig("plot.png", **o.savefig())
```

These are just dictionaries of Matplotlib kwargs with delusions of usefulness.
Every preset accepts overrides, so the escape hatch is the same as regular
Matplotlib: pass the keyword you actually want and move on with your life.

For the usual `bbox_inches="tight", dpi=300` ritual:

```python
fig.savefig("plot.png", **o.savefig())
fig.savefig("draft.png", **o.savefig(dpi=180, transparent=True))
```

If you want both PNG and PDF like a sane person:

```python
from fubumio import export

export.savefig(fig, "plot")       # plot.png and plot.pdf
export.savefig(fig, "plot.png")   # also plot.png and plot.pdf
export.saveclose(fig, "plot")     # same thing, then closes the figure
```

## Layouts

```python
from fubumio import layouts as layout

layout.PRL_SINGLE_IN     # 243 pt converted to inches
layout.PRL_DOUBLE_IN     # 486 pt converted to inches

fig, ax = layout.subplots()
fig, ax = layout.subplots(width="single")
fig, axs = layout.subplots(1, 2, width="double", aspect=0.45)

fig, ax = plt.subplots(figsize=(layout.PRL_SINGLE_IN, 2.2))
fig, ax = layout.subplots(width=300, unit="pt", aspect=0.62)
fig, ax = layout.subplots(figsize=(3.3, 3.0))  # explicit matplotlib still wins
```

PRL is the default because it is a reasonable first guess and saves everyone
from repeatedly remembering that a single column is `243 pt` and a double column
is `486 pt`. The inch constants are there for direct `figsize` use, because
Matplotlib insists on using freedom units. `layout.subplots()` only computes 
`figsize` and then gets out of Matplotlib's way. 

Bring your own bad decisions through normal `plt.subplots` kwargs.

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
fm.clean_legend(ax, ncols=2)
fm.drop_axis_labels(ax)
fm.drop_axis_labels(ax, axis="x", tick_labels=False, ticks=False)
fm.percent_axis(ax, axis="y", decimals=0, xmax=1.0)
fm.use_palette(ax, p.ina_contrast)
fm.label_panel(ax, "A")
```

Small axes helpers. `clean_axes()` hides unused spines, removes tick marks,
sets the grid, and strips the legend frame if one exists. It does not erase
axis labels, because sometimes a function should do one job instead of becoming
a junk drawer with a docstring. Use `drop_axis_labels()` when you actually want
the x label, y label, tick labels, and tick marks gone. Pass
`tick_labels=False` or `ticks=False` if you want to keep those. All helpers
return the axes so you can chain them if you are into that sort of thing.
`use_palette()` applies a color cycle to one axes when a global style would be
overkill, which is very mature of you.
`clean_legend()` recreates a compact legend from labeled artists and skips the
whole affair when there is nothing labeled, which is more restraint than most
notebooks deserve.

## Development

```bash
pip install -e ".[dev]"
pytest
ruff check .
```

The project is intentionally tiny. If a helper needs a flowchart, it probably
belongs in your analysis code, not here.
