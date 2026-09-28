#!/usr/bin/env python3
"""Reproduce Figure 4 -- Coordination configuration -> institutional
instrument -> governance location -> observed governance leverage, across
the four Episodes.

STATUS: newly created for this reproducibility package (see /code/README.md).
Minimal re-plot for verification, not a pixel-accurate copy. Institutionalisation
levels and GL5 status are taken as-is from data/leverage_pathways.csv, which
transcribes Stage4-Cross-Case-Matrix.md SS1/1a (see data/PROVENANCE.md) --
no level, category, or GL finding is recalculated or reinterpreted here.
"""
import csv
import pathlib

import matplotlib.pyplot as plt

DATA_DIR = pathlib.Path(__file__).parent / "data"
OUTPUT_DIR = pathlib.Path(__file__).parent / "output"

GL5_COLOR = {"not established": "#9a9a9a", "moderate": "#4859FD", "established": "#4859FD"}
GL5_LABEL = {"not established": "GL5 not established", "moderate": "GL5 (moderate)",
             "established": "GL5 established"}


def main():
    rows = list(csv.DictReader(open(DATA_DIR / "leverage_pathways.csv")))

    fig, axes = plt.subplots(1, len(rows), figsize=(3.1 * len(rows), 5.5), sharey=True)

    for ax, row in zip(axes, rows):
        ax.axis("off")
        ax.text(0.5, 0.95, row["episode"], ha="center", va="top", fontsize=11,
                 fontweight="bold", transform=ax.transAxes, wrap=True)
        ax.text(0.5, 0.80, row["institutionalisation_level"], ha="center", va="top",
                 fontsize=13, fontweight="bold", color="#6F47FC", transform=ax.transAxes)
        ax.text(0.5, 0.71, row["institutionalisation_label"], ha="center", va="top",
                 fontsize=8, color="#555555", transform=ax.transAxes)
        ax.annotate("", xy=(0.5, 0.50), xytext=(0.5, 0.63), xycoords="axes fraction",
                     arrowprops=dict(arrowstyle="->", color="#999999"))
        gl5 = row["gl5_status"]
        ax.text(0.5, 0.42, GL5_LABEL[gl5], ha="center", va="top", fontsize=11,
                 fontweight="bold", color=GL5_COLOR[gl5], transform=ax.transAxes)
        ax.text(0.5, 0.28, row["institutional_instrument"], ha="center", va="top",
                 fontsize=7.5, color="#333333", transform=ax.transAxes, wrap=True,
                 bbox=dict(boxstyle="round", fc="#f8f7f4", ec="none"))

    fig.suptitle("Figure 4 (reproduction) -- Coordination configuration -> institutional\n"
                  "instrument -> governance location -> observed governance leverage", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.9])

    OUTPUT_DIR.mkdir(exist_ok=True)
    out = OUTPUT_DIR / "figure4_reproduction.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
