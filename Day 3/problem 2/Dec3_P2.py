# o(n) solution

# turns the input into an array of chars
# 0(2) = o(1)
def clean_input(t):
    return t.rstrip("\n")


# cycles through given the slope information
# to count the number of # or trees
# less than o(n) really depend splope
# o(n/(M+A)*B) = o(n) where M is a row size, A is x slope, B is Num Columns
def num_trees_crashed(path, slopex, slopey):
    num_trees = row = col = 0
    max_cols = len(path[0])
    max_rows = len(path)
    while row < max_rows:
        if path[row][col] == "#":
            num_trees += 1

        col = (col + slopex) % max_cols
        row += slopey

    return num_trees


if __name__ == "__main__":
    inputs = []

    # reading in the input
    with open("../input.txt", "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(num_trees_crashed(inputs, 1, 1) *
          num_trees_crashed(inputs, 3, 1) *
          num_trees_crashed(inputs, 5, 1) *
          num_trees_crashed(inputs, 7, 1) *
          num_trees_crashed(inputs, 1, 2))

