import re
from math import inf

# file = "example_input_p2.txt"
file = "input.txt"


def solve(current_compound: str) -> int:
    steps = 0
    shortest_compound = ""
    while current_compound != 'e':
        shortest_len = inf

        for start, end in replacements:
            for re_match in re.finditer(end, current_compound):
                res = current_compound[:re_match.start()] + start + current_compound[re_match.end():]

                if shortest_len > len(res):
                    shortest_len = len(res)
                    shortest_compound = res

        current_compound = shortest_compound
        steps += 1
    return steps


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        temp_replacements, starting_string = f.read().strip().split("\n\n")

    replacements = [line.split(" => ") for line in temp_replacements.splitlines()]

    # Observations:
    # 1. all molecule replacements go from a short string to a long string
    #   for the example input this is not true, e => H for example breaks this prog
    #   solution: change while to include e => cur
    # 2. brute forcing without and special tricks isn't needed
    (print
     (solve(starting_string)))
