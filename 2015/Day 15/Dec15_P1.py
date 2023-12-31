import re

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> tuple[str, int, int, int, int]:
    ingredient, _, capacity, _, durability, _, flavour, _, texture, _, _ = re.sub(r"[:,]", "", t).split(" ")
    return ingredient, int(capacity), int(durability), int(flavour), int(texture)


seen = set()
ingredient_mappings = []
NUMBER_PROPERTIES = 4


def solve(room_left: int = 100) -> int:
    if len(seen) == len(ingredients) - 1:
        res = 1
        global NUMBER_PROPERTIES
        for cookie_property in range(NUMBER_PROPERTIES):
            total = 0
            for cookie, amount in zip(ingredients.values(), ingredient_mappings + [room_left]):
                total += cookie[cookie_property] * amount

            res *= max(total, 0)

        return res

    highest = -1

    for ingredient in ingredients:
        if ingredient in seen:
            continue

        seen.add(ingredient)
        for i in range(1, room_left - (len(ingredient) - len(seen))):
            ingredient_mappings.append(i)
            highest = max(highest, solve(room_left - i))
            ingredient_mappings.pop()
        seen.remove(ingredient)

    return highest


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())

    ingredients = {}
    for cookie_ingredient in inputs:
        ingredients[cookie_ingredient[0]] = cookie_ingredient[1:]

    print(solve())

