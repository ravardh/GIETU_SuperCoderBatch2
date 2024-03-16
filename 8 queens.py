class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.rows = [0] * n
        self.main_diag = [0] * (2 * n - 1)
        self.anti_diag = [0] * (2 * n - 1)
        self.solutions = []

    def is_safe(self, row, col):
        return not self.rows[row] and not self.main_diag[row + col] and not self.anti_diag[row - col + self.n - 1]

    def solve_queens(self, col):
        if col == self.n:
            temp_solution = []
            for i in range(self.n):
                temp_solution.append(self.board[i][:])
            self.solutions.append(temp_solution)
            return True

        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                self.rows[i] = 1
                self.main_diag[i + col] = 1
                self.anti_diag[i - col + self.n - 1] = 1

                self.solve_queens(col + 1)

                self.board[i][col] = 0
                self.rows[i] = 0
                self.main_diag[i + col] = 0
                self.anti_diag[i - col + self.n - 1] = 0

    def print_solutions(self):
        for solution in self.solutions:
            for row in solution:
                print(' '.join(map(str, row)))
            print()


def main():
    n = 8  # Assuming solving for 8 Queens
    queens = NQueens(n)
    queens.solve_queens(0)
    solutions_count = len(queens.solutions)
    if solutions_count == 0:
        print("No solutions found for", n, "Queens problem.")
    else:
        print("Number of solutions for", n, "Queens problem:", solutions_count)
        print("One possible arrangement for", n, "Queens problem:")
        queens.print_solutions()[0]  # Print one solution


if __name__ == "__main__":
    main()
