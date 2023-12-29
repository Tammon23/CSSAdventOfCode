# file = "example_input.txt"
file = "input.txt"


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().splitlines()

    num_char = 0
    memory = 0

    for line in inputs:
        re = 2 # counting the new "

        for ch in line:
            if ch == '"' or ch == "\\":
                re += 2
            else:
                re += 1

        num_char += len(line)
        memory += re

    print(memory - num_char)
