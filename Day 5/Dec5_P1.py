def clean_input(t):
    return t.strip("\n")

# calculates the seat ids of all seats on a plane
# then returns it
def highestSeatID(data):
    highest = float("-inf")
    for seat in data:
        row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
        col = int(seat[7:].replace("L", "0").replace("R", "1"), 2)
        cur = row * 8 + col

        if highest < cur:
            highest = cur

    return highest


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = f.readlines()

    print(highestSeatID(inputs))
