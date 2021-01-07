from src.GNode import GNode
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    """DiGraph - directed weighted graph data structure implemented by the given GraphInterface api"""

    def __init__(self):
        self.mc = 0
        self.edges = []
        self.vertices = {}

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.vertices)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return len(self.edges)

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
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
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        if node_id in self.vertices:
            return False
        vertex = GNode(node_id)
        if pos is not None:
            vertex.set_position(pos[0], pos[1], pos[2])
        self.vertices[node_id] = vertex
        self.mc += 1
        return True

    def get_edge_weight(self, src: int, dest: int) -> float:
        i = 0
        while i < self.e_size():
            e_p = self.edges[i]
            if e_p[0] == src and e_p[1] == dest:
                return e_p[2]
            i += 1
        return -1

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if node_id not in self.vertices:
            return False
        i = 0
        while i < self.e_size():
            p = self.edges[i]
            if node_id == p[0]:
                self.remove_edge(node_id, p[1])
            i += 1
        i = 0
        while i < self.e_size():
            p = self.edges[i]
            if node_id == p[1]:
                self.remove_edge(node_id, p[0])
            i += 1
        self.vertices.__delitem__(node_id)
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
         Removes an edge from the graph.
         @param node_id1: The start node of the edge
         @param node_id2: The end node of the edge
         @return: True if the edge was removed successfully, False o.w.

         Note: If such an edge does not exists the function will do nothing
         """
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
        """
        A method that returns a GNode object by given a specific node
        :param node_id:
        :return GNode:
        """
        return self.vertices.get(node_id)

    def has_edge(self, src: int, dest: int) -> bool:
        """
        A method that check if there's an edge from source to dest
        :param src:
        :param dest:
        :return bool:
        """
        i = 0
        while i < len(self.edges):
            p = self.edges[i]
            if p[0] == src and p[1] == dest:
                return True
            i += 1
        return False

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        outgoing = []
        i = 0
        while i < len(self.edges):
            p = self.edges[i]
            if id1 == p[0]:
                outgoing.append(p[1])
            i += 1
        dict_of_edges = {i: outgoing[i] for i in range(0, len(outgoing))}
        return dict_of_edges

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        incoming = []
        i = 0
        while i < len(self.edges):
            p = self.edges[i]
            if id1 == p[1]:
                incoming.append(p[0])
            i += 1
        dict_of_edges = {i: incoming[i] for i in range(0, len(incoming))}
        return dict_of_edges

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        return self.vertices

    def __repr__(self) -> str:

        graph_info = f"Graph: |V|={self.v_size()} , |E|={self.e_size()}\n"
        graph_info += "{"
        i = 0
        for j in self.vertices.keys():
            i += 1
            graph_info += f"{j}: {j}: |edges out| "
            graph_info += f"{len(self.all_out_edges_of_node(j).keys())} "
            graph_info += "|edges in| "
            graph_info += f"{len(self.all_in_edges_of_node(j).keys())}"

            if len(self.vertices.keys()) == i:
                graph_info += "}"
            else:
                graph_info += ", "
        return graph_info
