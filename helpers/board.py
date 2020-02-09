import numpy as np


class Board:

    def __init__(self, n, start_sequence):
        """
        Indonesian Dot Puzzle Board.

        :param n: size of the Board
        :param start_sequence: initial configuration of the board.
        """
        if len(start_sequence) != (n*n):
            raise ValueError("The start_sequence provided does not match the size of the matrix.")
        self.size = n
        self.board = self.create_board(start_sequence)
        self.goal = np.zeros((n, n))

    def __str__(self):
        s = ''
        for token_value in self.board.flatten():
            s = s + str(token_value)
        return s

    def create_board(self, start_sequence):
        """
        Creates the n x n board using the given start sequence.

        :param start_sequence: initial configuration of the board.
        :return: The created board object
        """
        return np.fromiter(start_sequence, dtype=int).reshape((self.size, self.size))

    def touch(self, row, col):
        """
        The only legal move is to touch a token, which has the effect of flipping it and hence changing its color from
        ◦ to •, or vice versa, but also flips its (at most) 4 adjacent tokens (those immediately up, down, left and right)
        provided that they are within the bounds of the board.

        :param row: Row that will be touched
        :param col: Column that will be touched
        """
        if row < 0 or row > self.size or col < 0 or col > self.size:
            raise IndexError('There is no token at location {}x{}.'.format(row, col))

        # flip middle
        self.board[row, col] = self.flip(self.board[row, col])

        # checking above
        if row > 0:
            self.board[row - 1, col] = self.flip(self.board[row - 1, col])

        # checking below
        if row + 1 < self.size:
            self.board[row + 1, col] = self.flip(self.board[row + 1, col])

        # checking left
        if col > 0:
            self.board[row, col - 1] = self.flip(self.board[row, col - 1])

        # checking right
        if col + 1 < self.size:
            self.board[row, col + 1] = self.flip(self.board[row, col + 1])

    def is_goal(self):
        return np.array_equal(self.board, self.goal)

    @staticmethod
    def flip(value):
        if not value == 0 and not value == 1:
            raise ValueError('Flip method can only take 1 or 0.')
        return 1 - value
