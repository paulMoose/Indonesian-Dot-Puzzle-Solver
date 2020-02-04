from Board.board import Board


class Solver:

    def __init__(self, board):
        self.board = board

class DFS(Solver):

    def __init__(self, board, max_d):
        super().__init__(board)
        self.max_d = max_d

    def test(self):
        print(self.board)


if __name__ == '__main__':
    initial_board = Board(4, '1110100111000111')
    dfs = DFS(initial_board, max_d=10)
    dfs.test()