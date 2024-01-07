from functools import reduce
from os import path
from typing import Literal
from helpers import get_game_id, get_power_per_line

input_path = path.join(path.dirname(__file__), 'input.txt')


def get_part_fun(part: 'Literal[1,2]'):
    def part_fun():
        with open(input_path) as f:
            line_func = get_game_id if part == 1 else get_power_per_line
            result = sum(line_func(line) for line in f.readlines())
            return result

    return part_fun


def part_one(): return get_part_fun(1)()


def part_two(): return get_part_fun(2)()


def main():
    print(part_one())  # 2685
    print(part_two())  # 83707


if __name__ == '__main__':
    main()
