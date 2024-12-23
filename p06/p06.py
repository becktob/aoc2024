from copy import deepcopy

import numpy

from helpers import string_to_array

directions = {'^': (-1, 0),
              '>': (0, +1),
              'v': (+1, 0),
              '<': (0, -1)}

type State = tuple[tuple[int, int], str]


class Maze:
    def __init__(self, raw_input):
        maze = string_to_array(raw_input)
        self.shape = maze.shape
        self.walls = set(tuple(ij.tolist()) for ij in numpy.argwhere(maze == '#'))
        self.start = self._find_start(maze)

    def _find_start(self, maze) -> State:
        direction = next(filter(lambda d: d in maze, directions.keys()))
        position = numpy.argwhere(maze == direction)
        assert 1 == len(position)
        position = position[0]
        return (int(position[0]), int(position[1])), str(direction)


def one_step(maze: Maze, state: State = None) -> State | None:
    current_position, current_direction = state

    dir_ij = directions[current_direction]
    next_position = (current_position[0] + dir_ij[0], current_position[1] + dir_ij[1])
    if not all(0 <= ij < shape for ij, shape in zip(next_position, maze.shape)):
        return None

    if next_position not in maze.walls:  # forward
        return next_position, current_direction
    else:  # turn
        new_direction = direction_after_turn(current_direction)
        return current_position, new_direction


def direction_after_turn(current_direction):
    symbols = list(directions.keys())
    i = symbols.index(current_direction)
    new_direction = symbols[(i + 1) % len(symbols)]
    return new_direction


def solve_part_1(raw_input):
    maze = Maze(raw_input)

    _, visited_states = run(maze)

    visited_positions = set(state[0] for state in visited_states)
    return len(visited_positions)


def run(maze: Maze, previously_visited: list[State] | None = None) -> (bool, list[State]):
    visited = [state := maze.start]

    if previously_visited:
        visited = previously_visited
        state = visited[-1]

    visited_set = set(visited)

    while (state := one_step(maze, state)) is not None:
        if state in visited_set:
            return True, visited
        visited.append(state)
        visited_set.add(state)

    return False, visited


def is_loop(maze: Maze, previously_visited: list[State] = None):
    is_loop, visited = run(maze, previously_visited)
    return is_loop


def solve_part_2(raw_input):
    maze = Maze(raw_input)

    # only need to try blocking places visited by basic maze
    basic_maze = deepcopy(maze)
    _, visited_in_basic = run(basic_maze)

    looping_blocks = set()
    for n, state in enumerate(visited_in_basic):
        block, _ = state
        if block == maze.start:
            continue
        blocked_maze = deepcopy(maze)
        blocked_maze.walls.add(block)
        if is_loop(blocked_maze):  # Todo: why doesn't passing (..., visited_in_basic[:n]) work here?
            print(n, block)
            looping_blocks.add(block)

    return len(looping_blocks)
