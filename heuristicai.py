import random
import game
import sys

# Author:			chrn (original by nneonneo)
# Date:				11.11.2016
# Description:		The logic of the AI to beat the game.

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
count = 0 

def find_best_move(board):
    bestmove = -1    
	
	# TODO:
	# Build a heuristic agent on your own that is much better than the random agent.
	# Your own agent doesn't have to beat the game.
    bestmove = find_best_move_random_agent()
    return bestmove

def find_best_move_random_agent():
    # modify this so that it is not random and their is some type of intelligence behind it. 
    # Does it matter if I know the values of the blocks
    # Does my program know the values of the block
    
    return random.choice([UP,DOWN,LEFT,RIGHT])


def execute_move(move, board):
    """
    move and return the grid without a new random tile 
	It won't affect the state of the game in the browser.
    """

    if move == UP:
        return game.merge_up(board)
    elif move == DOWN:
        return game.merge_down(board)
    elif move == LEFT:
        return game.merge_left(board)
    elif move == RIGHT:
        return game.merge_right(board)
    else:
        sys.exit("No valid move")

def board_equals(board, newboard):
    """
    Check if two boards are equal
    """
    return  (newboard == board).all()  

def first_two_moves():
    if count == 0: 
        return LEFT 
        count += 1 
    
    return Down 
