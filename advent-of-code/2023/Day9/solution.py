from os import path

input_path = path.join(path.dirname(__file__), 'input.txt')


def part_one():
    final_result = 0
    with open(input_path) as f:
        for line in f.readlines():
            numbers = [int(num) for num in line.strip().split()]
            numbers_list = [numbers]

            for idx in range(len(numbers) - 1):
                lista: 'list[int]' = []
                list_num = numbers_list[idx]
                for index, num in enumerate(list_num[0:-1]):
                    next_num = list_num[index+1]
                    lista.append(next_num - num)

                final_result += lista[-1]
                numbers_list.append(lista)

            final_result += numbers[-1]

    return final_result


def part_two():
    final_result = 0
    with open(input_path) as f:
        for line in f.readlines():
            numbers = [int(num) for num in line.strip().split()]
            numbers_list = [numbers]
            line_result = numbers[0] * -1

            for idx in range(len(numbers) - 1):
                list_num = numbers_list[idx]
                lista = [
                    list_num[index+1] - num for index, num in enumerate(list_num[0:-1])
                ]

                numbers_list.append(lista)
                line_result = (lista[0] + line_result) * -1

            final_result -= (line_result)

    return final_result


def main():
    print(part_one())  # 1798691765
    print(part_two())  # 1104


if __name__ == '__main__':
    main()
