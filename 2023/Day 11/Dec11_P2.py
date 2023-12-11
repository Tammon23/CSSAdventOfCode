from itertools import combinations
from typing import List

file = "example_input.txt"
# file = "input.txt"


def solve(data: List[List[str]]) -> int:
    galaxies = []
    rows = set()
    cols = set()
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            if val == "#":
                galaxies.append((r, c))
                rows.add(r)
                cols.add(c)

    missing_rows = set(range(len(data))) - rows
    missing_cols = set(range(len(data[0]))) - cols

    total = 0
    for s, e in combinations(galaxies, 2):
        x1, y1 = s
        x2, y2 = e
        row = len(missing_rows & set(range(min(x1, x2), max(x1, x2)))) * 999_999
        col = len(missing_cols & set(range(min(y1, y2), max(y1, y2)))) * 999_999

        total += abs(x1 - x2) + row + abs(y1 - y2) + col

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = [list(x) for x in f.read().splitlines()]

    print(solve(inputs))
