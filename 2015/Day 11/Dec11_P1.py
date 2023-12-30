from itertools import pairwise
from typing import Iterable

# file = "example_input.txt"
file = "input.txt"


def iter_string(string: list[int]) -> Iterable[list[int]]:
    a = ord('a')
    z = ord('z')

    i = len(string) - 1

    while True:
        string[i] += 1
        temp = i
        if string[i] > z:
            while temp >= 0 and string[temp] >= z:
                string[temp] = a
                temp -= 1

            if temp < 0:
                return string

            if temp != i:
                string[temp] += 1

        yield string


def solve(data: list[int]) -> str | None:
    disallowed = {ord(x) for x in "iol"}

    for nxt in iter_string(data):
        found_straight = False

        for i in range(len(nxt) - 2):
            if nxt[i] == (nxt[i + 1] - 1) == (nxt[i + 2] - 2):
                found_straight = True
                break

        if found_straight:
            first_pair = None
            found_pairs = False
            for x, y in pairwise(nxt):
                if x == y:
                    if first_pair is None:
                        first_pair = x, y
                    elif first_pair != (x, y):
                        found_pairs = True
                        break

            if found_pairs and not set(nxt) & disallowed:
                return ''.join(map(chr, nxt))

    return None


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = [ord(char) for char in f.read().strip()]

    print(solve(inputs))
