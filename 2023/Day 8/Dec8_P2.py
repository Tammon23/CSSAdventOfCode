from collections import defaultdict
from itertools import cycle
from math import lcm


file = "example_input.txt"
# file = "example_input_p2.txt"
# file = "input.txt"


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()
    mapping = {}
    instructions = inputs[0].strip()
    for line in inputs[2:]:
        key, value = line.strip().split("=")
        mapping[key.strip()] = [value.strip()[1:4], value.strip()[6:9]]

    cur = []

    for key in mapping:
        if key[-1] == "A":
            cur.append(key)

    counts = defaultdict(int)
    for i in range(len(cur)):
        length = 0
        cur_node = cur[i]
        for direction in cycle(instructions):
            length += 1

            if direction == "R":
                cur_node = mapping[cur_node][1]
            else:
                cur_node = mapping[cur_node][0]

            if cur_node[-1] == "Z":
                break

        counts[length] += 1

    print(lcm(*list(counts.keys())))

