import random


class Player:
    def __init__(self, name, mark, score):
        self.name = name
        self.mark = mark
        self.score = score


class Board(Player):
    def __init__(self):
        self.board = [' '] * 9

    def print_board(self):
        print(self.board[0], '|', self.board[1], '|', self.board[2])
        print('_ _ _ _ _')
        print(self.board[3], '|', self.board[4], '|', self.board[5])
        print('_ _ _ _ _')
        print(self.board[6], '|', self.board[7], '|', self.board[8])

    def Marking_a_place(self, choice, player):
        if self.board[choice] != ' ':
            return False
        else:
            self.board[choice] = player.mark
            return True

    def winning(self, player):
        if self.board[0] and self.board[1] and self.board[2] == player.mark:
            print('hey')


def Beginner_selection():
    first = random.randint(1, 10)
    return first


def Select_a_number(player):
    choice = int(input("\n{}, enter you place 0-8: ".format(player.name)))
    if -1 < choice < 9:
        return True, choice
    print('number not valid')
    return False, choice


def main():
    times = 5
    board = Board
    player_a = Player
    player_b = Player
    # op = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    player_a.name = 'omer'  # Player(input("enter you'r name: "), 'X', 0)
    player_a.mark = 'X'
    print(player_a.name)  # you'r mark is:"), player_a.mark) , " you'r score is:", player_a.score, "\n")

    player_b.name = 'dan'  # Player(input("enter you'r name: "), 'O', 0)
    player_b.mark = 'O'

    print(player_b.name)  # you'r mark is:")#, player_b.mark, " you'r score is:", player_b.score)

    if Beginner_selection() == 1:
        first = player_a
        second = player_b
    else:
        first = player_b
        second = player_a

    print('\n{} is first\n'.format(first.name))

    while times:
        times -= 1

        check = False
        # בחירת מקום על הלוח ע"י שחקן מס' X
        while check is False:
            check, the_number = Select_a_number(first)
            if check:
                check = board().Marking_a_place(the_number, first)
        board().print_board()

        # בדיקה אם יש ניצחון

        check = False
        # בחירת מקום על הלוח ע"י שחקן מס' X
        while check is False:
            check, the_number = Select_a_number(second)
            if check:
                check = board().Marking_a_place(the_number, second)
        board().print_board()


if __name__ == "__main__":
    # Call the main handler function
    main()
