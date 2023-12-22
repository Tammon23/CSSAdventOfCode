from collections import deque
from typing import Tuple

file = "example_input.txt"
# file = "input.txt"


def solve(start_position: Tuple[int, int]) -> int:
    global inputs

    q = deque([start_position])
    steps_left = 6  # <==============
    last_seen = None
    while steps_left >= 0 and q:

        seen = set()
        for _ in range(len(q)):
            r, c = q.popleft()

            if (r, c) in seen:
                continue

            seen.add((r, c))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < len(inputs) and 0 <= nc < len(inputs[0]) and inputs[nr][nc] == ".":
                    q.append((nr, nc))

        last_seen = seen
        steps_left -= 1

    return len(last_seen-set(q))


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = [list(x) for x in f.read().splitlines()]

        start = None
        for r, row in enumerate(inputs):
            for c, col in enumerate(row):
                if inputs[r][c] == "S":
                    start = r, c

    inputs[start[0]][start[1]] = "."
    print(solve(start))
