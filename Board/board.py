import numpy as np


class Board:

    def __init__(self, n, start_sequence):
        if len(start_sequence) != (n*n):
            raise ValueError("The start_sequence provided does not match the size of the matrix.")
        self.size = n
        self.board = self.create_board(start_sequence)
        self.goal = np.zeros((n, n))

    def __str__(self):
        return str(self.board)

    def create_board(self, start_sequence):
        return np.fromiter(start_sequence, dtype=int).reshape((self.size, self.size))

    def touch(self, row, col):
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

