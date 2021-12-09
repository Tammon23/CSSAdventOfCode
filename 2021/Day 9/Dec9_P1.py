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
        ans += element + 1

  return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(SomeFunction(inputs))
