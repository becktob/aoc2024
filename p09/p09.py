import itertools


class DiskMap:
    def __init__(self, line: str):
        file_lengths = line[::2]
        free_lengths = line[1::2]
        self.files = {id: int(size) for id, size in enumerate(file_lengths)}
        self.free = {id: int(size) for id, size in enumerate(free_lengths)}

        blocks = [None] * (len(self.free) + len(self.files))
        file_content = [[id] * size for id, size in self.files.items()]
        free_content = [[None] * size for size in self.free.values()]
        blocks[::2] = file_content
        blocks[1::2] = free_content

        self.disk = [val for block in blocks for val in block]

    def __repr__(self):
        disk_repr = ['.' if d is None else str(d) for d in self.disk]

        return "".join(disk_repr)

    def compact_one_step(self):
        first_free = self.disk.index(None)
        last_used = 1 + sum(1 for _ in itertools.takewhile(lambda i: i is None, self.disk[::-1]))
        self.disk[first_free] = self.disk[-last_used]
        self.disk[-last_used] = None
