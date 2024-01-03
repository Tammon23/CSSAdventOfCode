from itertools import combinations
from math import ceil

from Helper import Vector

# file = "example_input.txt"
file = "input.txt"


def player_wins_match(current_weapon: Vector, current_armour: Vector, current_rings: list[Vector]) -> bool:
    player_hit_points = 100
    player_damage = current_weapon.damage + sum(cur_ring.damage for cur_ring in current_rings)
    player_armour = current_armour.armour + sum(cur_ring.armour for cur_ring in current_rings)

    global boss_hit_points, boss_damage, boss_armour

    player_moves_to_win = ceil(boss_hit_points / max(player_damage - boss_armour, 1))
    boss_moves_to_win = ceil(player_hit_points / max(boss_damage - player_armour, 1))

    return player_moves_to_win <= boss_moves_to_win


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().splitlines()

    boss_hit_points = int(inputs[0].split(" ")[2])
    boss_damage = int(inputs[1].split(" ")[1])
    boss_armour = int(inputs[2].split(" ")[1])

    weapons = [
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0)
    ]

    armours = [
        (0, 0, 0),  # <-- optional armour
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5)
    ]

    rings = [
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    ]

    weapons = [Vector("cost damage armour", *x) for x in weapons]
    armours = [Vector("cost damage armour", *x) for x in armours]
    rings = [Vector("cost damage armour", *x) for x in rings]

    gold_spent = -1
    for weapon in weapons:
        for armour in armours:
            for num_rings in range(3):
                for ring in combinations(rings, num_rings):
                    if not player_wins_match(weapon, armour, ring):
                        gold_spent = max(gold_spent, weapon.cost + armour.cost + sum(x.cost for x in ring))

    print(gold_spent)
