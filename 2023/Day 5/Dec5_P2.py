file = "example_input.txt"
# file = "input.txt"

if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        lines = f.read().rstrip("\n").split("\n\n")

    temp = list(map(int, lines[0].split(":")[1].strip().split(" ")))
    seeds = zip(temp[::2], temp[1::2])

    mappings = []
    for mapping in lines[1:]:
        cur = []
        for info in mapping.split(":")[1].split("\n")[1:]:
            dest_start, source_start, length = map(int, info.split(" "))
            cur.append([source_start, source_start + length - 1, dest_start])

        mappings.append(cur)

    cur_minimums = []
    for s, dist in seeds:
        e = s + dist
        check_next = [(s, e)]

        for map_type in mappings:
            finished = []
            for a, b, offset in map_type:
                not_found = []
                while check_next:
                    start, end = check_next.pop()

                    if a <= start <= b < end:
                        finished.append((start - a + offset, b - a + offset))
                        not_found.append((b + 1, end))

                    elif a <= start <= b and end <= b:
                        finished.append((start - a + offset, end - a + offset))

                    elif start < a <= end <= b:
                        finished.append((offset, end - a + offset))
                        not_found.append((start, a - 1))

                    else:
                        not_found.append((start, end))

                check_next = not_found
            check_next = finished + check_next

        cur_minimums.append(min(check_next, key=lambda x: x[0])[0])

    print(min(cur_minimums))

"""
seed:
x, y
(79, 93)

maps:
a, b
Option 1 ==> if a <= x <= b and a <= y > b then finished.add((x - a + offset, b - a + offset))
(0, 80), offset                                 checknext.add((b + 1, y))

Option 2 ==> if a <= x <= b and a <= y <= b then finished.add((x - a + offset, y - a + offset))
(70, 95), offset   

Option 3 ==> if a > x <= b and a <= y <= b then finished.add((offset, y - a + offset))
(82, 100), offset                               checknext.add((x, a - 1))

option 4:
if all else fails add finished.add((x, y))

"""