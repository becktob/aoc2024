import re


class Robot:
    def __init__(self, raw_line: str):
        m = re.match("p=(.*) v=(.*)", raw_line)
        self.p_xy = tuple(int(xy) for xy in m.group(1).split(','))
        self.v_xy = tuple(int(xy) for xy in m.group(2).split(','))
