# Assignment 2: Tic-Tac-Toe
# due Monday 07/06 at 9:00am (EST)

# Author: 
# NetID: 

import random


def get_cell_string(val):
    """
    Returns a string corresponding to the provided value from the board state.

    val: 0 (none) or 1 (player 1) or 2 (player 2)
    returns: " " (0) or "x" (player 1) or "o" (player 2)
    """

    pass # Replace with Task 2 code


def print_row(board, row):
    """
    Prints out the current board state of the given row.

    board: a nested list containing the board state
    row: the row for which to print the board state
    """
    
    pass # Replace with Task 3 code


def print_board_state(board):
    """
    Prints out the current board state for debugging.

    board: a nested list containing the board state
    """
    
    pass # Replace with Task 4 code


def is_valid_grid_cell(board, x, y):
    """
    Returns a Boolean indicating whether the given grid position
    is a valid selection given the current board state.
    Also checks if the grid position is within the bounds of the board.

    board: a nested list containing the board state
    x: the grid x position
    y: the grid y position
    returns: True if a piece can be placed at (x, y),
             False otherwise
    """

    try:
        x, y = int(x), int(y)
    except:
        return False
    
    pass # Replace with Task 5 code


def update_board_state(board, x, y, player):
    """
    Updates the board state to indicate a player placed
    a marker at the specified grid position on the board.

    board: a nested list containing the board state
    x: the grid x position
    y: the grid y position
    player: 1 or 2
    """
    
    pass # Replace with Task 6 code


def player_row_win(board, player, row):
    """
    Returns a Boolean indicating whether the player
    won the game due to the given row.

    board: a nested list containing the board state
    player: 1 or 2
    row: 0, 1, or 2
    returns: a Boolean (True if the player has an entire row,
             False otherwise)
    """
    
    pass # Replace with Task 7 code


def player_column_win(board, player, col):
    """
    Returns a Boolean indicating whether the player
    won the game due to the given column.

    board: a nested list containing the board state
    player: 1 or 2
    col: 0, 1, or 2
    returns: a Boolean (True if the player has an entire column,
             False otherwise)
    """
    
    pass # Replace with Task 8 code


def player_diagonal_win(board, player):
    """
    Returns a Boolean indicating whether the player
    won the game due to either diagonal.

    board: a nested list containing the board state
    player: 1 or 2
    returns: a Boolean (True if the player has an entire diagonal,
             False otherwise)
    """
    
    pass # Replace with Task 9 code


def is_win(board, player):
    """
    Returns a Boolean indicating whether the player has
    won the game.
    
    board: a nested list containing the board state
    player: 1 or 2
    returns: a Boolean (True if the player won, False otherwise)
    """

    pass # Replace with Task 10 code


def is_draw(board):
    """
    Returns a Boolean indicating whether the game has ended in a draw.
    Assumes neither player has won.
    
    board: a nested list containing the board state
    returns: a Boolean (True if the game is a draw, False otherwise)
    """

    pass # Replace with Task 12 code


def player_2_turn(board):
    """
    Returns a randomly selected x and y value for Player 2's turn.

    board: a nested list containing the board state
    returns: two integers x and y (a valid board position for Player 2's next move)
    """

    x = random.randint(0, 2)
    y = random.randint(0, 2)

    while not is_valid_grid_cell(board, x, y):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
    
    return x, y


def play_game():
    """
    Play a game of Tic Tac Toe.
    """

    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    player = 1

    print()
    print("You are Player 1! You will make the first move of the game.")

    print()
    print("The board state is:")
    print_board_state(board)

    print("\n---------------------------------------------------------\n")
    
    game_over = False
    while not game_over:
        print(f"It's Player {player}'s turn!")
        print()
        
        if player == 1:
            print("Choose where you want to place your next marker!")
            x = input("Enter x position: ")
            y = input("Enter y position: ")

            while not is_valid_grid_cell(board, x, y):
                print("Sorry, that's not a valid board position!")
                print()
                print("Choose where you want to place your next marker!")
                x = input("Enter x position: ")
                y = input("Enter y position: ")
            
            x, y = int(x), int(y)
        
        elif player == 2:
            x, y = player_2_turn(board)

        update_board_state(board, x, y, player)

        print()
        print(f"Player {player} has placed their piece.")

        print()
        print("The new board state is:")
        print_board_state(board)

        if is_win(board, player):
            print(f"Player {player} has won!")
            game_over = True
        elif is_draw(board):
            print("The game has reached a draw.")
            game_over = True
        else:
            player = 3-player
        print("\n---------------------------------------------------------\n")
    print("Game over!")


