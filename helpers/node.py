import numpy as np


class Node:
    def __init__(self, board, parent, token, **kwargs):
        """
        Node object used to keep track of the order of the solution path.

        :param board: Indoneasian Dot Puzzle Board configuration
        :param parent: Previous configuration of this Node
        :param token: Token that was touched to arrive at this Node from it's parent
        :param kwargs: Keyword args to pass to :class:`helpers.node.Node`
        """
        self.depth = kwargs.get('depth', None)
        self.parent = parent
        self.board = board
        self.token_touched = token

    def __eq__(self, other):
        """
        Comparing 2 Nodes to see if they are the same. Used when verifying if a configuration is in the open or closed
        lists.
        :param other: Other Node
        :return: If the two are equal or not
        """
        if not isinstance(other, Node):
            return False

        return np.array_equal(self.board.board, other.board.board)

    def __str__(self):
        return '{} {}'.format(self.token_touched, str(self.board.board.flatten()))

    def __lt__(self, other):
        """
        Verifies which one of the nodes is considered smaller than the other. Used when sorting the list of
        possibilities by the one with white nodes first.

        :param other: Other Node
        :return: The smaller node.
        """
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
