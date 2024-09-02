import collections.abc as c

class NQueen:
    def n_queen(self, n):
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                    return False
            return True

        def solve(board, row):
            if row == n:
                result.append([x + 1 for x in board])
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(board, row + 1)

        if n == 0:
            return []
        result = []
        solve([0] * n, 0)
        return result

import unittest

class TestNQueen(unittest.TestCase):
    def test_single_queen(self):
        n_queen = NQueen()
        self.assertEqual(n_queen.n_queen(1), [[1]])

    def test_four_queens(self):
        n_queen = NQueen()
        self.assertEqual(n_queen.n_queen(4), [[2, 4, 1, 3], [3, 1, 4, 2]])

    def test_no_solution_for_three_queens(self):
        n_queen = NQueen()
        self.assertEqual(n_queen.n_queen(3), [])

    def test_five_queens(self):
        n_queen = NQueen()
        solutions = n_queen.n_queen(5)
        self.assertEqual(len(solutions), 10)

    def test_six_queens(self):
        n_queen = NQueen()
        solutions = n_queen.n_queen(6)
        self.assertEqual(len(solutions), 4)

    def test_seven_queens(self):
        n_queen = NQueen()
        solutions = n_queen.n_queen(7)
        self.assertEqual(len(solutions), 40)

    def test_eight_queens(self):
        n_queen = NQueen()
        solutions = n_queen.n_queen(8)
        self.assertEqual(len(solutions), 92)

    def test_nine_queens(self):
        n_queen = NQueen()
        solutions = n_queen.n_queen(9)
        self.assertEqual(len(solutions), 352)

    def test_ten_queens(self):
        n_queen = NQueen()
        solutions = n_queen.n_queen(10)
        self.assertEqual(len(solutions), 724)

    def test_invalid_input_zero(self):
        n_queen = NQueen()
        self.assertEqual(n_queen.n_queen(0), [])

if __name__ == "__main__":
    unittest.main()