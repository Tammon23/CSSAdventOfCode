from typing import Any, Iterable

# file = "example_input.txt"
file = "input.txt"


def clean_input(t: str) -> Any:
    value = int(t[1:])
    return -value if t[0] == "L" else value


def solve(data: Iterable[int]) -> Any:
    current = 50
    ans = 0

    for number in data:
        current = (current + number) % 100
        if current == 0:
            ans += 1

    return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())
        # inputs = f.read().splitlines()

    print(solve(inputs))
