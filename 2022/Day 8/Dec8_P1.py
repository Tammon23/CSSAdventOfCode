# file = "example_input.txt"
file = "input.txt"


def SomeFunction(data):
    trees = []
    for line in data:
        trees.append(list(map(int, list(line.rstrip()))))

    maxx = len(trees)
    maxy = len(trees[0])
    seen = [[False] * maxy for _ in range(maxx)]

    for r in range(len(trees)):
        # right to left
        highest = float("-inf")
        for c in range(len(trees[0])):
            if trees[r][c] > highest:
                seen[r][c] = True
                highest = trees[r][c]

        # left to right
        highest = float("-inf")
        for c in range(len(trees[0]) - 1, -1, -1):
            if trees[r][c] > highest:
                seen[r][c] = True
                highest = trees[r][c]

    transposed = list(zip(*trees))
    for r in range(len(transposed)):
        # right to left
        highest = float("-inf")
        for c in range(len(transposed[0])):
            if transposed[r][c] > highest:
                seen[c][r] = True
                highest = transposed[r][c]

        # left to right
        highest = float("-inf")
        for c in range(len(transposed[0]) - 1, -1, -1):
            if transposed[r][c] > highest:
                seen[c][r] = True
                highest = transposed[r][c]

    return sum(sum(l) for l in seen)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
