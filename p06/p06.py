import numpy

from helpers import string_to_array

directions = {'^': (-1, 0),
              '>': (0, +1),
              'v': (+1, 0),
              '<': (0, -1)}


def one_step(maze):
    current_direction = next(filter(lambda d: d in maze, directions.keys()))
    current_position = numpy.argwhere(maze == current_direction)
    assert 1 == len(current_position)
    current_position = current_position[0]
    maze[*current_position] = 'X'  # may be overwritten on turn

    next_position = current_position + directions[current_direction]
    in_bounds = ((0, 0) <= next_position).all() and (next_position < maze.shape).all()
    if not in_bounds:
        pass
    elif maze[*next_position] != '#':  # forward
        maze[*next_position] = current_direction
    else:  # turn
        symbols = list(directions.keys())
        i = symbols.index(current_direction)
        maze[*current_position] = symbols[(i + 1) % len(symbols)]
    return maze


def solve(raw_input):
    maze = string_to_array(raw_input)

    while any(d in maze for d in directions.keys()):
        maze = one_step(maze)

    return len(numpy.argwhere(maze == 'X'))
