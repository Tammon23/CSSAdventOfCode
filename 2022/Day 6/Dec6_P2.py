file = "example_input.txt"
# file = "input.txt"


def SomeFunction(data):
    line = data[0]

    for i in range(len(line) - 14):
        if len(set(line[i:i + 14])) == 14:
            return i + 14

    return -1


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
