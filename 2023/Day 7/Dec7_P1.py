from typing import Iterable, Tuple
from collections import Counter

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> Tuple[str, int]:
    hand, bid = t.strip("\n").split(" ")
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('9') + 2))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))

    return hand, int(bid)


def solve(data: Iterable[str]) -> int:

    score = []
    for hand, bid in data:
        c = sorted(Counter(hand).values())
        if c == [5]:
            cur = 7
        elif c == [1, 4]:
            cur = 6
        elif c == [2, 3]:
            cur = 5
        elif c == [1, 1, 3]:
            cur = 4
        elif c == [1, 2, 2]:
            cur = 3
        elif c == [1, 1, 1, 2]:
            cur = 2
        else:
            cur = 1

        score.append((cur, hand, bid))

    score.sort()
    winnings = 0
    for i, (_, _, bid) in enumerate(score, 1):
        winnings += i * bid

    return winnings


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.readlines())

    print(solve(inputs))
