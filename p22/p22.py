def mix_prune(number: int, value: int) -> int:
    return (number ^ value) % 16777216


def evolve_secret_number(number: int) -> int:
    number = mix_prune(number, number * 64)
    number = mix_prune(number, number // 32)
    number = mix_prune(number, number * 2048)
    return number

def evolve_often(number:int, times:int) -> int:
    for _ in range(times):
        number = evolve_secret_number(number)
    return number


def solve_part_1(raw_input: str) -> int:
    initial_secrets = [int(l) for l in raw_input.splitlines()]

    return sum(evolve_often(number, 2000) for number in initial_secrets)
