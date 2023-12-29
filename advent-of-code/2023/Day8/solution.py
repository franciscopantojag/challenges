from functools import reduce
from math import lcm
from os import path

input_path = path.join(path.dirname(__file__), 'input.txt')


def reducer(acc: 'dict[str, list[str]]', line: 'str'):
    left, right = line.strip().split(' = ')
    return {**acc, left: right[1:-1].split(', ')}


def part_one():
    with open(input_path) as f:
        [instructions, _, *map_lines] = f.readlines()
        map_dict = reduce(reducer, map_lines, dict())

    curr_key = 'AAA'
    result = 0

    while curr_key != 'ZZZ':
        for instruction in instructions.strip():
            instruction_index = 0 if instruction == 'L' else 1
            curr_key = map_dict[curr_key][instruction_index]

            result += 1

    return result


def part_two():
    with open(input_path) as f:
        [instructions, _, *map_lines] = f.readlines()
        map_dict = reduce(reducer, map_lines, dict())
        starts = [key for key in map_dict.keys() if key.endswith('A')]

    def get_loop(start: 'str'):
        current = start
        steps = 0
        while not current.endswith('Z'):
            for instruction in instructions.strip():
                edge_index = 0 if instruction == 'L' else 1
                current = map_dict[current][edge_index]
                steps += 1

        return steps

    loop_sizes = [get_loop(start) for start in starts]

    return lcm(*loop_sizes)


def main():
    print(part_one())  # 20777
    print(part_two())  # 13289612809129


if __name__ == '__main__':
    main()
