from typing import Iterable
import Helper

file = "example_input.txt"
# file = "input.txt"


def solve(data: Iterable[str]) -> int:
    cur = 0, 0
    visited = {cur}
    for direction in data:
        if direction == ">":
            cur = Helper.add_tuple(cur, Helper.Directions.RIGHT)

        elif direction == "<":
            cur = Helper.add_tuple(cur, Helper.Directions.LEFT)

        elif direction == "^":
            cur = Helper.add_tuple(cur, Helper.Directions.UP)

        else:
            cur = Helper.add_tuple(cur, Helper.Directions.DOWN)

        visited.add(cur)
    return len(visited)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(f.read().rstrip())

    print(solve(inputs))
