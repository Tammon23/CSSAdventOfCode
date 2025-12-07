from functools import lru_cache
from typing import Any

file = "example_input.txt"
# file = "input.txt"

@lru_cache
def solve(row: int, col: int) -> Any:
    maxRow = len(inputs)
    if col < 0 or col >= len(inputs[0]):
        return set()

    while row < maxRow:
        if inputs[row][col] == ".":
            row += 1

        elif inputs[row][col] == "^":
            return {(row,col)} | solve(row, col + 1) | solve(row, col - 1)

    return set()



if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().splitlines()

    print(len(solve(1, inputs[0].index("S"))))
