import random
import unittest

from DiGraph import DiGraph


class MyTestCase(unittest.TestCase):

    def generate_graph(self, v) -> DiGraph():
        i = 0
        g = DiGraph()
        while i < v:
            g.add_node(i)
            i += 1
        return g

    def test_add_sizes(self):
        g = self.generate_graph(10)
        # make a graph with 10 vertices
        i = 0
        while i < g.v_size()-1:
            g.add_edge(i, i+1, 2)
            i += 1
        # add each node its predecessor as an edge
        self.assertEqual(g.v_size(), 10)
        self.assertEqual(g.e_size(), 9)
        # verify edge and vertices sizes

    def test_remove(self):
        g = self.generate_graph(15)
        # generate a graph with 15 vertices
        g.remove_node(0)
        g.remove_node(1)
        g.remove_node(2)
        self.assertEqual(g.v_size(), 12)
        # Remove 3 vertices from the start and verify for amount of vertices

        g.add_edge(3, 4, 2)
        g.add_edge(3, 5, 2)
        g.add_edge(3, 6, 2)
        g.add_edge(3, 7, 2)
        g.add_edge(3, 8, 2)
        self.assertEqual(g.e_size(), 5)
        # Add 5 edges and verify they added

        g.remove_edge(3, 4)
        g.remove_edge(3, 5)
        g.remove_edge(3, 6)
        self.assertEqual(g.e_size(), 2)
        # remove 3 edges and verify they removed

    def test_has_edge(self):
        g = self.generate_graph(15)
        # generate a graph with 15 vertices
        size = g.v_size()
        for i in range(0, size):
            for j in range(0, size):
                g.add_edge(i, j, random.random()*100)
        self.assertEqual(g.e_size(), 225)
        # connect each vertex to the rest of the vertices approx - 15*15 edges = 225
        flag = True
        for i in range(0, size):
            for j in range(0, size):
                flag = g.has_edge(i, j)

        self.assertTrue(flag)
        # verify connections

    def test_get_node(self):
        g = self.generate_graph(10)
        # generate a graph with 10 vertices
        for i in range(0, 10):
            self.assertEqual(g.get_node(i).get_key(), i)
        # verify get_node works aka each key equals to the current index of the loop

        self.assertIsNone(g.get_node(12))
        self.assertIsNone(g.get_node(16))
        self.assertIsNone(g.get_node(13))
        self.assertIsNone(g.get_node(18))
        # verify that get_node don't hold unknown nodes

    def test_get_weight(self):
        g = self.generate_graph(5)
        g.add_edge(0, 1, 3)
        self.assertEqual(g.get_edge_weight(0, 1), 3)
        g.add_edge(2, 1, 6)
        self.assertEqual(g.get_edge_weight(2, 1), 6)
        # add two edges -> verify the weight

        g.add_edge(0, 1, 6)
        self.assertEqual(g.get_edge_weight(0, 1), 6)
        # update the weight and verify it updated

    def test_mc(self):
        g = self.generate_graph(20)
        self.assertEqual(g.get_mc(), 20)
        # create a graph with 20 vertices -> verify changes

        g.remove_node(0)
        g.remove_node(1)
        g.remove_node(2)
        g.remove_node(3)
        self.assertEqual(g.get_mc(), 24)
        # remove 4 vertices -> verify changes

        g.add_edge(0, 1, 20)
        g.add_edge(0, 3, 20)
        g.add_edge(0, 8, 20)
        self.assertEqual(g.get_mc(), 24)
        # check if connecting a node that does not exist with one that exist changes the modification
        # -> verify modifications

        g.add_edge(4, 5, 20)
        g.add_edge(5, 7, 9)
        g.add_edge(6, 8, 24)
        g.add_edge(9, 10, 6)
        self.assertEqual(g.get_mc(), 28)
        # add 4 edges, verify changes

        g.add_edge(4, 5, 23)
        g.add_edge(5, 7, 15)
        self.assertEqual(g.get_mc(), 30)
        # verify that updating the edge DOES changes the MC

        g.remove_edge(4, 5)
        g.remove_edge(9, 10)
        self.assertEqual(g.get_mc(), 32)
        # verify removing edge does change modification

        g.remove_edge(10, 12)
        g.remove_edge(17, 12)
        g.remove_edge(12, 16)
        g.remove_edge(1, 18)
        self.assertEqual(g.get_mc(), 32)
        # verify same MC when trying to delete edge that does not exist

    def test_from_vertex(self):
        g = self.generate_graph(20)
        g.add_edge(1, 2, 3)
        g.add_edge(1, 3, 3)
        g.add_edge(1, 4, 3)
        g.add_edge(1, 5, 3)
        g.add_edge(1, 6, 3)
        dic = {0: 2, 1: 3, 2: 4, 3: 5, 4: 6}
        self.assertDictEqual(g.all_out_edges_of_node(1), dic)
        # generate a graph with 20 vertices > add 5 edges from one vertex > verify
        self.assertDictEqual(g.all_out_edges_of_node(8), {})
        # verify an empty dictionary for a node that does not have an edge
        self.assertDictEqual(g.all_out_edges_of_node(99), {})
        # verify an empty dictionary for a node that does not have an edge and does not exist

    def test_to_vertex(self):
        g = self.generate_graph(10)
        g.add_edge(1, 2, 3)
        g.add_edge(1, 3, 3)
        g.add_edge(1, 4, 3)
        g.add_edge(1, 5, 3)
        g.add_edge(1, 6, 3)
        dic = {0: 1, 1: 3, 2: 4, 3: 5, 4: 6}
        self.assertDictEqual(g.all_in_edges_of_node(2), {0: 1})
        self.assertDictEqual(g.all_in_edges_of_node(3), {0: 1})
        self.assertDictEqual(g.all_in_edges_of_node(4), {0: 1})
        self.assertDictEqual(g.all_in_edges_of_node(5), {0: 1})
        self.assertDictEqual(g.all_in_edges_of_node(6), {0: 1})
        # generate a graph with 20 vertices > add 5 edges from one vertex > verify all of em point to the first
        self.assertDictEqual(g.all_in_edges_of_node(8), {})
        # verify an empty dictionary for a node that does not have an edge
        self.assertDictEqual(g.all_in_edges_of_node(99), {})
        # verify an empty dictionary for a node that does not have an edge and does not exist

    def test_get_all_v(self):
        g = self.generate_graph(5)
        dic = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
        res = g.get_all_v().values()
        self.assertEquals(res, dic.values())
        print(res)
        # generate graph with 10 vertices -> verify they return as a dictionary

        # g = DiGraph()
        # self.assertDictEqual(g.get_all_v(), {})


if __name__ == '__main__':
    unittest.main()
