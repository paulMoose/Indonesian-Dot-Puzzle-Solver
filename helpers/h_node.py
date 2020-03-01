from helpers.node import Node


class AStarNode(Node):
    def __init__(self, board, parent, token, **kwargs):
        super().__init__(board, parent, token, **kwargs)

        self.f = kwargs.get('f', 0)
        self.g = kwargs.get('g', 0)
        self.h = kwargs.get('h', 0)

    def __lt__(self, other):
        """
        Verifies which one of the nodes is considered smaller than the other. Used when sorting the list of
        possibilities by the smaller f(n).

        :param AStarNode other: Other Node
        :return: The smaller node.
        """
        # flattens multi-array board to 1D array
        flattened_board = self.board.board.flatten()
        flattened_other = other.board.board.flatten()

        if self.board.size != other.board.size:
            raise ValueError('Boards should be the same size to compare.')

        if self.f < other.f:
            return True
        elif self.f > other.f:
            return False
        else:  # if f(n) is a tie, evaluate first white token(s)
            for original_board, other_board in zip(flattened_board, flattened_other):
                if original_board < other_board:
                    return True
                elif other_board < original_board:
                    return False

        return True
