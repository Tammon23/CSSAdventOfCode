from collections import defaultdict
from typing import List

file = "example_input.txt"
# file = "input.txt"


def solve(data: List[str]) -> int:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    rowsize = len(data)
    colsize = len(data[0])
    ratios = defaultdict(list)
    star_positions = set()

    for r, row in enumerate(data):
        cur_number = ""
        for c, val in enumerate(row):
            if val.isdigit():
                cur_number += val

                for rmod, cmod in dirs:
                    newr = r + rmod
                    newc = c + cmod

                    if 0 <= newr < rowsize and 0 <= newc < colsize and data[newr][newc] == "*":
                        star_positions.add((newr, newc))

            elif cur_number != "":
                for pos in star_positions:
                    ratios[pos].append(int(cur_number))
                cur_number = ""
                star_positions = set()

    return sum(ratio[0] * ratio[1] if len(ratio) == 2 else 0 for ratio in ratios.values())


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(solve(inputs))
