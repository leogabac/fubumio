"""Small matplotlib utilities with fubumio color defaults."""

from . import color, colors, layouts, options, palettes
from .axes import clean_axes, drop_axis_labels, label_panel, percent_axis
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
    "drop_axis_labels",
    "label_panel",
    "layouts",
    "options",
    "palette",
    "palettes",
    "percent_axis",
    "rc_context",
]
