from functools import lru_cache

file = "example_input.txt"
# file = "input.txt"

@lru_cache
def solve(row: int, col: int) -> int:
    if col < 0 or col >= len(inputs[0]):
        return set()

    for row in range(row, len(inputs)):
        if inputs[row][col] == "^":
            return {(row, col)} | solve(row, col + 1) | solve(row, col - 1)

    return set()



if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().splitlines()

    print(len(solve(1, inputs[0].index("S"))))
