from itertools import combinations

file = "example_input.txt"
# file = "input.txt"


def solve(goal: int) -> int:
    minimum_number_of_containers = next(
        number_of_containers
        for number_of_containers in range(1, len(containers) + 1)
        for combo in combinations(containers, number_of_containers)
        if sum(combo) == goal
    )

    return sum(1 for combo in combinations(containers, minimum_number_of_containers) if sum(combo) == goal)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        containers = tuple(map(int, f.read().splitlines()))

    print(solve(goal=25))
