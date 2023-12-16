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


def move(r, c, dir):
    rmod, cmod = dirs[dir]
    return r + rmod, c + cmod, dir


def solve(floor: List[List[str]]) -> Set[Tuple[int, int, str]]:
    seen = set()
    q = deque([(0, 0, "r")])

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

    return seen


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        # inputs = map(clean_input, f.read().splitlines())
        inputs = [list(x) for x in f.read().splitlines()]

    reduced = {(x, y) for x, y, _ in solve(inputs)}
    total = 0
    for r, c in reduced:
        if 0 > r or r >= len(inputs) or 0 > c or c >= len(inputs[0]):
            continue
        total += 1

    print(total)
