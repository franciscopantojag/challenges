from os import path
from helpers import get_game_id, get_max_color

input_path = path.join(path.dirname(__file__), 'input.txt')

COLORS = {'red', 'green', 'blue'}

BAG_POSSIBLE = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def part_one():
    sum = 0
    with open(input_path) as f:
        for line in f.readlines():
            game_id = get_game_id(line)
            if game_id is None:
                continue

            game_id_pos = True

            for color in COLORS:
                bag_color_possible = BAG_POSSIBLE.get(color)
                if bag_color_possible is None:
                    continue

                max_color = get_max_color(line, color)

                if max_color > bag_color_possible:
                    game_id_pos = False
                    break

            if game_id_pos:
                sum += game_id
    return sum


def part_two():
    sum = 0

    with open(input_path) as f:
        for line in f.readlines():
            power_per_line = 1

            for color in COLORS:
                max_color = get_max_color(line, color)

                power_per_line *= max_color
            sum += power_per_line
    return sum


def main():
    print(part_one())  # 2685
    print(part_two())  # 83707


if __name__ == '__main__':
    main()
