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


def solve_part_1(raw_input):
    maze = string_to_array(raw_input)

    maze, _ = run(maze)

    return len(numpy.argwhere(maze == 'X'))


def run(maze):
    maze, next_position, next_direction = one_step(maze, None)

    visited = set()

    while next_position is not None:
        state = tuple(next_position.tolist()), next_direction
        if state in visited:
            return maze, True
        visited.add(state)

        maze, next_position, next_direction = one_step(maze, next_position, next_direction)

    return maze, False

def is_loop(maze):
    maze, is_loop = run(maze)
    return is_loop

def solve_part_2(raw_input):
    maze = string_to_array(raw_input)

    # only need to try blocking places visited by basic maze
    basic_maze = maze.copy()
    basic_run, *_ = run(basic_maze)
    visited_in_basic = numpy.argwhere(basic_run == 'X')

    looping_blocks = []
    for n, block in enumerate(visited_in_basic):
        if maze[*block] in directions.keys():
            continue
        blocked_maze = maze.copy()
        blocked_maze[*block] = '#'
        if is_loop(blocked_maze):
            print(n, block)
            looping_blocks.append(block)

    return len(looping_blocks)

