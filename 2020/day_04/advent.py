#!/usr/bin/env python

import os
import time
import re

required_fields = [
    "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",
]

def profile(function, validation_fn):
    print(f'{function.__name__}({validation_fn.__name__})')
    start = time.time()

    return_value = function(validation_fn)

    print(f'\t{return_value}')
    end = time.time()
    print(f'\t-> {end-start}')

    return return_value

def tokenize(data):
    passports = []

    tokens = []
    for line in data:
        if not line:
            passport = {}
            for token in tokens:
                key, value = token.split(":")
                passport[key] = value

            passports.append(passport)
            tokens = []
        else:
            tokens += line.split(" ")

    return passports

def validate_part_01(passports):
    valid_passports = 0

    for passport in passports:
        if all (key in passport for key in required_fields):
            valid_passports += 1

    return valid_passports

def is_valid_passport(passport):
    if not all (key in passport for key in required_fields):
        return False

    for key, value in passport.items():
        if key == "byr":
            if int(value) < 1920 or int(value) > 2002:
                return False
            continue

        if key == "iyr":
            if int(value) < 2010 or int(value) > 2020:
                return False
            continue

        if key == "eyr":
            if int(value) < 2020 or int(value) > 2030:
                return False
            continue

        if key == "hgt":
            if "cm" in value:
                hgt = int(value[:value.index("cm")])
                if hgt < 150 or hgt > 193:
                    return False
                continue

            if "in" in value:
                hgt = int(value[:value.index("in")])
                if hgt < 59 or hgt > 76:
                    return False
                continue

            return False

        if key == "hcl":
            if not re.match(r"#[a-f0-9]{6}", value):
                return False
            continue

        if key == "ecl":
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
            continue

        if key == "pid":
            if not re.match(r"^[0-9]{9}$", value):
                return False
            continue

    return True

def validate_part_02(passports):
    valid_passports = 0

    for passport in passports:
        if is_valid_passport(passport):
            valid_passports += 1

    return valid_passports

def day_04(validation_fn):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input")) as input_file:
        data = [ line.strip() for line in input_file.readlines() ]
        data.append("")

    passports = tokenize(data) 

    valid_passports = validation_fn(passports)
    return valid_passports

if __name__ == "__main__":
    profile(day_04, validate_part_01)
    profile(day_04, validate_part_02)
