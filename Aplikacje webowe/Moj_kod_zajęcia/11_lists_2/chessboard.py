#plansza do gry w szachy
#plansza 8/8 pól, czyli 8 wierszy po 8 elementów, lista list

#   A B C D E F G H
# 1 # # # # # # # #
# 2 # # # # # # # #
# 3 # # # # # # # #
# 4 # # # # # # # #
# 5 # # # # # # # #
# 6 # # # # # # # #
# 7 # # # # # # # #
# 8 # # # # # # # #

#chess_row = ["--", "--", "--", "--", "--", "--", "--", "--", ]
#chess_row = ["--" for i in range(8)]
#chessboard = [chess_row[:] for i in range(8)]
chessboard = [["--" for i in range(8)] for i in range(8)]
WHITE_POWN = "BP"
BLACK_POWN = "CP"
chessboard[3][4] = WHITE_POWN
chessboard[2][7] = BLACK_POWN

for chess_row in chessboard:
    for chess_square in chess_row:
        print(chess_square, end = " ")
    print()
