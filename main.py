from board import Board
from game import Game

if __name__ == '__main__':
    while True:
        print("1 - Start new Game")
        print("2 - Load a Game")
        try:
            choice = int(input("Choice: "))
            if choice < 1 or choice > 2:
                raise Exception("Input should be 1 or 2")
            if choice == 1:
                board = Board()
                game = Game(board)
                game.init_board()
                game.print_board()
                game.start_placement()
            else:
                print("input name of save-file:")
                name = input("Name: ")
                board = Board()
                game = Game(board)
                game.init_board()
                game.load_game(name)
        except ValueError:
            print("Input should be Integer")
        except Exception as er:
            print(er)
