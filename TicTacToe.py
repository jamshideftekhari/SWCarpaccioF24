class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        while True:
            self.display_board()
            move = self.get_user_input()
            self.make_move(move)

            if self.check_winner():
                self.display_board()
                print(f"Player {self.current_player} wins! Congratulations!")
                break
            elif self.is_board_full():
                self.display_board()
                print("It's a draw! The game is over.")
                break

            self.switch_player()

    def display_board(self):
        print(f"\n  {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print(" ---|---|---")
        print(f"  {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print(" ---|---|---")
        print(f"  {self.board[6]} | {self.board[7]} | {self.board[8]} \n")

    def get_user_input(self):
        while True:
            try:
                move = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
                if 0 <= move < 9 and self.board[move] == ' ':
                    return move
                else:
                    print("Invalid move. Please choose an empty position (1-9).")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def make_move(self, move):
        self.board[move] = self.current_player

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if (
                self.board[i] == self.board[i + 3] == self.board[i + 6] == self.current_player or
                self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] == self.current_player
            ):
                return True
        if (
            self.board[0] == self.board[4] == self.board[8] == self.current_player or
            self.board[2] == self.board[4] == self.board[6] == self.current_player
        ):
            return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
