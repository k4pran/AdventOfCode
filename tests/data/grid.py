import unittest

from data.grid import slice_right_segment, slice_left_segment, slice_down_segment, slice_up_segment, \
    slice_up_right_segment, slice_up_left_segment, slice_down_right_segment, slice_down_left_segment

# Sample grid for testing
GRID = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

class TestGridSliceFunctions(unittest.TestCase):

    def test_slice_right_row_segment(self):
        test_cases = [
            (GRID, 0, 0, 3, [1, 2, 3]),  # Normal case
            (GRID, 1, 2, 2, [8, 9]),     # Middle of the grid
            (GRID, 4, 3, 1, [24]),       # Single cell at the end
            (GRID, 2, 4, 3, [15]),       # Out-of-bounds truncation
        ]
        for grid, row, col, nb_cells, expected in test_cases:
            with self.subTest(grid=grid, row=row, col=col, nb_cells=nb_cells):
                self.assertEqual(slice_right_segment(grid, row, col, nb_cells), expected)

    def test_slice_left_row_segment(self):
        test_cases = [
            (GRID, 0, 4, 3, [5, 4, 3]),  # Normal case
            (GRID, 1, 3, 2, [9, 8]),     # Middle of the grid
            (GRID, 4, 1, 1, [22]),       # Single cell
            (GRID, 2, 0, 3, [11]),       # Out-of-bounds truncation
        ]
        for grid, row, col, nb_cells, expected in test_cases:
            with self.subTest(grid=grid, row=row, col=col, nb_cells=nb_cells):
                self.assertEqual(slice_left_segment(grid, row, col, nb_cells), expected)

    def test_slice_down_col_segment(self):
        test_cases = [
            (GRID, 0, 0, 3, [1, 6, 11]),  # Normal case
            (GRID, 2, 1, 2, [8, 13]),     # Middle of the grid
            (GRID, 4, 3, 1, [20]),        # Single cell
            (GRID, 1, 3, 3, [17, 22]),    # Out-of-bounds truncation
        ]
        for grid, col, row, nb_cells, expected in test_cases:
            with self.subTest(grid=grid, col=col, row=row, nb_cells=nb_cells):
                self.assertEqual(slice_down_segment(grid, col, row, nb_cells), expected)

    def test_slice_up_col_segment(self):
        test_cases = [
            (GRID, 4, 0, 3, [21, 16, 11]),  # Normal case
            (GRID, 3, 2, 2, [18, 13]),      # Middle of the grid
            (GRID, 1, 4, 1, [10]),          # Single cell
            (GRID, 1, 1, 3, [7, 2]),       # Out-of-bounds truncation
            (GRID, 2, 1, 3, [12, 7, 2]),       # Out-of-bounds truncation
        ]
        for grid, col, row, nb_cells, expected in test_cases:
            with self.subTest(grid=grid, col=col, row=row, nb_cells=nb_cells):
                self.assertEqual(slice_up_segment(grid, col, row, nb_cells), expected)

    def test_slice_up_right_segment(self):
        test_cases = [
            (GRID, 4, 0, 3, [21, 17, 13]),  # Normal case
            (GRID, 3, 1, 2, [17, 13]),     # Middle of the grid
            (GRID, 1, 3, 1, [9]),          # Single cell
            (GRID, 3, 3, 4, [19, 15]),     # Out-of-bounds truncation
        ]
        for grid, row, col, nb_cells, expected in test_cases:
            with self.subTest(grid=grid, row=row, col=col, nb_cells=nb_cells):
                self.assertEqual(slice_up_right_segment(grid, row, col, nb_cells), expected)

    def test_slice_up_left_segment(self):
        test_cases = [
            (GRID, 4, 4, 3, [25, 19, 13]),  # Normal case
            (GRID, 3, 3, 2, [19, 13]),     # Middle of the grid
            (GRID, 1, 1, 1, [7]),          # Single cell
            (GRID, 2, 0, 4, [11]),         # Out-of-bounds truncation
        ]
        for grid, row, col, nb_cells, expected in test_cases:
            with self.subTest(grid=grid, row=row, col=col, nb_cells=nb_cells):
                self.assertEqual(slice_up_left_segment(grid, row, col, nb_cells), expected)

    def test_slice_down_right_segment(self):
        test_cases = [
            (GRID, 0, 0, 3, [1, 7, 13]),  # Normal case
            (GRID, 1, 1, 2, [7, 13]),    # Middle of the grid
            (GRID, 3, 3, 1, [19]),       # Single cell
            (GRID, 2, 3, 4, [14, 20]),   # Out-of-bounds truncation
        ]
        for grid, row, col, nb_cells, expected in test_cases:
            with self.subTest(grid=grid, row=row, col=col, nb_cells=nb_cells):
                self.assertEqual(slice_down_right_segment(grid, row, col, nb_cells), expected)

    def test_slice_down_left_segment(self):
        test_cases = [
            # (GRID, 0, 4, 3, [5, 9, 13]),  # Normal case
            # (GRID, 1, 3, 2, [9, 13]),    # Middle of the grid
            # (GRID, 2, 2, 1, [13]),       # Single cell
            (GRID, 4, 0, 4, [21]),       # Out-of-bounds truncation
        ]
        for grid, row, col, nb_cells, expected in test_cases:
            with self.subTest(grid=grid, row=row, col=col, nb_cells=nb_cells):
                self.assertEqual(slice_down_left_segment(grid, row, col, nb_cells), expected)

    def test_empty_grid(self):
        empty_grid = []
        self.assertEqual(slice_right_segment(empty_grid, 0, 0, 3), None)
        self.assertEqual(slice_left_segment(empty_grid, 0, 0, 3), None)
        self.assertEqual(slice_down_segment(empty_grid, 0, 0, 3), None)
        self.assertEqual(slice_up_segment(empty_grid, 0, 0, 3), None)
        self.assertEqual(slice_up_right_segment(empty_grid, 0, 0, 3), None)
        self.assertEqual(slice_down_right_segment(empty_grid, 0, 0, 3), None)
        self.assertEqual(slice_up_left_segment(empty_grid, 0, 0, 3), None)
        self.assertEqual(slice_down_left_segment(empty_grid, 0, 0, 3), None)

    def test_single_row_or_column(self):
        single_row_grid = [[1, 2, 3, 4, 5]]
        self.assertEqual(slice_right_segment(single_row_grid, 0, 0, 3), [1, 2, 3])
        self.assertEqual(slice_left_segment(single_row_grid, 0, 4, 3), [5, 4, 3])

        single_col_grid = [[1], [2], [3], [4], [5]]
        self.assertEqual(slice_down_segment(single_col_grid, 0, 0, 3), [1, 2, 3])
        self.assertEqual(slice_up_segment(single_col_grid, 4, 0, 3), [5, 4, 3])

    def test_zero_cells(self):
        self.assertEqual(slice_right_segment(GRID, 0, 0, 0), None)
        self.assertEqual(slice_left_segment(GRID, 0, 4, 0), None)
        self.assertEqual(slice_down_segment(GRID, 0, 0, 0), None)
        self.assertEqual(slice_up_segment(GRID, 4, 0, 0), None)
        self.assertEqual(slice_up_right_segment(GRID, 4, 0, 0), None)
        self.assertEqual(slice_down_right_segment(GRID, 4, 0, 0), None)
        self.assertEqual(slice_up_left_segment(GRID, 4, 0, 0), None)
        self.assertEqual(slice_down_left_segment(GRID, 4, 0, 0), None)

    def test_diagonals_with_edges(self):
        self.assertEqual(slice_up_right_segment(GRID, 0, 0, 3), [1])  # Top-left corner
        self.assertEqual(slice_up_left_segment(GRID, 0, 4, 3), [5])  # Top-right corner
        self.assertEqual(slice_down_right_segment(GRID, 4, 0, 3), [21])  # Bottom-left corner
        self.assertEqual(slice_down_left_segment(GRID, 4, 4, 3), [25])  # Bottom-right corner


if __name__ == "__main__":
    unittest.main()
