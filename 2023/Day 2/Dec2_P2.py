from typing import List

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> dict[str, List[int]]:
    sets = t.split(":")[1].split(";")
    res = {'b': [], 'r': [], 'g': []}
    for s in sets:
        for cubes in s.split(", "):
            num, col = cubes.strip().split(" ")
            res[col[0]].append(int(num))
    return res


def solve(data: dict[str, List[int]]) -> int:
    ans = 0
    for game in data:
        temp = 1
        if game["r"]:
            temp *= max(game["r"])

        if game["g"]:
            temp *= max(game["g"])

        if game["b"]:
            temp *= max(game["b"])

        ans += temp

    return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.readlines())

    print(solve(inputs))

