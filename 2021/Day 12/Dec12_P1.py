# file = "example_input.txt"
file = "input.txt"


def SomeFunction(cave, visited=None):
    if visited is None:
        visited = set()

    if cave == "end":
        return 1

    total = 0
    for next_cave in inputs[cave]:
        if next_cave in visited:
            continue
        total += SomeFunction(next_cave, visited | {cave} if cave == cave.lower() else visited)
    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = {}
        for line in f.readlines():
            l, r = line.strip().split("-")
            inputs[l] = inputs.get(l, []) + [r]
            inputs[r] = inputs.get(r, []) + [l]

    print(SomeFunction("start"))
