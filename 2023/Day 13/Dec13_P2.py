from typing import List

file = "example_input.txt"
# file = "input.txt"


def get_diff(left: str, right: str) -> int:
    result = 0
    for ll, rr in zip(left, right):
        if ll != rr:
            result += 1
    return result


def solve(data: List[str]) -> None | int:
    size = len(data)
    for x in range(size - 1):
        smudge_found = False
        i = x
        j = x + 1

        while i >= 0 and j < size:
            num_diff = get_diff(data[i], data[j])

            if num_diff > 1:
                break

            if num_diff == 1 and smudge_found:
                break

            if num_diff == 1:
                smudge_found = True

            i -= 1
            j += 1

        if (i == -1 or j == size) and smudge_found:
            return x + 1

    return None


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = [x.split("\n") for x in f.read().strip().split("\n\n")]

    total = 0

    for pattern in inputs:
        res = solve(pattern)
        if res is None:  # transpose
            pattern = list(zip(*pattern))
            total += solve(pattern)
        else:
            total += res * 100

    print(total)
