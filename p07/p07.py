import itertools
import operator


def can_make_true(result: int, operands: list[int]):
    possible_operators = (operator.add, operator.mul)

    operator_combinations = itertools.product(
        possible_operators,
        repeat=len(operands) - 1)

    possible_results = [apply(ops, operands) for ops in operator_combinations]
    return any(result == r for r in possible_results)


def apply(ops, operands):
    acc = operands[0]
    for op, operand in zip(ops, operands[1:]):
        acc = op(acc, operand)
    return acc
