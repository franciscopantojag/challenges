from os import path
from helpers import get_maps, calc_val

input_path = path.join(path.dirname(__file__), 'input.txt')


def part_one():
    result: 'int | None' = None

    with open(input_path) as f:
        lines = [line.strip()
                 for line in f.readlines() if len(line.strip()) > 0]
        seeds = [int(num) for num in lines[0].split(':')[1].split()]

        maps = get_maps(lines)

        for seed in seeds:
            first_val_search = maps[0]
            val1 = calc_val(seed, first_val_search)

            second_val_search = maps[1]
            val2 = calc_val(val1, second_val_search)

            third_val_search = maps[2]
            val3 = calc_val(val2, third_val_search)

            fourth_val_search = maps[3]
            val4 = calc_val(val3, fourth_val_search)

            fifth_val_search = maps[4]
            val5 = calc_val(val4, fifth_val_search)

            sixth_val_search = maps[5]
            val6 = calc_val(val5, sixth_val_search)

            seven_val_search = maps[6]
            val7 = calc_val(val6, seven_val_search)

            if result == None or val7 < result:
                result = val7

    return result


def main():
    print(part_one())  # 621354867


if __name__ == '__main__':
    main()
