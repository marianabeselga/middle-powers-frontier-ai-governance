#!/usr/bin/env python3
"""Reproduce Figure 5 -- Where coordination pathways reach, stall, or break --
from the six-stage analytical spine coded per Episode.

STATUS: newly created for this reproducibility package (see /code/README.md).
Minimal re-plot for verification, not a pixel-accurate copy. Per-stage
status codes (y=reached, m=moderate confidence, x=not reached) are taken
as-is from data/pathway_breaks.csv, which transcribes Stage4-Cross-Case-
Matrix.md SS4/9 (see data/PROVENANCE.md) -- no stage status is recalculated
or reinterpreted here.
"""
import csv
import pathlib

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

DATA_DIR = pathlib.Path(__file__).parent / "data"
OUTPUT_DIR = pathlib.Path(__file__).parent / "output"

STAGES = ["Capabilities\nmobilised", "Relational\ncoordination", "Institutional\ninstrument",
          "Governance\nlocation", "Institutional/information\n(GL1-3)",
          "Regulatory/behavioural\n(GL4-5)"]
STAGE_COLS = ["capabilities_mobilised", "relational_coordination", "institutional_instrument",
              "governance_location", "institutional_information_gl1_3", "regulatory_behavioural_gl4_5"]

STATUS_STYLE = {
    "y": dict(facecolor="#5161fd", edgecolor="#5161fd", marker="o"),
    "m": dict(facecolor="#aeb5f8", edgecolor="#4859FD", marker="o"),
    "x": dict(facecolor="white", edgecolor="#999999", marker="x"),
}


def main():
    rows = list(csv.DictReader(open(DATA_DIR / "pathway_breaks.csv")))

    fig, ax = plt.subplots(figsize=(13, 1.3 * len(rows) + 2))

    for ri, row in enumerate(rows):
        y = len(rows) - ri - 1
        ax.text(-0.5, y, row["episode"], ha="right", va="center", fontsize=11, fontweight="bold")
        prev_x = None
        for si, col in enumerate(STAGE_COLS):
            status = row[col]
            style = STATUS_STYLE[status]
            if prev_x is not None:
                ax.plot([prev_x, si], [y, y], color="#999999", linewidth=1, alpha=0.4,
                         linestyle="--" if status == "x" else "-")
            if status == "x":
                ax.scatter([si], [y], marker="x", s=140, color="#999999", linewidths=2, zorder=3)
            else:
                ax.add_patch(Circle((si, y), 0.28, facecolor=style["facecolor"],
                                     edgecolor=style["edgecolor"], linewidth=1.4, zorder=3))
            prev_x = si
        ax.text(0, y - 0.45, row["note"], fontsize=8, style="italic", color="#555555", ha="left")

    for si, label in enumerate(STAGES):
        ax.text(si, len(rows) + 0.1, label, ha="center", va="bottom", fontsize=8.5, fontweight="bold")

    ax.set_xlim(-3.3, len(STAGES) - 0.3)
    ax.set_ylim(-0.9, len(rows) + 0.9)
    ax.axis("off")
    ax.set_title("Figure 5 (reproduction) -- Where coordination pathways reach, stall, or break",
                  fontsize=12, pad=10)

    legend_handles = [
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#5161fd", markersize=12, label="Stage reached"),
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#aeb5f8", markeredgecolor="#4859FD", markersize=12, label="Moderate confidence"),
        plt.Line2D([0], [0], marker="x", color="#999999", markersize=10, linewidth=0, label="Not reached (break)"),
    ]
    ax.legend(handles=legend_handles, loc="lower center", bbox_to_anchor=(0.5, -0.15),
              ncol=3, frameon=False, fontsize=9)

    OUTPUT_DIR.mkdir(exist_ok=True)
    out = OUTPUT_DIR / "figure5_reproduction.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
