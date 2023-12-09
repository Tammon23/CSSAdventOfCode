from typing import Iterable, List

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> List[int]:
    return list(map(int, t.strip("\n").split(" ")))


def solve(data: Iterable[str]) -> int:
    total = 0
    for seq in data:
        cur_seq = [seq]

        while any(cur_seq[-1]):
            cur_seq.append([cur_seq[-1][i + 1] - cur_seq[-1][i] for i in range(len(cur_seq[-1]) - 1)])

        cur = cur_seq[-1][0]
        for i in range(len(cur_seq) - 2, -1, -1):
            cur = cur_seq[i][0] - cur

        total += cur

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.readlines())

    print(solve(inputs))
