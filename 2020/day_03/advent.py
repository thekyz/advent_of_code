#!/usr/bin/env python

import os
import time


def profile(function, args):
    print(f'{function.__name__}({args})')
    start = time.time()

    return_value = function(args)

    print(f'\t{return_value}')
    end = time.time()
    print(f'\t-> {end-start}')

    return return_value

def get_encountered_trees(tree_map, length, height, right_slope, down_slope, pos_x, pos_y):
    encountered_trees = 0

    # reached the bottom of the map?
    if pos_x >= height:
        return encountered_trees

    pos_y_rel = pos_y % length

    #print(f'at ({pos_x},{pos_y}) ({pos_x},{pos_y_rel}) tree_map[{pos_x}][{pos_y_rel}] = {tree_map[pos_x][pos_y_rel]}')

    if tree_map[pos_x][pos_y_rel]:
        encountered_trees += 1

    down_trees =  get_encountered_trees(tree_map, length, height, right_slope, down_slope, pos_x + down_slope, pos_y + right_slope)

    return down_trees + encountered_trees


def day_03(slope):
    right_slope, down_slope = slope
    tree_map = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input")) as input_file:
        tree_map = [
            [ not c == '.' for c in line.strip() ]
                for line in input_file.readlines()
        ]

    length = len(tree_map[0])
    height = len(tree_map)

    return get_encountered_trees(tree_map, length, height, right_slope, down_slope, 0, 0)


if __name__ == "__main__":
    print( profile(day_03, (1, 1)) * profile(day_03, (3, 1)) * profile(day_03, (5, 1)) * profile(day_03, (7, 1)) * profile(day_03, (1, 2)))
