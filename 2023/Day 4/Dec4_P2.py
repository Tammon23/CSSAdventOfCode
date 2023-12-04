from typing import Tuple, Set, List

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> Tuple[Set[str], Set[str]]:
    winning, picked = t.split(":")[1].strip().split("|")
    winning = set(winning.strip().split(" "))
    picked = set(picked.strip().split(" "))

    return winning - {''}, picked - {''}


def solve(data: List[str]) -> int:
    card_counts = [1] * len(data)

    for card, (winning, picked) in enumerate(data):
        winning_numbers = len(winning.intersection(picked))
        for i in range(winning_numbers):
            card_counts[card + i + 1] += card_counts[card]

    return sum(card_counts)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(solve(inputs))
