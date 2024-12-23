from collections import defaultdict
from itertools import combinations


def find_direct_triplets(raw_input: str) -> set[tuple[str]]:
    pairs = raw_input.splitlines()

    node_neighbors = defaultdict(set)
    for pair in pairs:
        edge = pair.split('-')
        for node in edge:
            node_neighbors[node].update(edge)

    direct_triplets = set()
    for node, neighbors in node_neighbors.items():
        for triplet in combinations(neighbors, 3):
            if all(n in node_neighbors[m] for n, m in combinations(triplet, 2)):
                direct_triplets.add(tuple(sorted(triplet)))

    return direct_triplets
