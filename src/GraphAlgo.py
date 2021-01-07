from typing import List

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
import sys


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        graph_pointer = self.graph
        open(file_name, mode='r')

    def dijkstra(self, src: int, dest: int) -> (float, list):
        """
    function Dijkstra(Graph, source):

     create vertex set Q

     for each vertex v in Graph:
         dist[v] ← INFINITY
         prev[v] ← UNDEFINED
         add v to Q
      dist[source] ← 0

      while Q is not empty:
         u ← vertex in Q with min dist[u]

          remove u from Q

          for each neighbor v of u:           // only v that are still in Q
              alt ← dist[u] + length(u, v)
              if alt < dist[v]:
                 dist[v] ← alt
                  prev[v] ← u

      return dist[], prev[]
        :param src:
        :param dest:
        :return:
    """
        self.reset_nodes_tags()
        paths = {}
        container = []
        pointer = 0
        container.append(self.graph.get_node(src))
        paths[src] = 0
        container[0].set_tag(0)
        while pointer < len(container):
            node_pointer = container[pointer]
            src_key = node_pointer.get_key()
            node_neighbors = self.graph.all_out_edges_of_node(src_key)
            path_weight = paths[src_key]
            for i in range(0, len(node_neighbors)):
                dest_key = node_neighbors[i]
                edge_weight = self.graph.get_edge_weight(src_key, dest_key)
                node_pointer = self.graph.get_node(dest_key)
                if node_pointer.get_tag() == 0:
                    paths[dest_key] = edge_weight + path_weight
                    container.append(node_pointer)
                    node_pointer.set_tag(0)
            container[pointer].set_tag(1)
            node_pointer += 1

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass

    def reset_nodes_tags(self) -> None:
        i = 0
        while i < self.graph.v_size():
            nodes = self.graph.get_all_v()
            n_key = nodes[i]
            n = self.graph.get_node(n_key)
            n.set_tag(-1)
            i += 1
