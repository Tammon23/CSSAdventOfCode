from functools import lru_cache
from typing import Any

file = "example_input.txt"
# file = "input.txt"

@lru_cache
def solve(row: int, col: int) -> Any:
    maxRow = len(inputs)
    if col < 0 or col >= len(inputs[0]):
        return 0

    while row < maxRow:
        if inputs[row][col] == ".":
            row += 1

        elif inputs[row][col] == "^":
            return 1 + solve(row, col + 1) + solve(row, col - 1)

    return 0


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().splitlines()

    print(solve(1, inputs[0].index("S")) + 1)

