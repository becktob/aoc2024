type Key = tuple[int, int, int, int, int]
type Lock = tuple[int, int, int, int, int]


def parse_locks_keys(raw_input: str) -> (list[Key], list[Lock]):
    raw_lock_keys = raw_input.split('\n\n')

    raw_locks = [block for block in raw_lock_keys if block[0] == '#']
    raw_keys = [block for block in raw_lock_keys if block[0] == '.']

    def count_hash_columwise(lines: str):
        columns = zip(*lines.splitlines())
        return tuple(sum(1 for c in col[1:-1] if c == '#') for col in columns)

    locks = [count_hash_columwise(raw) for raw in raw_locks]
    keys = [count_hash_columwise(raw) for raw in raw_keys]

    return locks, keys


def fit(key: Key, lock: Lock) -> bool:
    return all(k + l <= 5 for k, l in zip(key, lock))
