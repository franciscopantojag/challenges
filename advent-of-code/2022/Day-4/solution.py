import os
from typing import Callable

input_path = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'


def principal(get_is_acc: 'Callable[[list[list[int]]], bool]'):
    sum = 0
    with open(input_path, 'r') as f:
        for l in f:
            line = l.replace('\n', '')
            acc = [[int(num) for num in pair.split('-')]
                   for pair in line.split(',')]
            is_accumulable = get_is_acc(acc)
            if is_accumulable:
                sum += 1
    return sum


def part_two():
    def get_is_acc(acc: 'list[list[int]]'):
        [[x1, x2], [y1, y2]] = acc
        return y1 <= x2 and y1 >= x1 or x1 <= y2 and x1 >= y1
    return principal(get_is_acc)


def part_one():
    def get_is_acc(acc: 'list[list[int]]'):
        [[x1, x2], [y1, y2]] = acc
        return x1 <= y1 <= y2 <= x2 or y1 <= x1 <= x2 <= y2

    return principal(get_is_acc)


def main():
    print(part_two())
    print(part_one())


if __name__ == '__main__':
    main()
