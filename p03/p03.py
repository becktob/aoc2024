import re


def find_mul(program) -> list[tuple[int, int]]:
    matches = re.finditer(r'mul\((?P<a>[0-9]{1,3}),(?P<b>[0-9]{1,3})\)', program)
    return [(int(m['a']), int(m['b'])) for m in matches]

def solve_part_1(program) -> int:
    pairs = find_mul(program)

    return sum(p[0]*p[1] for p in pairs)

def solve_part_2(program) -> int:
    programm_disabled = re.sub(r"don't\(\).*?do\(\)", "DISABLED", program)

    return solve_part_1(programm_disabled)
