from itertools import combinations, product
from typing import Iterable


class Keypad:
    def __init__(self, rows: Iterable[str]):
        self.char_positions: dict[str, tuple[int, int]] = dict()
        for i, row in enumerate(rows):
            for j, char in enumerate(row):
                self.char_positions[char] = (i, j) if char != '-' else None

    def __getitem__(self, char: str):
        return self.char_positions[char]


numeric_keypad = Keypad(('789', '456', '123', '-0A'))
directional_keypad = Keypad(('-^A', '<v>'))


def shortest_key_sequences(sequence_to_push: str,
                           keypad_layout: Keypad = None,
                           start_char='A') -> list[str]:
    if sequence_to_push == '':
        return ['']

    if keypad_layout is None:
        keypad_layout = numeric_keypad

    i_from, j_from = keypad_layout[start_char]
    i_to, j_to = keypad_layout[sequence_to_push[0]]

    d_col = j_to - j_from
    col_char = ('>' if d_col > 0 else '<')
    d_row = i_to - i_from
    row_char = ('v' if d_row > 0 else '^')

    total_keys = abs(d_col) + abs(d_row)
    indices_row = combinations(range(total_keys), abs(d_row))

    sequences_head = []
    for indices in indices_row:
        key_combination = "".join([row_char if i in indices else col_char for i in range(total_keys)]) + 'A'
        sequences_head.append(key_combination)

    sequences_tail = shortest_key_sequences(sequence_to_push[1:], keypad_layout, sequence_to_push[0])
    return [head + tail for head, tail in product(sequences_head, sequences_tail)]


def sequential_sequence(sequence_to_push: str, keypads: Iterable[Keypad]):
    sequences = [sequence_to_push]

    for keypad in keypads:
        sequences = [s for inner in sequences for s in shortest_key_sequences(inner, keypad)]

    shortest_len = min(map(len, sequences))

    return [s for s in sequences if len(s) == shortest_len]


def score_code(code: str):
    keypads = numeric_keypad, directional_keypad, directional_keypad

    sequences = sequential_sequence(code, keypads)

    shortest_len = min(map(len, sequences))

    return int(code.replace('A', '')) * shortest_len


def solve_part_1(raw_input: str):
    return sum(map(score_code, raw_input.splitlines()))
