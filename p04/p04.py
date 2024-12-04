import numpy


def string_to_array(content, dtype=numpy.uint8):
    lines = content.strip().split('\n')
    chars = [[c for c in l] for l in lines]
    return numpy.array(chars)


def find_xmases(input: numpy.ndarray[str]):
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
    curly_xmases = find_xmases(input)

    for curly in curly_xmases:
        first_delta = numpy.array(curly[1]) - curly[0]
        if all(all(numpy.array(n) - m == first_delta) for n, m in zip(curly[1:], curly[:-1])):
            yield curly


def solve_part_1(raw_input):
    input = string_to_array(raw_input)
    xmases_found = list(find_straight_xmases(input))
    return len(xmases_found)
