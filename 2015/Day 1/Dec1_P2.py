from typing import Iterable

file = "example_input.txt"
# file = "input.txt"


def solve(data: Iterable[str]) -> int:
    floor = 0

    for i, ch in enumerate(data):
        if ch == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            return i + 1

    return -1


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(f.read().strip())

    print(solve(inputs))
