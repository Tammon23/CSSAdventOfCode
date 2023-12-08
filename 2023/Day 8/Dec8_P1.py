from itertools import cycle

# file = "example_input.txt"
file = "input.txt"


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().splitlines()

    mapping = {}
    instructions, _, *maps = inputs
    for line in maps:
        key, value = line.split(" = ")
        mapping[key] = value[1:-1].split(", ")

    cur = "AAA"
    for length, direction in enumerate(cycle(instructions), 1):
        cur = mapping[cur][1 if direction == "R" else 0]

        if cur == "ZZZ":
            break

    print(length)

