from collections import Counter


# find number of questions given
# a list of groupings
def numAnsweredQuestions(data):
    c = numMembersInGroup = 0
    answered_questions = Counter()
    for line in data:

        # group divider
        if line == "\n":
            for q in answered_questions:
                if answered_questions[q] == numMembersInGroup:
                    c += 1
            c -= 1  # removing the newline
            answered_questions.clear()
            numMembersInGroup = 0

        else:
            numMembersInGroup += 1
            answered_questions.update(Counter(line))

    else:
        for q in answered_questions:
            if answered_questions[q] == numMembersInGroup:
                c += 1

    return c - 1


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = f.readlines()

    print(numAnsweredQuestions(inputs))
