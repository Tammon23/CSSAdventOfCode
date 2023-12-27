from typing import Iterable

file = "example_input.txt"
# file = "input.txt"


def solve(data: Iterable[str]) -> int:
    floor = 0

    for ch in data:
        if ch == "(":
            floor += 1
        else:
            floor -= 1

    return floor


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(f.read().strip())

    print(solve(inputs))
