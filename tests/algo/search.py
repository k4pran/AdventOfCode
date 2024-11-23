import unittest
from algo.search import bfs, bfs_with_adj_func, dfs_recursive, dfs


class TestBFS(unittest.TestCase):
    def setUp(self):
        # Example graph as an adjacency list (dictionary)
        self.adjacency_list_graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }

        # Example graph as a list of edges
        self.edge_list_graph = [
            ('A', 'B'),
            ('A', 'C'),
            ('B', 'D'),
            ('B', 'E'),
            ('C', 'F'),
            ('E', 'F')
        ]

        # Adjacency function for edge list graph
        self.get_adjacents = lambda node, haystack: [
            v for u, v in haystack if u == node
        ] + [
            u for u, v in haystack if v == node
        ]

    def test_bfs_with_adjacency_list(self):
        # Test BFS with an adjacency list
        self.assertTrue(bfs(self.adjacency_list_graph, 'A', 'F'))
        self.assertFalse(bfs(self.adjacency_list_graph, 'A', 'G'))

    def test_bfs_with_edge_list(self):
        # Test BFS with an edge list using bfs_with_adj_func
        self.assertTrue(bfs_with_adj_func(self.edge_list_graph, 'A', 'F', self.get_adjacents))
        self.assertFalse(bfs_with_adj_func(self.edge_list_graph, 'A', 'G', self.get_adjacents))

    def test_bfs_with_disconnected_graph(self):
        # Test BFS with disconnected graph (both adjacency list and edge list)
        disconnected_graph = {
            'A': ['B'],
            'B': [],
            'C': ['D'],
            'D': []
        }
        disconnected_edges = [
            ('A', 'B'),
            ('C', 'D')
        ]

        self.assertFalse(bfs(disconnected_graph, 'A', 'D'))
        self.assertFalse(bfs_with_adj_func(disconnected_edges, 'A', 'D', self.get_adjacents))

    def test_bfs_with_single_node(self):
        # Test BFS with a single-node graph
        single_node_graph = {'A': []}
        single_node_edges = []

        self.assertTrue(bfs(single_node_graph, 'A', 'A'))
        self.assertTrue(bfs_with_adj_func(single_node_edges, 'A', 'A', self.get_adjacents))
        self.assertFalse(bfs(single_node_graph, 'A', 'B'))
        self.assertFalse(bfs_with_adj_func(single_node_edges, 'A', 'B', self.get_adjacents))


class TestDFS(unittest.TestCase):
    def setUp(self):
        # Example graph as an adjacency list (dictionary)
        self.adjacency_list_graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }

        # Example disconnected graph
        self.disconnected_graph = {
            'A': ['B'],
            'B': [],
            'C': ['D'],
            'D': []
        }

        # Graph with a single node
        self.single_node_graph = {'A': []}

        # Graph with cycles
        self.cyclic_graph = {
            'A': ['B', 'C'],
            'B': ['D', 'A'],
            'C': ['E'],
            'D': [],
            'E': ['B']
        }

    def parameterized_dfs_tests(self, dfs_func):
        # Test DFS with adjacency list graph
        self.assertTrue(dfs_func(self.adjacency_list_graph, 'A', 'F'))
        self.assertFalse(dfs_func(self.adjacency_list_graph, 'A', 'G'))

        # Test DFS with disconnected graph
        self.assertFalse(dfs_func(self.disconnected_graph, 'A', 'D'))
        self.assertTrue(dfs_func(self.disconnected_graph, 'A', 'B'))

        # Test DFS with single node
        self.assertTrue(dfs_func(self.single_node_graph, 'A', 'A'))
        self.assertFalse(dfs_func(self.single_node_graph, 'A', 'B'))

        # Test DFS with cyclic graph
        self.assertTrue(dfs_func(self.cyclic_graph, 'A', 'E'))
        self.assertFalse(dfs_func(self.cyclic_graph, 'A', 'Z'))

    def test_iterative_dfs(self):
        self.parameterized_dfs_tests(dfs)

    def test_recursive_dfs(self):
        self.parameterized_dfs_tests(dfs_recursive)

if __name__ == '__main__':
    unittest.main()
