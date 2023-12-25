from itertools import combinations
import Helper

# file = "example_input.txt"
file = "input.txt"


# thanks to: https://stackoverflow.com/a/20677983/3889449
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None, None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def solve():
    count = 0
    for rock1, rock2 in combinations(rocks, 2):
        rock1_position, rock1_velocity = rock1
        rock2_position, rock2_velocity = rock2

        x, y = line_intersection(
            (rock1_position, Helper.add_tuple(rock1_position, rock1_velocity)),
            (rock2_position, Helper.add_tuple(rock2_position, rock2_velocity))
        )

        if x is None:
            continue

        if all(
            (x - p[0] > 0) == (v[0] > 0) and (y - p[1] > 0) == (v[1] > 0)
            for p, v in [rock1, rock2]
        ):
            pass
        else:
            continue

        lower_bound = 200000000000000
        upper_bound = 400000000000000
        if lower_bound <= x <= upper_bound and lower_bound <= y <= upper_bound:
            count += 1

    return count


if __name__ == "__main__":
    rocks = []

    # reading in the input
    with open(file, "r") as f:
        for i, line in enumerate(f.read().splitlines()):
            position, vel = line.split(" @ ")
            rocks.append((tuple(map(int, position.split(", "))), tuple(map(int, vel.split(", "))) ))
    print(solve())
