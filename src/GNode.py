import sys


class GNode:

    def __init__(self, key):
        self.key = key
        self.info = ""
        self.weight = sys.maxint
        self.position = None
        self.tag = -1;

    def get_key(self):
        return self.key

    def get_info(self):
        return self.info;

    def get_weight(self):
        return self.weight

    def get_position(self):
        return self.position

    def get_tag(self):
        return self.tag

    def set_key(self, key):
        self.key = key

    def set_position(self, position):
        self.position = position

    def set_info(self, info):
        self.info = info

    def set_tag(self, tag):
        self.tag = tag
