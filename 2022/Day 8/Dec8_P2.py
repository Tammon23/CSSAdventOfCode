file = "example_input.txt"
# file = "input.txt"


def SomeFunction(data):
    trees = []
    for line in data:
        trees.append(list(map(int, list(line.rstrip()))))

    maxx = len(trees)
    maxy = len(trees[0])
    seen = [[1] * maxy for _ in range(maxx)]

    for r in range(len(trees)):
        for i in range(len(trees[0])):  # right to left
            count = 0
            for j in range(i + 1, len(trees[0])):
                count += 1
                if trees[r][i] <= trees[r][j]:
                    break
            seen[r][i] *= count if count != 0 else 1

        for i in range(len(trees[0]) - 1, -1, -1):  # left ot right
            count = 0
            for j in range(i - 1, -1, -1):
                count += 1
                if trees[r][i] <= trees[r][j]:
                    break
            seen[r][i] *= count if count != 0 else 1

    transposed = list(zip(*trees))
    for r in range(len(transposed)):
        for i in range(len(transposed[0])):  # up to down
            count = 0
            for j in range(i + 1, len(transposed[0])):
                count += 1
                if transposed[r][i] <= transposed[r][j]:
                    break
            seen[i][r] *= count if count != 0 else 1

        for i in range(len(transposed[0]) - 1, -1, -1):  # down to up
            count = 0
            for j in range(i - 1, -1, -1):
                count += 1
                if transposed[r][i] <= transposed[r][j]:
                    break
            seen[i][r] *= count if count != 0 else 1

    highest = 1
    for r, row in enumerate(seen):
        for c, val in enumerate(row):
            if c in [0, len(seen) -1] or r in [0, len(seen[0]) - 1]:
                continue
            else:
                highest = max(highest, val)

    return highest


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
