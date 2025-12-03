from typing import Any, Iterable

# file = "example_input.txt"
file = "input.txt"


def clean_input(t: str) -> Any:
    return [tuple(map(int, range_.split("-"))) for range_ in t.split(",")]


def is_invalid(x):
    size = len(x)
    for k in range(2, size + 1):
        n = len(x)
        if n % k == 0:
            repeat_len = n // k
            subpart = x[:repeat_len]
            if all(x[j:j + repeat_len] == subpart for j in range(repeat_len, size, repeat_len)):
                return True
    return False

def solve(data: Iterable[tuple[int, int]]) -> Any:
    total = 0
    for start, end in data:
        for i in range(start, end+1):
            g = is_invalid(str(i))
            if g:
                total += i

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = clean_input(f.read())
        # inputs = f.read().splitlines()

    print(solve(inputs))
