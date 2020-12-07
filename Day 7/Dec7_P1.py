# this would be 10000x better if done recursively
# but where is the fun in that

def clean_input(t):
    return t.strip("\n")


# finds all outer bags with an inner bag
# that matches a given search term
def search_info(data, search_term):
    new_bags = set()
    for line in data:
        bag_info = line.split("bags contain")
        outterbag = bag_info[0].strip()
        innerBag = bag_info[1]

        if search_term in innerBag:
            new_bags.add(outterbag)

    return new_bags


# given a list of rules this function will
# iterevly retrieve the amount of sub bags
# (bags within bags withing bags..) that a single bag type
# is allowed to hold
def getAmountOfSubbags(data):
    # finding the first round of outer bags to
    # look in
    sub_bags = search_info(data, "shiny gold")

    finished = sub_bags.copy()  # a list of outer bags we searched already
    new_data = set()  # contains a new collection of outer bags to check
    while 1:
        if len(sub_bags) == 0:
            break

        new_data.clear()
        for bag in sub_bags:
            new_data = new_data.union(search_info(data, bag))

        # removing the bags we already checked
        sub_bags = new_data.difference(finished)

        # updating the set of bags we already checked
        finished = finished.union(new_data)

    return len(finished)


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(getAmountOfSubbags(inputs))
