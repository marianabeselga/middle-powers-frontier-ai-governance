#!/usr/bin/env python3
"""Reproduce Figure 1 -- Capability and structural-condition configurations
by country -- from the coded country-profile data.

STATUS: newly created for this reproducibility package (see /code/README.md).
This is a plain, minimal re-plot for verification purposes: it is not a
pixel-accurate copy of the published figure's custom layout, and it
introduces no new coding, aggregation, or ranking. Cell values, category
labels, and the "no aggregate score" rule are taken as-is from
data/capability_structural_matrix.csv (see data/PROVENANCE.md).
"""
import csv
import pathlib

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

DATA_DIR = pathlib.Path(__file__).parent / "data"
OUTPUT_DIR = pathlib.Path(__file__).parent / "output"

# Documented project palette (README.md / Codebook), reused for consistency
# only -- not a new design decision.
CAP_FILL = {"LTD": "#ced1f6", "MOD": "#959ff9", "STR": "#4f5ffd"}
CAP_TEXT = {"LTD": "#1e1e1e", "MOD": "#1e1e1e", "STR": "#f8f7f4"}
STRUC_FILL = {"MIX": "#ab94f8", "ENB": "#744efc", "CON": "#e0533d"}
STRUC_TEXT = {"MIX": "#1e1e1e", "ENB": "#f8f7f4", "CON": "#f8f7f4"}
CAP_LABEL = {"LTD": "Limited", "MOD": "Moderate", "STR": "Strong"}
STRUC_LABEL = {"MIX": "Mixed", "ENB": "Enabling", "CON": "Constraining"}

C_COLS = ["C1", "C2", "C3", "C4", "C5"]
S_COLS = ["S1", "S2", "S3", "S4"]


def main():
    rows = list(csv.DictReader(open(DATA_DIR / "capability_structural_matrix.csv")))

    n_rows = len(rows)
    n_cols = len(C_COLS) + 1 + len(S_COLS)  # +1 gap column
    fig, ax = plt.subplots(figsize=(11, 1.1 * n_rows + 1.5))

    for ri, row in enumerate(rows):
        y = n_rows - ri - 1
        ax.text(-0.3, y + 0.5, row["country"], ha="right", va="center",
                 fontsize=11, fontweight="bold")
        for ci, col in enumerate(C_COLS):
            val = row[col]
            ax.add_patch(Rectangle((ci, y), 0.9, 0.9, facecolor=CAP_FILL[val],
                                    edgecolor="#1e1e1e", linewidth=0.3))
            ax.text(ci + 0.45, y + 0.45, val, ha="center", va="center",
                     fontsize=9, fontweight="bold", color=CAP_TEXT[val])
        for si, col in enumerate(S_COLS):
            val = row[col]
            x = len(C_COLS) + 1 + si
            ax.add_patch(Rectangle((x, y), 0.9, 0.9, facecolor=STRUC_FILL[val],
                                    edgecolor="#1e1e1e", linewidth=0.3))
            ax.text(x + 0.45, y + 0.45, val, ha="center", va="center",
                     fontsize=9, fontweight="bold", color=STRUC_TEXT[val])

    for ci, col in enumerate(C_COLS):
        ax.text(ci + 0.45, n_rows + 0.3, col, ha="center", fontsize=10, fontweight="bold")
    for si, col in enumerate(S_COLS):
        x = len(C_COLS) + 1 + si
        ax.text(x + 0.45, n_rows + 0.3, col, ha="center", fontsize=10, fontweight="bold")
    ax.text((len(C_COLS)) / 2, n_rows + 0.9, "CAPABILITIES", ha="center",
             fontsize=10, fontweight="bold", color="#4859FD")
    ax.text(len(C_COLS) + 1 + len(S_COLS) / 2, n_rows + 0.9, "STRUCTURAL CONDITIONS",
             ha="center", fontsize=10, fontweight="bold", color="#6F47FC")

    ax.set_xlim(-3.6, n_cols + 0.5)
    ax.set_ylim(-0.3, n_rows + 1.4)
    ax.axis("off")
    ax.set_title("Figure 1 (reproduction) -- Capability and structural-condition\n"
                  "configurations by country", fontsize=12, pad=14)

    legend_elems = [Rectangle((0, 0), 1, 1, facecolor=c) for c in CAP_FILL.values()]
    legend_labels = [CAP_LABEL[k] for k in CAP_FILL]
    legend_elems += [Rectangle((0, 0), 1, 1, facecolor=c) for k, c in STRUC_FILL.items() if k in ("MIX", "ENB")]
    legend_labels += [STRUC_LABEL[k] for k in ("MIX", "ENB")]
    ax.legend(legend_elems, legend_labels, loc="lower center",
              bbox_to_anchor=(0.5, -0.12), ncol=5, frameon=False, fontsize=8)

    OUTPUT_DIR.mkdir(exist_ok=True)
    out = OUTPUT_DIR / "figure1_reproduction.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
