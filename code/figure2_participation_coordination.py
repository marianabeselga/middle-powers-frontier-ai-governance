#!/usr/bin/env python3
"""Reproduce Figure 2 -- Participation versus established coordination,
by Episode -- from the Stage 5 relational datasets.

STATUS: newly created for this reproducibility package (see /code/README.md).
Minimal re-plot for verification, not a pixel-accurate copy. Per-cell
status (established / participated-only / no participation) and the two
density statistics are derived directly from data/participation_matrix.csv,
data/direct_coordination_edges.csv, and data/hub_coordination_edges.csv,
using the same method as compute_network_density.py.
"""
import csv
import pathlib

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from compute_network_density import bipartite_participation_density, direct_coordination_density

DATA_DIR = pathlib.Path(__file__).parent / "data"
OUTPUT_DIR = pathlib.Path(__file__).parent / "output"

ACTORS = ["Brazil", "Canada", "India", "Japan", "South Korea", "Singapore"]
ACTOR_ID = {"Brazil": "CTY-BRA", "Canada": "CTY-CAN", "India": "CTY-IND",
            "Japan": "CTY-JPN", "South Korea": "CTY-KOR", "Singapore": "CTY-SGP"}
EPISODES = ["Bletchley Sequence", "AISI Network", "Hiroshima AI Process", "GPAI"]
EP_ID = {"Bletchley Sequence": "EP-BLETCHLEY-SEQUENCE-2023", "AISI Network": "EP-AISI-NETWORK-2024",
          "Hiroshima AI Process": "EP-HIROSHIMA-AI-2024", "GPAI": "EP-GPAI-2024"}


def established_actor_episode_pairs():
    """(actor_id, episode_id) pairs with at least one established coordination tie."""
    pairs = set()
    for row in csv.DictReader(open(DATA_DIR / "direct_coordination_edges.csv")):
        pairs.add((row["source_actor"], row["episode_id"]))
        pairs.add((row["target_actor"], row["episode_id"]))
    for row in csv.DictReader(open(DATA_DIR / "hub_coordination_edges.csv")):
        pairs.add((row["source_actor"], row["episode_id"]))
    return pairs


def main():
    participation = {(r["actor"], r["episode"]): r["participates"] == "1"
                      for r in csv.DictReader(open(DATA_DIR / "participation_matrix.csv"))}
    established = established_actor_episode_pairs()

    fig, ax = plt.subplots(figsize=(11, 1.1 * len(EPISODES) + 1.5))

    for ei, ep in enumerate(EPISODES):
        y = len(EPISODES) - ei - 1
        ax.text(-0.4, y + 0.5, ep, ha="right", va="center", fontsize=10, fontweight="bold")
        for ai, actor in enumerate(ACTORS):
            participates = participation.get((actor, ep), False)
            is_established = (ACTOR_ID[actor], EP_ID[ep]) in established
            if is_established:
                fc, ec, marker_text = "#4f5ffd", "#4f5ffd", "EST"
            elif participates:
                fc, ec, marker_text = "#cfc2f6", "#6F47FC", "part."
            else:
                fc, ec, marker_text = "white", "#1e1e1e", ""
            ax.add_patch(Circle((ai, y + 0.5), 0.42, facecolor=fc, edgecolor=ec,
                                 linewidth=1.4, linestyle="-" if participates else "--"))
            if marker_text:
                color = "white" if is_established else "#1e1e1e"
                ax.text(ai, y + 0.5, marker_text, ha="center", va="center",
                         fontsize=7, fontweight="bold", color=color)

    for ai, actor in enumerate(ACTORS):
        ax.text(ai, len(EPISODES) + 0.3, actor, ha="center", fontsize=8, fontweight="bold")

    ax.set_xlim(-3.2, len(ACTORS) + 0.5)
    ax.set_ylim(-0.3, len(EPISODES) + 1.0)
    ax.axis("off")

    density_incl, density_excl = bipartite_participation_density()
    coord_density = direct_coordination_density()
    ax.set_title(
        "Figure 2 (reproduction) -- Participation vs. established coordination\n"
        f"Participation-network density: {density_excl:.3f}-{density_incl:.3f}   |   "
        f"Established dyadic-coordination density: {coord_density:.3f}",
        fontsize=11, pad=16)

    OUTPUT_DIR.mkdir(exist_ok=True)
    out = OUTPUT_DIR / "figure2_reproduction.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
