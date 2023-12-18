from collections import deque
from math import inf
from typing import Any, Iterable, Tuple

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> Tuple[str, int]:
    dir_, l, _ = t.split(" ")
    return dir_, int(l)


def add_tuple(tuple1: Tuple[int, int], tuple2: Tuple[int, int]) -> Tuple[int, int]:
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]


def solve(data: Iterable[str]) -> Any:
    cur = 0, 0
    seen = {cur}

    dirs = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1)
    }

    for direction, walk in data:
        for i in range(walk):
            cur = add_tuple(cur, dirs[direction])
            seen.add(cur)

    min_x = min_y = inf
    max_x = max_y = -inf
    for r, c in seen:
        min_x = min(min_x, r)
        min_y = min(min_y, c)

        max_x = max(max_x, r)
        max_y = max(max_y, c)

    q = deque([(1, 1)])  # assuming the following point is in the box
    while q:
        r, c = q.popleft()

        if (r, c) in seen:
            continue

        seen.add((r, c))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + dr
            nc = c + dc
            q.append((nr, nc))

    return len(seen)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())

    print(solve(inputs))
