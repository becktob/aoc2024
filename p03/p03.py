import re


def find_mul(program, disable=False) -> list[tuple[int, int]]:
    matches = re.finditer(r'mul\((?P<a>[0-9]{1,3}),(?P<b>[0-9]{1,3})\)', program)

    if disable:
        do_dont = re.finditer(r"do(n't)?\(\)", program)
        position_enabled = {m.start(): m[0]=="do()" for m in do_dont}

        def is_enabled(match: re.Match):
            preceding_directives = [enabled for start, enabled in position_enabled.items() if start < match.start()]
            if preceding_directives:
                return preceding_directives[-1]  # Dict ordered by default in python now
            else:
                return True  # At beginning: No directive -> enabled

        matches = [m for m in matches if is_enabled(m)]

    return [(int(m['a']), int(m['b'])) for m in matches]


def solve_part_1(program) -> int:
    pairs = find_mul(program)

    return sum(p[0] * p[1] for p in pairs)


def solve_part_2(program) -> int:
    pairs = find_mul(program, disable=True)

    return sum(p[0] * p[1] for p in pairs)
