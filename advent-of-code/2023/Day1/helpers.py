import re

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

num_as_strs = set(map.keys())


def get_final_num(line: 'str'):
    nums = [char for char in line if char.isdigit()]
    result = int(f'{nums[0]}{nums[-1]}')

    return result


def get_final_num_part_two(line: 'str'):
    line = line.strip()

    numbers_with_indexes = [
        [int(char), index] for index, char in enumerate(line) if char.isdigit()
    ]

    for num_as_str in num_as_strs:
        matches = list(re.finditer(num_as_str, line))
        for match_obj in matches:
            num = map[match_obj.group()]
            num_start_pos = match_obj.start()

            numbers_with_indexes.append([num, num_start_pos])

    final_list = sorted(
        numbers_with_indexes, key=lambda tup: tup[1]
    )

    first = final_list[0][0]
    last = final_list[-1][0]

    return int(f'{first}{last}')
