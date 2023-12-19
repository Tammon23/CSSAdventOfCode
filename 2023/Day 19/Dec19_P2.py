from typing import Dict, Tuple

file = "example_input.txt"
# file = "input.txt"


solutions = []


# side effect, modifies solutions list
def solve(valid_ranges: Dict[str, Tuple[int, int]], cur: str) -> None:
    if cur in "RA":
        if cur == "A":
            solutions.append(valid_ranges)
        return

    for rule, nxt in workflows[cur][:-1]:
        if rule[1] == "<":
            temp = valid_ranges.copy()
            letter, v = rule.split("<")
            old = temp[letter]
            temp[letter] = old[0], min(int(v) - 1, old[1])

            valid_ranges[letter] = int(v), old[1]
            solve(temp, nxt)

        elif rule[1] == ">":
            temp = valid_ranges.copy()
            letter, v = rule.split(">")
            old = temp[letter]
            temp[letter] = max(int(v) + 1, old[0]), old[1]
            valid_ranges[letter] = old[0], int(v)
            solve(temp, nxt)

    solve(valid_ranges, workflows[cur][-1])


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        e = f.read().strip().split("\n\n")[0]

        workflows = {}
        for line in e.split("\n"):
            name, info = line[:-1].split("{")
            t = info.split(",")
            workflows[name] = [p.split(":") for p in t[:-1]] + [t[-1]]

        ranges = {x: (1, 4000) for x in "xmas"}
        solve(ranges, "in")

        ans = 0
        for solution in solutions:
            res = 1
            for lower, upper in solution.values():
                res *= upper - lower + 1
            ans += res

        print(ans)
