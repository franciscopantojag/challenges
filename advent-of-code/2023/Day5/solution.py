from os import path
from helpers import get_maps, calc_val, get_seed_location

input_path = path.join(path.dirname(__file__), 'input.txt')


def part_one():
    with open(input_path) as f:
        lines = f.readlines()

        maps = get_maps(lines)
        seeds = [int(num) for num in lines[0].split(':')[1].split()]

        result = min(
            get_seed_location(maps, seed) for seed in seeds
        )

        return result


def main():
    print(part_one())  # 621354867


if __name__ == '__main__':
    main()
