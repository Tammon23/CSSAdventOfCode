from typing import Set, Tuple

# file = "example_input.txt"
file = "input.txt"


def rotate(coordinates: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    global max_columns
    temp = set()
    for row, col in coordinates:
        n = complex(row, col) * -1j
        temp.add((int(n.real), int(n.imag) + max_columns - 1))
    return temp


def drop() -> None:
    global air, round_rock

    for row, col in sorted(round_rock):
        for x in range(row - 1, -2, -1):
            if (x, col) in air:
                continue

            round_rock.remove((row, col))
            round_rock.add((x + 1, col))

            if row != x + 1:
                air.discard((x + 1, col))
                air.add((row, col))

            break


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = [list(row) for row in f.read().splitlines()]

    air = set()
    round_rock = set()

    max_rows = len(inputs)
    max_columns = len(inputs[0])

    for r, row in enumerate(inputs):
        for c, val in enumerate(row):
            if val == ".":
                air.add((r, c))
            elif val == "O":
                round_rock.add((r, c))

    seen = {}
    cycle_path = []

    for cycle in range(1_000_000_000):
        frozen_air, frozen_round_rock = frozenset(air), frozenset(round_rock)

        offset = seen.get((frozen_air, frozen_round_rock), None)
        if offset is not None:
            final_round_rock = cycle_path[(1_000_000_000 - offset) % (cycle - offset) + offset]

            print(sum(max_rows - r for r, _ in final_round_rock))
            break

        seen[frozen_air, frozen_round_rock] = cycle
        cycle_path.append(frozen_round_rock)

        for tilt in range(4):
            drop()

            air = rotate(air)
            round_rock = rotate(round_rock)
