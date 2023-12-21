def get_maps(lines: 'list[str]'):
    lines_map: 'list[list[str]]' = []
    curr = []
    for line in lines[1:] + ['map']:
        if 'map' not in line:
            curr.append(line)
        else:
            if len(curr) > 0:
                lines_map.append(curr)
            curr = []

    return [[[int(raw_num) for raw_num in map_line.split()] for map_line in mp] for mp in lines_map]


def calc_val(num: 'int', search: 'list[list[int]]'):
    for arr in search:
        inp_min = arr[1]
        val_to_add = arr[0] - inp_min
        inp_max = inp_min + arr[2]
        if num >= inp_min and num <= inp_max:
            return num + val_to_add
    return num


def get_seed_location(maps: 'list[list[list[int]]]', seed: 'int'):
    curr_val = None
    for val_search in maps:
        curr_val = calc_val(curr_val or seed, val_search)

    if curr_val == None:
        raise Exception('Could not calculate seed location')

    return curr_val
