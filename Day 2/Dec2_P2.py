# o(2n) = o(n) solution
import re


# removes the from the input then returns the
# int value of it
# o(n)
def clean_input(t):
    # 7 - 9 l: vslmtglbc
    t = re.split("-|:| ", t)
    t[0] = int(t[0]) - 1  # changing it to 0 indexing
    t[1] = int(t[1]) - 1
    return t


# given a list of rules and a password to test
# it sees if that rule works on the password
# o(n)
def validate_password(passwords):
    num_valid = 0

    # p[0] = index of first char
    # p[1] = index of second char
    # p[2] = char to test for
    # p[4] = string to test
    for index1, index2, char_to_look_for, _, test_string in passwords:

        if test_string[index1] == char_to_look_for or test_string[index2] == char_to_look_for:
            num_valid += 1

        if test_string[index1] == char_to_look_for and test_string[index2] == char_to_look_for:
            num_valid -= 1

    return num_valid


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(validate_password(inputs))
