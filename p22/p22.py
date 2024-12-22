def mix_prune(number: int, value: int) -> int:
    return (number ^ value) % 16777216


def evolve_secret_number(number: int) -> int:
    number = mix_prune(number, number * 64)
    number = mix_prune(number, number // 32)
    number = mix_prune(number, number * 2048)
    return number


def evolve_often(number: int, times: int) -> int:
    for _ in range(times):
        number = evolve_secret_number(number)
    return number


def solve_part_1(raw_input: str) -> int:
    initial_secrets = [int(l) for l in raw_input.splitlines()]

    return sum(evolve_often(number, 2000) for number in initial_secrets)


def sale_from_sequence(initial: int, sequence: tuple[int, int, int, int]) -> int:
    value_from_sequence = dict()

    secrets = []
    number = initial
    for _ in range(2000):
        number = evolve_secret_number(number)
        secrets.append(number)

    public = [s % 10 for s in secrets]
    changes = [s2 - s1 for s1, s2 in zip(public, public[1:])]

    for start in range(4, 2000 - 4):
        this_sequence = tuple(changes[start: start + 4])
        if this_sequence not in value_from_sequence:
            value_from_sequence[this_sequence] = public[start + 4]

    return value_from_sequence.get(sequence)
