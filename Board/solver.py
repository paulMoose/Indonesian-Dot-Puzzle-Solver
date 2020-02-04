from Board.board import Board
import numpy as np

import copy

# TODO: Output 2 files (search.txt and solution.txt)
# TODO: Optimize the DFS (this is just a quick implementation)


class Node:
    def __init__(self, board, parent):
        self.parent = parent
        self.board = board

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        return np.array_equal(self.parent, other.parent) and np.array_equal(self.board, other.board)

    def __str__(self):
        return str(self.board.board.flatten())


class Solver:

    def __init__(self, board):
        self.board = board
        self.open = [Node(self.board, None)]
        self.closed = []

    def get_possible_moves(self, parent_board):
        possibilities = list()

        # TODO: I dont like this n**2, could possibly be optimized
        for row, col in np.ndindex(parent_board.size, parent_board.size):
            child_board = copy.deepcopy(parent_board)
            child_board.touch(row, col)
            new_node = Node(child_board, parent_board)
            already_visited = False
            for closed_node in self.closed:
                if closed_node == new_node:
                    already_visited = True
            for open_node in self.open:
                if open_node == new_node:
                    already_visited = True

            if not already_visited:
                possibilities.append(Node(child_board, parent_board))

        return possibilities


class DFS(Solver):

    def __init__(self, board, max_d):
        super().__init__(board)
        self.max_d = max_d

    def solve(self):

        while len(self.open) != 0:
            x = self.open.pop()
            if x.board.is_goal():
                return x
            else:
                children = self.get_possible_moves(x.board)
                self.closed.append(x)
                self.open = children + self.open

        return None


if __name__ == '__main__':
    board = Board(2, '1101')
    solver = DFS(board, 0)
    print(solver.solve())