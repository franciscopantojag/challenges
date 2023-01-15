import os
import time

input_path = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'


with open(input_path) as file:
    matrix = [[int(x) for x in list(line.replace('\n', ''))] for line in file]

n_columns = len(matrix[0])
n_rows = len(matrix)


def part_one():
    print(f'Start time: {time.perf_counter()}')
    result = (n_columns * 2) + ((n_rows * 2) - 4)
    for i in range(1, n_rows - 1):
        for j in range(1, n_columns - 1):
            n_look = matrix[i][j]
            num_left = max(matrix[i][:j])
            num_right = max(matrix[i][j+1:])
            is_visible_right_or_left = n_look > num_left or n_look > num_right
            if is_visible_right_or_left:
                result += 1
                continue

            num_top = max([l[j] for l in matrix][:i])
            is_visible_top = n_look > num_top
            if is_visible_top:
                result += 1
                continue

            num_bottom = max([l[j] for l in matrix][i+1:])
            is_visible_bottom = n_look > num_bottom
            if is_visible_bottom:
                result += 1
                continue
    print(f'End time: {time.perf_counter()}')
    return result


def build_get_count(n_look: 'int'):
    def get_count(nums: 'list[int]'):
        blockers = [index for index, x in enumerate(nums) if x >= n_look]
        if len(blockers) == 0:
            return len(nums)
        return blockers[0] + 1
    return get_count


def part_two():
    result = 1
    for i in range(1, n_rows - 1):
        for j in range(1, n_columns - 1):
            n_look = matrix[i][j]
            get_count = build_get_count(n_look)

            nums_left = matrix[i][:j]
            nums_left.reverse()
            count_left = get_count(nums_left)

            nums_right = matrix[i][j+1:]
            count_right = get_count(nums_right)

            nums_top = [l[j] for l in matrix][:i]
            nums_top.reverse()
            count_top = get_count(nums_top)

            nums_bottom = [l[j] for l in matrix][i+1:]
            count_bottom = get_count(nums_bottom)

            n_total = count_left * count_right * count_top * count_bottom
            if n_total > result:
                result = n_total
    return result


def main():
    print(part_one())  # 1849
    print(part_two())  # 201600


if __name__ == '__main__':
    main()
