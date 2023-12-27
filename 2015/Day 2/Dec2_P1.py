from typing import Iterable

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> Iterable[int]:
    return map(int, t.split("x"))


def solve(data: Iterable[Iterable[int]]) -> int:
    ans = 0
    for box in data:
        l, w, h = box

        ans += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, l * h, w * h)

    return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())

    print(solve(inputs))
