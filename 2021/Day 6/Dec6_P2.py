from collections import Counter

# file = "example_input.txt"
file = "input.txt"

def SomeFunction(fish, max_date):
  temp = {}

  while (max_date := (max_date - 1)):
    for fish_time in fish:
      if not fish_time:
        temp[6] = temp.get(6, 0) + fish[fish_time]
        temp[8] = fish[fish_time]
      else:
        temp[fish_time-1] = temp.get(fish_time-1, 0) + fish[fish_time]
    
    fish = temp.copy()
    temp.clear()

  return sum([fish[fish_time] for fish_time in fish])
    

if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = Counter(map(int, f.read().strip().split(",")))

    print(SomeFunction(inputs, 257))