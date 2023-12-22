from math import sqrt, ceil


def get_line_nums(line_num: 'str'):
    return [int(num) for num in line_num.split(':')[1].split()]


def calc_win_ways(time: 'int', record_distance: 'int'):
    # Read about quadratic formula/functions/equations
    x = ((-1 * time) + sqrt((time ** 2) -
                            (4 * -1 * (-1 * record_distance)))) / -2

    return (time + 1) - (2 * ceil(x))


def get_line_num(line_num: 'str'):
    return int(''.join(line_num.split(':')[1].split()))
