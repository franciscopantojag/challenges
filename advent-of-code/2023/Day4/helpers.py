def get_nums_from_line(line_raw: 'str'):
    nums_raw = line_raw.split(':')[1].strip().split('|')
    [nums_win, nums_have] = [list(map(int, x.split())) for x in nums_raw]

    return [nums_win, nums_have]


def get_number_of_intersections(win: 'list[int]', have: 'list[int]'):
    return len(set(win).intersection(have))


def get_score(number_of_intersections: 'int'):
    if number_of_intersections == 0:
        return 0

    return 2 ** (number_of_intersections - 1)
