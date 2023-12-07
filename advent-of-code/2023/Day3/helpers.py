import re


def has_non_numeric_or_dot_chars(input_string: 'str'):
    return bool(re.search(r'[^0-9.]', input_string))


def is_index_inside(st: 'str|list[str]', index: 'int'):
    return index >= 0 and index <= len(st) - 1


def get_top_or_bottom_comparison(prev_or_next_line: 'str', start: 'int', end: 'int'):
    start_pos = max(start - 1, 0)

    end_pos_raw = end + 1
    end_pos = end_pos_raw if is_index_inside(
        prev_or_next_line, end_pos_raw) else end

    return prev_or_next_line[start_pos: end_pos]
