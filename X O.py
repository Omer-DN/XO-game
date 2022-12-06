import random


class Player:
    """
    A player's class
    """

    def __init__(self, name, mark, score):
        self.name = name
        self.mark = mark
        self.score = score

        """
        Checks if any character has been entered
        """

    def check_name(self):
        while self.name == '' or self.name == ' ':
            self.name = input('enter your name again: ')
        print('hello {}'.format(self.name))


class Board:
    """
    A class of game board
    """

    def __init__(self):
        self.board = [' '] * 9

    def print_board(self):
        """
        board printing
        """
        print(self.board[0], '|', self.board[1], '|', self.board[2])
        print('_ _ _ _ _')
        print(self.board[3], '|', self.board[4], '|', self.board[5])
        print('_ _ _ _ _')
        print(self.board[6], '|', self.board[7], '|', self.board[8])

    def Marking_a_place(self, choice, player):
        """
        Checking the position on the board if it is empty
        :param choice: the selected number
        :param player: the player
        :return: False If the place is taken
                True If the place is empty
        """
        if self.board[choice] != ' ':
            print('\nthis place is taken')
            return False
        else:
            self.board[choice] = player.mark
            return True

    def if_win(self, op, player):
        """
        Victory check
        :param op:All winning options
        :param player:the player
        :return:True if there is victory, false if there is no victory
        """
        mark = player.mark
        for i in op:
            check = 0
            for x in i:
                if self.board[x] == mark:
                    check += 1
                if check == 3:
                    print("{} win!".format(player.name))
                    player.score += 2
                    return True
        return False

    def Prevents_victory(self, player, op):
        """
        :param op:All winning options
        :param player:the player
        :return: Returns the option to prevent the other player from winning
        """
        mark = player.mark
        for i in op:
            check = []
            for x in i:
                x = int(x)
                if self.board[x] == mark:
                    check.append(x)
                if len(check) == 2:
                    for number in i:
                        if number not in check:
                            if self.board[number] == ' ':
                                return True, number
        return False, None


def Beginner_selection():
    """
    A coin toss which player starts
    :return: number
    """
    first = random.randint(1, 2)
    return first


def Select_a_number(board, player):
    """
    Entering a number for a non-computer player
    :param board:
    :param player: the player
    :return: true or false, and the number chosen
    """
    while True:
        try:
            choice = input("{}, Enter you place 1-9: \n"
                           "Enter 'p' to print the board: \n".format(player.name))
            print('\n')
            if choice == 'p':
                board.print_board()
            if choice == 's':
                print(player.score)

            elif 0 < int(choice) < 10:
                return True, int(choice) - 1

        except ValueError:
            print('ValueError')


def choose_for_computer():
    """
    The function receives the instance of the board, and an instance of the player,
     and marks the place with the selected number
    :param :instance of the player
    """
    print('\ncomputer choose a number\n')
    return random.randint(0, 8)


def check_number(number):
    if number == 0:
        return True
    elif number == 1:
        return True
    return False


def keep_play():
    """
    Whether to continue playing after the game is over
    return:True or false, whether to continue playing or not (respectively)
    """
    keep_to_play = input("ENTER 'y' to keep play ")
    if keep_to_play == 'y':
        return True
    return False


def main():
    numberOfGames = 5
    board = Board()
    PossibilitiesToWin = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    first_of_computer = True
    vs_computer = int(input("play vs computer - 1\nplay vs human - 0\nyour choice: "))

    # Input integrity check
    while True:
        if check_number(vs_computer):
            break
        vs_computer = input('ENTER 0 or 1: ')

    print('------------------')

    player_a = Player(input("enter you'r name: "), 'X', 0)
    player_a.check_name()

    if vs_computer == 1:
        player_b = Player('computer', 'O', 0)
    else:
        player_b = Player(input("enter you'r name: "), 'O', 0)
        player_b.check_name()
    print('------------------')

    if Beginner_selection() == 1:
        # Inserting values into a player's performances according to the lottery number
        first, second = player_a, player_b
    else:
        first, second = player_b, player_a

    print('{} is first\n'.format(first.name))
    print('------------------')

    board.print_board()
    # ---------------------------------------------------------------------------------------------- #
    while numberOfGames:
        numberOfGames -= 1
        check = False
        if first.name == 'computer':
            # The computer picks a number for the first time
            if first_of_computer:
                first_of_computer = False
                while True:
                    number = choose_for_computer()
                    if board.Marking_a_place(number, first):
                        break
            else:
                while check is False:
                    # Choosing a computer drawn number
                    check_pos, number = board.Prevents_victory(first, PossibilitiesToWin)
                    if check_pos is False:
                        check_pos, number = board.Prevents_victory(second, PossibilitiesToWin)

                    # Checking whether the location of the number is captured
                    # If the number position is free, then put the computer's choice in it,
                    # and exit the while loop
                    if check_pos:
                        check_pos = board.Marking_a_place(number, first)
                    while check_pos is False:
                        number = choose_for_computer()
                        if board.Marking_a_place(number, first):
                            check_pos = True
                    check = True

        elif first.name != 'computer':
            while check is False:
                check, number = Select_a_number(board, first)
                if check:
                    if board.Marking_a_place(number, first):
                        break
                    check = False

        board.print_board()
        print('\n')
        check_winning = board.if_win(PossibilitiesToWin, first)
        if check_winning:
            first.score += 1
        if check_winning or numberOfGames == 0:
            if keep_play():
                board = Board()
            else:
                exit()

        check = False
        while check is False:
            if second.name == 'computer':
                # The computer picks a number for the first time
                if first_of_computer:
                    first_of_computer = False
                    check = True
                    while True:
                        number = choose_for_computer()
                        if board.Marking_a_place(number, second):
                            break
                    # The computer picks a number the second time and so on
                else:
                    while check is False:
                        # Choosing a computer drawn number
                        check_pos, number = board.Prevents_victory(second, PossibilitiesToWin)
                        if check_pos is False:
                            check_pos, number = board.Prevents_victory(first, PossibilitiesToWin)
                        # Checking whether the location of the number is captured
                        # If the number position is free, then put the computer's choice in it,
                        # and exit the while loop
                        if check_pos:
                            check_pos = board.Marking_a_place(number, second)
                        while check_pos is False:
                            number = choose_for_computer()
                            if board.Marking_a_place(number, second):
                                check_pos = True
                        check = True

            else:
                while check is False:
                    check, number = Select_a_number(board, second)
                    if check:
                        if board.Marking_a_place(number, second):
                            break
                        check = False

            board.print_board()
            print('\n')
            check_winning = board.if_win(PossibilitiesToWin, second)
            if check_winning:
                second.score += 1
            if check_winning or numberOfGames == 0:
                if keep_play():
                    board = Board()
                else:
                    exit()


if __name__ == "__main__":
    # Call the main handler function
    main()
