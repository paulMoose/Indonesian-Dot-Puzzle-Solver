from core.solver import Solver
from helpers.h_node import AStarNode
from helpers.heuristics import Heuristics
import heapq as open_list

import numpy as np
import copy


class BFS(Solver):
    def __init__(self, size, board_values, **kwargs):
        super().__init__(size, board_values, id=kwargs.get('id'))
        self.open = [AStarNode(self.board, None, 0, f=0, g=0, h=0)]
        self.max_l = kwargs.get('max_l', None)

        self.clear_search_path_if_exists('bfs')

    def get_possible_moves(self, parent_node):
        """
        Method used to see what the next possible moves are from the current token positions on the board.

        Ties between equivalent boards are broken by preferring the board that has its first white token(s)
        at an earlier position based on a left-to-right, then top-down order.

        :param AStarNode parent_node: Node from which the possible moves will be calculated.
        :return: A sorted list of the possible moves to take.
        """
        possibilities = []  # list possible children

        # Creating all the possible board configurations
        for row, col in np.ndindex(parent_node.board.size, parent_node.board.size):
            child_board = copy.deepcopy(parent_node.board)

            touched_token = '{}{}'.format(self.alphabet[row], col + 1)

            child_board.touch(row, col)
            h_of_child = Heuristics.h1(child_board)
            f_of_child = h_of_child
            new_node = AStarNode(child_board, parent_node, touched_token, f=f_of_child, h=h_of_child)

            if not (new_node in self.closed or new_node in self.open):
                possibilities.append(new_node)

        possibilities.sort()  # uses the overridden function of __lt__

        return possibilities

    def solve(self):
        """
        Used to solve a Indonesian Dot Puzzle using the Algorithm A*.
        Will backtrack when the max length is reached.

        :return: The solution path if found or None if no solution exists.
        """
        length = 1
        children = []
        while len(self.open) != 0:
            current_node = open_list.heappop(self.open)
            self.add_to_search_path(
                current_node.board,
                'bfs',
                f=current_node.f,
                h=current_node.h,
            )
            if current_node.board.is_goal():
                self.write_solution_path(self.get_solution_path(current_node), 'bfs')
                return self.get_solution_path(current_node)
            if length <= self.max_l:
                children = self.get_possible_moves(current_node)
            else:
                self.write_solution_path(None, 'bfs')
                return None  # No solution found
            self.closed.append(current_node)  # put visited node in closed list
            for child in children:
                open_list.heappush(self.open, child)

            children.clear()
            length += 1

        self.write_solution_path(None, 'bfs')
        return None  # No solution found
