from typing import List

file = "example_input.txt"
# file = "input.txt"


def solve(data: List[str]) -> None | int:
    # try row sym
    size = len(data)
    for x in range(size-1):
        i = x
        j = i + 1
        while i >= 0 and j < size and data[i] == data[j]:
            i -= 1
            j += 1

        if i == -1 or j == size:
            return x + 1

    return None


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = [x.split("\n") for x in f.read().strip().split("\n\n")]

    total = 0
    for pattern in inputs:
        res = solve(pattern)

        if res is None: # transpose
            pattern = list(zip(*pattern))
            total += solve(pattern)
        else:
            total += res * 100

    print(total)