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
        while self.name == '':
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
                        if number not in check and op[number] != ' ':
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
        choice = input("{}, enter you place 0-8: \n"
                       "print 'p' to print all board: ".format(player.name))
        print('\n')
        if choice == 'p':
            board.print_board()
        elif -1 < int(choice) < 9:
            return True, int(choice)
        else:
            print('number not valid')


def choose_for_computer(player):
    """
    The function receives the instance of the board, and an instance of the player,
     and marks the place with the selected number
    :param player:instance of the player
    """
    print('\ncomputer choose a number\n')
    return random.randint(0, 8)


def check_number(number):
    try:
        # Convert it into integer
        val = int(number)
        print("Input is an integer number. Number = ", val)
        return True
    except ValueError:
        try:
            # Convert it into float
            val = float(number)
            # print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a number. It's a string")


def keep_play(option):
    """
    Whether to continue playing after the game is over
    :param option:Letter
    :return:True or false, whether to continue playing or not (respectively)
    """
    if option == 'y':
        return True
    return False


def main():
    numberOfGames = 5
    board = Board()
    PossibilitiesToWin = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    first_of_computer = True

    vs_computer = int(input("play vs computer - 1\nplay vs human - 0\nyour choice: "))
    print('------------------')
    # Input integrity check
    while True:
        # check_number(human_vs)
        if 1 == int(vs_computer):
            print('you play vs computer')
            break
        elif 0 == int(vs_computer):
            print('you play vs friend')
            break
        else:
            vs_computer = int(input("enter '1', or '0': "))

    player_a = Player(input("enter you'r name: "), 'X', 0)
    player_a.check_name()

    if vs_computer == 1:
        player_b = Player('computer', 'O', 0)
        print('computer is ready!')
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
                    number = choose_for_computer(first)
                    if board.Marking_a_place(number, first):
                        break
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
                        check_pos = board.Marking_a_place(number, first)
                    while check_pos is False:
                        number = choose_for_computer(first)
                        if board.Marking_a_place(number, first):
                            check_pos = True
                    check = True

        elif first.name != 'computer':
            while check is False:
                check, number = Select_a_number(board, first)
                if check:
                    board.Marking_a_place(number, first)
                    break

        board.print_board()
        print('\n')
        if board.if_win(PossibilitiesToWin, first):
            exit()

        check = False
        while check is False:
            if second.name == 'computer':
                # The computer picks a number for the first time
                if first_of_computer:
                    first_of_computer = False
                    check = True
                    while True:
                        number = choose_for_computer(second)
                        if board.Marking_a_place(number, second):
                            break
                    # The computer picks a number the second time and so on
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
                            check_pos = board.Marking_a_place(number, second)
                        while check_pos is False:
                            number = choose_for_computer(second)
                            if board.Marking_a_place(number, second):
                                check_pos = True
                        check = True

            else:
                while True:
                    check, number = Select_a_number(board, second)
                    if board.Marking_a_place(number, second):
                        break

            board.print_board()
            print('\n')
            if board.if_win(PossibilitiesToWin, second):
                exit()


if __name__ == "__main__":
    # Call the main handler function
    main()
