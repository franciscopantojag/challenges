from functools import reduce, cmp_to_key
from os import path
from helpers import sorted_by, reducer


input_path = path.join(path.dirname(__file__), 'input.txt')


def part_one():
    with open(input_path) as f:
        lines = [line.strip() for line in f.readlines()]

        cmp = cmp_to_key(sorted_by)
        lines.sort(key=cmp)

        result = reduce(reducer, enumerate(lines), 0)

        return result


def main():
    print(part_one())  # 254024898


if __name__ == '__main__':
    main()
