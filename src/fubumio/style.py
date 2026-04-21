"""Matplotlib rcParams for the fubumio style."""

from __future__ import annotations

from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from typing import Any

import matplotlib as mpl

from . import colors as c
from . import palettes as p

STYLE: dict[str, Any] = {
    "axes.axisbelow": True,
    "axes.edgecolor": c.neutral.ink,
    "axes.facecolor": c.neutral.paper,
    "axes.grid": True,
    "axes.labelcolor": c.neutral.ink,
    "axes.labelsize": 11,
    "axes.linewidth": 0.8,
    "axes.prop_cycle": p.cycle(p.paper),
    "axes.spines.right": False,
    "axes.spines.top": False,
    "figure.dpi": 120,
    "figure.facecolor": c.neutral.paper,
    "figure.figsize": (7.0, 4.2),
    "font.family": "serif",
    "font.size": 10,
    "grid.color": c.neutral.grid,
    "grid.linewidth": 0.7,
    "grid.alpha": 0.8,
    "legend.frameon": False,
    "lines.linewidth": 2.0,
    "savefig.bbox": "tight",
    "savefig.dpi": 180,
    "savefig.facecolor": c.neutral.paper,
    "text.latex.preamble": r"\usepackage{amsfonts}",
    "text.usetex": True,
    "xtick.color": c.neutral.ink,
    "xtick.labelsize": 10,
    "ytick.color": c.neutral.ink,
    "ytick.labelsize": 10,
    "pgf.texsystem": "pdflatex",
    "pgf.rcfonts": False,
}


def apply_style(overrides: Mapping[str, Any] | None = None) -> None:
    """Apply the fubumio matplotlib style globally."""

    rc = STYLE.copy()
    if overrides:
        rc.update(overrides)
    mpl.rcParams.update(rc)


@contextmanager
def rc_context(overrides: Mapping[str, Any] | None = None) -> Iterator[None]:
    """Temporarily use the fubumio style inside a ``with`` block."""

    rc = STYLE.copy()
    if overrides:
        rc.update(overrides)
    with mpl.rc_context(rc):
        yield
