from typing import Mapping

file = "example_input.txt"
# file = "input.txt"


def solve(parts: Mapping[str, int]) -> int:
    cur = "in"

    while cur not in "RA":
        rules = workflows[cur]
        for rule, nxt in rules[:-1]:
            if rule[1] == "<":
                letter, v = rule.split("<")
                if parts[letter] < int(v):
                    cur = nxt
                    break

            elif rule[1] == ">":
                letter, v = rule.split(">")
                if parts[letter] > int(v):
                    cur = nxt
                    break
        else:
            cur = rules[-1]

    return cur == "A"


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        e = f.read().strip().split("\n\n")

        workflows = {}
        for line in e[0].split("\n"):
            name, info = line[:-1].split("{")
            t = info.split(",")
            workflows[name] = [p.split(":") for p in t[:-1]] + [t[-1]]

        ratings = []
        for line in e[1].split("\n"):
            temp = {}
            for value in line[1:-1].split(","):
                key, v = value.split("=")
                temp[key] = int(v)
            ratings.append(temp)

        total = 0
        for part in ratings:
            if solve(part):
                total += sum(part.values())

        print(total)

