from collections import deque
from typing import List, Set, Tuple

file = "example_input.txt"
# file = "input.txt"

dirs = {
    "d": (1, 0),
    "u": (-1, 0),
    "l": (0, -1),
    "r": (0, 1)
}


def move(r: int, c: int, facing:str):
    rmod, cmod = dirs[facing]
    return r + rmod, c + cmod, facing


def solve(floor: List[List[str]], start_row: int, start_col: int, start_facing: str) -> int:
    seen = set()
    q = deque([(start_row, start_col, start_facing)])

    while q:
        r, c, dir = q.popleft()

        if (r, c, dir) in seen:
            continue

        seen.add((r, c, dir))

        if 0 > r or r >= len(floor) or 0 > c or c >= len(floor[0]):
            continue

        cur = floor[r][c]

        if cur == ".":
            q.append(move(r, c, dir))

        elif cur == "|":
            if dir in "rl":
                q.append(move(r, c, "u"))
                q.append(move(r, c, "d"))

            else:
                q.append(move(r, c, dir))

        elif cur == "-":
            if dir in "ud":
                q.append(move(r, c, "l"))
                q.append(move(r, c, "r"))
            else:
                q.append(move(r, c, dir))

        elif cur == "/":
            if dir == "r":
                q.append(move(r, c, "u"))
            elif dir == "l":
                q.append(move(r, c, "d"))
            elif dir == "u":
                q.append(move(r, c, "r"))
            elif dir == "d":
                q.append(move(r, c, "l"))

        else:
            if dir == "r":
                q.append(move(r, c, "d"))
            elif dir == "l":
                q.append(move(r, c, "u"))
            elif dir == "u":
                q.append(move(r, c, "l"))
            elif dir == "d":
                q.append(move(r, c, "r"))

    return score(seen)


def score(seen: Set[Tuple[int, int, str]]) -> int:
    reduced = {(x, y) for x, y, _ in seen}
    total = 0
    for r, c in reduced:
        if 0 > r or r >= len(inputs) or 0 > c or c >= len(inputs[0]):
            continue
        total += 1

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = [list(x) for x in f.read().splitlines()]

    best = 0
    for i in range(0, len(inputs)):
        best = max(best,
                   solve(inputs, i, 0, "r"),
                   solve(inputs, i, len(inputs[0]) - 1, "l")
                   )

    for i in range(0, len(inputs[0])):
        best = max(best,
                   solve(inputs, 0, i, "d"),
                   solve(inputs, len(inputs) - 1, i, "u")
                   )

    print(best)
