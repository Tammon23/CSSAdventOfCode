file = "example_input.txt"
# file = "input.txt"


def clean_input(t):
    return t.strip("\n")


def SomeFunction(data):
    return data


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        # inputs = map(clean_input, f.readlines())
        inputs = f.readlines()

    print(SomeFunction(inputs))
