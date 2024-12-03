import re


def find_mul(program) -> list[tuple[int, int]]:
    matches = re.finditer('mul\((?P<a>[0-9]{1,3}),(?P<b>[0-9]{1,3})\)', program)
    return [(int(m['a']), int(m['b'])) for m in matches]
