from itertools import cycle
from math import lcm


# file = "example_input.txt"
file = "example_input_p2.txt"
# file = "input.txt"


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().splitlines()

    mapping = {}
    instructions, _, *maps = inputs
    for line in maps:
        key, value = line.split(" = ")
        mapping[key] = value[1:-1].split(", ")

    cur = filter(lambda x: x.endswith("A"), mapping.keys())
    counts = set()

    for i, cur_node in enumerate(cur):
        length = 0
        for direction in cycle(instructions):
            length += 1
            cur_node = mapping[cur_node][1 if direction == "R" else 0]

            if cur_node.endswith("Z"):
                break

        counts.add(length)

    print(lcm(*counts))

