def get_maps(lines: 'list[str]'):
    curr: 'list[tuple[int, int, int]]' = []
    lines_map: 'list[list[tuple[int, int, int]]]' = []

    for line in lines[3:]:
        line = line.strip()

        if line and 'map' not in line:
            inp = [int(raw_num) for raw_num in line.split()]
            range_min_source = inp[1]
            range_max_source = range_min_source + inp[2] - 1
            add_to_source = inp[0] - range_min_source

            curr.append((range_min_source, range_max_source, add_to_source))
        elif curr:
            lines_map.append(curr)
            curr = []

    if curr:
        lines_map.append(curr)

    return lines_map


def calc_val(num: 'int', search: 'list[tuple[int, int, int]]'):
    for [range_min_source, range_max_source, add_to_source] in search:
        if num >= range_min_source and num <= range_max_source:
            return num + add_to_source

    return num


def get_seed_location(maps: 'list[list[tuple[int, int, int]]]', seed: 'int'):
    curr_val = calc_val(seed, maps[0])

    for val_search in maps[1:]:
        curr_val = calc_val(curr_val, val_search)

    return curr_val
