board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def game_over():
    if board[0][0] == board[0][1] == board[0][2] != " ":
        return True
    if board[1][0] == board[1][1] == board[1][2] != " ":
        return True
    if board[2][0] == board[2][1] == board[2][2] != " ":
        return True
    if board[0][0] == board[1][0] == board[2][0] != " ":
        return True
    if board[0][1] == board[1][1] == board[2][1] != " ":
        return True
    if board[0][2] == board[1][2] == board[2][2] != " ":
        return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    if " " not in board[0] and " " not in board[1] and " " not in board[2]:
        return True


def main():
    movements = 0
    while True:
        print("Player X, enter your move. ")
        row = int(input("Row: "))
        col = int(input("Column: "))
        while row > 2 or col > 2 or board[row][col] != " " :
            print("Invalid move, try again")
            row = int(input("Row: "))
            col = int(input("Column: "))
        board[row][col] = "X"
        movements += 1
        for row in board:
            print(row)
        if movements == 9:
            break
        if game_over():
            print("Player X wins!")
            break
        print("Player O, enter your move. ")
        row = int(input("Row: "))
        col = int(input("Column: "))
        while row > 2 or col > 2 or board[row][col] != " ":
            print("Invalid move, try again")
            row = int(input("Row: "))
            col = int(input("Column: "))
        board[row][col] = "O"
        movements += 1
        for row in board:
            print(row)
        if movements == 9:
            break
        if game_over():
            print("Player O wins!")
            break
    if movements == 9:
        print("Game over!, no one wins.")

        

if __name__ == "__main__":
    main()

# board = [[" " for _ in range(3)] for _ in range(3)]

# def game_over():
#     lines = board + [list(col) for col in zip(*board)] + [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
#     for line in lines:
#         if line[0] == line[1] == line[2] != " ":
#             return True
#     return all(cell != " " for row in board for cell in row)

# def print_board():
#     for row in board:
#         print(row)

# def player_move(player):
#     while True:
#         row = int(input(f"Player {player}, enter your move (row 0-2): "))
#         col = int(input(f"Player {player}, enter your move (column 0-2): "))
#         if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
#             board[row][col] = player
#             break
#         else:
#             print("Invalid move, try again")

# def main():
#     for turn in range(9):
#         print_board()
#         player = "X" if turn % 2 == 0 else "O"
#         player_move(player)
#         if game_over():
#             print_board()
#             print(f"Player {player} wins!")
#             return
#     print_board()
#     print("Game over! It's a draw.")

# if __name__ == "__main__":
#     main()