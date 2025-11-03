class NQBacktracking:
    def __init__(self):
        self.ld = [0] * 30
        self.rd = [0] * 30
        self.cl = [0] * 30
    def printSolution(self, board):
        print("\n\nN Queen Backtracking Solution:")
        for line in board:
            print(" ".join(map(str, line)))
    def solveNQUtil(self, board, col):
        if col >= N:
            return True
        for i in range(N):
            if (self.ld[i - col + N - 1] != 1 and
                self.rd[i + col] != 1) and self.cl[i] != 1:
                board[i][col] = 1
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 1
                if self.solveNQUtil(board, col + 1):
                    return True
                board[i][col] = 0  # BACKTRACK
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 0
        return False
    def solveNQ(self):
        board = [[0 for _ in range(N)] for __ in range(N)]
        if self.solveNQUtil(board, 0) == False:
            print("Solution does not exist")
            return False
        self.printSolution(board)
        return True
if __name__ == "__main__":
    N = 4
    NQBt = NQBacktracking()
    NQBt.solveNQ()