if __name__ == "__main__":
    print("Let's test your code!")
    print()

    board = [[2, 0, 0],
             [1, 2, 0],
             [0, 1, 0]]

    ###################### Task 2 ######################

    # print("Task 2 tests:\n-------------\n")
    # print(get_cell_string(0), "should be", " ")
    # print(get_cell_string(1), "should be", "x")
    # print(get_cell_string(2), "should be", "o")
    # print()
 
    ###################### Task 3 ######################

    # print("Task 3 tests:\n-------------\n")
    # print_row(board, 0)
    # print("should have printed")
    # print("|o| | |")
    # print()

    # print_row(board, 1)
    # print("should have printed")
    # print("|x|o| |")
    # print()

    # print_row(board, 2)
    # print("should have printed")
    # print("| |x| |")
    # print()

    ###################### Task 4 ######################

    # print("Task 4 test:\n-------------\n")
    # print_board_state(board)
    # print("\nshould have printed\n")
    # print("-------\n|o| | |\n-------\n|x|o| |\n-------\n| |x| |\n-------\n")

    ###################### Task 5 ######################

    # print("Task 5 tests:\n-------------\n")
    # print(is_valid_grid_cell(board, "x", 1), "should be False")
    # print(is_valid_grid_cell(board, 1, "y"), "should be False")
    # print(is_valid_grid_cell(board, -1, 0), "should be False")
    # print(is_valid_grid_cell(board, 0, -1), "should be False")
    # print(is_valid_grid_cell(board, 4, 0), "should be False")
    # print(is_valid_grid_cell(board, 0, 4), "should be False")
    # print(is_valid_grid_cell(board, 0, 0), "should be False")
    # print(is_valid_grid_cell(board, 0, 1), "should be True")
    # print(is_valid_grid_cell(board, "0", "1"), "should be True")
    # print()

    ###################### Task 6 ######################

    # print("Task 6 tests:\n-------------\n")
    # update_board_state(board, 0, 2, 1)
    # print_board_state(board)
    # print("should have printed")
    # print("-------\n|o| |x|\n-------\n|x|o| |\n-------\n| |x| |\n-------\n")
    # update_board_state(board, 2, 0, 2)
    # print_board_state(board)
    # print("should have printed")
    # print("-------\n|o| |x|\n-------\n|x|o| |\n-------\n|o|x| |\n-------\n")
    # update_board_state(board, 0, 0, 1)
    # print_board_state(board)
    # print("should have printed")
    # print("-------\n|o| |x|\n-------\n|x|o| |\n-------\n|o|x| |\n-------\n")
    # print()

    ###################### Task 7 ######################

    # print("Task 7 tests:\n-------------\n")
    # board = [[2, 2, 0],
    #          [2, 2, 2],
    #          [1, 1, 1]]
    # print(player_row_win(board, 1, 0), "should be False")
    # print(player_row_win(board, 2, 0), "should be False")
    # print(player_row_win(board, 2, 1), "should be True")
    # print(player_row_win(board, 1, 1), "should be False")
    # print(player_row_win(board, 2, 2), "should be False")
    # print(player_row_win(board, 1, 2), "should be True")
    # print()

    ###################### Task 8 ######################
    
    # print("Task 8 tests:\n-------------\n")
    # board = [[2, 2, 1],
    #          [2, 2, 1],
    #          [0, 2, 1]]
    # print(player_column_win(board, 1, 0), "should be False")
    # print(player_column_win(board, 2, 0), "should be False")
    # print(player_column_win(board, 2, 1), "should be True")
    # print(player_column_win(board, 1, 1), "should be False")
    # print(player_column_win(board, 2, 2), "should be False")
    # print(player_column_win(board, 1, 2), "should be True")
    # print()

    ###################### Task 9 ######################

        # print("Task 9 tests:\n-------------\n")
    # board = [[1, 2, 2],
    #          [2, 1, 0],
    #          [0, 0, 1]]
    # print(player_diagonal_win(board, 1), "should be True")
    # print(player_diagonal_win(board, 2), "should be False")
    # board = [[1, 0, 2],
    #          [1, 2, 0],
    #          [2, 0, 1]]
    # print(player_diagonal_win(board, 2), "should be True")
    # print(player_diagonal_win(board, 1), "should be False")
    # board = [[1, 2, 0],
    #          [0, 1, 2],
    #          [2, 0, 2]]
    # print(player_diagonal_win(board, 1), "should be False")
    # print(player_diagonal_win(board, 2), "should be False")
    # print()

    ###################### Task 10 ######################

    # print("Task 10 tests:\n-------------\n")
    # print(is_win(board, 1), "should be False")
    # print(is_win(board, 2), "should be False")
    # board = [[1, 1, 1],
    #          [0, 2, 1],
    #          [2, 0, 2]]
    # print(is_win(board, 1), "should be True")
    # print(is_win(board, 2), "should be False")
    # board = [[1, 2, 2],
    #          [0, 2, 1],
    #          [1, 2, 2]]
    # print(is_win(board, 1), "should be False")
    # print(is_win(board, 2), "should be True")
    # board = [[1, 2, 2],
    #          [0, 1, 1],
    #          [1, 2, 1]]
    # print(is_win(board, 1), "should be True")
    # print(is_win(board, 2), "should be False")
    # print()

    ###################### Task 12 ######################

    # print("Task 12 tests:\n-------------\n")
    # print(is_draw(board), "should be False")
    # board = [[1, 2, 1],
    #          [1, 2, 2],
    #          [2, 1, 1]]
    # print(is_draw(board), "should be True")
    # print()

    ################### Play the game! ###################
    # play_game()