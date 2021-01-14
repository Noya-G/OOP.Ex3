import json
from random import random

import matplotlib.pyplot as plt
from typing import List

from src.DiGraph import DiGraph
from src.GNode import GNode
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    """
 *  1) This class represents a Graph-Theory Algorithms on a directed weighted graph that is based on the given
 *     GraphAlgoInterface api.
 *
 *  2) This class and the algorithm is based on a Tree data structure
 *
 * This class contains all the requested methods:
 *              - get_graph
 *              - load
 *              - load_from_json
 *              - save_to_json
 *              - shortestPath
 *              - connected_component
 *              - connected_component by given a vertex
 *              - plot_graph
 *
 * Dijkstra's Shortest-Path algorithm:
 *
 *
 * function Dijkstra(Graph,source):
 *
 *   	create vertex set Q
 *
 *   	for each vertex v in Graph:		//Initialization
 *   		dist[v] <- INFINITY		//Unknown distance from source to V
 *   		prev[v] <- UNDEFINED		//Previous node in optimal path from source
 *   		add v to Q			//All nodes initially in Q (unvisited nodes)
 *
 *      dist[source] <- 0			//Distance from source to source
 *
 *   	while Q is not empty:
 *   		u <- vertex in Q with min dist[u] //Source node will be selected first
 *   		remove u from Q
 *
 *
 *   		for each neighbor v of u:        // where v is still in Q
 *   			alt <- dist[u] + length(u,v)
 *   			if alt < dist[v]:	 // A shorter path to v has been found
 *   			dist[v] <- alt
 *   			prev[v] <- u
 *
 *   	return dist[], prev[]
    """

    def __init__(self, graph: DiGraph = None):
        """
            init method
        :param graph:
        """
        if graph is None:
            self.graph = DiGraph()
        else:
            self.graph = graph

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
                        position = str(node.get_position()[0]) + "," + str(node.get_position()[1]) + "," + str(
                            node.get_position()[2])
                        graph["Nodes"].append({'pos': position, "id": node.get_key()})

                file.write(json.dumps(graph))
                file.close()
                return True

        except OSError:
            print("File", file_name, " not found! ")
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through

        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        if id1 not in self.graph.vertices or id2 not in self.graph.vertices:
            return float('inf'), []
        if id1 == id2:
            return 0, [id1]
        ans = self.dijksytra_algo(id1, id2)
        return ans

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        based on two helping functions below and compare them
        @param id1: The node id
        @return: The list of nodes in the SCC

        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        component_original = self.connected_component_aid_original_geph(id1)
        component_revers = self.connected_component_aid_reverse_geph(id1)
        container = []
        for k in component_original:
            for m in component_revers:
                if k == m:
                    if k not in container:
                        container.append(k)
                        self.graph.get_node(k).set_info("in")
        container.sort()
        return container

    def connected_component_aid_original_geph(self, id1):
        """
        A method that helps us in connected components by a given node.
        gets all keys tags of every nodes that are connected to the id1 node
        :param id1:
        :return: container
        """
        self.reset_nodes_tags()
        container = []
        pointer = 0
        container.append(id1)
        while pointer < len(container):
            key = container[pointer]
            node_neighbors = self.graph.all_out_edges_of_node(key)
            for m in range(0, len(node_neighbors)):
                neighbor_key = list(node_neighbors.keys())[m]
                node_pointer = self.graph.get_node(neighbor_key)
                if node_pointer.get_tag() == -1:
                    container.append(neighbor_key)
                    node_pointer.set_tag(1)
            pointer += 1
        return container

    def connected_component_aid_reverse_geph(self, id1):
        """
        A method that helps us in connected components by a given node.
        gets all keys tags of every nodes that are connected to the id1 node but the only
        change is that the function reverse the graph
        :param id1:
        :return: container
        """
        self.reset_nodes_tags()
        container = []
        pointer = 0
        container.append(id1)
        while pointer < len(container):
            key = container[pointer]
            node_neighbors = self.graph.all_in_edges_of_node(key)
            for m in range(0, len(node_neighbors)):
                neighbor_key = list(node_neighbors.keys())[m]
                node_pointer = self.graph.get_node(neighbor_key)
                if node_pointer.get_tag() == -1:
                    container.append(neighbor_key)
                    node_pointer.set_tag(1)
            pointer += 1
        return container

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        check each vertex on the connected_components by given a node
        @return: The list all SCC

        Notes:
        If the graph is None the function should return an empty list []
        """
        self.reset_nodes_info()
        ans = []
        graph_nodes = self.graph.get_all_v()
        for n in graph_nodes:
            if self.graph.get_node(n).get_info() != "in":
                mid_ans = self.connected_component(n)
                ans.append(mid_ans)
        return ans

    def reset_nodes_info(self) -> None:
        """
        Aid function that walks all over the graph and reset each node's info
        :return: None
        """
        for k in self.graph.get_all_v():
            self.graph.get_node(k).set_info("")

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        self.reset_nodes_tags()
        x = []
        y = []
        key = []
        graph_vertex = self.graph.get_all_v()
        for i in graph_vertex:
            node_pointer = self.graph.get_node(i)
            pos = node_pointer.get_position()
            if pos is None:
                node_pointer.set_position(random() * 434, random() * 35, 0)
            pos = node_pointer.get_position()
            x.append(pos[0])
            y.append(pos[1])
            key.append(i)
        fig, ax = plt.subplots()
        ax.scatter(x, y)

        for i in self.graph.edges:
            src = self.graph.get_node(i[0])
            dest = self.graph.get_node(i[1])
            src_x = src.get_position()[0]
            src_y = src.get_position()[1]
            dest_x = dest.get_position()[0]
            dest_y = dest.get_position()[1]
            x_list = [src_x, dest_x]
            y_list = [src_y, dest_y]
            ax.annotate("", xy=(dest_x, dest_y), xytext=(src_x, src_y), arrowprops=dict(arrowstyle="->"), color="RED")
            plt.plot(x_list, y_list, color="CYAN")
        for i, txt in enumerate(key):
            ax.annotate(key[i], (x[i], y[i]), color="BLUE")
        plt.title("Directed Weighted Graph - graph visualization")
        plt.show()

    def reset_nodes_tags(self) -> None:
        """
        Aid function that walks all over the graph and reset each node's tag
        :return: None
        """
        for k in self.graph.get_all_v():
            self.graph.get_node(k).set_tag(-1)

    def dijksytra_algo(self, src, dest) -> (float, list):
        """
        Dijkstra's shortest path algorithm (mentioned above) that is being implemented
        :param src:
        :param dest:
        :return: (float, list)
        """
        self.reset_nodes_tags()
        paths = {}
        container = []
        pointer = 0
        container.append(self.graph.get_node(src))
        paths[src] = 0
        container[0].set_tag(0)
        # create a dictionary, a list a variable, put inside the list the src node and resets everything created
        while pointer < len(container):
            node_o_pointer = container[pointer]
            src_key = node_o_pointer.get_key()
            node_neighbors = self.graph.all_out_edges_of_node(src_key)
            path_weight = paths[src_key]
            for k in range(0, len(node_neighbors)):
                # walks over the node neighbors
                dest_key = list(node_neighbors.keys())[k]
                edge_weight = self.graph.get_edge_weight(src_key, dest_key)
                node_pointer = self.graph.get_node(dest_key)
                tag = node_pointer.get_tag()
                if tag != -1:
                    # checks if the node is visited
                    new_path = path_weight + edge_weight
                    if new_path < paths[dest_key]:
                        paths[dest_key] = new_path
                if node_pointer.get_tag() == -1:
                    # checks if the node is unvisited
                    container.append(node_pointer)
                    paths[dest_key] = path_weight + edge_weight
                    node_pointer.set_tag(0)
            node_o_pointer.set_tag(1)
            pointer += 1
        if dest not in paths:
            # if didn't find destination node in paths list
            return float('inf'), []
        ans = []
        pointer = 0
        key = dest
        ans.append(key)
        while src not in ans and pointer < len(ans):
            key_pointer = ans[pointer]
            path_key = paths[key_pointer]
            key_neighbors = self.graph.all_in_edges_of_node(key_pointer)
            for l in key_neighbors:
                if l in paths:
                    path_n = paths[l]
                    e_b = self.graph.get_edge_weight(l, key_pointer)
                    if round(e_b + path_n, 7) == round(path_key, 7):
                        ans.append(l)
                        break
            pointer += 1
        return paths[dest], ans


