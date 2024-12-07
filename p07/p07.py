import itertools
import operator


def can_make_true(result: int, operands: list[int], possible_operators = None):
    if possible_operators is None:
        possible_operators = (operator.add, operator.mul)

    operator_combinations = itertools.product(
        possible_operators,
        repeat=len(operands) - 1)

    possible_results = (apply(ops, operands) for ops in operator_combinations)
    return any(result == r for r in possible_results)


def apply(ops, operands):
    acc = operands[0]
    for op, operand in zip(ops, operands[1:]):
        acc = op(acc, operand)
    return acc


class Equation:
    def __init__(self, line: str):
        raw_result, raw_operands = line.split(':')
        self.result = int(raw_result)
        self.operands = [int(n) for n in raw_operands.split()]


def solve_part_1(raw_input: str):
    equations = [Equation(line) for line in raw_input.splitlines()]

    true_able = [eq for eq in equations if can_make_true(eq.result, eq.operands)]

    return sum(eq.result for eq in true_able)

def solve_part_2(raw_input: str):
    equations = [Equation(line) for line in raw_input.splitlines()]

    possible_operators = (operator.add,
                          operator.mul,
                          lambda a, b: 10**len(str(b))*a + b)

    true_able = [eq for eq in equations if can_make_true(eq.result, eq.operands, possible_operators)]

    return sum(eq.result for eq in true_able)
