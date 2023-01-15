import os

input_path = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'

LENGTH_PART_ONE = 4
LENGTH_PART_TWO = 14


def find_n_chars(length: 'int'):
    with open(input_path, 'r') as f:
        content = f.read().replace('\n', '')
    limit = len(content) - (length - 1)
    result = None
    for i in range(limit):
        last_pos = i + length
        word = content[i: last_pos]
        if (len(word) == len(set(word))):
            result = last_pos
            break
    return result


def part_one():
    return find_n_chars(LENGTH_PART_ONE)


def part_two():
    return find_n_chars(LENGTH_PART_TWO)


def main():
    print(part_one())  # 1920
    print(part_two())  # 2334


if __name__ == '__main__':
    main()
