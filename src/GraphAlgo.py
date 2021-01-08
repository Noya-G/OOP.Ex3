import json
from typing import List

from DiGraph import DiGraph
from GNode import GNode
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
        """
        A method that loads the current graph from a json file.
        in order to implement the function we used the previous assignment's code
        plus:
        https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/
        https://www.w3schools.com/python/python_try_except.asp
        https://www.geeksforgeeks.org/saving-text-json-and-csv-to-a-file-in-python/
        :param file_name:
        :return:
        """
        if self.graph is None:
            return False
        try:
            file_n = open(file_name, 'r')
            json_graph = json.loads(file_n.read())
            for i in json_graph['Edges']:
                src = int(i['src]'])
                w = float(i['w'])
                dst = int(i['dest'])
                self.graph.add_edge(src, dst, w)

            for i in json_graph['Node']:
                node = GNode(i['id'])
                position = tuple((float, i['pos'].split(',')))
                self.graph.add_node(node.get_key(), position)
            file_n.close()
            return True
        except OSError:
            print("File does not exist!\n")
            return False

    # def save_to_json(self, file_name: str) -> bool:
    #     """
    #     A method that saves the current graph into json file.
    #     in order to implement the function we used the previous assignment's code
    #     plus:
    #     https://www.geeksforgeeks.org/read-json-file-using-python/
    #     https://www.w3schools.com/python/python_try_except.asp
    #
    #     :param file_name:
    #     :return: boolean
    #     """
    #     try:
    #         with open(file_name, 'w') as file:
    #             graph = {"Edges": [], "Nodes": []}
    #             for k in self.graph.edges:
    #                 graph['Edges'].append({'src': k[0], 'w': k[2], 'dest': k[1]})
    #
    #             for j in self.graph.vertices:
    #                 node = self.graph.get_node(j)
    #                 if node.get_position() is None:
    #                     position = "0,0,0"
    #                 else:
    #                     position = str(node.get_position()[0]) + "," + str(node.get_position()[2]) + "," + str(
    #                         node.get_position()[1])
    #                 d = {"pos:", position, "id:", node.get_key()}
    #                 graph['Nodes'].append(d)
    #                 # graph['Nodes'].append("{pos:" + position, "id:" + node.get_key() + "}"
    #                 # graph['Nodes'].append("{\"pos\":" + str(
    #                 #     node.get_position()[0] + "," + str(node.get_position()[1]) + "," + str(
    #                 #         node.get_position()[2])) +
    #                 #                       "\"id\":" + node.get_key() + "}")
    #             str_graph = json.dumps(graph, indent=4)
    #             file.write(str_graph)
    #             return True
    #     except OSError:
    #         print("Error, can't save file")
    #         return False

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

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass

    def reset_nodes_tags(self) -> None:
        """
        Aid function that walks all over the graph and reset each node's tag
        :return: None
        """
        i = 0
        while i < self.graph.v_size():
            nodes = self.graph.get_all_v()
            n_key = nodes[i]
            n = self.graph.get_node(n_key)
            n.set_tag(-1)
            i += 1


if __name__ == '__main__':
    g = GraphAlgo()
    i = 0
    while i < 5:
        g.graph.add_node(i)
        i += 1

    while i < 4:
        g.graph.add_edge(i, i + 1, 2.5)
        i += 1

    g.save_to_json("file")
