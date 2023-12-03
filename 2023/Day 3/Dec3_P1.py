from typing import List

file = "example_input.txt"
# file = "input.txt"


def solve(data: List[str]) -> int:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    rowsize = len(data)
    colsize = len(data[0])
    total = 0

    for r, row in enumerate(data):
        isPart = False
        cur_number = ""
        for c, val in enumerate(row):
            if val.isdigit():
                cur_number += val

                for rmod, cmod in dirs:
                    newr = r + rmod
                    newc = c + cmod

                    if isPart or (0 <= newr < rowsize and 0 <= newc < colsize and not data[newr][newc].isdigit() and data[newr][newc] != "." and data[newr][newc] != '\n'):
                        isPart = True

            elif cur_number != "":
                if isPart:
                    total += int(cur_number)
                isPart = False
                cur_number = ""

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(solve(inputs))
