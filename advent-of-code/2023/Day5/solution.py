from os import path
from helpers import get_maps, calc_val, get_seed_location

input_path = path.join(path.dirname(__file__), 'input.txt')


def part_one():
    result: 'int | None' = None

    with open(input_path) as f:
        lines = [line.strip()
                 for line in f.readlines() if len(line.strip()) > 0]
        seeds = [int(num) for num in lines[0].split(':')[1].split()]

        maps = get_maps(lines)

        for seed in seeds:
            seed_location = get_seed_location(maps, seed)

            if result == None or seed_location < result:
                result = seed_location

    return result


def main():
    print(part_one())  # 621354867


if __name__ == '__main__':
    main()
