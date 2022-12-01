# file = "example_input.txt"
file = "input.txt"


def SomeFunction(data):
    highest = float("-inf")
    temp = 0
    for line in data:
        if line == "\n":
            highest = max(highest, temp)
            temp = 0
        else:
            temp += int(line.strip())
    return highest


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
