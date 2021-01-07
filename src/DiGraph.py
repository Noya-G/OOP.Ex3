from src.GNode import GNode
from src.EdgeData import EdgeData
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.mc = 0
        self.edges = []
        self.vertices = {}
        self.income_adjacent = []
        self.outbound_adjacent = []

    def v_size(self) -> int:
        return len(self.vertices)

    def e_size(self) -> int:
        return len(self.edges)

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if weight < 0:
            return False
        if self.get_node(id1) is None or self.get_node(id2) is None:
            return False
        if self.get_node(id1) is None and self.get_node(id2) is None:
            return False
        i = 0
        while i < len(self.edges):
            p = self.edges[i]
            if p[0] == id1 and p[1] == id2:
                self.edges.remove((id1, id2, p[2]))
                self.edges.append((id1, id2, weight))
                self.mc += 1
                return True
            i += 1
        self.edges.append((id1, id2, weight))
        self.mc += 1

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.vertices:
            return False
        vertex = GNode(node_id)
        if pos is not None:
            vertex.set_position(pos[0], pos[1], pos[2])
        self.vertices[node_id] = vertex
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.vertices:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.vertices and node_id2 not in self.vertices:
            return False
        if node_id1 not in self.vertices or node_id2 not in self.vertices:
            return False
        if not self.has_edge(node_id1, node_id2):
            return False
        i = 0
        while i < len(self.edges):
            p = self.edges[i]
            if p[0] == node_id1 and p[1] == node_id2:
                self.edges.remove((node_id1, node_id2, p[2]))
                self.mc += 1
                return True
            i += 1

    def get_node(self, node_id: int) -> GNode:
        return self.vertices.get(node_id)

    def has_edge(self, src: int, dest: int) -> bool:
        i = 0
        while i < len(self.edges):
            p = self.edges[i]
            if p[0] == src and p[1] == dest:
                return True
            i += 1
        return False

    def all_out_edges_of_node(self, id1: int) -> dict:
        outgoing = []
        i = 0
        while i < len(self.edges):
            p = self.edges[i]
            if p[0] == id1:
                outgoing[i] = p[1]
            i += 1
        return dict.fromkeys(outgoing)

    def all_in_edges_of_node(self, id1: int) -> dict:
        pass

    def get_all_v(self) -> dict:
        return self.vertices

    def get_edge(self, src: int, dest: int) -> float:
        # for later!!!!!
        pass


if __name__ == '__main__':
    g1 = DiGraph()
    g = GNode(2)
    g.set_position(1, 2, 3)
    g1.add_node(g.get_key(), g.get_position())
    # print(g1.get_node(2).get_position())
    g1.add_node(3, (1, 2, 3))
    g1.add_node(4)
    g1.add_edge(2, 3, 1.1)
    g1.add_edge(2, 4, 1)
    print(g1.has_edge(2, 3))
    # g1.add_node(600)
    g1.add_node(200)
    print("before changes: ", g1.edges)
    g1.add_edge(2, 4, 4)
    g1.remove_edge(5, 6)
    print("after changes: ", g1.edges)
    print(g1.all_in_edges_of_node(2))
