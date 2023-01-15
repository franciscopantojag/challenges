import os

input_path = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'

with open(input_path) as file:
    cicle = 1
    register_X = 1
    positions = (20, 60, 100, 140, 180, 220, 260, 300)

    index = 0
    result = 0
    for line in file:
        compare = positions[index]
        if line.startswith('noop'):
            cicle += 1
            if cicle == compare:
                signal = compare * register_X
                result += signal
                index += 1
        else:
            increment = int(line.replace('\n', '').split(' ')[1])
            test = compare - 1 == cicle
            if test:
                signal = compare * register_X
                result += signal
                index += 1
            register_X += increment
            cicle += 2
            if cicle == compare:
                signal = compare * register_X
                result += signal
                index += 1
    print(result)
