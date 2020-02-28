from helpers.board import Board
from helpers.node import Node
from pathlib import Path

import numpy as np
import string
import copy


class Solver:
    def __init__(self, size, board_values, **kwargs):
        """
        Base class for the various solver classes that will be implemented in this project.

        :param int size: Size of the indonesian dot puzzle board
        :param string board_values: Initial board values wanted to be solved (0 for white, 1 for black)
        :param kwargs: Keyword args to pass to :class:`core.solver.Solver`
        """
        self.board = Board(n=size, start_sequence=board_values)
        self.id = kwargs.get('id', None)
        self.alphabet = list(string.ascii_uppercase)

        self.open = [Node(self.board, None, 0)]
        self.closed = []  # list structure is common to all type of algorithm

    def get_possible_moves(self, parent_node):
        """
        Method used to see what the next possible moves are from the current token positions on the board.

        Ties between equivalent boards are broken by preferring the board that has its first white token(s)
        at an earlier position based on a left-to-right, then top-down order.

        :param Node parent_node: Node from which the possible moves will be calculated.
        :return: A sorted list of the possible moves to take.
        """
        possibilities = []  # list possible children

        # Creating all the possible board configurations
        for row, col in np.ndindex(parent_node.board.size, parent_node.board.size):
            child_board = copy.deepcopy(parent_node.board)

            touched_token = '{}{}'.format(self.alphabet[row], col + 1)

            child_board.touch(row, col)
            new_node = Node(child_board, parent_node, touched_token)

            if not (new_node in self.closed or new_node in self.open):
                possibilities.append(new_node)

        possibilities.sort()  # uses the overridden function of __lt__

        return possibilities

    def solve(self):
        raise NotImplementedError()

    def write_solution_path(self, solution, algorithm):
        Path('output').mkdir(parents=True, exist_ok=True)
        file_path = 'output/{}_{}_solution.txt'.format(self.id, algorithm)
        with open(file_path, 'w') as writer:
            if solution:
                for step in solution:
                    writer.write('{}\n'.format(step))
            else:
                writer.write('no solution')

    def clear_search_path_if_exists(self, algorithm):
        """
        Needed in order to clear the contents of a file before appending the next searches to the search path.

        :param algorithm: Specifies the algorithm used to solve the puzzle
        """
        file_path = Path('output/{}_{}_search.txt'.format(self.id, algorithm))

        if file_path.exists():
            file_path.unlink()

    def add_to_search_path(self, search, algorithm, **kwargs):
        Path('output').mkdir(parents=True, exist_ok=True)
        file_path = 'output/{}_{}_search.txt'.format(self.id, algorithm)

        f = kwargs.get('f', 0)
        g = kwargs.get('g', 0)
        h = kwargs.get('h', 0)

        with open(file_path, 'a') as file:
            file.write('{} {} {} {}\n'.format(f, g, h, search))

    @staticmethod
    def get_solution_path(end_node):
        solution_path = []
        current_node = end_node
        while current_node is not None:
            touched_token = current_node.token_touched
            board = current_node.board

            step = '{} {}'.format(touched_token, board)

            solution_path.append(step)
            current_node = current_node.parent
        return list(reversed(solution_path))
