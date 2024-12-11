from typing import Iterable, Generator, Iterator


def blink(stones: Iterable[int]) -> Iterator[int]:
    for stone in stones:
        if stone == 0:
            yield 1
        else:
            raise NotImplementedError
