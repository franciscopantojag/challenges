import os

input_path = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'

LENGTH = 4

stacks = list[list[str]]


def build_inst(l: 'list[str]'):
    test = list(filter(lambda x: x.isdigit(), l))
    return [int(x) for x in test]


def build_stacks(raw_stacks: 'str'):
    rows = raw_stacks.split('\n')
    indic = rows.pop()
    rows.reverse()
    n_columns = int(list(indic.replace(' ', ''))[-1])
    arr: 'stacks' = [[] for _ in range(n_columns)]
    for row in rows:
        for i in range(1, n_columns + 1):
            letter = list(row[(i-1) * LENGTH:i*LENGTH])[1]
            if letter.isalpha():
                arr[i-1].append(letter)

    return arr


def move(stacks: 'stacks', reverse: 'bool', n_leters: 'int', _from: 'int', to: 'int'):
    letters_move = stacks[_from - 1][-n_leters:]
    if reverse:
        letters_move.reverse()
    stacks[to - 1] = stacks[to - 1] + letters_move
    stacks[_from - 1] = stacks[_from - 1][0:-n_leters]


def get_stacks_instructions():
    with open(input_path, 'r') as f:
        text = f.read()
    [stas, inst] = text.split('\n\n')
    new_inst = [x.split(' ') for x in inst.split('\n')]
    instructions = [build_inst(x) for x in new_inst][:-1]
    stacks = build_stacks(stas)
    return instructions, stacks


def build_res(stacks: 'stacks'):
    return ''.join([column[-1] for column in stacks])


def part_one():
    instructions, stacks = get_stacks_instructions()
    for inst in instructions:
        move(stacks, True, *inst)
    return build_res(stacks)


def part_two():
    instructions, stacks = get_stacks_instructions()
    for inst in instructions:
        move(stacks, False, *inst)
    return build_res(stacks)


def main():
    print(part_one())
    print(part_two())


if __name__ == '__main__':
    main()
