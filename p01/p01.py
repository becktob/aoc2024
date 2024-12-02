def report_is_good(levels: list[int]):
    deltas = [j - i for j,i in zip(levels[1:], levels[:-1])]

    deltas_small_enough = all(abs(d)<=3 for d in deltas)

    deltas_same_sign_and_nonzero = all(d < 0 for d in deltas) or all(d > 0 for d in deltas)

    return deltas_small_enough and deltas_same_sign_and_nonzero
