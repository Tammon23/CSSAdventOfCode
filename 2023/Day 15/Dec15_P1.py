from typing import List

file = "example_input.txt"
# file = "input.txt"


def solve(data: List[str]) -> int:
    total = 0
    for step in data:
        cur = 0
        for ch in step:
            cur += ord(ch)
            cur *= 17
            cur %= 256

        total += cur
    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        initialization_sequence = f.read().strip("\n").split(",")

    print(solve(initialization_sequence))
