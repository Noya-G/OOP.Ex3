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
        https://www.geeksforgeeks.org/read-json-file-using-python/

        :param file_name:
        :return:
        """
        try:
            with open(file_name, 'r') as file_n:
                g_s = file_n.read()
                json_graph = json.loads(g_s)
            for m in json_graph['Nodes']:
                key = m.get("id")
                pos = m.get("pos")
                if "pos" not in m:
                    node = GNode(key)
                    key = node.get_key()
                    self.graph.add_node(key)
                else:
                    node = GNode(key)
                    key = node.get_key()
                    self.graph.add_node(key)
                    position = tuple((float, m['pos'].split(',')))
                    self.graph.add_node(key, position)
            for k in json_graph['Edges']:
                src = int(k.get('src'))
                w = float(k.get('w'))
                dst = int(k.get('dest'))
                self.graph.add_edge(src, dst, w)
            file_n.close()
            return True
        except OSError:
            print("File does not exist!\n")
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        A method that saves the current graph into json file.
        in order to implement the function we used the previous assignment's code
        plus:

        https://www.w3schools.com/python/python_try_except.asp
        https://www.geeksforgeeks.org/saving-text-json-and-csv-to-a-file-in-python/
        :param file_name:
        :return: boolean
        """
        try:
            with open(file_name, 'w') as file:
                graph = {"Edges": [], "Nodes": []}
                for k in self.graph.edges:
                    graph["Edges"].append({"src": k[0], "w": k[2], "dest": k[1]})

                for j in self.graph.vertices:
                    node = self.graph.get_node(j)
                    if node.get_position() is None:
                        graph["Nodes"].append({"id": node.get_key()})
                    else:
                        position = str(node.get_position()[0]) + "," + str(node.get_position()[1]) + "," + str(node.get_position()[2])
                        graph["Nodes"].append({'pos': position, "id": node.get_key()})

                file.write(json.dumps(graph))
                file.close()
                return True

        except OSError:
            print("File", file_name, " not found! ")
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        self.reset_nodes_tags()
        container = []
        pointer = 0
        container.append(id1)
        while pointer < len(container):
            key = container[pointer]
            node_neighbors = self.graph.all_out_edges_of_node(key)
            for m in node_neighbors:
                neighbor_key = node_neighbors[m]
                node_pointer = self.graph.get_node(neighbor_key)
                if node_pointer.get_tag() == -1:
                    container.append(neighbor_key)
                    node_pointer.set_tag(1)
            pointer += 1
        return container

    def connected_components(self) -> List[list]:
        ans = []
        graph_nodes = self.graph.get_all_v()
        for n in graph_nodes:
            ans.append(self.connected_component(n))
        return ans

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

    def dijksytra_algo(self, src, dest) -> (float, list):

        self.reset_nodes_tags()
        ans = []
        paths = {}
        container = []
        pointer = 0
        container.append(self.graph.get_node(src))
        paths[src] = 0
        container[0].set_tag(0)
        while pointer < len(container):
            node_o_pointer = container[pointer]
            src_key = node_o_pointer.get_key()
            node_neighbors = self.graph.all_out_edges_of_node(src_key)
            path_weight = paths[src_key]
            for k in range(0, len(node_neighbors)):
                dest_key = node_neighbors[k]
                edge_weight = self.graph.get_edge_weight(src_key, dest_key)
                node_pointer = self.graph.get_node(dest_key)
                minus_1 = -1
                tag = node_pointer.get_tag()
                if node_pointer.get_tag() == 0:
                    if path_weight + edge_weight < paths[dest_key]:
                        paths[dest_key] = path_weight + edge_weight
                else:
                    container.append(node_pointer)
                    paths[dest_key] = path_weight + edge_weight
                    node_pointer.set_tag(0)
            node_o_pointer.set_tag(1)
            pointer += 1
        ans.append(dest)
        pointer = 0
        key = dest
        while src not in ans:
            key = ans[pointer]
            w1 = paths[key]
            for l in paths:
                w2 = paths[l]
                w_e = self.graph.get_edge_weight(l, key)
                if w_e is not None:
                    if w2 + w_e is w1:
                        key = l
                        ans.append(l)
            pointer += 1
        return paths[dest_key], ans


if __name__ == '__main__':
    g = GraphAlgo()
    i = 0
    while i < 6:
        g.graph.add_node(i)
        i += 1

    g.graph.add_edge(0, 1, 5)
    g.graph.add_edge(0, 2, 3)
    g.graph.add_edge(1, 3, 6)
    g.graph.add_edge(1, 2, 2)
    g.graph.add_edge(2, 4, 4)
    g.graph.add_edge(2, 5, 2)
    g.graph.add_edge(2, 3, 7)
    g.graph.add_edge(3, 4, -1)
    g.graph.add_edge(4, 5, -2)





