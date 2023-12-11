from collections import deque
from typing import Tuple, List

file = "example_input.txt"
# file = "input.txt"


def get_start(data: List[List[str]]) -> Tuple[int, int]:
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col == "S":
                return r, c


def solve(data: List[List[str]], sx: int, sy: int) -> int:
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    movemap = {
        (-1, 0): "S|LJ",  # up
        (1, 0): "S|7F",  # down
        (0, -1): "S-J7",  # left
        (0, 1): "S-LF"  # right
    }

    seen = {(sx, sy)}
    q = deque([(sx, sy)])
    while q:
        r, c = q.popleft()
        cur = data[r][c]

        for rmod, cmod in dirs:
            nr = r + rmod
            nc = c + cmod

            if (0 <= nr < len(data)
                    and 0 <= nc < len(data[0])
                    and (nr, nc) not in seen
                    and cur in movemap[rmod, cmod]
                    and data[nr][nc] != "S"
                    and data[nr][nc] in movemap[rmod * -1, cmod * -1]):
                seen.add((nr, nc))
                q.append((nr, nc))

    return len(seen) // 2


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        grid = [list(x) for x in f.read().splitlines()]

    print(solve(grid, *get_start(grid)))
