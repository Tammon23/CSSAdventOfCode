# file = "example_input.txt"
file = "input.txt"

def pprint(dots):
    maxx = max(list(zip(*dots))[0]) + 1
    maxy = max(list(zip(*dots))[1]) + 1

    paper = [[" "] * (maxx + 1) for _ in range(maxy + 1)]
    for x, y in dots:
        paper[y][x] = "#"

    return "\n".join([''.join(row) for row in paper])

def SomeFunction(dots, folds):
    for axis, index in folds:
        index = int(index)
        if axis == "x":
            dots = [(x if x < index else index - (x-index), y) for x,y in dots]
        else:
            dots = [(x, y if y < index else index - (y-index)) for x,y in dots]

    return dots


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        dots, folds = f.read().split("\n\n")
        dots = [list(map(int, pair.split(","))) for pair in dots.split("\n")]
        folds = [fold.replace("fold along ", "").split("=") for fold in folds.split("\n")]

    print(pprint(SomeFunction(dots, folds)))
