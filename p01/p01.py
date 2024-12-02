import collections
from typing import Iterable


def distances_of_smallest(list_a: Iterable, list_b: Iterable):
    list_a, list_b = list(list_a), list(list_b)
    list_a.sort()
    list_b.sort()

    return [abs(a - b) for a, b in zip(list_a, list_b)]


def solve_part_1(raw_input: str):
    list_a, list_b = zip(*(map(int, line.split()) for line in raw_input.splitlines()))
    return sum(distances_of_smallest(list_a, list_b))


def similarity_score(list_a: Iterable, list_b: Iterable):
    list_a, list_b = list(list_a), list(list_b)

    counts_in_b = collections.Counter(list_b)

    return sum(counts_in_b[item] * item for item in list_a)
