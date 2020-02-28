#!/usr/bin/env python3

from pathlib import Path

import sys
import argparse
import os

sys.path.append(Path(__file__).resolve().parents[1].as_posix())
from core.dfs import DFS
from core.bfs import BFS
from core.a_star import AStar


def parser():
    parser = argparse.ArgumentParser(description='Solves an n x n Indonesian Dot Puzzle')
    parser.add_argument('input', help='the path of an input file that contains test cases')
    return parser


def main():
    args = parser().parse_args()

    try:
        p = Path(args.input)
        with p.open() as reader:
            tests = reader.readlines()

            for index, test in enumerate(tests):
                test = test.split()

                puzzle_size = int(test[0])
                max_d = int(test[1])
                max_l = int(test[2])
                board_values = test[3]

                dfs_solver = DFS(puzzle_size, board_values, max_d=max_d, id=index)
                dfs_solver.solve()

                bfs_solver = BFS(puzzle_size, board_values, max_l=max_l, id=index)
                bfs_solver.solve()

                a_star_solver = AStar(puzzle_size, board_values, max_l=max_l, id=index)
                a_star_solver.solve()

    except FileNotFoundError:
        print("The input file specified does not exit.")

    save_location = os.getcwd()
    print('Output was saved at {}/output'.format(save_location))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
