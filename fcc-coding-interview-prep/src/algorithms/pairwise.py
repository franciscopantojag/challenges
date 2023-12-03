# https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/pairwise

def pairwise(arr: 'list[int]', arg: 'int'):
    lista = []
    for index, x in enumerate(arr):
        test = arg - x
        if test in arr:
            test2 = list(filter(lambda x: isinstance(x, int), [idx if test == erre else None for idx,
                                                               erre in enumerate(arr)]))

            for al in test2:
                er = index not in lista
                er2 = al not in lista
                er3 = index != al
                er4 = er and er2 and er3
                if er4:
                    lista.append(index)
                    lista.append(al)

    print(sum(lista))


def main():
    pairwise([1, 4, 2, 3, 0, 5], 7)  # 11
    pairwise([1, 3, 2, 4], 4)  # 1
    pairwise([1, 1, 1], 2)  # 1
    pairwise([0, 0, 0, 0, 1, 1], 1)  # 10
    pairwise([], 100)  # 0


if __name__ == '__main__':
    main()
