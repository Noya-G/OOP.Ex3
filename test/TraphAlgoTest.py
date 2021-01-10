import unittest

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def generate_graph(self, v) -> DiGraph():
        i = 0
        g = DiGraph()
        while i < v:
            g.add_node(i)
            i += 1
        return g

    def test_GET_GRAPH(self):
        g = self.generate_graph(5)
        # create a graph
        g_algo = GraphAlgo(g)
        # init graph in graph algo object
        self.assertEqual(g_algo.get_graph(), g)
        # verify graph and graph within graph algo are the same

        g_algo_b = GraphAlgo()
        # make graph algo object
        self.assertIsNotNone(g_algo_b)
        # verify new empty graph algo isn't none

    def test_LOAD_SAVE(self):
        g = self.generate_graph(5)
        # create a graph
        g_algo = GraphAlgo(g)
        # init graph algo object with the graph above
        self.assertTrue(g_algo.save_to_json("test_file"))
        # verify the save function works

        self.assertTrue(g_algo.load_from_json('../data/A5'))
        # load from JSON given graph
        self.assertTrue(g_algo.get_graph().v_size(), 48)
        # verify amount of vertices within the graph compared to JSON graph
        self.assertTrue(g_algo.get_graph().e_size(), 166)
        # verify amount of edges within the graph compared to JSON graph

        self.assertTrue(g_algo.load_from_json('test_file'))
        # load the previous saved graph on the current loaded graph
        self.assertTrue(g_algo.get_graph().v_size(), 5)
        # verify amount of vertices within the graph compared to JSON graph
        self.assertTrue(g_algo.get_graph().e_size(), 0)
        # verify amount of edges within the graph compared to JSON graph

    def test_connected_components_A(self):
        g = self.generate_graph(7)
        g_algo = GraphAlgo(g)
        g_algo.get_graph().add_edge(0, 1, 1)
        g_algo.get_graph().add_edge(1, 0, 1)
        g_algo.get_graph().add_edge(1, 2, 2)
        g_algo.get_graph().add_edge(2, 1, 3)
        g_algo.get_graph().add_edge(0, 3, 4)
        g_algo.get_graph().add_edge(3, 1, 5)
        g_algo.get_graph().add_edge(0, 4, 2)
        g_algo.get_graph().add_edge(4, 5, 5)
        g_algo.get_graph().add_edge(5, 4, 2)
        self.assertEqual(g_algo.connected_component(0), [0, 1, 2, 3])
        self.assertEqual(g_algo.connected_component(4), [4, 5])
        self.assertEqual(g_algo.connected_component(6), [6])
        # generate a graph with 7 vertices -> init graph algo object -> add multiple edges ->
        # verify connected components -> add another vertex with no edge -> verify connected components for itself

        g1 = GraphAlgo()
        self.assertEqual(g1.connected_component(8), [])
        # verify connected components on a node that does not exists -> suppose to return an empty list

        graph_none = DiGraph()
        graph_none = None
        g2 = GraphAlgo(graph_none)
        self.assertEqual(g1.connected_component(8), [])
        # verify connected components on a node that does not exists -> with a graph that is None ->
        # suppose to return an empty list

    def test_connected_components_B(self):
        g = self.generate_graph(7)
        g_algo = GraphAlgo(g)
        g_algo.get_graph().add_edge(0, 1, 1)
        g_algo.get_graph().add_edge(1, 0, 1)
        g_algo.get_graph().add_edge(1, 2, 2)
        g_algo.get_graph().add_edge(2, 1, 3)
        g_algo.get_graph().add_edge(0, 3, 4)
        g_algo.get_graph().add_edge(3, 1, 5)
        g_algo.get_graph().add_edge(0, 4, 2)
        g_algo.get_graph().add_edge(4, 5, 5)
        g_algo.get_graph().add_edge(5, 4, 2)
        self.assertEqual(g_algo.connected_components(), [[0, 1, 2, 3], [4, 5], [6]])
        # make a graph wth 7 vertices -> connect edges -> verify connected components

        g1 = GraphAlgo()
        self.assertEqual(g1.connected_components(), [])
        # verify connected components on an empty list

    def test_shortest_path(self):
        g = self.generate_graph(7)
        g_algo = GraphAlgo(g)
        g_algo.get_graph().add_edge(0, 1, 2)
        g_algo.get_graph().add_edge(1, 0, 1)
        g_algo.get_graph().add_edge(1, 2, 1)
        g_algo.get_graph().add_edge(2, 1, 1)
        g_algo.get_graph().add_edge(0, 3, 3)
        g_algo.get_graph().add_edge(3, 1, 1)
        g_algo.get_graph().add_edge(0, 4, 5)
        g_algo.get_graph().add_edge(4, 5, 2)
        g_algo.get_graph().add_edge(5, 4, 1)
        self.assertEqual(g_algo.shortest_path(0, 2)[1], [0, 1, 2])
        self.assertEqual(g_algo.shortest_path(4, 5)[1], [4, 5])
        self.assertEqual(g_algo.shortest_path(3, 2)[1], [1, 2, 3])
        self.assertEqual(g_algo.shortest_path(3, 9)[1], [])
        self.assertEqual(g_algo.shortest_path(9, 10)[1], [])
        self.assertEqual(g_algo.shortest_path(9, 1)[1], [])
        # generate a graph with 7 vertices -> init it as graph_algo -> verify shortest paths
        # verify edge cases on edges that does not exist with nodes that does not exist


if __name__ == '__main__':
    unittest.main()
