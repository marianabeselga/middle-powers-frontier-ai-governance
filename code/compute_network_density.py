#!/usr/bin/env python3
"""Reproduce the network-density figures reported in Figure 2 and the
Stage 5B network-metrics dataset.

STATUS: newly created for this reproducibility package. The original
computation script is not available (see /code/README.md and the root
README's Limitations section) -- this reimplements the same, already
documented method from the raw relational data in /code/data, it does
not introduce any new calculation, metric, or methodological choice.

Method (as documented in data/network/Stage5B-Network-Metrics-Dataset.md):
  - Bipartite participation/access network: density = edges / (6 actors x 4 episodes).
    Reported both including and excluding Brazil's single observer-tier tie.
  - Direct actor-to-actor established-coordination network (Table 2A only):
    simple graph density = 2E / (N(N-1)) over the 6 study actors.
Uses networkx 3.2.1, the version cited in the source dataset, so the
computed values can be checked against the documented method exactly.
"""
import csv
import pathlib

import networkx as nx

DATA_DIR = pathlib.Path(__file__).parent / "data"


def bipartite_participation_density():
    rows = list(csv.DictReader(open(DATA_DIR / "participation_matrix.csv")))
    actors = sorted({r["actor"] for r in rows})
    episodes = sorted({r["episode"] for r in rows})
    max_ties = len(actors) * len(episodes)

    edges_all = [r for r in rows if r["participates"] == "1"]
    edges_excl_observer = [r for r in edges_all if r["tier"] != "observer"]

    density_incl = len(edges_all) / max_ties
    density_excl = len(edges_excl_observer) / max_ties

    print("Bipartite participation/access network")
    print(f"  actors={len(actors)} episodes={len(episodes)} max_possible_ties={max_ties}")
    print(f"  edges including observer-tier tie: {len(edges_all)} -> density = {density_incl:.3f}")
    print(f"  edges excluding observer-tier tie: {len(edges_excl_observer)} -> density = {density_excl:.3f}")
    print(f"  (Figure 2 / Stage 5B report: 0.917 including, 0.875 excluding)")
    return density_incl, density_excl


def direct_coordination_density():
    rows = list(csv.DictReader(open(DATA_DIR / "direct_coordination_edges.csv")))
    actors = ["CTY-BRA", "CTY-CAN", "CTY-IND", "CTY-JPN", "CTY-KOR", "CTY-SGP"]

    g = nx.Graph()
    g.add_nodes_from(actors)
    for r in rows:
        g.add_edge(r["source_actor"], r["target_actor"])

    density = nx.density(g)
    components = list(nx.connected_components(g))
    betweenness = nx.betweenness_centrality(g)

    print()
    print("Direct actor-to-actor established-coordination network (Table 2A only)")
    print(f"  nodes={g.number_of_nodes()} edges={g.number_of_edges()} -> density = {density:.3f}")
    print(f"  (Figure 2 / Stage 5B report: 0.133)")
    print(f"  connected components: {len(components)}")
    for actor in actors:
        print(f"    {actor}: degree={g.degree(actor)} betweenness={betweenness[actor]:.3f}")
    return density


if __name__ == "__main__":
    print(f"networkx version: {nx.__version__} (source dataset cites 3.2.1)")
    print()
    bipartite_participation_density()
    direct_coordination_density()
