# file = "example_input.txt"
file = "input.txt"


def SomeFunction(dots, folds):
    for axis, index in folds:
        index = int(index)
        if axis == "x":
            dots = [(x if x < index else index - (x-index), y) for x,y in dots]
        else:
            dots = [(x, y if y < index else index - (y-index)) for x,y in dots]

    return len(set(dots))


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        dots, folds = f.read().split("\n\n")
        dots = [list(map(int, pair.split(","))) for pair in dots.split("\n")]
        folds = [fold.replace("fold along ", "").split("=") for fold in folds.split("\n")]

    # we only care about the first fold, so dismiss the rest
    print(SomeFunction(dots, folds[:1]))
