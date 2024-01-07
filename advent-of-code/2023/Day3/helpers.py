from functools import reduce
import re
from os import path

input_path = path.join(path.dirname(__file__), 'input.txt')


def complete_num_given_pos(symb_col: 'int', line: 'str'):
    is_col_in_line = (symb_col >= 0) and (symb_col <= len(line) - 1)
    if not is_col_in_line:
        return

    num_str = line[symb_col]
    if not num_str.isdigit():
        return

    idx_right = symb_col + 1

    while idx_right <= (len(line) - 1) and line[idx_right].isdigit():
        num_str += line[idx_right]
        idx_right += 1

    idx_left = symb_col - 1

    while idx_left >= 0 and line[idx_left].isdigit():
        num_str = f'{line[idx_left]}{num_str}'
        idx_left -= 1

    return int(num_str)


def get_nums_for_line(symb_col: 'int', line: 'str'):
    cols = [symb_col]
    if not line[symb_col].isdigit():
        cols += [symb_col + 1, symb_col - 1]

    res_raw = [complete_num_given_pos(col, line) for col in cols]
    result = [num for num in res_raw if num != None]

    return result


def get_results():
    result = 0
    gear_ratios_sum = 0

    with open(input_path) as f:
        lines = f.readlines()
        for row, line in enumerate(lines):
            line = line.strip()

            line_symbol_matches = re.finditer(r'[^0-9.]', line)
            for symb in line_symbol_matches:
                symb_col = symb.start()

                lines_to_process = [line]
                if row > 0:
                    # we have a prev line
                    lines_to_process.append(lines[row - 1])

                has_next_line = (row + 1) <= (len(lines) - 1)
                if has_next_line:
                    lines_to_process.append(lines[row + 1])

                nums_for_this_symbol = reduce(
                    lambda acc, line_to_process:
                        acc + get_nums_for_line(symb_col, line_to_process),
                    lines_to_process,
                    []
                )

                result += sum(nums_for_this_symbol)

                gear_ratio = 0
                if len(nums_for_this_symbol) == 2:
                    gear_ratio = nums_for_this_symbol[0] * \
                        nums_for_this_symbol[1]

                gear_ratios_sum += gear_ratio

    return result, gear_ratios_sum
