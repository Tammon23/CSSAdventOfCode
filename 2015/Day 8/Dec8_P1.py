# file = "example_input.txt"
file = "input.txt"


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().splitlines()

    num_char = 0
    memory = 0

    for line in inputs:
        num_char += len(line)
        memory += len(eval(line))

    print(num_char - memory)
