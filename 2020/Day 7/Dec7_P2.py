# this would be 10000x better if done recursively
# but where is the fun in that
import re


# turning the input into a dict comprised of
# the outer bag as the key, and a list of tuples
# containing an inner bag and the required amounts
def bag_values(data):
    seen = {}
    for bag in data:
        bag_info = bag.replace(".\n", "").split("bags contain")
        outerbag = bag_info[0].strip()
        innerData = []
        for bag in bag_info[1].split(","):
            bags = re.sub(" bags?", "", bag).strip().split(" ", 1)
            if bags[0] != "no":
                innerData.append((bags[1], int(bags[0])))

        seen[outerbag] = innerData if len(innerData) != 0 else 0

    return seen

# finds the exact number of sub bags needed to make the outer bag
# considered valid
def find_bag_value(bag_values, search_term):
    numChanges = {}
    numInnerBags = {}

    if search_term not in bag_values:
        return -1

    # calculating the number of inner bags for each outer bag
    for value in bag_values:
        if type(bag_values[value]) == int:
            numInnerBags[value] = 0

        else:
            total_inner_bag = 0
            for inner_bag in bag_values[value]:
                total_inner_bag += inner_bag[1]

            numInnerBags[value] = total_inner_bag

    while 1:
        for value in bag_values:
            inner_bags = bag_values[value]

            if type(inner_bags) == int:
                continue

            # searching through each direct inner bag of an outer bag
            for index, bag in enumerate(inner_bags):

                # if we know how many sub bags an inner bags contains
                # then replace that value with the integer amount
                if type(bag) == tuple and type(bag_values[bag[0]]) == int:
                    bag_values[value][index] = bag_values[bag[0]] * bag[1]

                    # tracking the amount of changes weve made already
                    # to know when we should sum the elements
                    if value in numChanges:
                        numChanges[value] += 1
                    else:
                        numChanges[value] = 1

                # calculating the amount of sub bags assuming we know
                # the amount of all sub bags in an inner bag

                if value in numChanges:
                    if type(bag_values[value]) != int and numChanges[value] == len(bag_values[value]):
                        if search_term == value:
                            return sum(bag_values[value]) + numInnerBags[value]

                        bag_values[value] = sum(bag_values[value]) + numInnerBags[value]

    # shouldn't ever reach here
    return -2


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = f.readlines()

    print(find_bag_value(bag_values(inputs), "shiny gold"))

    # x = number_of_inner_bags + number_of_inner_bags * amount_of_sub_bags
    # 126 = 2 + 2*62 shiny gold bags contain 2 dark red bags.
    # 62 = 2 + 2*30 dark red bags contain 2 dark orange bags.
    # 30 = 2 + 2*14 dark orange bags contain 2 dark yellow bags.
    # 14 = 2 + 2*6 dark yellow bags contain 2 dark green bags.
    # 6 = 2 + 2*2  dark green bags contain 2 dark blue bags.
    # 2 = 2 + 2*0 dark blue bags contain 2 dark violet bags.
    # 0 = 0 dark violet bags contain no other bags.
