# file = "example_input.txt"
file = "input.txt"


def SomeFunction(data):
    total = 0
    for i in range(len(data) // 3):
        a, b, c = map(lambda x: set(x.strip()), data[i * 3:i * 3 + 3])
        (item,) = a.intersection(b).intersection(c)
        if item.islower():
            total += ord(item) - ord("a") + 1
        else:
            total += ord(item) - ord("A") + 1 + 26

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
