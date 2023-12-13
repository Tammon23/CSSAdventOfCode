from functools import cache
from typing import Tuple

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> Tuple[str, Tuple[int, ...]]:
    spring, encoding = t.split(" ")
    return "?".join([spring for _ in range(5)]), tuple(map(int, encoding.split(","))) * 5


@cache
def solve(data: Tuple[str, Tuple[int, ...]]) -> int:
    spring, encoding = data

    if not spring:
        return encoding == ()

    if not encoding:
        return "#" not in spring

    cur_total = 0
    if spring[0] in "?.":  # ? ==> .
        cur_total += solve((spring[1:], encoding))

    if (spring[0] in "#?"  # ? ==> #
            and encoding[0] <= len(spring)
            and "." not in spring[:encoding[0]]):

        if encoding[0] == len(spring) or spring[encoding[0]] != "#":
            cur_total += solve((spring[encoding[0] + 1:], encoding[1:]))

    return cur_total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())

    print(sum(solve(row) for row in inputs))
