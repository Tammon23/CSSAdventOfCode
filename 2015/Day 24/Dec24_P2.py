from itertools import combinations
from typing import Iterable

import Helper

file = "example_input.txt"
# file = "input.txt"


def can_create_two_groups(group: Iterable[int], goal: int) -> bool:
    group = set(group)
    remaining = weights - group

    for group_size2 in range(1, len(remaining)-2):
        for combo in combinations(remaining, group_size2):
            if goal == sum(combo):

                group2_remaining = remaining - set(combo)
                for group_size3 in range(1, len(remaining) - group_size2):
                    for combo2 in combinations(group2_remaining, group_size3):
                        if goal == sum(combo2) == sum(group2_remaining - set(combo2)):
                            return True

    return False


def solve(number_of_groups: int) -> int:
    goal: int = sum(weights) // number_of_groups

    for first_group_size in range(1, len(weights)):

        potential_group_ones = []

        for combo in combinations(weights, first_group_size):
            if sum(combo) == goal:
                potential_group_ones.append(combo)

        for group1 in sorted(potential_group_ones, key=Helper.product):
            if can_create_two_groups(group1, goal):
                return Helper.product(group1)

    return -1


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        weights = set(map(int, f.read().splitlines()))

    print(solve(4))
