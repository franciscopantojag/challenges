import os

input_path = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'


with open(input_path) as file:
    instructions = [line.replace('\n', '').split(' ') for line in file]


vector_by_direction = {
    'U': [0, 1],
    'R': [1, 0],
    'D': [0, -1],
    'L': [-1, 0]
}


def add_vectors(v1: 'list[int]', v2: 'list[int]'):
    [x1, y1] = v1
    [x2, y2] = v2
    return [x1 + x2, y1 + y2]


def build_tail_movement(head: 'list[int]', tail: 'list[int]'):
    [head_x, head_y] = head
    [tail_x, tail_y] = tail
    raw_movement_x = head_x - tail_x
    raw_movement_y = head_y - tail_y
    distance_x = abs(raw_movement_x)
    distance_y = abs(raw_movement_y)
    same_row = distance_x == 0
    same_column = distance_y == 0
    same_row_or_column = same_row or same_column
    should_tail_move_x = distance_x > 1
    should_tail_move_y = distance_y > 1

    tail_movement: 'list[int]' = [0, 0]
    should_tail_move = should_tail_move_x or should_tail_move_y
    if should_tail_move:
        raw_movement_x = head_x - tail_x
        if same_row_or_column:
            if should_tail_move_x:
                offset_x_one = 1
                offset_x_two = -1
                movement_x_one = head_x - offset_x_one - tail_x
                movement_x_two = head_x - offset_x_two - tail_x

                movement_x = movement_x_one
                if abs(movement_x_one) > abs(movement_x_two):
                    movement_x = movement_x_two
                tail_movement = [movement_x, 0]
            else:
                offset_y_one = 1
                offset_y_two = -1
                movement_y_one = head_y - offset_y_one - tail_y
                movement_y_two = head_y - offset_y_two - tail_y

                movement_y = movement_y_one
                if abs(movement_y_one) > abs(movement_y_two):
                    movement_y = movement_y_two
                tail_movement = [0, movement_y]
        else:
            offset_x_one = 1 if distance_x >= distance_y else 0
            offset_x_two = -1 if distance_x >= distance_y else 0
            offset_y_one = 1 if distance_y >= distance_x else 0
            offset_y_two = -1 if distance_y >= distance_x else 0
            movement_x_one = head_x - offset_x_one - tail_x
            movement_x_two = head_x - offset_x_two - tail_x
            movement_y_one = head_y - offset_y_one - tail_y
            movement_y_two = head_y - offset_y_two - tail_y

            movement_x = movement_x_one
            if abs(movement_x_one) > abs(movement_x_two):
                movement_x = movement_x_two

            movement_y = movement_y_one
            if abs(movement_y_one) > abs(movement_y_two):
                movement_y = movement_y_two
            tail_movement = [movement_x, movement_y]

    return tail_movement


def part_one():
    head = [0, 0]
    tail = [0, 0]
    tail_positions_set: 'set[str]' = set()
    for instruction in instructions:
        [direction, steps_str] = instruction
        if not steps_str.isdigit():
            [steps_str, direction] = instruction
        steps = int(steps_str)
        vector_move = vector_by_direction[direction]
        for _ in range(steps):
            head = add_vectors(head, vector_move)
            tail_movement = build_tail_movement(head, tail)
            tail = add_vectors(tail, tail_movement)
            tail_positions_set.add(str(tail))
    return len(tail_positions_set)


def part_two():
    head = [0, 0]
    tail_1 = [0, 0]
    tail_2 = [0, 0]
    tail_3 = [0, 0]
    tail_4 = [0, 0]
    tail_5 = [0, 0]
    tail_6 = [0, 0]
    tail_7 = [0, 0]
    tail_8 = [0, 0]
    tail_9 = [0, 0]
    tail_positions_set: 'set[str]' = set()
    for instruction in instructions:
        [direction, steps_str] = instruction
        if not steps_str.isdigit():
            [steps_str, direction] = instruction
        steps = int(steps_str)
        vector_move = vector_by_direction[direction]
        for _ in range(steps):
            head = add_vectors(head, vector_move)
            tail_1_movement = build_tail_movement(head, tail_1)
            tail_1 = add_vectors(tail_1, tail_1_movement)

            tail_2_movement = build_tail_movement(tail_1, tail_2)
            tail_2 = add_vectors(tail_2, tail_2_movement)

            tail_3_movement = build_tail_movement(tail_2, tail_3)
            tail_3 = add_vectors(tail_3, tail_3_movement)

            tail_4_movement = build_tail_movement(tail_3, tail_4)
            tail_4 = add_vectors(tail_4, tail_4_movement)

            tail_5_movement = build_tail_movement(tail_4, tail_5)
            tail_5 = add_vectors(tail_5, tail_5_movement)

            tail_6_movement = build_tail_movement(tail_5, tail_6)
            tail_6 = add_vectors(tail_6, tail_6_movement)

            tail_7_movement = build_tail_movement(tail_6, tail_7)
            tail_7 = add_vectors(tail_7, tail_7_movement)

            tail_8_movement = build_tail_movement(tail_7, tail_8)
            tail_8 = add_vectors(tail_8, tail_8_movement)

            tail_9_movement = build_tail_movement(tail_8, tail_9)
            tail_9 = add_vectors(tail_9, tail_9_movement)

            tail_positions_set.add(str(tail_9))
    return len(tail_positions_set)


def main():
    print(part_one())  # 6209
    print(part_two())  # 2460


if __name__ == '__main__':
    main()
