from typing import Iterable

file = "input.txt"


def clean_input(t: str) -> str:
    return t.strip("\n")


def solve(data: Iterable[str]) -> int:
    sum = 0
    for line in data:
        number = 0
        for c in line:
            if c.isdigit():
                number = int(c) * 10
                break

        for c in reversed(line):
            if c.isdigit():
                number += int(c)
                break

        sum += number
    return sum


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.readlines())

    print(solve(inputs))
