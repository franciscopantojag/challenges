from functools import reduce
from os import path
from helpers import calc_win_ways, get_line_num, get_line_nums

input_path = path.join(path.dirname(__file__), 'input.txt')


def part_one():
    with open(input_path) as f:
        [times, record_distances] = [
            get_line_nums(line) for line in f.readlines()
        ]

        result = reduce(
            lambda a, b: a * calc_win_ways(b[1], record_distances[b[0]]),
            enumerate(times),
            1
        )

        return result


def part_two():
    with open(input_path) as f:
        [time, record_distance] = [
            get_line_num(line) for line in f.readlines()
        ]

        return calc_win_ways(time, record_distance)


def main():
    print(part_one())  # 170000
    print(part_two())  # 20537782


if __name__ == '__main__':
    main()
