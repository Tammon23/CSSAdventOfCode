from typing import Any, Iterable

# file = "example_input.txt"
file = "input.txt"


def clean_input(t: str) -> Any:
    return [tuple(map(int, range_.split("-"))) for range_ in t.split(",")]


def solve(data: Iterable[tuple[int, int]]) -> Any:
    total = 0
    for start, end in data:
        for i in range(start, end+1):
            test = str(i)
            n = len(test)
            if n > 1 and test[:n//2] == test[n//2:]:
                total += i

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = clean_input(f.read())
        # inputs = f.read().splitlines()

    print(solve(inputs))
