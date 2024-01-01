from itertools import batched

file = "input.txt"


def clean_input(t: str) -> dict[str, int]:
    res = {}
    for name, value in batched(t.replace(",", ":").split(": ")[1:], n=2):
        res[name] = int(value)

    return res


def solve() -> int:

    for sue, gifts in enumerate(inputs, 1):
        for item, amount in ticker_tape.items():
            if item not in gifts or gifts[item] == amount:
                continue

            break
        else:
            return sue

    return -1


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.read().splitlines()))

    ticker_tape = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    print(solve())
