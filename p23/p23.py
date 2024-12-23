from collections import defaultdict
from itertools import combinations


def find_neighbors(raw_input: str) -> dict[str, set[str]]:
    pairs = raw_input.splitlines()
    node_neighbors = defaultdict(set)
    for pair in pairs:
        edge = pair.split('-')
        for node in edge:
            node_neighbors[node].update(edge)
    return node_neighbors


def find_direct_triplets(raw_input: str) -> set[tuple[str]]:
    node_neighbors = find_neighbors(raw_input)

    direct_triplets = set()
    for node, neighbors in node_neighbors.items():
        for triplet in combinations(neighbors, 3):
            if all(n in node_neighbors[m] for n, m in combinations(triplet, 2)):
                direct_triplets.add(tuple(sorted(triplet)))

    return direct_triplets


def solve_part_1(raw_input: str):
    triplets = find_direct_triplets(raw_input)

    return sum(1 for t in triplets if any(node[0] == 't' for node in t))


def find_groups(raw_input: str):
    pairs = raw_input.splitlines()
    node_groups = defaultdict(set)
    for pair in pairs:
        n, m = pair.split('-')
        group = {m, n}
        group.update(node_groups[m])
        group.update(node_groups[n])
        for k in group:
            node_groups[k] = group

    return set(tuple(g) for g in node_groups.values())


def find_largest_direct_group(raw_input: str) -> tuple[str]:
    node_neighbors = find_neighbors(raw_input)

    largest_direct = ()
    for node, neighbors in node_neighbors.items():
        for group_size in range(len(largest_direct) + 1, len(neighbors)):
            group = find_any_direct_group_of_size(node_neighbors, group_size)
            if group is not None:
                largest_direct = group

    return largest_direct


def find_any_direct_group_of_size(neighbors: dict[str, set[str]], size: int) -> tuple[str] | None:
    for group in combinations(neighbors, size):
        if all(n in neighbors[m] for n, m in combinations(group, 2)):
            return tuple(sorted(group))
    return None


def solve_part_2(raw_input: str):
    return ",".join(find_largest_direct_group(raw_input))
