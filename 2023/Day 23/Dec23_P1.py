import Helper
import sys

sys.setrecursionlimit(99999)

file = "example_input.txt"
# file = "input.txt"


depth = 0
seen = {(0, 1)}


def dfs(start_r: int, start_c: int, length: int = 0) -> int:

    if start_r == len(inputs) - 1 and start_c == len(inputs[0]) - 2:
        return length

    best_length = -1
    for rmod, cmod in Helper.strs_to_directions.values():
        r = start_r + rmod
        c = start_c + cmod

        if 0 <= r < len(inputs) and 0 <= c < len(inputs[0]) and inputs[r][c] != "#" and (r, c) not in seen:
            seen.add((r, c))

            if (inputs[r][c] == "." or
                    inputs[r][c] == ">" and (rmod, cmod) == Helper.Directions.RIGHT or
                    inputs[r][c] == "v" and (rmod, cmod) == Helper.Directions.DOWN or
                    inputs[r][c] == "<" and (rmod, cmod) == Helper.Directions.LEFT or
                    inputs[r][c] == "^" and (rmod, cmod) == Helper.Directions.UP):

                best_len = dfs(r, c, length + 1)
                best_length = max(best_length, best_len)

            seen.remove((r, c))
    return best_length if best_length != -1 else -1


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = [list(x) for x in f.read().splitlines()]

    print(dfs(0, 1))
