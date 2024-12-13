import re


def parse_xy(raw_button):
    m = re.match('.*: X=?(.*?), Y=?(.*)', raw_button)
    return tuple(int(xy) for xy in (m.group(1), m.group(2)))


class ClawMachine:
    def __init__(self, raw_input):
        raw_a, raw_b, raw_prize = raw_input.split('\n')

        self.xy_a = parse_xy(raw_a)
        self.xy_b = parse_xy(raw_b)
        self.xy_prize = parse_xy(raw_prize)
