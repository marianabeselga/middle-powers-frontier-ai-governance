#!/usr/bin/env python3
"""Reproduce Figure 3 -- Actor-to-configuration coordination network -- from
Table 2A/2B of the established-coordination dataset.

STATUS: newly created for this reproducibility package (see /code/README.md).
Minimal re-plot for verification, not a pixel-accurate copy of the published
layout. This draws exactly the edges in data/hub_coordination_edges.csv (22)
and data/direct_coordination_edges.csv (2, shown as a muted dashed overlay,
matching the published figure's treatment) -- no one-mode projection and no
edge is added or inferred beyond what those two files already contain,
consistent with the Codebook's explicit rule against inferring actor-to-actor
ties from shared hub membership.
"""
import csv
import pathlib

import matplotlib.pyplot as plt
import networkx as nx

DATA_DIR = pathlib.Path(__file__).parent / "data"
OUTPUT_DIR = pathlib.Path(__file__).parent / "output"

ACTORS = ["CTY-BRA", "CTY-CAN", "CTY-IND", "CTY-JPN", "CTY-KOR", "CTY-SGP"]
ACTOR_LABEL = {"CTY-BRA": "Brazil", "CTY-CAN": "Canada", "CTY-IND": "India",
               "CTY-JPN": "Japan", "CTY-KOR": "South Korea", "CTY-SGP": "Singapore"}


def main():
    hub_edges = list(csv.DictReader(open(DATA_DIR / "hub_coordination_edges.csv")))
    dyadic_edges = list(csv.DictReader(open(DATA_DIR / "direct_coordination_edges.csv")))
    hubs = sorted({r["target_hub"] for r in hub_edges})

    g = nx.Graph()
    g.add_nodes_from(ACTORS, bipartite=0)
    g.add_nodes_from(hubs, bipartite=1)
    for r in hub_edges:
        g.add_edge(r["source_actor"], r["target_hub"])

    pos = {}
    for i, a in enumerate(ACTORS):
        pos[a] = (0, len(ACTORS) - 1 - i)
    for i, h in enumerate(hubs):
        pos[h] = (3, (len(ACTORS) - 1) * (len(hubs) - 1 - i) / max(len(hubs) - 1, 1))

    fig, ax = plt.subplots(figsize=(11, 7))
    nx.draw_networkx_edges(g, pos, ax=ax, edge_color="#1e1e1e", alpha=0.25, width=1.2)

    # muted dashed overlay for the two genuinely dyadic ties (Table 2A) -- context only
    for r in dyadic_edges:
        x1, y1 = pos[r["source_actor"]]
        x2, y2 = pos[r["target_actor"]]
        ax.plot([x1 - 0.15, x1 - 0.15], [y1, y2], linestyle="--", color="#4859FD",
                 alpha=0.6, linewidth=1.3)

    nx.draw_networkx_nodes(g, pos, nodelist=ACTORS, ax=ax, node_color="#4f5ffd",
                            node_size=1400, edgecolors="#1e1e1e", linewidths=0.5)
    nx.draw_networkx_nodes(g, pos, nodelist=hubs, ax=ax, node_color="#e2d9fa",
                            node_shape="s", node_size=2600, edgecolors="#6F47FC", linewidths=0.8)

    for a in ACTORS:
        x, y = pos[a]
        ax.text(x, y, ACTOR_LABEL[a][:3].upper(), ha="center", va="center",
                 fontsize=8, fontweight="bold", color="white")
    for h in hubs:
        x, y = pos[h]
        label = "\n".join(h[i:i + 22] for i in range(0, len(h), 22))
        ax.text(x, y, label, ha="center", va="center", fontsize=6.5, fontweight="bold")

    ax.set_title("Figure 3 (reproduction) -- Actor-to-configuration coordination network\n"
                  f"{len(ACTORS)} actors, {len(hubs)} hubs, {len(hub_edges)} hub edges "
                  f"+ {len(dyadic_edges)} dyadic ties (dashed, context only)", fontsize=11)
    ax.axis("off")
    fig.tight_layout()

    OUTPUT_DIR.mkdir(exist_ok=True)
    out = OUTPUT_DIR / "figure3_reproduction.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"wrote {out}")
    print(f"nodes={g.number_of_nodes()} ({len(ACTORS)} actors + {len(hubs)} hubs) edges={g.number_of_edges()}")


if __name__ == "__main__":
    main()
