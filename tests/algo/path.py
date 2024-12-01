import unittest
import math

from algo.path import dijkstra


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.graphs = {
            # Simple graph
            "simple": {
                "graph": {
                    "A": {"B": 1, "C": 4},
                    "B": {"A": 1, "C": 2, "D": 5},
                    "C": {"A": 4, "B": 2, "D": 1},
                    "D": {"B": 5, "C": 1}
                },
                "start": "A",
                "expected": {"A": 0, "B": 1, "C": 3, "D": 4}
            },
            # Disconnected graph
            "disconnected": {
                "graph": {
                    "A": {"B": 2},
                    "B": {"A": 2},
                    "C": {"D": 1},
                    "D": {"C": 1}
                },
                "start": "A",
                "expected": {"A": 0, "B": 2, "C": math.inf, "D": math.inf}
            },
            # Single node graph
            "single_node": {
                "graph": {"A": {}},
                "start": "A",
                "expected": {"A": 0}
            },
            # Cyclic graph
            "cyclic": {
                "graph": {
                    "X": {"Y": 7, "Z": 5},
                    "Y": {"X": 7, "Z": 2, "W": 3},
                    "Z": {"X": 5, "Y": 2, "W": 6},
                    "W": {"Y": 3, "Z": 6, "V": 1},
                    "V": {"W": 1}
                },
                "start": "X",
                "expected": {"X": 0, "Y": 7, "Z": 5, "W": 10, "V": 11}
            },
            # Graph with unreachable nodes
            "unreachable": {
                "graph": {
                    "A": {"B": 3},
                    "B": {"C": 2},
                    "C": {},
                    "D": {}
                },
                "start": "A",
                "expected": {"A": 0, "B": 3, "C": 5, "D": math.inf}
            }
        }

    def parameterized_test(self, graph, start, expected):
        result = dijkstra(graph, start)
        self.assertEqual(result, expected)

    def test_dijkstra(self):
        for test_name, test_data in self.graphs.items():
            with self.subTest(test_name=test_name):
                self.parameterized_test(
                    test_data["graph"], test_data["start"], test_data["expected"]
                )


if __name__ == "__main__":
    unittest.main()
