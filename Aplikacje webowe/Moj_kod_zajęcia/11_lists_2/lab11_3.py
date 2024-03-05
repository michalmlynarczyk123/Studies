import random

chessboard = [["--" for i in range(8)]for i in range(8)]
pieces = ["BP", "WP", "WP", "BQ", "WT"]
possitions = random.sample([i for i in range(64)], len(pieces))

print(possitions)

for i in range(len(possitions)):
    row = possitions[i] // 8
    column = possitions[i] % 8 - 1
    chessboard[row][column] = pieces[i]

for row  in range(len(chessboard)):
    if row == 0:
        print(" ", "A", "B", "C", "D", "E", "F", "G", "H", sep = "  ")
    print(row + 1, end = " ")
    for column in range(len(chessboard[row])):
        print(chessboard[row][column], end = " ")
    print()