from os import path
from helpers import get_nums_from_line, get_number_of_intersections, get_score

input_path = path.join(path.dirname(__file__), 'input.txt')


def part_one():
    result = 0
    with open(input_path) as f:
        for line_raw in f.readlines():
            [num_win, num_have] = get_nums_from_line(line_raw)

            number_of_intersections = get_number_of_intersections(
                num_win, num_have)

            result += get_score(number_of_intersections)
    return result


def part_two():
    copies_by_line: 'dict[int, int]' = dict()

    with open(input_path) as f:
        lines = f.readlines()
        lines_no = len(lines)

        for index, line_raw in enumerate(lines):
            line_no = index + 1

            [num_win, num_have] = get_nums_from_line(line_raw)

            number_of_intersections = get_number_of_intersections(
                num_win, num_have)

            line_copies_no = copies_by_line.get(line_no, 0)

            if line_no <= lines_no:
                for copy_target in range(line_no + 1, line_no + 1 + number_of_intersections):
                    copies_by_line[copy_target] = 1 + line_copies_no + \
                        copies_by_line.get(copy_target, 0)

    total_copies = sum(copies_by_line.values())

    return total_copies + lines_no


def main():
    print(part_one())  # 33950
    print(part_two())  # 14814534


if __name__ == '__main__':
    main()
