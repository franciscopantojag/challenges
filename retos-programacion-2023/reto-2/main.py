SCORES = ['Love', 15, 30, 40]

P1 = 'P1'
P2 = 'P2'


def tenis(sequence: 'list[str]'):
    p1 = p2 = 0

    for play in sequence:
        if play == P1:
            if p2 == 4:
                p2 -= 1
            else:
                p1 += 1
        elif play == P2:
            if p1 == 4:
                p1 -= 1
            else:
                p2 += 1
        else:
            continue

        if p1 >= 5:
            print('Ha ganado P1')
            return
        if p2 >= 5:
            print('Ha ganado P2')
            return

        if p1 == p2 and p1 == 3:
            print('Deuce')
            continue
        if p1 == 4:
            print('Ventaja P1')
            continue
        if p2 == 4:
            print('Ventaja P2')
            continue
        print(f'{SCORES[p1]} - {SCORES[p2]}')


def main():
    tenis([P1, P1, P2, P2, P1, P2, P1, P2, P1, P1, P2, P2])


if __name__ == '__main__':
    main()
