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
    total = 0

    with open(input_path) as f:
        copies_by_line: 'dict[int, int]' = dict()
        lines = f.readlines()
        cards_no = len(lines)

        for index, line_raw in enumerate(lines):
            card_no = index + 1

            [num_win, num_have] = get_nums_from_line(line_raw)

            number_of_intersections = get_number_of_intersections(
                num_win, num_have)

            card_count = copies_by_line.get(card_no, 0) + 1

            total += card_count

            if card_no <= cards_no:
                for copy_target in range(card_no + 1, card_no + 1 + number_of_intersections):
                    copies_by_line[copy_target] = card_count + \
                        copies_by_line.get(copy_target, 0)

    return total


def main():
    print(part_one())  # 33950
    print(part_two())  # 14814534


if __name__ == '__main__':
    main()
