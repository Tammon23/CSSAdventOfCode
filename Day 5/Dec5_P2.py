def clean_input(t):
    return t.strip("\n")

# finds my seat id in a given ids
# assuming all digits are present
# mine is the digit that is missing
def mySeatID(data):
    seats = []
    for seat in data:
        row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
        col = int(seat[7:].replace("L", "0").replace("R", "1"), 2)
        cur = row * 8 + col
        seats.append(cur)

    seats.sort()

    for i in range(len(seats)-1):
        if seats[i] != seats[1+i] - 1:
            return seats[i] + 1
    return -1


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        # inputs = map(clean_input, f.readlines())
        inputs = f.readlines()

    print(mySeatID(inputs))
