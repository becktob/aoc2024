class DiskMap:
    def __init__(self, line: str):
        file_lengths = line[::2]
        free_lengths = line[1::2]
        self.files = {id: int(size) for id, size in enumerate(file_lengths)}
        self.free = {id: int(size) for id, size in enumerate(free_lengths)}

    def __repr__(self):
        disk_repr = [None] * (len(self.free) + len(self.files))

        disk_repr[::2] = [str(id) * size for id, size in self.files.items()]
        disk_repr[1::2] = ['.' * size for id, size in self.free.items()]

        return "".join(disk_repr)
