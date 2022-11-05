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
            print('this place is taken')
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
                            return number

    def choose_for_computer(self, player, op):
        """
        Choosing a number for "computer" when it's not the first time
        :param player: the computer
        :param op:All winning options
        :return:
        """
        print('computer choose a number\n')
        return self.Prevents_victory(player, op)


def Beginner_selection():
    """
    A coin toss which player starts
    :return: number
    """
    first = random.randint(1, 2)
    return first


def Select_a_number(player):
    """
    Entering a number for a non-computer player
    :param player: the player
    :return: true or false, and the number chosen
    """
    choice = int(input("\n{}, enter you place 0-8: ".format(player.name)))
    if -1 < choice < 9:
        return True, choice
    print('number not valid')
    return False, choice


def choose_for_first_time(board, player):
    """
    The function receives the instance of the board, and an instance of the player,
     and marks the place with the selected number
    :param board:instance of the board
    :param player:instance of the player
    """
    print('computer choose a number\n')
    num = random.randint(0, 8)
    board.Marking_a_place(num, player)


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
    times = 5
    board = Board()
    OP = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    array = ['a']
    vs_computer = int(input("if you want to play vs computer, enter 1, else enter 0: "))
    while vs_computer !=0 or vs_computer != 1:
        vs_computer = int(input("enter again: "))
    player_a = Player(input("enter you'r name: "), 'X', 0)
    player_a.check_name()

    if vs_computer == 1:
        player_b = Player('computer', 'O', 0)
        print('you play vs computer')
    else:
        player_b = Player(input("enter you'r name: "), 'O', 0)
        player_b.check_name()

    if Beginner_selection() == 1:
        # Inserting values into a player's performances according to the lottery number
        first, second = player_a, player_b
    else:
        first, second = player_b, player_a

    print('\n{} is first\n'.format(first.name))

    while times:
        times -= 1

        check = False
        while check is False:
            if first.name == 'computer' and 'a' in array:
                choose_for_first_time(board, first)
                array[0] = 'b'
                check = True
            elif first.name == 'computer' and 'c' in array:
                number = board.choose_for_computer(first, OP)
                check = board.Marking_a_place(number, first)
            elif first.name != 'computer':
                check, number = Select_a_number(first)
                if check:
                    check = board.Marking_a_place(number, first)
            array[0] = 'c'
            board.print_board()
            print('\n')
            if board.if_win(OP, first):
                exit()

        check = False
        while check is False:
            array[0] = 'c'
            if second.name == 'computer' and 'a' in array:
                choose_for_first_time(board, first)
                array[0] = 'b'
                check = True
            elif second.name == 'computer' and 'c' in array:
                number = board.choose_for_computer(second, OP)
                check = board.Marking_a_place(number, second)
            else:
                check, number = Select_a_number(second)
                if check:
                    check = board.Marking_a_place(number, second)
        board.print_board()
        print('\n')
        if board.if_win(OP, second):
            exit()

    print("There is no winner in this game \n")
    first.score += 1
    second.score += 1


if __name__ == "__main__":
    # Call the main handler function
    main()
