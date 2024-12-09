import itertools


class DiskMap:
    def __init__(self, line: str):
        file_lengths = line[::2]
        free_lengths = line[1::2]
        self.files = {id: int(size) for id, size in enumerate(file_lengths)}
        self.free = {id: int(size) for id, size in enumerate(free_lengths)}

        self.generate_disk()

    def generate_disk(self):
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
        last_used = sum(1 for _ in itertools.takewhile(lambda i: i is None, self.disk[::-1]))
        self.disk[first_free] = self.disk[-1 - last_used]
        self.disk[-1 - last_used] = None

    def compact_all(self):
        while not self.is_compact():
            self.compact_one_step()

    def is_compact(self):
        last_used = sum(1 for _ in itertools.takewhile(lambda i: i is None, self.disk[::-1]))
        free_count = self.disk.count(None)
        return last_used == free_count

    def checksum(self):
        return sum(pos * id for pos, id in enumerate(self.disk) if id is not None)


def solve_part_1(raw_input: str):
    map = DiskMap(raw_input.strip())
    map.compact_all()
    return map.checksum()


class File:
    def __init__(self, id, size, pos):
        self.id = id
        self.size = size
        self.pos = pos


class DiskMap2:
    def __init__(self, line: str):
        self.free_by_pos = dict()  # TODO: naming?
        self.files_by_pos = dict()
        is_file = True
        total_pos = 0
        file_id = 0
        for block_len in line:
            block_len = int(block_len)
            if is_file:
                self.files_by_pos.update({total_pos: File(file_id, block_len, total_pos)})
                file_id += 1
            else:
                self.free_by_pos.update({total_pos: block_len})

            is_file = not is_file
            total_pos += block_len

    def generate_disk(self):
        disk = [-1] * (sum(self.free_by_pos.values()) + sum(f.size for f in self.files_by_pos.values()))

        for pos, file in self.files_by_pos.items():
            disk[pos: pos + file.size] = [file.id] * file.size

        for pos, len in self.free_by_pos.items():
            disk[pos: pos + len] = [None] * len

        return disk

    def __repr__(self):
        disk = self.generate_disk()
        disk_repr = ['.' if d is None else chr(d+ord('0')) for d in disk]

        return "".join(disk_repr)

    def compact_all(self):
        files = list(self.files_by_pos.values())
        files.sort(key=lambda f: f.id, reverse=True)
        for file in files:
            free_items = list(self.free_by_pos.items())
            free_items.sort(key=lambda item: item[0])
            try:
                free_before = next((pos, l) for pos, l in free_items if pos < file.pos and l >= file.size)
            except StopIteration:
                continue

            pos_free, len_free = free_before

            remaining_free_size = len_free - file.size
            remaining_free_pos = pos_free + file.size
            self.free_by_pos.pop(pos_free)  # remove old free
            self.free_by_pos.update({remaining_free_pos: remaining_free_size})  # add remaining free
            # TODO: consolidate neighboring free blocks into one (not necessary for single pass?)

            self.files_by_pos.pop(file.pos)  # remove file
            self.free_by_pos.update({file.pos: file.size})  # replace file with free
            file.pos = pos_free
            self.files_by_pos.update({pos_free: file})  # insert file

    def checksum(self):
        disk = self.generate_disk()
        return sum(pos * id for pos, id in enumerate(disk) if id is not None)


def solve_part_2(raw_input):
    map = DiskMap2(raw_input.strip())
    map.compact_all()
    return map.checksum()
