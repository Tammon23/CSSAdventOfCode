from typing import Any, Iterable

# file = "example_input.txt"
file = "input.txt"


def clean_input(t: str) -> Any:
    return list(map(int, list(t)))

def solve(data: Iterable[str]) -> Any:
    total = 0
    for bank in data:
        n = len(bank)
        best = ''
        for i in range(12):
            x = max(bank[:n - 12 + i + 1])
            bank = bank[bank.index(x) + 1:]
            n = len(bank)
            best += x
        total += int(best)
    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        # inputs = map(clean_input, f.read().splitlines())
        inputs = f.read().splitlines()
    print(solve(inputs))
