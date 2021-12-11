file = "example_input.txt"
# file = "input.txt"


def pprint(data, s=10):
    print("-" * s * 4)
    for d in data:
        print(d)


def clean_input(t):
    return list(map(int, list(t.strip("\n"))))


def SomeFunction(data):
    grid_size = 10
    queue = []
    zeroes = []
    step = 1
    num_flashes = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    while step <= 100:
        # pprint(data) # shows each step
        seen = set()
        for i, row in enumerate(data):
            for j, octopus in enumerate(row):

                if octopus == 9:
                    queue.append((i, j))
                    seen.add((i, j))
                else:
                    data[i][j] = octopus + 1

        while len(queue) != 0:
            flash_x, flash_y = queue.pop(0)
            for x, y in directions:
                new_x, new_y = flash_x + x, flash_y + y
                if 0 <= new_x < grid_size and 0 <= new_y < grid_size:  # if the current point is a valid point
                    if data[new_x][new_y] == 9:  # check if the octopus will be flash. if so
                        if (new_x, new_y) not in seen:  # check if we are still processing it, if not
                            queue.append((new_x, new_y))  # schedule it to be processed and mark that we've
                            seen.add((new_x, new_y))  # seen it
                    else:
                        data[new_x][new_y] += 1

            zeroes.append((flash_x, flash_y))  # mark the octopus as "reset flash"

        num_flashes += len(zeroes)
        for x, y in zeroes:
            data[x][y] = 0
        zeroes.clear()
        seen.clear()
        step += 1
    return num_flashes


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(SomeFunction(inputs))
