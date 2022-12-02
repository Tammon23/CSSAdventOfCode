# file = "example_input.txt"
file = "input.txt"


def SomeFunction(data):
    score = 0
    for l in data:
        a, b = l.split()
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


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
