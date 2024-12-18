class Ram:
    def __init__(self, raw_input: str):
        self.corrupted = [(int(xy) for xy in l.split(',')) for l in raw_input.splitlines()]
        self.size = max(xy for c in self.corrupted for xy in c)
