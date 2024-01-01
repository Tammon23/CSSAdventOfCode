file = "example_input.txt"
# file = "input.txt"


def solve(numRows: int, numCols: int, steps: int) -> int:
    corners = {(0, 0), (numRows - 1, 0), (numRows - 1, numCols - 1), (0, numCols - 1)}
    on_lights = corners.copy()
    for r, row in enumerate(inputs):
        for c, val in enumerate(row):
            if val == "#":
                on_lights.add((r, c))

    for step in range(steps):
        nxt_on = corners.copy()
        for row in range(numRows):
            for col in range(numCols):
                if (row, col) in corners:
                    continue

                num_neighbours_on = 0
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                    nr = row + dr
                    nc = col + dc

                    if (nr, nc) in on_lights:
                        num_neighbours_on += 1

                # on to start with
                if (row, col) in on_lights:
                    if num_neighbours_on in [2, 3]:
                        nxt_on.add((row, col))

                # off to start with
                else:
                    if num_neighbours_on == 3:
                        nxt_on.add((row, col))

        on_lights = nxt_on

    return len(on_lights)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = [list(row) for row in f.read().splitlines()]

    max_rows = len(inputs)
    max_cols = len(inputs[0])

    print(solve(max_rows, max_cols, steps=5))
