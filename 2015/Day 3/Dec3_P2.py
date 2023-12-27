from typing import Iterable
import Helper

file = "example_input.txt"
# file = "input.txt"


def solve(data: Iterable[str]) -> int:
    cur = 0, 0
    visited = {cur}
    turns = [cur, cur]

    i = 0
    for direction in data:
        cur = turns[i]
        if direction == ">":
            cur = Helper.add_tuple(cur, Helper.Directions.RIGHT)

        elif direction == "<":
            cur = Helper.add_tuple(cur, Helper.Directions.LEFT)

        elif direction == "^":
            cur = Helper.add_tuple(cur, Helper.Directions.UP)

        else:
            cur = Helper.add_tuple(cur, Helper.Directions.DOWN)

        turns[i] = cur
        i = (i + 1) % 2
        visited.add(cur)
    return len(visited)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(f.read().rstrip())

    print(solve(inputs))
