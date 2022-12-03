# file = "example_input.txt"
file = "input.txt"


def SomeFunction(data):
    total = 0
    for line in data:
        n = len(line)
        a, b = set(line[:n // 2]), set(line[n // 2:])
        (item,) = a.intersection(b)
        if item.islower():
            total += ord(item) - ord("a") + 1
        else:
            total += ord(item) - ord("A") + 27
    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
