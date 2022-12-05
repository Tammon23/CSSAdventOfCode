import re
from textwrap import wrap

file = "example_input.txt"
# file = "input.txt"


def SomeFunction(data):
    crates = []
    pileSizes = 0

    # reading each line until we read all the crate stacks
    for i, line in enumerate(data):
        sub_line = wrap(line.rstrip(), 4, drop_whitespace=False)
        if sub_line[0] == " 1":
            pileSizes = len(sub_line)
            break
        crates.append(sub_line.copy())

    # making each sub_line length uniform and transposing the horizontal stacks into vertical stacks
    crates = list(zip(*[c + [""] * (pileSizes - len(c)) for c in crates]))

    # filtering out each empty line and cleaning up the input
    cratesgroup = [list(filter(lambda x: x != '    ' and len(x), t)) for t in crates]
    cratesgroup = [[c[1] for c in crates] for crates in cratesgroup]

    # doing the stack moving manually
    for line in data[i + 2:]:
        a, b, c = map(int, re.match(r'move (\d+) from (\d+) to (\d+)', line).groups())

        b -= 1
        c -= 1

        old_part = cratesgroup[b][:a]
        cratesgroup[b] = cratesgroup[b][a:]
        cratesgroup[c] = old_part + cratesgroup[c]

    return "".join([t[0] for t in cratesgroup])


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
