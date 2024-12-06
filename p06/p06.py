import numpy

from helpers import string_to_array

directions = {'^': (-1, 0),
              '>': (0, +1),
              'v': (+1, 0),
              '<': (0, -1)}


def one_step(maze, current_position=None, current_direction=None):
    if current_position is None and current_direction is None:
        current_direction = next(filter(lambda d: d in maze, directions.keys()))
        current_position = numpy.argwhere(maze == current_direction)
        assert 1 == len(current_position)
        current_position = current_position[0]
    maze[*current_position] = 'X'  # may be overwritten on turn

    next_position = current_position + directions[current_direction]
    in_bounds = ((0, 0) <= next_position).all() and (next_position < maze.shape).all()
    if not in_bounds:
        return maze, None, None

    if maze[*next_position] != '#':  # forward
        maze[*next_position] = current_direction
        return maze, next_position, current_direction
    else:  # turn
        symbols = list(directions.keys())
        i = symbols.index(current_direction)
        new_direction = symbols[(i + 1) % len(symbols)]
        maze[*current_position] = new_direction
        return maze, current_position, new_direction


def solve(raw_input):
    maze = string_to_array(raw_input)

    maze, next_position, next_direction = one_step(maze, None)
    while next_position is not None:
        maze, next_position, next_direction = one_step(maze, next_position, next_direction)

    return len(numpy.argwhere(maze == 'X'))
