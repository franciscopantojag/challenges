def get_last_element(arr: 'list[str]'):
    try:
        return arr[len(arr) - 1]
    except:
        return None


dictionary = {
    "SOUTH": "NORTH",
    "NORTH": "SOUTH",
    "EAST": "WEST",
    "WEST": "EAST"
}


def reduce_directions(directions: 'list[str]') -> list[str]:
    dirs: 'list[str]' = []
    for dir in directions:
        last_element = get_last_element(dirs)
        opp = dictionary.get(dir, None)
        if opp == last_element:
            dirs.pop()
        else:
            dirs.append(dir)

    return dirs


plan = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(reduce_directions(plan))
