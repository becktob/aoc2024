import numpy

from helpers import string_to_array, in_bounds

directions = {'^': (-1, 0),
              '>': (0, +1),
              'v': (+1, 0),
              '<': (0, -1)}

type State = tuple[tuple[int, int], str]


def one_step(maze, state: State = None) -> (numpy.ndarray, State):
    current_position, current_direction = state
    maze[*current_position] = 'X'  # may be overwritten on turn

    dir_ij = directions[current_direction]
    next_position = (current_position[0] + dir_ij[0], current_position[1] + dir_ij[1])
    if not in_bounds(numpy.array(next_position), maze):
        return maze, None

    if maze[*next_position] != '#':  # forward
        maze[*next_position] = current_direction
        return maze, (next_position, current_direction)
    else:  # turn
        new_direction = direction_after_turn(current_direction)
        maze[*current_position] = new_direction
        return maze, (current_position, new_direction)


def find_start(maze) -> State:
    direction = next(filter(lambda d: d in maze, directions.keys()))
    position = numpy.argwhere(maze == direction)
    assert 1 == len(position)
    position = position[0]
    return (int(position[0]), int(position[1])), str(direction)


def direction_after_turn(current_direction):
    symbols = list(directions.keys())
    i = symbols.index(current_direction)
    new_direction = symbols[(i + 1) % len(symbols)]
    return new_direction


def solve_part_1(raw_input):
    maze = string_to_array(raw_input)

    maze, _ = run(maze)

    return len(numpy.argwhere(maze == 'X'))


def run(maze):
    start_state = find_start(maze)
    maze, next_state = one_step(maze, start_state)

    visited = set()

    while next_state is not None:
        if next_state in visited:
            return maze, True
        visited.add(next_state)

        maze, next_state = one_step(maze, next_state)

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
