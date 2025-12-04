from typing import Any, Iterable

# file = "example_input.txt"
file = "input.txt"

def solve(data: Iterable[str]) -> Any:
    total = 0
    for bank in data:
        best = 0
        for i in range(len(bank)-1):
            for j in range(i+1,len(bank)):
                best = max(best, int(bank[i]+bank[j]))

        total += best
    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().splitlines()

    print(solve(inputs))
