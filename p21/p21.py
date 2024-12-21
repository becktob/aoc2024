numeric_keypad_rows = '789', '456', '123', '-0A'

numeric_keypad = dict()
for i, row in enumerate(numeric_keypad_rows):
    for j, char in enumerate(row):
        numeric_keypad[char] = (i, j) if char != '-' else None


def shortest_key_sequences(sequence_to_push: str,
                           keypad_layout: dict[str, tuple[int, int]] = None,
                           start_char='A') -> list[str]:
    if sequence_to_push == '':
        return ['']

    if keypad_layout is None:
        keypad_layout = numeric_keypad

    i_from, j_from = keypad_layout[start_char]
    i_to, j_to = keypad_layout[sequence_to_push[0]]

    d_col = j_to - j_from
    col_chars = abs(d_col) * ('>' if d_col > 0 else '<')
    d_row = i_to - i_from
    row_chars = abs(d_row) * ('v' if d_col > 0 else '^')

    keys_this_char = col_chars + row_chars + 'A'

    sequences_tail = shortest_key_sequences(sequence_to_push[1:], keypad_layout, sequence_to_push[0])
    return [keys_this_char + tail for tail in sequences_tail]
