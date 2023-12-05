from os import path

input_path = path.join(path.dirname(__file__), 'input.txt')


def main():
    sum = 0

    with open(input_path) as f:
        for line in f.readlines():
            nums = [x for x in line if x.isdigit()]
            nums_len = len(nums)

            dig_first = nums[0]
            dig_last = dig_first if nums_len == 1 else nums[-1]
            num = int(f'{dig_first}{dig_last}')
            sum += num

    print(sum)  # 55447


if __name__ == '__main__':
    main()
