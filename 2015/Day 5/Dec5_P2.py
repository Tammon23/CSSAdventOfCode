from collections import defaultdict
from typing import Iterable

file = "example_input.txt"
# file = "input.txt"


def solve(data: Iterable[str]) -> int:
    ans = 0
    for string in data:
        overlapping = defaultdict(set)
        property1 = False
        for i in range(len(string) - 1):
            cur = string[i:i + 2]

            if cur in overlapping and len(overlapping[cur] - {(i - 1)}) > 0:
                property1 = True
                break
            else:
                overlapping[cur].add(i)

        for i in range(len(string) - 2):
            if string[i] == string[i + 2]:
                break
        else:
            continue

        if property1:
            ans += 1

    return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().splitlines()

    print(solve(inputs))
