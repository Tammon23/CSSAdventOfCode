import json

file = "example_input.txt"
# file = "input.txt"


def solve(data: dict | list | int | str) -> int:
    total = 0

    if isinstance(data, dict):
        if "red" not in data.values():
            total = sum(solve(v) for v in data.values())

    elif isinstance(data, list):
        total = sum(solve(v) for v in data)

    elif isinstance(data, int):
        total = data

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = json.loads(f.read().strip())

    print(solve(inputs))
