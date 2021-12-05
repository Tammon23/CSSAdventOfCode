# file = "example_input.txt"
file = "input.txt"

max_x = max_y = -1


def clean_input(t):
    global max_x, max_y
    s = t.strip("\n").split(",")
    x1, y1, x2, y2 = list(map(int, [s[0]] + s[1].split(" -> ") + [s[2]]))
    max_x = x1 if x1 > max_x else max_x
    max_x = x2 if x2 > max_x else max_x
    max_y = y1 if y1 > max_y else max_y
    max_y = y2 if y2 > max_y else max_y
    return x1, y1, x2, y2


def SomeFunction(data):
    r = 0
    area = [[0] * (max_y + 1) for _ in range(max_x + 1)]

    for row in data:
        x1, y1, x2, y2 = row

        if y1 == y2:
            if x1 >= x2:
                while x1 >= x2:
                    area[x1][y1] += 1
                    x1 -= 1
            else:
                while x1 <= x2:
                    area[x1][y1] += 1
                    x1 += 1

        elif x1 == x2:
            if y1 >= y2:
                while y1 >= y2:
                    area[x1][y1] += 1
                    y1 -= 1
            else:
                while y1 <= y2:
                    area[x1][y1] += 1
                    y1 += 1

        else:
            if x1 > x2 and y1 > y2:
                while x1 >= x2:
                    area[x1][y1] += 1
                    x1 -= 1
                    y1 -= 1

            elif x1 < x2 and y1 < y2:
                while x1 <= x2:
                    area[x1][y1] += 1
                    x1 += 1
                    y1 += 1

            elif x1 < x2 and y1 > y2:
                while x1 <= x2:
                    area[x1][y1] += 1
                    x1 += 1
                    y1 -= 1

            elif x1 > x2 and y1 < y2:
                while x1 >= x2:
                    area[x1][y1] += 1
                    x1 -= 1
                    y1 += 1

    for row in area:
        for num_overlap in row:
            if num_overlap >= 2:
                r += 1

    return r


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(SomeFunction(inputs))
