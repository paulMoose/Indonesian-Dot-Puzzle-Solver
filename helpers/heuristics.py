import numpy as np
import copy


class Heuristics:
    @staticmethod
    def h1(current_board):
        """
        Heuristic 1. Hamming distance: counts the number of 1's in the flattened_board

        :param current_board: board of current node
        :return: Heuristic value.
        """
        flattened_board = current_board.board.flatten()
        return sum(flattened_board)

    @staticmethod
    def h2(input_board):
        """
        Heuristic 2.

        :param input_board: board of current node
        :return: Heuristic value.
        """
        board_size = input_board.size
        white_token = 0
        black_token = 1
        h_value = 0
        for row, col in np.ndindex(board_size, board_size):
            current_board = copy.deepcopy(input_board.board)
            current_token = current_board[row, col]

            if current_token == black_token:  # let's evaluate
                # checking above
                if row > 0 and current_board[row - 1, col] == white_token:
                    h_value += 1

                # checking below
                if (row + 1) < board_size and current_board[row + 1, col] == white_token:
                    h_value += 1

                # checking left
                if col > 0 and current_board[row, col - 1] == white_token:
                    h_value += 1

                # checking right
                if col + 1 < board_size and current_board[row, col + 1] == white_token:
                    h_value += 1

        return h_value

    @staticmethod
    def h3(input_board):
        """
        Heuristic 2.

        :param input_board: board of current node
        :return: Heuristic value.
        """

