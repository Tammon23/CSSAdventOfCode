file = "example_input.txt"


# file = "input.txt"


def SomeFunction(data):
    score = 0
    for line in data:
        a, b = line.split()
        if b == "X":
            score += 1
        elif b == "Y":
            score += 2
        else:
            score += 3

        if a == "A" and b == "Y" or a == "B" and b == "Z" or a == "C" and b == "X":
            score += 6

        if a == "A" and b == "X" or a == "B" and b == "Y" or a == "C" and b == "Z":
            score += 3

    return score


def SomeFunction2(data):
    score = 0
    theirs, mine = ["A", "B", "C"], ["X", "Y", "Z"]
    for line in data:
        a, b = line.split()
        score += ord(b) - ord("X") + 1

        if (theirs.index(a) + 1) % 3 == mine.index(b):
            score += 6

        if theirs.index(a) == mine.index(b):
            score += 3

    return score


def SomeFunction3(data):
    score = 0
    for line in data:
        a, b = line.split()
        score += ord(b) - ord("X") + 1

        if (ord(a) - ord("A") + 1) % 3 == ord(b) - ord("X"):
            score += 6

        elif ord(a) - ord("A") == ord(b) - ord("X"):
            score += 3

    return score


def SomeFunction4(data):
    score = 0
    for line in data:
        a, b = line.split()
        score += ord(b) - ord("X") + 1
        t = (ord(a) - ord(b)) % 3
        if t == 0:
            score += 6
        elif t == 2:
            score += 3

    return score


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
    print(SomeFunction2(inputs))
    print(SomeFunction3(inputs))
    print(SomeFunction4(inputs))
