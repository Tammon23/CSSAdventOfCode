file = "example_input.txt"
# file = "input.txt"

def ltos(letter):
    if letter == "A":
        return 1
    elif letter == "B":
        return 2
    else:
        return 3


def SomeFunction(data):
    score = 0
    for l in data:
        a, b = l.split()

        if b == "X":
            if a == "A":
                score += ltos("C")
            elif a == "B":
                score += ltos("A")
            else:
                score += ltos("B")
        elif b == "Y":
            score += ltos(a) + 3

        else:
            if a == "A":
                score += ltos("B")
            elif a == "B":
                score += ltos("C")
            else:
                score += ltos("A")
            score += 6

    return score


def SomeFunction2(data):
    score = 0
    cases = ["A", "B", "C"]
    for l in data:
        a, b = l.split()
        if b == "X":
            score += ltos(cases[cases.index(a) - 1])
        elif b == "Y":
            score += ltos(a) + 3
        else:
            score += ltos(cases[(cases.index(a) + 1) % 3]) + 6

    return score


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
    print(SomeFunction2(inputs))
