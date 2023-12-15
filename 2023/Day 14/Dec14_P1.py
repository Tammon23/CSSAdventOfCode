from typing import List

file = "example_input.txt"
# file = "input.txt"


def solve(data: List[List[str]]) -> int:
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            if val == "O":
                next_r = r - 1
                while next_r >= 0 and data[next_r][c] == ".":
                    next_r -= 1

                data[next_r + 1][c] = "O"
                if r != next_r + 1:
                    data[r][c] = "."

    return sum(r * row.count("O") for r, row in enumerate(reversed(data), 1))


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        platform = [list(row) for row in f.read().splitlines()]

    print(solve(platform))
