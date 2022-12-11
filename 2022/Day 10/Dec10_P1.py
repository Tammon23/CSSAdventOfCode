# file = "example_input.txt"
file = "input.txt"


def SomeFunction(data):
    cycle = res = 0
    reg = 1
    for line in data:
        line = line.strip()
        if len(line) == 4:
            cycle += 1
            if ((cycle - 20) % 40) == 0:
                res += cycle * reg

        else:
            _, amt = line.split()
            for i in range(2):
                cycle += 1
                if ((cycle - 20) % 40) == 0:
                    res += cycle * reg

            reg += int(amt)

    return res


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
