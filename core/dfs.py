from core.solver import Solver
from helpers.node import Node


class DFS(Solver):

    def __init__(self, size, board_values, **kwargs):
        super().__init__(size, board_values, id=kwargs.get('id'))
        self.max_d = kwargs.get('max_d', None)

        self.clear_search_path_if_exists('dfs')

    def solve(self):
        """
        Used to solve a Indonesian Dot Puzzle using the Depth first search method. Will backtrack when the max depth
        level is reached.

        :return: The solution path if found or None if no solution exists.
        """
        depth = 1
        while len(self.open) != 0:
            x = self.open.pop()
            self.add_to_search_path(x.board, 'dfs')
            if x.board.is_goal():
                self.write_solution_path(self.get_solution_path(x), 'dfs')
                return self.get_solution_path(x)
            if depth <= self.max_d:
                children = self.get_possible_moves(x)
            self.closed.append(x)  # put visited node in closed list
            self.open = children + self.open  # putting children in list as a stack behaviour
            children.clear()
            depth += 1

        self.write_solution_path(None, 'dfs')
        return None
