file = "example_input.txt"
# file = "input.txt"


def clean_input(t):
    return list(map(int, list(t.strip("\n"))))


def traverse_basin(seen, data, i, j, max_row, max_col):
  ans = 0
  seen[i][j] = True

  dir = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
  for x, y in dir:
      if 0 <= x < max_row and 0 <= y < max_col and not seen[x][y] and  data[i][j] < data[x][y] and data[x][y] != 9:
          ans += 1 + traverse_basin(seen, data, x, y, max_row, max_col)
  
  return ans
  

def SomeFunction(data, max_row, max_col):
  basin_sizes = []

  for i, row in enumerate(data):
    for j, element in enumerate(row):
      dir = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
      score = max_score = 0
      for x,y in dir:
        if 0 <= x < max_row and 0 <= y < max_col:
          max_score += 1
          if element < data[x][y]:
            score += 1

      if score == max_score and score != 0:
        seen = [[False] * len(data[0]) for _ in range(len(data))]
        basin_sizes.append(traverse_basin(seen, data, i, j, max_row, max_col) + 1)        

  ans = 1
  for top_3 in sorted(basin_sizes)[-3:]:
    ans *= top_3

  return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(SomeFunction(inputs, len(inputs), len(inputs[0])))
