"""Axes helpers for common matplotlib cleanup."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Literal

from matplotlib.axes import Axes
from matplotlib.ticker import PercentFormatter

Side = Literal["left", "right", "top", "bottom"]


def clean_axes(
    ax: Axes,
    *,
    keep: Iterable[Side] = ("left", "bottom"),
    grid: bool = True,
    legend: bool = True,
) -> Axes:
    """Hide unused spines, soften ticks, and optionally clean the legend."""

    visible = set(keep)
    for side, spine in ax.spines.items():
        spine.set_visible(side in visible)
    ax.tick_params(length=0)
    ax.grid(grid)

    if legend:
        current = ax.get_legend()
        if current is not None:
            current.set_frame_on(False)
    return ax


def percent_axis(
    ax: Axes,
    *,
    axis: Literal["x", "y"] = "y",
    decimals: int = 0,
    xmax: float = 1.0,
) -> Axes:
    """Format an axis as percentages."""

    formatter = PercentFormatter(xmax=xmax, decimals=decimals)
    if axis == "x":
        ax.xaxis.set_major_formatter(formatter)
    else:
        ax.yaxis.set_major_formatter(formatter)
    return ax


def label_panel(
    ax: Axes,
    label: str,
    *,
    x: float = -0.08,
    y: float = 1.04,
    weight: str = "bold",
    size: int = 12,
) -> Axes:
    """Add a small panel label like ``A`` or ``B`` above an axes."""

    ax.text(
        x,
        y,
        label,
        transform=ax.transAxes,
        fontweight=weight,
        fontsize=size,
        va="bottom",
        ha="left",
    )
    return ax
