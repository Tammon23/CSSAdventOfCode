from collections import deque
from typing import Tuple, List, Set

file = "example_input.txt"
# file = "input.txt"


def get_start(data: List[List[str]]) -> Tuple[int, int]:
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col == "S":
                return r, c


def get_path_points(data: List[List[str]]) -> Set[Tuple[int, int]]:
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

    return seen


def enclosed_area() -> List[List[int]]:
    pipe_dirs = {
        "|": {U, D},
        "-": {L, R},
        "L": {U, R},
        "J": {U, L},
        "7": {D, L},
        "F": {D, R}
    }

    s_values = set(pipe_dirs)
    if sx == 0 or D not in pipe_dirs[grid[sx - 1][sy]]:
        s_values -= set("|LJ")

    if sx == maxr - 1 or U not in pipe_dirs[grid[sx + 1][sy]]:
        s_values -= set("|7F")

    if sy == 0 or R not in pipe_dirs[grid[sx][sy - 1]]:
        s_values -= set("-J7")

    if sy == maxc - 1 or L not in pipe_dirs[grid[sx][sy + 1]]:
        s_values -= set("-LF")

    s, = s_values
    grid[sx][sy] = s

    new_grid = [[False] * maxc * 3 for _ in range(maxr * 3)]

    for r, c in points:

        cur = grid[r][c]
        r = r * 3 + 1
        c = c * 3 + 1
        new_grid[r][c] = True

        if U in pipe_dirs[cur]:
            new_grid[r - 1][c] = True

        if D in pipe_dirs[cur]:
            new_grid[r + 1][c] = True

        if L in pipe_dirs[cur]:
            new_grid[r][c - 1] = True

        if R in pipe_dirs[cur]:
            new_grid[r][c + 1] = True

    return new_grid


def solve(new_grid: List[List[int]]) -> int:
    outer = set()
    q = deque([(0, 0)])
    total = 0

    while q:
        r, c = q.popleft()
        if (r, c) in outer:
            continue

        outer.add((r, c))

        for rmod, cmod in [U, D, R, L]:
            nr = r + rmod
            nc = c + cmod

            if 0 <= nr < maxr * 3 and 0 <= nc < maxc * 3 and not new_grid[nr][nc]:
                q.append((nr, nc))

    for r in range(len(grid)):
        for c in range(len(grid[0])):

            if (r, c) in points or (r * 3 + 1, c * 3 + 1) in outer:
                continue

            total += 1

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        grid = [list(x) for x in f.read().splitlines()]

    sx, sy = get_start(grid)
    U = -1, 0
    D = 1, 0
    L = 0, -1
    R = 0, 1

    maxr, maxc = len(grid), len(grid[0])
    points = get_path_points(grid)

    print(solve(enclosed_area()))
