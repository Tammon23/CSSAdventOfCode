from collections import defaultdict
from itertools import pairwise

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> tuple[str, int, str]:
    person, _, gain_or_lose, happiness_amount, *_, nbr = t.split(" ")
    happiness_amount = int(happiness_amount)
    if gain_or_lose == "lose":
        happiness_amount = -happiness_amount

    return person, happiness_amount, nbr[:-1]


seen = set()
cycle = []


def solve() -> int:
    if len(cycle) == len(seating):
        cur_happiness = seating[cycle[-1]][cycle[0]] + seating[cycle[0]][cycle[-1]]
        for nbr1, nbr2 in pairwise(cycle):
            cur_happiness += seating[nbr1][nbr2]
            cur_happiness += seating[nbr2][nbr1]

        return cur_happiness

    highest = -1
    for person in seating.keys():
        if person not in seen:
            seen.add(person)
            cycle.append(person)

            highest = max(highest, solve())

            seen.remove(person)
            cycle.pop()

    return highest


if __name__ == "__main__":
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())

    seating = defaultdict(dict)
    for person1, amount, person2 in inputs:
        seating[person1][person2] = amount

    print(solve())
