"""Small matplotlib utilities with fubumio color defaults."""

from . import color, colors, palettes
from .axes import clean_axes, label_panel, percent_axis
from .palette import (
    Color,
    Palette,
    cycle,
    palette,
)
from .style import STYLE, apply_style, rc_context

__all__ = [
    "Color",
    "Palette",
    "STYLE",
    "apply_style",
    "clean_axes",
    "color",
    "colors",
    "cycle",
    "label_panel",
    "palette",
    "palettes",
    "percent_axis",
    "rc_context",
]
