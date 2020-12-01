#!/usr/bin/env python

import os
import time


def profile(function):
    print(function.__name__)
    start = time.time()
    print(f'\t{function()}')
    end = time.time()
    print(f'\t-> {end-start}')


def day_01_part_01():
    input_data = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input")) as input_file:
        input_data = [ int(line.strip()) for line in input_file.readlines()]

    n_index = 0
    for n in input_data:
        m_index = 0
        for m in input_data[n_index+1:]:
            if n + m == 2020:
                return n * m

            m_index += 1
        n_index += 1


def day_01_part_02():
    input_data = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input")) as input_file:
        input_data = [ int(line.strip()) for line in input_file.readlines()]

    n_index = 0
    for n in input_data:
        m_index = 0
        for m in input_data[n_index + 1:]:
            k_index = 0
            for k in input_data[m_index +1:]:
                if n + m + k == 2020:
                    return n * m * k

                k_index += 1

            m_index += 1

        n_index += 1


if __name__ == "__main__":
    profile(day_01_part_01)
    profile(day_01_part_02)
