from helpers import string_to_array


class Warehouse:
    def __init__(self, map_string: str):
        self.map = string_to_array(map_string)


def parse(raw_input) -> (Warehouse, list[str]):
    raw_warehouse, raw_commands = raw_input.split('\n\n')
    return Warehouse(raw_warehouse), list(raw_commands.strip())
