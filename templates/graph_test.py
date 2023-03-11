import unittest

from .graph import get_edges, top_sort  # type: ignore


class GraphTests(unittest.TestCase):
    def test_get_edges_1(self):
        edges = get_edges(3, [[1, 2], [1, 3]])
        self.assertEqual(edges, {1: {2, 3}, 2: set(), 3: set()})

    def test_get_edges_2(self):
        edges = get_edges(3, [[1, 2], [2, 3], [3, 1], [2, 3]])
        self.assertEqual(edges, {1: {2}, 2: {3}, 3: {1}})

    def test_get_edges_3(self):
        edges = get_edges(3, [[1, 2], [3, 2]])
        self.assertEqual(edges, {1: {2}, 2: set(), 3: {2}})

    def test_top_sort_1(self):
        actual = top_sort({1: {2, 3}, 2: set(), 3: set()})
        self.assertEqual(actual, [1, 3, 2])

    def test_top_sort_2(self):
        actual = top_sort({1: {2}, 2: {3}, 3: {1}})
        self.assertEqual(actual, [])

    def test_top_sort_3(self):
        actual = top_sort({1: {2}, 2: set(), 3: {2}})
        self.assertEqual(actual, [3, 1, 2])


if __name__ == "__main__":
    unittest.main()
