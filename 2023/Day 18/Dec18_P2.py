from typing import Iterable, Tuple

file = "example_input.txt"
# file = "input.txt"

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def clean_input(t: str) -> Tuple[int, int]:
    num = t.split(" ")[2]
    return int(num[-2]), int(num[2:-2], 16)


def solve(data: Iterable[Tuple[int, int]]) -> int:
    cur = 0, 0
    boundary_points = [cur]
    perimeter = 0
    for direction, walk in data:
        facing = dirs[direction]
        cur = (cur[0] + facing[0] * walk, cur[1] + facing[1] * walk)
        boundary_points.append(cur)
        perimeter += walk

    # shoelace formula
    boundary_points.reverse()
    area = 0
    for i in range(len(boundary_points) - 1):
        x1, y1 = boundary_points[i]
        x2, y2 = boundary_points[i + 1]
        area += (y1 + y2) * (x1 - x2)

    area //= 2

    # picks algorithm
    # i = inner, A = Area, b = Boundary
    # A = b/2 + i - 1 => i = A - b/2 + 1
    # modify to include 1/2 unit offset
    # i = A - b/2 + b + 1 => A + b/2 + 1
    return area + (perimeter // 2) + 1


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())

    print(solve(inputs))
