from os import path
from helpers import get_final_num, get_final_num_part_two

input_path = path.join(path.dirname(__file__), 'input.txt')


def part_one():
    with open(input_path) as f:
        result = sum(get_final_num(line) for line in f.readlines())
        return result


def part_two():
    with open(input_path) as f:
        result = sum(get_final_num_part_two(line) for line in f.readlines())
        return result


def main():
    print(part_one())  # 55447
    print(part_two())  # 54706


if __name__ == '__main__':
    main()
