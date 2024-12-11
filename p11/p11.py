from typing import Iterable, Generator, Iterator


def blink(stones: Iterable[int]) -> Iterator[int]:
    for stone in stones:
        if stone == 0:
            yield 1
        elif 10 <= stone <= 99:
            yield from (int(digit) for digit in str(stone))
        else:
            yield stone * 2024
