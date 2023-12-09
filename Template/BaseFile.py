from typing import Any, Iterable

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> Any:
    return t


def solve(data: Iterable[str]) -> Any:
    return data


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        # inputs = map(clean_input, f.read().splitlines())
        inputs = f.read().splitlines()

    print(solve(inputs))
