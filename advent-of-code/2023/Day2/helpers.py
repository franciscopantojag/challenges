import re


def get_game_id(line: 'str'):
    game_id_match = re.search('Game\\s\\d+', line)
    if game_id_match is None:
        return None

    game_id = int(game_id_match.group().split(' ')[1])

    return game_id


def get_max_color(line: 'str', color: 'str'):
    reg_exp = f'\\d+\\s{color}'
    color_matches: 'list[str]' = re.findall(reg_exp, line)

    max_color = max([int(color_match.split(' ')[0])
                    for color_match in color_matches])

    return max_color
