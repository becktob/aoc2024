import numpy


def string_to_array(content, dtype=numpy.uint8):
    lines = content.strip().split('\n')
    chars = [[c for c in l] for l in lines]
    return numpy.array(chars)


def find_xmases(input: numpy.ndarray[str]):
    query = 'XMAS'

    paths_todo = zip(*numpy.where(query[0] == input))

    paths_todo = [[coords] for coords in paths_todo]

    while paths_todo:
        path = paths_todo.pop(0)
        if len(path) == len(query):
            yield path
            continue

        next_letter = query[len(path)]
        tail = path[-1]

        next_letter_locations = zip(*numpy.where(next_letter == input))

        next_letter_neighbors = [loc for loc in next_letter_locations
                                 if abs(loc[0] - tail[0]) <= 1
                                 and abs(loc[1] - tail[1]) <= 1]

        for next_coord in next_letter_neighbors:
            path_todo = path + [next_coord]
            paths_todo.append(path_todo)
