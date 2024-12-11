from functools import cache
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


@cache
def num_stones(stone: int, blinks_todo: int):
    if blinks_todo == 0:
        return 1

    stones_one_blink = blink([stone])

    return sum(num_stones(s, blinks_todo - 1) for s in stones_one_blink)


def solve_part_1(raw_input: str, num_blinks=25):
    stones = map(int, raw_input.split())

    return sum(num_stones(s, num_blinks) for s in stones)
