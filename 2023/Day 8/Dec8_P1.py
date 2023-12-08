from itertools import cycle

file = "example_input.txt"
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

    cur = "AAA"
    length = 0
    for direction in cycle(instructions):
        length += 1
        if direction == "R":
            cur = mapping[cur][1]
        else:
            cur = mapping[cur][0]

        if cur == "ZZZ":
            break

    print(length)

