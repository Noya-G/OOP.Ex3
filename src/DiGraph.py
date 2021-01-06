from src.GNode import GNode
from src.EdgeData import EdgeData
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.mc = 0
        self.edges = []
        self.vertices = {}
        self.income_adjacent = {}
        self.outbound_adjacent = {}

    def v_size(self) -> int:
        return len(self.vertices)

    def e_size(self) -> int:
        return len(self.edges)

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if weight < 0:
            return False

        if id1 == id2:
            return False

        if self.get_node(id1) is None or self.get_node(id2) is None:
            return False

        if self.get_node(id1) is None and self.get_node(id2) is None:
            return False

        # if self.has_edge(id1, id2):
        #     return False

        # self.edges[id1][id2] = weight
        self.income_adjacent[id2] = id1
        self.outbound_adjacent[id1] = id2
        self.mc += 1

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.vertices:
            return False
        vertex = GNode(node_id)
        if pos is not None:
            vertex.set_position(pos[0], pos[1], pos[2])
        self.vertices[node_id] = vertex
        self.outbound_adjacent[node_id] = {}
        self.income_adjacent[node_id] = {}
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.vertices:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if not self.has_edge(node_id1, node_id2):
            return False

    def get_node(self, node_id: int) -> GNode:
        return self.vertices.get(node_id)

    def has_edge(self, src: int, dest: int) -> bool:
        if src in self.income_adjacent[dest] and src in self.outbound_adjacent[dest] and \
                dest in self.income_adjacent[src]:
            return True
        return False

    def all_out_edges_of_node(self, id1: int) -> dict:
        pass

    def all_in_edges_of_node(self, id1: int) -> dict:
        pass

    def get_all_v(self) -> dict:
        return self.vertices


