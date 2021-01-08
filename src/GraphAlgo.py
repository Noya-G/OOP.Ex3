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
        except IOError:
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
                        node.set_position(0, 0, 0)
                    position = str(node.get_position()[0]) + "," + str(node.get_position()[1]) + "," + str(node.get_position()[2])
                    graph["Nodes"].append({'pos': position, "id": node.get_key()})

                file.write(json.dumps(graph))
                file.close()
                return True

        except OSError:
            print("File", file_name, " not found! ")
            return False

    def dijkstra(self, src: int, dest: int) -> (float, list):
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
    g.graph.add_edge(1,2,3)
    print("size of edgessss", g.graph.e_size())
    g.save_to_json("file2")
    g.load_from_json("A0")
    print(g.graph.edges)
