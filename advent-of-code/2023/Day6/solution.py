from os import path

from Day6.helpers import calc_win_ways, get_line_num, get_line_nums

input_path = path.join(path.dirname(__file__), 'input.txt')


def part_one():
    result = 1
    with open(input_path) as f:
        [line_times, line_record_distances] = f.readlines()
        times = get_line_nums(line_times)
        record_distances = get_line_nums(line_record_distances)

        for index, time in enumerate(times):
            record_distance = record_distances[index]

            result *= calc_win_ways(time, record_distance)

    return result


def part_two():
    with open(input_path) as f:
        [line_time, line_record_distance] = f.readlines()
        time = get_line_num(line_time)
        record_distance = get_line_num(line_record_distance)

        return calc_win_ways(time, record_distance)


def main():
    print(part_one())  # 170000
    print(part_two())  # 20537782


if __name__ == '__main__':
    main()
