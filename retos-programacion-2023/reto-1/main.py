NATURAL_TO_LEET = {
    "A": '4',
    "B": 'I3',
    "C": '[',
    "D": ')',
    "E": '3',
    "F": '|=',
    'G': '&',
    'H': '#',
    'I': '1',
    'J': ',_|',
    'K': '>|',
    'L': '1',
    'M': '/\\/\\',
    'N': '^/',
    'O': '0',
    'P': '|*',
    'Q': '(_,)',
    'R': 'I2',
    'S': '5',
    'T': '7',
    'U': '(_)',
    'V': '\/',
    'W': '\/\/',
    'X': '><',
    'Y': 'j',
    'Z': '2',
    '1': 'L',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'b',
    '7': 'T',
    '8': 'B',
    '9': 'g',
    '0': 'o'
}


def transform_text(text: 'str'):
    return ''.join(
        map(lambda char: NATURAL_TO_LEET.get(char.upper(), char), text))


def main():
    print(transform_text('Hola mi nombre es Pedro, y tengo 24 años'))


if __name__ == '__main__':
    main()
