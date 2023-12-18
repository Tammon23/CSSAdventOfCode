from collections import namedtuple
from queue import PriorityQueue
from typing import List

file = "example_input.txt"
# file = "input.txt"


def solve(data: List[List[int]]) -> int:
    Point = namedtuple("Point", "HeatLoss Row Col FacingRow FacingCol Depth")
    q = PriorityQueue()
    q.put(Point(0, 0, 0, 1, 0, 0))
    q.put(Point(0, 0, 0, 0, 1, 0))
    seen = {(0, 0, 1, 0, 0): 0, (0, 0, 0, 1, 0): 0}

    goal = (len(data) - 1, len(data[0]) - 1)

    while not q.empty():
        point = q.get()

        if (point.Row, point.Col) == goal:
            return point.HeatLoss

        key = (point.Row, point.Col, point.FacingRow, point.FacingCol, point.Depth)
        if point.HeatLoss < seen[key]:
            continue

        dirs = []
        if point.Depth < 10:
            dirs.append((point.FacingRow, point.FacingCol))  # continue going straight

        if point.Depth >= 4:
            dirs.append((point.FacingCol, -point.FacingRow))  # turn right
            dirs.append((-point.FacingCol, point.FacingRow))  # turn left

        for dr, dc in dirs:
            r = dr + point.Row
            c = dc + point.Col
            if 0 <= r < len(data) and 0 <= c < len(data[0]):
                heat_loss = point.HeatLoss + data[r][c]
                key = (r, c, dr, dc, point.Depth + 1 if (dr, dc) == (point.FacingRow, point.FacingCol) else 1)
                # no way to get to start or no better way -> update best cost
                if key not in seen or heat_loss < seen[key]:
                    seen[key] = heat_loss
                    q.put(Point(heat_loss, *key))
    return -1


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = [list(map(int, x)) for x in f.read().splitlines()]

    print(solve(inputs))
