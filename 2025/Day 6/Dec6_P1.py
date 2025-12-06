import re
from functools import reduce

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", t)))


def solve(data: list[list[int]], operators: list[str]) -> int:
    total = 0
    for numbers, op in zip(data, operators):
        if op == "+":
            total += sum(numbers)
        else:
            total += reduce(lambda x,y: x*y, numbers)

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        *numbers, operators = f.read().splitlines()
    numbers = [list(row) for row in zip(*map(clean_input, numbers))]
    operators = re.findall(r"[*+]", operators)

    print(solve(numbers, operators))
