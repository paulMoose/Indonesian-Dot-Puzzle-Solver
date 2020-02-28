from helpers.node import Node


class AStarNode(Node):
    def __init__(self, board, parent, token, **kwargs):
        super().__init__(board, parent, token)
        self.f = kwargs.get('f')
        self.g = kwargs.get('g')
        self.h = kwargs.get('h')

    def h(self, flattened_board):
        """
        Heuristic 1. Hamming distance: counts the number of 1's in the flattened_board

        :param flattened_board: 1D array board
        :return: Heuristic value.
        """
        return sum(flattened_board)

    def __lt__(self, other):
        """
        Verifies which one of the nodes is considered smaller than the other. Used when sorting the list of
        possibilities by the smaller f(n).

        :param other: Other Node
        :return: The smaller node.
        """
        # flattens multi-array board to 1D array
        flattened_board = self.board.board.flatten()
        flattened_other = other.board.board.flatten()

        if self.board.size != other.board.size:
            raise ValueError('Boards should be the same size to compare.')

        f_of_board = self.h(flattened_board) + self.g
        f_of_other = self.h(flattened_other) + other.g

        if f_of_board < f_of_other:
            return True
        elif f_of_board > f_of_other:
            return False

        return True
