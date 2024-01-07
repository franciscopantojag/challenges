from curses.ascii import isdigit
from functools import reduce
import re
from os import path

input_path = path.join(path.dirname(__file__), 'input.txt')


def complete_num_given_pos(symb_col: 'int', line: 'str'):
    if not ((symb_col >= 0) and (symb_col <= len(line) - 1)):
        return

    num_str = line[symb_col]
    if not num_str.isdigit():
        return

    idx = symb_col + 1

    while idx <= (len(line) - 1):
        curr_char = line[idx]
        if curr_char.isdigit():
            num_str += curr_char
        else:
            break
        idx += 1

    idx = symb_col - 1

    while idx >= 0:
        curr_char = line[idx]
        if curr_char.isdigit():
            num_str = f'{curr_char}{num_str}'

        else:
            break
        idx -= 1

    return int(num_str)


def get_nums_for_columns(cols: 'list[int]', line: 'str'):
    res_raw = [complete_num_given_pos(col, line) for col in cols]
    result = [num for num in res_raw if num != None]

    return result


def get_nums_for_line(symb_col: 'int', line: 'str'):
    cols = [symb_col]
    if not line[symb_col].isdigit():
        cols += [symb_col + 1, symb_col - 1]

    return get_nums_for_columns(cols, line)


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
                    lambda acc, line_to_process: acc + get_nums_for_line(
                        symb_col, line_to_process),
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
