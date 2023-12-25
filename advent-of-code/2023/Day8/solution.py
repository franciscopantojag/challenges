from os import path

input_path = path.join(path.dirname(__file__), 'input.txt')


def part_one():
    with open(input_path) as f:
        lines = f.readlines()
        instructions = lines[0].strip()
        map_dict: 'dict[str, list[str]]' = {}

        for line in lines[2:]:
            left, right = line.strip().split(' = ')
            map_dict[left] = right[1:-1].split(', ')

    curr_key = 'AAA'
    result = 0

    while curr_key != 'ZZZ':
        instruction = instructions[result % len(instructions)]
        left_or_right = 0 if instruction == 'L' else 1
        curr_key = map_dict[curr_key][left_or_right]

        result += 1

    return result


def main():
    print(part_one())  # 20777


if __name__ == '__main__':
    main()
