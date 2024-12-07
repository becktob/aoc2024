import operator


def can_make_true(result: int, operands: list[int]):
    possible_operators = (operator.add, operator.mul)
    possible_results = [op(*operands)
                        for op in possible_operators]
    return any(result == r for r in possible_results)
