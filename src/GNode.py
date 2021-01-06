import sys


class GNode:

    def __init__(self, key):
        self.key = key
        self.info = ""
        self.weight = sys.maxsize
        self.pos = None
        self.tag = -1

    def get_key(self):
        return self.key

    def get_info(self):
        return self.info

    def get_weight(self):
        return self.weight

    def get_position(self):
        return self.pos

    def get_tag(self):
        return self.tag

    def set_key(self, key):
        self.key = key

    def set_position(self, x, y, z):
        self.pos = [x, y, z]

    def set_info(self, info):
        self.info = info

    def set_tag(self, tag):
        self.tag = tag

    def __repr__(self) -> str:
        return f"{self.key}"
