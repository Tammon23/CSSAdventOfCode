import re

# file = "example_input.txt"
file = "input.txt"


def SomeFunction(data):
    total = 0
    for line in data:
        a, b = line.split(",")
        a1, a2 = a.split("-")
        if a1 == a2:
            suba = {int(a1)}
        else:
            suba = set(range(int(a1), int(a2) + 1))
        b1, b2 = b.split("-")

        if b1 == b2:
            subb = {int(b1)}
        else:
            subb = set(range(int(b1), int(b2) + 1))

        if len(subb - suba) < len(subb) or len(suba - subb) < len(suba):
            total += 1

    return total


def SomeFunction2(data):
    total = 0
    for line in data:
        a1, a2, b1, b2 = map(int, re.split("[-,]", line))
        suba = set(range(a1, a2 + 1))
        subb = set(range(b1, b2 + 1))

        if suba.intersection(subb):
            total += 1

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
    print(SomeFunction2(inputs))
