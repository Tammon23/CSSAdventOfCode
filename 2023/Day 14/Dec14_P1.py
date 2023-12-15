from typing import Any, Iterable

# file = "example_input.txt"
file = "input.txt"


def clean_input(t: str) -> Any:
    return t


def solve(data: Iterable[str]) -> Any:
    # for row in data:
    #     print("".join(row))
    # print("-"*9)
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            if val == "O":
                next_r = r - 1
                while next_r >= 0 and data[next_r][c]  == ".":
                    next_r -= 1

                data[next_r+1][c] = "O"
                if r != next_r + 1:
                    data[r][c] = "."

    total = 0
    for r, row in enumerate(reversed(data), 1):
        total += r * row.count("O")
    # for row in data:
    #     print("".join(row))
    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        # inputs = map(clean_input, f.read().splitlines())
        inputs = [list(row) for row in f.read().splitlines()]

    print(solve(inputs))
