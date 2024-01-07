from os import path
from helpers import get_nums_from_line, get_number_of_intersections, get_score

input_path = path.join(path.dirname(__file__), 'input.txt')


def get_score_per_line(line: 'str'):
    line = line.strip()
    [nums_win, nums_have] = get_nums_from_line(line)

    number_of_intersections = get_number_of_intersections(
        nums_win, nums_have
    )

    return get_score(number_of_intersections)


def part_one():
    with open(input_path) as f:
        result = sum(get_score_per_line(line) for line in f.readlines())
        return result


def part_two():
    total = 0

    with open(input_path) as f:
        copies_by_card_no: 'dict[int, int]' = dict()

        for index, line_raw in enumerate(f.readlines()):
            card_no = index + 1

            [nums_win, nums_have] = get_nums_from_line(line_raw)

            number_of_intersections = get_number_of_intersections(
                nums_win, nums_have)

            card_count = copies_by_card_no.get(card_no, 0) + 1

            total += card_count

            for copy_target in range(card_no + 1, card_no + 1 + number_of_intersections):
                copies_by_card_no[copy_target] = card_count + \
                    copies_by_card_no.get(copy_target, 0)

    return total


def main():
    print(part_one())  # 33950
    print(part_two())  # 14814534


if __name__ == '__main__':
    main()
