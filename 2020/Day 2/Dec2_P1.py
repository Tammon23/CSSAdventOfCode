# o(2n) = o(n) solution
import re

# removes the from the input then returns the
# int value of it
# o(n)
def clean_input(t):
    # 7 - 9 l: vslmtglbc
    t = re.split("-|:| ", t)
    t[0] = int(t[0])
    t[1] = int(t[1])
    return t

# given a list of policies (rules) and a password to test
# it sees if that rule works on the password
# o(n)
def validate_password(passwords):
    num_valid = 0

    # p[0] = least amount
    # p[1] = max amount
    # p[2] = char to test for
    # p[4] = string to test
    for p in passwords:
        num_chars = p[4].count(p[2])
        if num_chars >= p[0] and num_chars <= p[1]:
            num_valid += 1

    return num_valid

if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(validate_password(inputs))
