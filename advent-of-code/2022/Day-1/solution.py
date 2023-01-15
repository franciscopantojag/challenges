import os

input_path = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'


def part1():
    file = open(input_path)
    result = 0
    acc = 0
    for line in file:
        real_line = line.replace('\n', '')
        if (real_line == ''):
            if result < acc:
                result = acc
            acc = 0
        else:
            acc += int(real_line)
    file.close()
    return result


def part2():
    file = open(input_path)
    result = []
    acc = 0
    for line in file:
        real_line = line.replace('\n', '')
        if (real_line == ''):
            result.append(acc)
            acc = 0
        else:
            acc += int(real_line)
    file.close()
    result.sort(reverse=True)
    return sum(result[:3])


def main():
    print(part2())


if __name__ == '__main__':
    main()
