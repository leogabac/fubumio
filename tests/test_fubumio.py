import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.colors import is_color_like

import fubumio as fm
from fubumio import colors as c
from fubumio import options as o
from fubumio import palettes as p


def test_palette_returns_hex_colors():
    assert fm.palette("duo")[:2] == ("#58BFCB", "#D35C7F")


def test_color_namespaces_expose_hex_values():
    assert c.fubuki.base == "#58BFCB"
    assert c.fubuki.base.hex == "#58BFCB"
    assert c.fubuki.base.name == "fubuki.base"
    assert c.mio.dark == "#87344F"
    assert c.ina.purple == "#594967"
    assert c.suisei.blue == "#76a7e8"
    assert is_color_like(c.ina.gold)
    assert c.named["ink"] is c.neutral.ink


def test_palette_module_exposes_named_palettes():
    assert c.ina.gold == "#eaa36d"
    assert c.basic.dark_blue == "#000a64"
    assert p.ina_contrast == ("#594967", "#eaa36d")
    assert p.get("ina_contrast") == p.ina_contrast


def test_new_palettes_include_imported_colors():
    assert p.ina == (
        "#323142",
        "#eaa36d",
        "#d1527a",
        "#594967",
        "#ca7845",
    )
    assert fm.palette("suisei") == p.suisei


def test_plot_options_expose_overridable_matplotlib_kwargs():
    assert o.line(c.ina.gold) == {
        "color": c.ina.gold,
        "linewidth": 2.0,
        "solid_capstyle": "round",
    }
    assert o.line(c.ina.gold, linewidth=1.2, alpha=0.8) == {
        "color": c.ina.gold,
        "linewidth": 1.2,
        "solid_capstyle": "round",
        "alpha": 0.8,
    }
    assert o.markers(c.ina.purple, markersize=3)["markersize"] == 3
    assert o.scatter(c.suisei.blue, s=12)["s"] == 12
    assert o.errorbar(c.mio.base, capsize=4)["capsize"] == 4


def test_rc_context_applies_and_restores_style():
    before = plt.rcParams["axes.facecolor"]
    with fm.rc_context():
        assert plt.rcParams["axes.facecolor"] == "#FAFAF7"
        assert plt.rcParams["font.family"] == ["serif"]
        assert plt.rcParams["text.usetex"] is True
        assert plt.rcParams["text.latex.preamble"] == r"\usepackage{amsfonts}"
        assert plt.rcParams["pgf.texsystem"] == "pdflatex"
        assert plt.rcParams["pgf.rcfonts"] is False
        assert plt.rcParams["axes.labelsize"] == 11
        assert plt.rcParams["xtick.color"] == "#22242A"
        assert plt.rcParams["xtick.labelsize"] == 10
        assert plt.rcParams["ytick.color"] == "#22242A"
        assert plt.rcParams["ytick.labelsize"] == 10
    assert plt.rcParams["axes.facecolor"] == before


def test_axes_helpers_return_axes():
    fig, ax = plt.subplots()
    try:
        ax.plot([0, 1], [0.2, 0.8], label="line", **o.line(c.ina.gold))
        ax.plot([0, 1], [0.1, 0.7], **o.markers(c.ina.purple))
        ax.scatter([0.5], [0.4], **o.scatter(c.suisei.blue))
        ax.errorbar([0.7], [0.5], [0.1], **o.errorbar(c.mio.base))
        ax.legend()
        assert fm.clean_axes(ax) is ax
        assert fm.percent_axis(ax) is ax
        assert fm.label_panel(ax, "A") is ax
    finally:
        plt.close(fig)


def test_drop_axis_labels_removes_selected_labels():
    fig, ax = plt.subplots()
    try:
        ax.plot([0, 1], [0, 1])
        ax.set(xlabel="x label", ylabel="y label")
        assert fm.drop_axis_labels(ax, "x") is ax
        assert ax.get_xlabel() == ""
        assert ax.get_ylabel() == "y label"
        assert not any(label.get_visible() for label in ax.get_xticklabels())
        assert any(label.get_visible() for label in ax.get_yticklabels())
        assert not any(tick.get_visible() for tick in ax.xaxis.get_ticklines())

        ax.set(xlabel="x label", ylabel="y label")
        fm.drop_axis_labels(ax, "y")
        assert ax.get_xlabel() == "x label"
        assert ax.get_ylabel() == ""
        assert not any(label.get_visible() for label in ax.get_yticklabels())
        assert not any(tick.get_visible() for tick in ax.yaxis.get_ticklines())

        ax.set(xlabel="x label", ylabel="y label")
        fm.drop_axis_labels(ax)
        assert ax.get_xlabel() == ""
        assert ax.get_ylabel() == ""
        assert not any(label.get_visible() for label in ax.get_xticklabels())
        assert not any(label.get_visible() for label in ax.get_yticklabels())
    finally:
        plt.close(fig)


def test_drop_axis_labels_can_keep_tick_labels_and_ticks():
    fig, ax = plt.subplots()
    try:
        ax.plot([0, 1], [0, 1])
        ax.set(xlabel="x label", ylabel="y label")
        fm.drop_axis_labels(ax, tick_labels=False, ticks=False)
        assert ax.get_xlabel() == ""
        assert ax.get_ylabel() == ""
        assert any(label.get_visible() for label in ax.get_xticklabels())
        assert any(label.get_visible() for label in ax.get_yticklabels())
        assert any(tick.get_visible() for tick in ax.xaxis.get_ticklines())
        assert any(tick.get_visible() for tick in ax.yaxis.get_ticklines())
    finally:
        plt.close(fig)
