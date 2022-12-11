# file = "example_input.txt"
file = "input.txt"


def calc(TrailX, TrailY, x, y):
    deltax = abs(TrailX - x)
    deltay = abs(TrailY - y)

    if deltay >= 2 and deltax >= 2:
        # .H.H.
        # H...H
        # ..T..
        # H...H
        # .H.H.
        TrailX = x - 1 if TrailX < x else x + 1
        TrailY = y - 1 if TrailY < y else y + 1

    elif deltax >= 2:
        # .....
        # H.T.H
        # .....
        TrailX = x - 1 if TrailX < x else x + 1
        TrailY = y

    elif deltay >= 2:
        TrailY = y - 1 if TrailY < y else y + 1
        TrailX = x

    return TrailX, TrailY


def SomeFunction(data):
    x = y = 0
    Trailings = [(0, 0) for _ in range(9)]
    been = set()
    D = {"R": (1, 0), "U": (0, -1), "L": (-1, 0), "D": (0, 1)}

    for line in data:
        a, b = line.split()
        b = int(b)
        ymod, xmod = D[a]
        for _ in range(b):
            x += xmod
            y += ymod
            Trailings[0] = calc(*Trailings[0], x, y)
            for i in range(1, 9):
                Trailings[i] = calc(*Trailings[i], *Trailings[i - 1])

            been.add(Trailings[-1])
    return len(been)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
