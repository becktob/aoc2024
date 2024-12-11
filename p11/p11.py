from typing import Iterable, Iterator


def blink(stones: Iterable[int]) -> Iterator[int]:
    for stone in stones:
        if stone == 0:
            yield 1
        elif len(str(stone)) % 2 == 0:
            digits = str(stone)
            half = len(digits) // 2
            yield from map(int, (digits[:half], digits[half:]))
        else:
            yield stone * 2024


def solve_part_1(raw_input: str):
    stones = map(int, raw_input.split())

    for i in range(25):
        stones = list(blink(stones))

    return len(list(stones))
