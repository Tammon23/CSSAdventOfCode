def clean_input(t):
    return t.strip("\n")


def SomeFunction(data):
    pass


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        # inputs = map(clean_input, f.readlines())
        inputs = f.readlines()

    print(SomeFunction(inputs))
