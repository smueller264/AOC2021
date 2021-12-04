import numpy as np


def main():

    testnumbers = [
        7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1
    ]

    testboards = [

        [[22, 13, 17, 11, 0],
         [8, 2, 23, 4,    24],
         [21,  9, 14, 16,  7],
         [6, 10,  3, 18,  5],
         [1, 12, 20, 15, 19]],

        [[3, 15,  0,  2, 22],
         [9, 18, 13, 17,  5],
         [19,  8,  7, 25, 23],
         [20, 11, 10, 24,  4],
         [14, 21, 16, 12,  6]],

        [[14, 21, 17, 24,  4],
         [10, 16, 15,  9, 19],
         [18,  8, 23, 26, 20],
         [22, 11, 13,  6,  5],
         [2,  0, 12,  3,  7, ]]
    ]

    # with open("test_input.txt") as file:

    #    result = [[x for x in line.split()] for line in file]
    boards = []
    numbers = []
    board = []
    file = open("input.txt")
    for line in file:
        # first line
        if (len(line) > 15):
            line = line.split(",")
            line = list(map(str.strip, line))
            numbers = list(map(int, line))
            continue
        # empty line
        if line == "\n":
            if (len(board) > 0):
                boards.append(board)
                board = []
            continue
        else:
            line = line.split()
            line = list(map(str.strip, line))
            board.append(list(map(int, line)))
    boards.append(board)

    print(numbers)
    print()
    print(boards)

    winner_board_and_numbers = find_winner(numbers, boards)

    calculate_score(winner_board_and_numbers[0], winner_board_and_numbers[1])


def calculate_score(board, winning_numbers):
    unmarked_numbers = []
    for line in board:
        for number in line:
            if number not in winning_numbers:
                unmarked_numbers.append(number)
    print(sum(unmarked_numbers))
    print(sum(unmarked_numbers) * winning_numbers[len(winning_numbers) - 1])


def find_winner(numbers, boards):
    winner_boards = []
    latest_winner = []
    latest_numbers = []
    oldboards = boards
    for i in range(5, len(numbers) - 1):
        for board in boards:
            oldboard = board
            board = np.array(board)
            for line in board:
                print(numbers[:i])
                print(line)
                if all(item in numbers[:i] for item in line):
                    print("winner")
                    latest_winner = board
                    latest_numbers = numbers[:i]
                    winner_boards.append(oldboard)
                    break
            transposed = board.transpose()
            for line in transposed:
                if all(item in numbers[:i] for item in line):
                    print("winner")
                    latest_winner = board
                    latest_numbers = numbers[:i]
                    winner_boards.append(oldboard)
                    break
            if all(item in winner_boards for item in oldboards):
                print("end")
                print(np.array(oldboards))
                print("winner boards")
                print(np.array(winner_boards))
                print("last winne")
                print(np.array(latest_winner))
                print(latest_numbers)
                return latest_winner, latest_numbers


if __name__ == '__main__':
    main()
