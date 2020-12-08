def clean_input(t):
    t = t.strip("\n").split(" ")
    t[1] = int(t[1])
    return t[0], t[1]


# given a list of instructions this function will either
# isolate the point where the infinite loop, loops back
# of if it doesnt have an infinite loop it will return
# the accumulator
def find_first_infinite(data):
    i = acc = 0
    visited = set()
    visited_order = []
    while i < len(data):
        if i in visited:
            return None, visited_order

        visited.add(i)
        visited_order.append(i)

        if data[i][0] == 'jmp':

            if i + data[i][1] in visited:
                visited_order.append(i + data[i][1])
                return None, visited_order
            else:
                i += data[i][1]
                continue

        elif data[i][0] == 'acc':
            acc += data[i][1]
        i += 1

    return acc, visited_order


# corrects the cause of an infinite loop in a set of instructions
# then returns the correct accumulator after it has been fixed
def FindCorrectAccumulator(data):
    success, visited_order = find_first_infinite(data)
    if success is None:
        for i, v in enumerate(visited_order):
            if v == visited_order[-1]:
                break

        # isolating a group of instructions to test
        # swapping nops to jmps and jmps to nops
        visited_order = visited_order[visited_order.index(visited_order[-1])+1:-1]

        # testing said instructions
        for brute in visited_order:
            duplicate = data.copy()
            duplicate[brute] = ("jmp", duplicate[brute][1]) if duplicate[brute][0] == "nop" else ("nop", 0)
            success, t = find_first_infinite(duplicate)
            if success is not None:
                return success

    else:
        return success


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(FindCorrectAccumulator(inputs))
