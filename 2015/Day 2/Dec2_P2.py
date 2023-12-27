from typing import Iterable

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> Iterable[int]:
    return map(int, t.split("x"))


def solve(data: Iterable[Iterable[int]]) -> int:
    ans = 0
    for box in data:
        l, w, h = box
        ans += min(2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h) + l * w * h

    return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().strip().splitlines())

    print(solve(inputs))
