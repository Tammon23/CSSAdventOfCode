from typing import Any, Iterable

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> Any:
    return list(map(int, t.split("-")))

def solve(fresh: list[list[int]], available: list[int]) -> Any:
    ans = 0
    fresh.sort(key=lambda x: x[0])

    for ingred in available:
        for start, end in fresh:
            if start <= ingred <= end:
                ans += 1
                break
            if start > ingred:
                break
    return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().split("\n\n")
        fresh, available = list(map(clean_input, inputs[0].splitlines())), list(map(int, inputs[1].splitlines()))

    print(solve(fresh, available))
