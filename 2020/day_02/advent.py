#!/usr/bin/env python

import os
import time


def profile(function, validation_function):
    print(f'{function.__name__}({validation_function.__name__})')
    start = time.time()
    print(f'\t{function(validation_function)}')
    end = time.time()
    print(f'\t-> {end-start}')


def tokenize(line):
    policy_set, password = line.split(":")
    policy_range, policy_letter = policy_set.split(" ")
    policy_range_min, policy_range_max = policy_range.split("-")
    return int(policy_range_min), int(policy_range_max), policy_letter, password


def validate_part_01(password_validation):
    policy_range_min, policy_range_max, policy_letter, password = password_validation

    policy_letter_count = 0
    for c in password:
        if c == policy_letter:
            policy_letter_count += 1

    if policy_letter_count >= policy_range_min and policy_letter_count <= policy_range_max:
        return True

    return False


def validate_part_02(password_validation):
    policy_pos_1, policy_pos_2, policy_letter, password = password_validation

    if (password[policy_pos_1] == policy_letter) ^ (password[policy_pos_2] == policy_letter):
        return True

    return False


def day_02(validation_fn):
    passwords = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input")) as input_file:
        password_sets = [ tokenize(line.strip()) for line in input_file.readlines()]

    valid_passwords = 0
    for password_validation in password_sets:
        if validation_fn(password_validation):
            valid_passwords += 1

    return valid_passwords


if __name__ == "__main__":
    profile(day_02, validate_part_01)
    profile(day_02, validate_part_02)
