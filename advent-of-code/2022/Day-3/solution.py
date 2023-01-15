import os
from string import ascii_lowercase, ascii_uppercase

input_path = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'


def get_val(common):
    value: 'None | int' = None
    try:
        value = ascii_lowercase.index(common) + 1
    except:
        try:
            value = ascii_uppercase.index(common) + 27
        except:
            pass
    return value


def part_one():
    sum = 0
    with open(input_path, 'r') as f:
        for l in f:
            line = l.replace('\n', '')
            length_part = int(len(line) / 2)
            common = list(set(line[:length_part]).intersection(
                line[length_part:]))[0]
            value = get_val(common)
            if (value == None):
                continue
            sum += value
    return sum


def part_two():
    arr: 'list[str]' = []
    sum: 'int' = 0
    with open(input_path, 'r') as f:
        for l in f:
            line = l.replace('\n', '')
            arr.append(line)
            if len(arr) == 3:
                common = list(set(arr[0]).intersection(
                    arr[1]).intersection(arr[2]))[0]
                value = get_val(common)
                if value == None:
                    continue
                sum += value
                arr = []
    return sum


def main():
    print(part_two())


if __name__ == '__main__':
    main()
