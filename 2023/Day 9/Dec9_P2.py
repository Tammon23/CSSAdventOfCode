from typing import Iterable, List

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> List[int]:
    return list(map(int, t.split(" ")))


def solve(data: Iterable[str]) -> int:
    total = 0
    for seq in data:
        cur_seq = [seq]

        while any(cur_seq[-1]):
            cur_seq.append([cur_seq[-1][i + 1] - cur_seq[-1][i] for i in range(len(cur_seq[-1]) - 1)])

        cur = 0
        for calc_seq in reversed(cur_seq):
            cur = calc_seq[0] - cur

        total += cur

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())

    print(solve(inputs))
