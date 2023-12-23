from collections import defaultdict
from typing import Iterable, Generator

file = "example_input.txt"
# file = "input.txt"


brick_id = -1


def clean_input(t: str) -> tuple[tuple[int, ...], tuple[int, ...], int]:
    global brick_id
    left, right = t.split("~")
    left = list(map(int, left.split(",")))
    right = list(map(int, right.split(",")))
    brick_id += 1
    return tuple(left), tuple(right), brick_id


def get_brick_coords(start: tuple[int, ...], end: tuple[int, ...]) -> Generator[tuple[int, ...], None, None]:
    x1, y1, z1 = start
    x2, y2, z2 = end

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                yield x, y, z


def move_z(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return left[:-1] + (left[-1] - 1,), right[:-1] + (right[-1] - 1,)


def solve(data: Iterable[tuple[tuple[int, ...], tuple[int, ...], int]]) -> int:
    board = {}
    floor_height = 0
    bricks = []

    for rock in sorted(data, key=lambda start: start[0][2]):
        old_left, old_right, id_number = rock

        while True:  # bring the rock as far down as possible
            new_left, new_right = move_z(old_left, old_right)
            for x, y, z in get_brick_coords(new_left, new_right):
                if (x, y, z) in board or z <= floor_height:
                    break
            else:
                old_left, old_right = new_left, new_right
                continue

            bricks.append((old_left, old_right, id_number))
            board.update({(x, y, z): id_number for x, y, z in get_brick_coords(old_left, old_right)})

            break

    supported_by = defaultdict(set)
    for brick in bricks:
        left, right, id_number = brick
        for x, y, z in get_brick_coords(*move_z(left, right)):
            if (x, y, z) in board:
                by = board[x, y, z]
                if by != id_number:
                    supported_by[id_number].add(by)

    supports_who = defaultdict(list)
    for id_number, v in supported_by.items():
        for x in v:
            if x != id_number:
                supports_who[x].append(id_number)

    ans = 0
    for brick in range(len(bricks)):
        supporting = supports_who.get(brick, [])
        all_bricks_safe = True
        for s in supporting:
            if len(supported_by[s]) == 1:
                all_bricks_safe = False
                break

        if all_bricks_safe:
            ans += 1

    return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())

    print(solve(inputs))
