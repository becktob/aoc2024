def report_is_good(levels: list[int]):
    deltas = [j - i for j,i in zip(levels[1:], levels[:-1])]

    differences_small_enough = all(abs(d)<=3 for d in deltas)

    return differences_small_enough