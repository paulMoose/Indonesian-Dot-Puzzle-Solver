from core.solver import Solver
import heapq as open_list


class AStar(Solver):
    """
    TODO: description
    """

    def __init__(self, size, board_values, **kwargs):
        super().__init__(size, board_values, id=kwargs.get('id'))
        self.max_l = kwargs.get('max_l', None)

        self.clear_search_path_if_exists('a_star')

    def solve(self):
        """
        Used to solve a Indonesian Dot Puzzle using the Algorithm A*.
        TODO: what does max_l do?

        :return: The solution path if found or None if no solution exists.
        """
        while len(self.open) != 0:
            open_list.heapify(open)  # converts list to a heap | sorts it into a heap
            x = self.open.heappop(open)
            self.add_to_search_path(x.board, 'a_star')
            if x.board.is_goal():
                self.write_solution_path(self.get_solution_path(x), 'a_star')
                return self.get_solution_path(x)
            # TODO: check max_l
            children = self.get_possible_moves(x)
            self.closed.append(x)  # put visited node in closed list
            self.open.extend(children)
            children.clear()
            # TODO: update max_l

        self.write_solution_path(None, 'a_star')
        return None  # No solution found
