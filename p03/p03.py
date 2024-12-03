import re


def find_mul(program, disable=False) -> list[tuple[int, int]]:
    matches = re.finditer(r'mul\((?P<a>[0-9]{1,3}),(?P<b>[0-9]{1,3})\)', program)

    if disable:
        do_dont = list(re.finditer(r"do(n't)?\(\)", program))

        def is_enabled(match: re.Match):
            preceding_directives = [directive for directive in do_dont if directive.start() < match.start()]
            active_directive = max(preceding_directives, key=lambda m: m.start(), default=None)
            if active_directive is None:
                return True
            else:
                return active_directive[0] == "do()"

        matches = [m for m in matches if is_enabled(m)]

    return [(int(m['a']), int(m['b'])) for m in matches]


def solve_part_1(program) -> int:
    pairs = find_mul(program)

    return sum(p[0] * p[1] for p in pairs)


def solve_part_2(program) -> int:
    pairs = find_mul(program, disable=True)

    return sum(p[0] * p[1] for p in pairs)
