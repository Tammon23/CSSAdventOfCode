from typing import Iterable, Tuple, Set

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> Tuple[Set[str], Set[str]]:
    winning, picked = t.split(":")[1].strip().split("|")
    winning = set(winning.strip().split(" "))
    picked = set(picked.strip().split(" "))

    return winning - {''}, picked - {''}


def solve(data: Iterable[str]) -> int:
    total = 0
    for winning, picked in data:
        winning_numbers = len(winning.intersection(picked))
        if winning_numbers != 0:
            total += 1 << winning_numbers - 1

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.readlines())

    print(solve(inputs))
