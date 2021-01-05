class EdgeData:

    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def __repr__(self):
        return "(src: {}, dest: {}, weight: {})".format(self.src, self.dest, self.weight)



