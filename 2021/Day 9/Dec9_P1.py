file = "example_input.txt"
# file = "input.txt"


def clean_input(t):
    return list(map(int, list(t.strip("\n"))))


def SomeFunction(data):
  max_row = len(data)
  max_col = len(data[0])
  ans = 0
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
        ans += element + 1

  return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(SomeFunction(inputs))
