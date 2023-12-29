from functools import reduce, cmp_to_key
from os import path
from typing import Literal
from helpers import get_sorted_by, reducer


input_path = path.join(path.dirname(__file__), 'input.txt')


def get_part_fun(part: 'Literal[1,2]'):
    def fun():
        with open(input_path) as f:
            cmp = cmp_to_key(get_sorted_by(part == 2))
            sorted_lines = sorted(f.readlines(), key=cmp)

            result = reduce(reducer, enumerate(sorted_lines), 0)
            return result
    return fun


def part_one(): return get_part_fun(1)()


def part_two(): return get_part_fun(2)()


def main():
    print(part_one())  # 254024898
    print(part_two())  # 254115617


if __name__ == '__main__':
    main()
