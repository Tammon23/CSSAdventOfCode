from typing import List

file = "example_input.txt"
# file = "input.txt"


def solve(data: List[int]) -> int:
    time, record = data
    stop = time // 2
    c = 0
    for i in range(1, stop + 1):
        dist = i * (time - i)
        if record < dist:
            c += 1

    return c * 2 if time % 2 == 1 else c * 2 - 1


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    race_data = []
    for x in inputs:
        race_data.append(int(x.strip("\n").split(":")[1].replace(" ", "")))

    print(solve(race_data))
