import unittest

from src.GNode import GNode


class MyTestCase(unittest.TestCase):

    def test_set_get_key(self):
        node = GNode(5)
        self.assertEqual(node.get_key(), 5)
        # make a node -> verify key

        node.set_key(3)
        self.assertEqual(node.get_key(), 3)
        # update node -> verify key

    def test_set_get_info(self):
        node = GNode(5)
        node.set_info("info")
        self.assertEqual(node.get_info(), "info")
        # make a node, set an info -> verify info

        node.set_info("updated")
        self.assertEqual(node.get_info(), "updated")
        # update info -> verify info

    def test_set_get_position(self):
        node = GNode(8)
        self.assertIsNone(node.get_position())
        # make a node -> verify position is None

        node.set_position(3, 2, 1)
        self.assertIsNotNone(node.get_position())
        self.assertTupleEqual(tuple(node.get_position()), (3, 2, 1))
        # set position to the node -> verify position & position is not None

        node.set_position(5, 1, 1)
        self.assertTupleEqual(tuple(node.get_position()), (5, 1, 1))
        # update position of the node -> verify position

    def test_set_get_tag(self):
        node = GNode(7)
        self.assertEqual(node.get_tag(), -1)
        # make a node -> verify tag is -1

        node.set_tag(0)
        self.assertEqual(node.get_tag(), 0)
        # update node's tag -> verify tag


if __name__ == '__main__':
    unittest.main()
