from typing import Tuple, List

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> Tuple[List[str], List[int]]:
    spring, encoding = t.split(" ")
    return list(spring), list(map(int, encoding.split(",")))


def is_valid(line: List[str], encoding: List[int]) -> bool:
    return list(map(len, filter(lambda x: x != "", "".join(line).split(".")))) == encoding


def solve(data: Tuple[List[str], List[int]], i=0) -> int:
    spring, encoding = data

    if i == len(spring):
        return 1 if is_valid(spring, encoding) else 0

    cur_total = 0
    if spring[i] != "?":
        cur_total += solve(data, i + 1)

    else:
        sping_c = spring.copy()

        for sym in ["#", "."]:
            sping_c[i] = sym
            cur_total += solve((sping_c, encoding), i + 1)

    return cur_total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())

    print(sum(solve(row) for row in inputs))
