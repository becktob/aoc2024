import numpy


def string_to_array(content, dtype=numpy.uint8):
    lines = content.strip().split('\n')
    chars = [[c for c in l] for l in lines]
    return numpy.array(chars)


def find_xmases(input: numpy.ndarray[str]):
    # warning: might be unused/badly tested; not needed for actualy solution
    query = 'XMAS'

    where_letter = {letter: list(zip(*numpy.where(letter == input))) for letter in query}

    paths_todo = where_letter[query[0]]

    paths_todo = [[coords] for coords in paths_todo]

    while paths_todo:
        path = paths_todo.pop(0)
        if len(path) == len(query):
            yield path
            continue

        next_letter = query[len(path)]

        next_letter_locations = where_letter[next_letter]

        next_letter_neighbors = [loc for loc in next_letter_locations
                                 if any_neighbor(loc, path)]

        for next_coord in next_letter_neighbors:
            path_todo = path + [next_coord]
            paths_todo.append(path_todo)


def any_neighbor(loc, path):
    tail = path[-1]
    return abs(loc[0] - tail[0]) <= 1 and abs(loc[1] - tail[1]) <= 1


def find_straight_xmases(input):
    query = 'XMAS'

    x_locs = zip(*numpy.where(query[0] == input))

    directions = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if not 0 == dy == dx]

    for i, j in x_locs:
        for di, dj in directions:
            coords_on_path = [(i + n * di, j + n * dj) for n in range(len(query))]
            if any(any(c < 0 or c >= len(input) for c in coords) for coords in coords_on_path):
                continue

            letters_on_path = [input[_i, _j] for _i, _j in coords_on_path]
            if "".join(letters_on_path) == query:
                yield coords_on_path


def solve_part_1(raw_input):
    input = string_to_array(raw_input)
    xmases_found = list(find_straight_xmases(input))
    return len(xmases_found)


def find_x_mases(input):
    a_locs = zip(*numpy.where('A' == input))

    for i, j in a_locs:
        if i in (0, len(input) - 1) or j in (0, len(input) - 1):
            continue
        diag_1 = set((input[i + 1, j - 1], input[i - 1, j + 1]))
        diag_2 = set((input[i + 1, j + 1], input[i - 1, j - 1]))
        if diag_1 == {'M', 'S'} == diag_2:
            yield i, j


def solve_part_2(raw_input):
    input = string_to_array(raw_input)
    x_mases_found = list(find_x_mases(input))
    return len(x_mases_found)
