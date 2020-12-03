# o(n) solution

# turns the input into an array of chars
# o(n) could be o(1) but idk how to remove
# last char in o(1) so
def clean_input(t):
    return t.strip("\n")


# cycles through given the slope information
# to count the number of # or trees
# o(n/M+3) = o(n) where M is a row size
def num_trees_crashed(path):
    num_trees = row = col = 0
    max_cols = len(path[0])
    max_rows = len(path)
    while row < max_rows:
        if path[row][col] == "#":
            num_trees += 1

        col = (col + 3) % max_cols
        row += 1

    return num_trees


if __name__ == "__main__":
    inputs = []

    # reading in the input
    with open("../input.txt", "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(num_trees_crashed(inputs))

