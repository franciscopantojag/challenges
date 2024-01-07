from functools import reduce
import re

BAG_POSSIBLE = {
    'red': 12,
    'green': 13,
    'blue': 14
}

COLORS = set(BAG_POSSIBLE.keys())


def get_max_color(line: 'str', color: 'str'):
    color_with_values: 'list[str]' = re.split(
        '[,;]', line.strip().split(':')[1].strip()
    )

    resp = max(
        int(st.strip().split()[0]) for st in color_with_values if color in st
    )

    return resp


def get_game_id(line: 'str'):
    game_id_pos = all(
        get_max_color(line, color) <= BAG_POSSIBLE[color] for color in COLORS
    )

    game_id_raw = int(line.strip().split(':')[0].split()[1])

    return game_id_raw if game_id_pos else 0


def get_power_per_line(line: 'str'):
    power_per_line = reduce(
        lambda acc, color: acc * get_max_color(line, color),
        COLORS,
        1
    )

    return power_per_line
