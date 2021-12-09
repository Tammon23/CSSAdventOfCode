file = "example_input.txt"
# file = "input.txt" 


def clean_input(t):
    return list(map(int, list(t.strip("\n"))))


def find_small_basins(data, max_row, max_col):
  basin_locs = []

  for i, row in enumerate(data):
    for j, element in enumerate(row):
      score = max_score = 0
      if i + 1 < max_row :
        max_score += 1
        if element < data[i+1][j]: 
          score += 1

      if i - 1 >= 0:
        max_score += 1
        if element < data[i-1][j]:
          score += 1

      if j + 1 < max_col:
        max_score += 1
        if element < data[i][j+1]:
          score += 1

      if j - 1 >= 0:
        max_score += 1
        if element < data[i][j-1]:
          score += 1

      if score == max_score and score != 0:
        basin_locs.append((i, j))

  return basin_locs


def traverse_basin(seen, data, i, j, max_row, max_col):
  element = data[i][j]
  ans = 0

  # we return -1 because when we do our down, up, right, left checks we increment
  # our count if we see a 9, so to undo that we decrement here. Alternativly, adding
  # a check in the if the next num is 9 would eliminate the need for it under here 
  if element == 9:
    return -1
  
  seen[i][j] = True
  # check down
  if i + 1 < max_row and not seen[i+1][j] and element < data[i+1][j]:
      re = traverse_basin(seen, data, i+1, j, max_row, max_col)
      ans += 1 + re 

  # check up
  if i - 1 >= 0 and not seen[i-1][j] and element < data[i-1][j]:
      re = traverse_basin(seen, data, i-1, j, max_row, max_col)
      ans += 1 + re 

  # check right
  if j + 1 < max_col and not seen[i][j+1] and element < data[i][j+1]:
      re = traverse_basin(seen, data, i, j+1, max_row, max_col)
      ans += 1 + re 

  # check left
  if j - 1 >= 0 and not seen[i][j-1] and element < data[i][j-1]:
      re = traverse_basin(seen, data, i, j-1, max_row, max_col)
      ans += 1 + re 

  return ans
  

def SomeFunction(data):
  total = []
  max_row = len(data)
  max_col = len(data[0])

  locs = find_small_basins(data, max_row, max_col)

  for x, y in locs:
    seen = [[False] * len(data[0]) for _ in range(len(data))]
    total.append(traverse_basin(seen, data, x, y, max_row, max_col) + 1)
  
  ans = 1
  for top_3 in sorted(total)[-3:]:
    ans *= top_3

  return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(SomeFunction(inputs))
