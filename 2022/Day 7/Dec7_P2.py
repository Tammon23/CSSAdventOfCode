from collections import defaultdict

file = "example_input.txt"
# file = "input.txt"


def SomeFunction(data):
    path = []
    sizes = defaultdict(int)
    dir = defaultdict(list)
    for line in data:
        line = line.split()
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    path = ["/"]
                elif line[2] == "..":
                    path.pop()
                else:
                    path.append(line[2])

        else:
            if line[0] == "dir":
                dir[path[-1]].append(path + [line[1]])

            else:
                s = int(line[0])
                for i in range(len(path), 0, -1):
                    sizes[tuple(path[:i])] += s

    remove_space = sizes[("/",)] - 40000000

    smallest = float('inf')
    for size in sizes.values():
        if remove_space - size <= 0:
            smallest = min(smallest, size)

    return smallest


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
