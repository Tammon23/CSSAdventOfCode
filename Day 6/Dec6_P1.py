# find number of questions given
# a list of groupings
def numAnsweredQuestions(data):
    c = 0
    answered_questions = set()
    for line in data:
        if line == "\n":
            c += len(answered_questions) - 1  # -1 to ignore newline
            answered_questions.clear()
        else:
            answered_questions = answered_questions.union(line)

    return c + len(answered_questions) - 1  # dealing with last group


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = f.readlines()

    print(numAnsweredQuestions(inputs))
