from typing import Tuple, Iterable

file = "example_input.txt"
# file = "input.txt"


def solve(race: Iterable[Tuple[int, int]]) -> int:
    ans = 1
    for time, record in race:
        stop = time // 2
        c = 0
        for i in range(1, stop + 1):
            dist = i * (time - i)
            if record < dist:
                c += 1

        if time % 2:
            ans *= c * 2
        else:
            ans *= c * 2 - 1
    return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    race_data = []
    for x in inputs:
        t = []
        for y in x.strip("\n").split(":")[1].split(" "):
            if y != "":
                t.append(int(y))
        race_data.append(t)

    print(solve(zip(*race_data)))
