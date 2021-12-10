file = "example_input.txt"
# file = "input.txt"


def clean_input(t):
    return t.strip("\n")


def SomeFunction(data):
    stack = []
    total_scores = []
    symbol = {"(":")", "[":"]", "{":"}", "<":">"}
    score = {")": 1, "]": 2, "}": 3, ">": 4}
    for line in data:
        stack.clear()
        sub_total = 0
        for sym in line:
            if sym in symbol:
                stack.append(sym)
            else:
                open = stack.pop()
                if sym != symbol[open]:
                    break
        else:

            for remaining in reversed(stack):
                sub_total = sub_total * 5 + score[symbol[remaining]]

            total_scores.append(sub_total)

    total_scores.sort()
    return total_scores[len(total_scores)//2]


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.readlines())

    print(SomeFunction(inputs))
