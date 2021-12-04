# file = "example_input.txt"
file = "input.txt"


def display_board(b, title="\nnew board"):
    print(title)
    for row in b:
        print(row)


def check_board(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                return i, j, True

    return -1, -1, False


def isWinner(score_board):
    for row in score_board:
        if all(row):
            return True

    for i in range(5):
        col = [row[i] for row in score_board]
        if all(col):
            return True

    return False


def calculate_score(called_nums, board, score_board, score):
    total = 0
    for i in range(5):
        for j in range(5):
            if not score_board[i][j]:
                total += int(board[i][j])
    return total * int(called_nums[score])


def SomeFunction(called_nums, data):
    # tracking the worst and best number of times a number is called for a board to win
    worst_score = -1
    best_score = float("inf")

    worst_board = best_board = 0  # indexes of each current worst/best board
    worst_score_board = best_score_board = None
    for boardindex, board in enumerate(data):
        score_board = [[False] * 5 for _ in range(5)]

        # finding how many moves it takes to win a board worst on the order of numbers given
        for numSeenNumbers, num in enumerate(called_nums):
            x, y, found = check_board(board, num)
            if found:
                score_board[x][y] = found
            # print(numSeenNumbers, num)

            # seeing if this board beats the worst or best record
            if isWinner(score_board):
                if worst_score < numSeenNumbers:
                    worst_score = numSeenNumbers
                    worst_board = boardindex
                    worst_score_board = score_board

                if best_score > numSeenNumbers:
                    best_score = numSeenNumbers
                    best_board = boardindex
                    best_score_board = score_board
                break

    return calculate_score(called_nums, boards[best_board], best_score_board, best_score), \
           calculate_score(called_nums, boards[worst_board], worst_score_board, worst_score)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        lines = f.readlines()
        order_of_numbers = lines[0].strip().split(",")
        all_boards = lines[2:]
        last_row = len(all_boards) - 1
        boards = []
        subboard = []
        for i, row in enumerate(all_boards):
            if row == "\n":
                boards.append(subboard.copy())
                subboard.clear()

            else:
                subboard.append(list(filter(None, row.strip().split(" "))))

            if i == last_row:
                boards.append(subboard.copy())

    p1, p2 = SomeFunction(order_of_numbers, boards)
    print(f"Part 1: {p1} Part 2: {p2}")
