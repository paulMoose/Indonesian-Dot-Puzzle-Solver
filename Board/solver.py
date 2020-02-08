from Board.board import Board
import numpy as np

import copy

# TODO: Output 2 files (search.txt and solution.txt)

    
class Node:
    def __init__(self, board, parent, **kwargs):
        self.depth = kwargs.get('depth', None)
        self.parent = parent
        self.board = board

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        return np.array_equal(self.board.board, other.board.board)

    def __str__(self):
        # str = 'Board: {} ==> Parent: {}'.format(self.board.board.flatten(), self.parent.board.flatten())
        return str(self.board.board.flatten())

    def __lt__(self, other):
        flattened_board = self.board.board.flatten()
        flattened_other = other.board.board.flatten()

        if self.board.size != other.board.size:
            raise ValueError('Boards should be the same size to compare.')

        for original_board, other_board in zip(flattened_board, flattened_other):
            if original_board < other_board:
                return True
            elif other_board < original_board:
                return False

        return True


class Solver:

    def __init__(self, board):
        self.board = board
        self.open = [Node(self.board, None)]
        self.closed = []

    def get_possible_moves(self, parent_node):
        possibilities = []

        # Creating all the possible board configurations
        for row, col in np.ndindex(parent_node.board.size, parent_node.board.size):
            child_board = copy.deepcopy(parent_node.board)
            child_board.touch(row, col)
            new_node = Node(child_board, parent_node)

            if not (new_node in self.closed or new_node in self.open):
                possibilities.append(new_node)

        possibilities.sort()

        return possibilities

    def solve(self):
        raise NotImplementedError()

    @staticmethod
    def get_solution_path(end_node):
        path = []
        # print(type(end_node))
        current = end_node
        while current is not None:
            # print(current)
            # print('parent board = {}'.format(current.parent))
            path.append(current.board)
            current = current.parent
        return path[::-1]


class DFS(Solver):

    def __init__(self, board, **kwargs):
        super().__init__(board)
        self.max_d = kwargs.get('max_d', None)

    def solve(self):
        # TODO: test max_d
        depth = 0
        while len(self.open) != 0:
            x = self.open.pop()
            # print('testing {}'.format(x)) # TODO: add to search_dfs
            if x.board.is_goal():
                return self.get_solution_path(x)
            if depth < self.max_d:
                children = self.get_possible_moves(x)
            self.closed.append(x)
            self.open = children + self.open
            children = []
            depth += 1

        return None




if __name__ == '__main__':
    board = Board(3, '111001011')
    solver = DFS(board, max_d=800)

    for step in solver.solve():
        print(step.board.flatten())
