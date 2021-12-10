file = "example_input.txt"
# file = "input.txt"


def clean_input(t):
    return t.strip("\n")


def SomeFunction(data):
    stack = []
    total = 0
    symbol = {"(":")", "[":"]", "{":"}", "<":">"}
    score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for line in data:
        stack.clear()
        for sym in line:
            if sym in symbol:
                stack.append(sym)
            else:
                open = stack.pop()
                if sym != symbol[open]:
                    total += score[sym]
                    break

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.readlines())
        # inputs = f.readlines()

    print(SomeFunction(inputs))
