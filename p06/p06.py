import numpy


def one_step(maze):
    directions = {'^': (-1, 0),
                  '>': (0, +1),
                  'v': (+1, 0),
                  '<': (0, -1)}
    current_direction = next(filter(lambda d: d in maze, directions.keys()))
    current_position = numpy.argwhere(maze == current_direction)
    assert 1 == len(current_position)
    current_position = current_position[0]

    next_position = current_position + directions[current_direction]
    if maze [*next_position] != '#':  # forward
        maze[*next_position] = current_direction
        maze[*current_position] = 'X'
    else:  # turn
        symbols = list(directions.keys())
        i = symbols.index(current_direction)
        maze[*current_position] = symbols[(i + 1) % len(symbols)]
    return maze
