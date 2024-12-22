from collections import defaultdict


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
    value_from_sequence = value_dict(initial)

    return value_from_sequence.get(sequence, 0)


def value_dict(initial, num_evol=2000):
    value_from_sequence = dict()
    secrets = []
    number = initial
    for _ in range(num_evol):
        secrets.append(number)
        number = evolve_secret_number(number)
    public = [s % 10 for s in secrets]
    changes = [s2 - s1 for s1, s2 in zip(public, public[1:])]
    for start in range(num_evol - 4):
        this_sequence = tuple(changes[start: start + 4])
        if this_sequence not in value_from_sequence:
            value_from_sequence[this_sequence] = public[start + 4]
    return value_from_sequence


def solve_part_2(raw_input: str):
    initial_secrets = [int(l) for l in raw_input.splitlines()]
    value_dicts = [value_dict(i) for i in initial_secrets]

    sequence_returns = defaultdict(int)
    for vd in value_dicts:
        for seq, val in vd.items():
            sequence_returns[seq] += val

    best_return = max(sequence_returns.items(), key=lambda item: item[1])
    print(best_return)

    return best_return[1]
