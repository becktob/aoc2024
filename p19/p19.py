from functools import cache


def parse_towels_designs(raw_input: str) -> (tuple[str], tuple[str]):
    raw_towels, raw_designs = raw_input.split('\n\n')
    towels = tuple(raw_towels.split(', '))
    designs = tuple(raw_designs.splitlines())
    return towels, designs


def find_combinations(design: str, towels: tuple[str]) -> list[list[str]]:
    towels_matching_beginning = [t for t in towels if all(d == t for d, t in zip(design, t))]

    combinations = []
    for beginning in towels_matching_beginning:
        if beginning == design:
            combinations.append([beginning])
        elif remaining := design[len(beginning):]:
            ends = find_combinations(remaining, towels)
            combinations += [[beginning] + end for end in ends]

    return combinations


def can_combine(design: str, towels: tuple[str]) -> bool:
    towels_matching_beginning = [t for t in towels if all(d == t for d, t in zip(design, t))]

    for beginning in towels_matching_beginning:
        if beginning == design:
            return True
        elif remaining := design[len(beginning):]:
            if can_combine(remaining, towels):
                return True

    return False

@cache
def count_combine(design: str, towels: tuple[str]) -> int:
    towels_matching_beginning = [t for t in towels if all(d == t for d, t in zip(design, t))]

    combinations = 0
    for beginning in towels_matching_beginning:
        if beginning == design:
            combinations += 1
        elif remaining := design[len(beginning):]:
            combinations += count_combine(remaining, towels)

    return combinations


def solve_part_1(raw_input: str):
    towels, designs = parse_towels_designs(raw_input)
    return sum(1 for d in designs if can_combine(d, towels))


def solve_part_2(raw_input: str):
    towels, designs = parse_towels_designs(raw_input)
    return sum(count_combine(d, towels) for d in designs)
