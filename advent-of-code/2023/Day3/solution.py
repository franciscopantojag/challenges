from os import path
import re
from helpers import is_index_inside, get_top_or_bottom_comparison, has_non_numeric_or_dot_chars

input_path = path.join(path.dirname(__file__), 'input.txt')


def part_one():
    result = 0
    with open(input_path) as f:
        lines = f.readlines()
        for row, line in enumerate(lines):
            matches = re.finditer('\\d+', line)

            for match_obj in matches:
                num = int(match_obj.group())
                num_pos_start = match_obj.start()
                num_pos_end = match_obj.end()

                str_compare = ''

                # prev row compare
                prev_row_num = row - 1
                has_prev_row = is_index_inside(lines, prev_row_num)

                if has_prev_row:
                    prev_line = lines[prev_row_num]
                    str_compare = get_top_or_bottom_comparison(
                        prev_line, num_pos_start, num_pos_end)

                # left char compare
                char_left_col = num_pos_start - 1
                if is_index_inside(line, char_left_col):
                    str_compare += line[char_left_col]

                # right char compare
                if is_index_inside(line, num_pos_end):
                    str_compare += line[num_pos_end]

                # next row compare
                next_row_num = row + 1
                has_next_row = is_index_inside(lines, next_row_num)

                if has_next_row:
                    next_line = lines[next_row_num]
                    str_compare += get_top_or_bottom_comparison(
                        next_line, num_pos_start, num_pos_end)

                str_compare = str_compare.replace('\n', '')

                if has_non_numeric_or_dot_chars(str_compare):
                    result += num

    return result


def main():
    print(part_one())  # 535235


if __name__ == '__main__':
    main()
