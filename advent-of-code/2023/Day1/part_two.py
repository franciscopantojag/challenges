
from os import path

input_path = path.join(path.dirname(__file__), 'input.txt')

map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

num_as_strs = [*map.keys()]


def build_num(line: 'str'):
    nums_with_indexes: 'list[list[int]]' = []

    for num_str in num_as_strs:
        if num_str in line:
            num = map[num_str]
            nums_with_indexes.append([num, line.index(num_str)])

    for index, char in enumerate(line):
        if char.isdigit():
            nums_with_indexes.append([int(char), index])

    nums_with_indexes.sort(key=take_second)
    print(nums_with_indexes)
    digit_first = nums_with_indexes[0][0]
    digit_last = digit_first if len(
        nums_with_indexes) == 1 else nums_with_indexes[-1][0]

    final_num = int(f'{digit_first}{digit_last}')
    print(final_num)
    return final_num


def take_second(a: 'list[int]'): return a[1]


def main():
    sum = 0

    with open(input_path) as f:
        for line in f.readlines():
            line_num = build_num(line)
            sum += line_num
    print(sum)


if __name__ == '__main__':
    main()
