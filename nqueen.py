class Main:
    def __init__(self):
        self.N = 0

    def main(self):
        queen = Main()
        print("board size")
        queen.N = int(input())
        if queen.NQ():
            print("queen pos is")
        else:
            print("No pos")

    def printSolution(self, b):
        for i in range(self.N):
            for j in range(self.N):
                if b[i][j] == 1:
                    print(" 1 ", end="")
                else:
                    print(" 0 ", end="")
            print()

    def isSafe(self, b, row, col):
        for i in range(col):
            if b[row][i] == 1:
                return False
        i = row
        j = col
        while i >= 0 and j >= 0:
            if b[i][j] == 1:
                return False
            i -= 1
            j -= 1
        i = row
        j = col
        while j >= 0 and i < self.N:
            if b[i][j] == 1:
                return False
            i += 1
            j -= 1
        return True

    def solveNQ(self, b, col):
        if col >= self.N:
            return True
        for i in range(self.N):
            if self.isSafe(b, i, col):
                b[i][col] = 1
                if self.solveNQ(b, col + 1):
                    return True
                b[i][col] = 0
        return False

    def NQ(self):
        b = [[0] * self.N for _ in range(self.N)]
        if not self.solveNQ(b, 0):
            return False
        self.printSolution(b)
        return True

queen = Main()
queen.main()