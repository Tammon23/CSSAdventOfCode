file = "example_input.txt"
# file = "input.txt"


def SomeFunction(data):
    cycle = res = 0
    reg = 1
    CRT = [[" "] * 40 for _ in range(6)]

    for line in data:
        line = line.strip()
        if len(line) == 4:
            cycle += 1

            x, y = (cycle - 1) // 40, (cycle - 1) % 40
            CRT[x][y] = '#' if abs(reg - ((cycle - 1) % 40)) <= 1 else " "

            if ((cycle - 20) % 40) == 0:
                res += reg * cycle

        else:
            _, amt = line.split()
            for i in range(2):
                cycle += 1
                x, y = (cycle - 1) // 40, (cycle - 1) % 40
                CRT[x][y] = '#' if abs(reg - ((cycle - 1) % 40)) <= 1 else " "
                if ((cycle - 20) % 40) == 0:
                    res += reg * cycle

            reg += int(amt)

    return "\n".join([''.join(t) for t in CRT])


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
