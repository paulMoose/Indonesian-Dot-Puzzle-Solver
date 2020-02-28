from core.solver import Solver
import heapq as open_list


class AStar(Solver):
    def __init__(self, size, board_values, **kwargs):
        super().__init__(size, board_values, id=kwargs.get('id'))
        self.max_l = kwargs.get('max_l', None)

        self.clear_search_path_if_exists('a_star')

    def solve(self):
        """
        Used to solve a Indonesian Dot Puzzle using the Algorithm A*.
        Will backtrack when the max length is reached.

        :return: The solution path if found or None if no solution exists.
        """
        length = 1
        children = []
        while len(self.open) != 0:
            current_node = self.open.heappop(open)
            self.add_to_search_path(current_node.board, 'a_star', f=current_node.f, g=current_node.g, h=current_node.h)
            if current_node.board.is_goal():
                self.write_solution_path(self.get_solution_path(current_node), 'a_star')
                return self.get_solution_path(current_node)
            if length <= self.max_l:
                children = self.get_possible_moves(current_node)
            self.closed.append(current_node)  # put visited node in closed list
            for child in children:
                open_list.heappush(open, child)

            children.clear()
            length += 1

        self.write_solution_path(None, 'a_star')
        return None  # No solution found
