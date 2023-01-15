import os

input_path = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'

mapper = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    'win': 6,
    "draw": 3
}


def part1():
    file = open(input_path)
    acc = 0
    for line in file:
        real_line = line.replace('\n', '')
        [opp, me] = real_line.split(' ')
        play_points = mapper[me]
        acc += play_points
        win = me == 'X' and opp == 'C' or me == 'Y' and opp == 'A' or me == 'Z' and opp == 'B'
        draw = me == 'X' and opp == 'A' or me == 'Y' and opp == 'B' or me == 'Z' and opp == 'C'
        if draw:
            acc += mapper['draw']
        if win:
            acc += mapper['win']

    return acc


def part2():
    file = open(input_path)
    acc = 0
    mapper = {
        'A': {
            'X': {
                'me': 'C',
                'score': 0 + 3
            },
            "Y": {
                'me': 'A',
                'score': 3 + 1
            },
            'Z': {
                'me': 'B',
                "score": 6 + 2
            }
        },
        'B': {
            'X': {
                'me': 'A',
                'score': 0 + 1
            },
            'Y': {
                'me': 'B',
                'score': 3 + 2
            },
            "Z": {
                'me': 'C',
                'score': 6 + 3
            }
        },
        'C': {
            'X': {
                'me': 'B',
                'score': 0 + 2
            },
            'Y': {
                'me': 'C',
                'score': 3 + 3
            },
            "Z": {
                'me': 'A',
                'score': 6 + 1
            }
        }
    }
    for line in file:
        real_line = line.replace('\n', '')
        [opp, result] = real_line.split(' ')
        acc += mapper[opp][result]['score']
    return acc


def main():
    print(part2())


if __name__ == '__main__':
    main()
