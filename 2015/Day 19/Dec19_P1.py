from collections import defaultdict
import re

file = "example_input.txt"
# file = "input.txt"


def solve(base_compound: list[str]) -> int:

    compound: set[str] = set()
    for index, molecule in enumerate(base_compound):
        old = base_compound[index]
        for new in replacements.get(molecule, []):
            base_compound[index] = new
            compound.add("".join(base_compound))
        base_compound[index] = old

    return len(compound)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        temp_replacements, starting_string = f.read().strip().split("\n\n")

    starting_string = re.compile('[A-Z][a-z]*').findall(starting_string)
    replacements = defaultdict(list)

    for line in temp_replacements.splitlines():
        start, end = line.split(" => ")
        replacements[start].append(end)

    print(solve(starting_string))
