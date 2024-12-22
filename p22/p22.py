def mix_prune(number: int, value: int) -> int:
    return (number ^ value) % 16777216


def evolve_secret_number(number: int) -> int:
    number = mix_prune(number, number * 64)
    number = mix_prune(number, number // 32)
    number = mix_prune(number, number * 2048)
    return number
