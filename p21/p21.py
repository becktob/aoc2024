import sys
from functools import cache
from itertools import combinations, product
from typing import Iterable


class Keypad:
    def __init__(self, rows: Iterable[str]):
        self.char_positions: dict[str, tuple[int, int]] = dict()
        self.gap: tuple[int, int]
        for i, row in enumerate(rows):
            for j, char in enumerate(row):
                if char == '-':
                    self.gap = (i, j)
                else:
                    self.char_positions[char] = (i, j)

    def __getitem__(self, char: str):
        return self.char_positions[char]


numeric_keypad = Keypad(('789', '456', '123', '-0A'))
directional_keypad = Keypad(('-^A', '<v>'))


def shortest_key_sequences(sequence_to_push: str,
                           keypad_layout: Keypad = None,
                           start_char='A',
                           simple_only=False) -> list[str]:
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
    col_chars = abs(d_col) * col_char
    row_chars = abs(d_row) * row_char

    sequences_head = set()
    if simple_only:
        sequences_head.add(row_chars + col_chars + 'A')
        sequences_head.add(col_chars + row_chars + 'A')
    else:
        total_keys = abs(d_col) + abs(d_row)
        indices_row = combinations(range(total_keys), abs(d_row))

        for indices in indices_row:
            key_combination = "".join([row_char if i in indices else col_char for i in range(total_keys)]) + 'A'
            sequences_head.add(key_combination)

    if keypad_layout.gap == (i_from, j_to):
        sequences_head.remove(col_chars + row_chars + 'A')
    if keypad_layout.gap == (i_to, j_from):
        sequences_head.remove(row_chars + col_chars + 'A')

    sequences_tail = shortest_key_sequences(sequence_to_push[1:], keypad_layout, sequence_to_push[0])
    return [head + tail for head, tail in product(sequences_head, sequences_tail)]


def sequential_sequence(sequence_to_push: str, keypads: tuple):
    sequences = [sequence_to_push]

    for keypad in keypads:
        sequences = [s for inner in sequences for s in shortest_key_sequences(inner, keypad)]

    shortest_len = min(map(len, sequences))

    return [s for s in sequences if len(s) == shortest_len]


def shortest_button_to_button(b_from, b_to, keypads: tuple) -> list[str]:
    sequences_this_keypad = shortest_key_sequences(b_to, keypads[0], b_from, simple_only=True)
    if len(keypads) == 1:
        return sequences_this_keypad

    button_to_button = []
    for seq in sequences_this_keypad:
        seq_from_A = 'A' + seq
        combinations_this_sequence = [shortest_button_to_button(f, t, keypads[1:]) for f, t in
                                      zip(seq_from_A[:-1], seq_from_A[1:])]
        combinations_this_sequence = ["".join(segments) for segments in product(*combinations_this_sequence)]
        button_to_button += combinations_this_sequence

    return button_to_button


@cache
def count_shortest_button_to_button(b_from, b_to, keypads: tuple) -> int:
    if len(keypads) == 0:
        return 1

    button_to_button = sys.maxsize
    for seq in shortest_key_sequences(b_to, keypads[0], b_from, simple_only=True):
        this_b2b = sum(count_shortest_button_to_button(f, t, keypads[1:]) for f, t in zip('A' + seq, seq))
        button_to_button = min(button_to_button, this_b2b)

    return button_to_button


def score_code(code: str):
    keypads = numeric_keypad, directional_keypad, directional_keypad

    sequences = shortest_button_to_button('A', code, keypads)

    shortest_len = min(map(len, sequences))

    return int(code.replace('A', '')) * shortest_len


def score_code_count_only(code: str, keypads=None):
    if keypads is None:
        keypads = numeric_keypad, directional_keypad, directional_keypad

    return int(code.replace('A', '')) * count_shortest_button_to_button('A', code, keypads)


def solve_part_1(raw_input: str):
    return sum(map(score_code, raw_input.splitlines()))


def solve_part_2(raw_input: str):
    keypads = [numeric_keypad] + [directional_keypad] * 25
    keypads = tuple(keypads)
    return sum(map(lambda code: score_code_count_only(code, keypads), raw_input.splitlines()))
