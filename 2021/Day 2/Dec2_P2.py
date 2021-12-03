file = "example_input.txt"
# file = "input.txt"


def clean_input(t):
    direction, amount = t.strip("\n").split(" ")
    return direction, int(amount)


def SomeFunction(data):
    pos = depth = aim = 0
    for direction, amount in data:
        if direction == "forward":
            pos += amount
            depth += aim * amount
        elif direction == "up":
            aim -= amount
        else:
            aim += amount
    return pos * depth


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.readlines())
        # inputs = f.readlines()

    print(SomeFunction(inputs))
