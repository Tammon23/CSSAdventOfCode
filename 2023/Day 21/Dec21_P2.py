from collections import deque

file = "input.txt"


def solve(start_r: int, start_c: int, goal: int) -> int:
    global inputs
    q = deque([(start_r, start_c)])
    steps_left = 0
    last_seen = None
    while steps_left <= goal:
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
        steps_left += 1

    return len(last_seen - set(q))


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = [list(x) for x in f.read().splitlines()]

        sr = sc = -1
        for r, row in enumerate(inputs):
            for c, col in enumerate(row):
                if inputs[r][c] == "S":
                    sr, sc = r, c

    inputs[sr][sc] = "."

    size = len(inputs) - 1
    steps = 26501365
    ans = 0

    max_width = (steps // (size + 1)) - 1  # with of entire tessellated lot

    ans += solve(sr, sc, (size + 1) * 2) * ((max_width + 1) // 2 * 2) ** 2
    ans += solve(sr, sc, (size + 1) * 2 + 1) * (max_width // 2 * 2 + 1) ** 2

    # cardinals
    ans += solve(size, sc, size) + solve(sr, 0, size) + solve(0, sc, size) + solve(sr, size, size)

    small = 0
    for r, c in [(size, 0), (size, size), (0, 0), (0, size)]:
        small += solve(r, c, (size + 1) // 2 - 1)

    ans += small * (max_width + 1)

    big = 0
    for r, c in [(size, 0), (size, size), (0, 0), (0, size)]:
        big += solve(r, c,  (size + 1) * 3 // 2 - 1)

    ans += big * max_width

    print(ans)
