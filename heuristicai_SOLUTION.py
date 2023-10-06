import random
import sys

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
count = 0

def find_best_move(board):
    best_move = -1
    global count

    # Rule 1: Place the largest value in a corner and stay there.
    if count == 0:
        best_move = DOWN
        count += 1
        return best_move
    elif count == 1:
        best_move = RIGHT
        count += 1
        return best_move

    # Rule 2: Choose two directions to keep the largest value in the chosen corner.
    # Prioritize filling a row to open a third possible direction,
    # merging blocks to open more space, and merging large blocks.
    best_move = prioritize_moves(board)
    return best_move

def prioritize_moves(board):
    # Implement logic to prioritize moves based on rules 2a(i), 2a(ii), and 2a(iii).
    # You can analyze the current board state and choose moves accordingly.

    # For example, you can check which directions are valid based on the current board state
    # and prioritize moves to achieve the desired outcome.

    # This is a placeholder logic. You should replace it with your own implementation.
    valid_moves = get_valid_moves(board)
    if valid_moves:
        return random.choice(valid_moves)
    else:
        # Rule 3: If you cannot move in 3 directions from above, move in the fourth direction
        # while trying to follow Rule 1.
        return follow_rule_1()

def follow_rule_1():
    # Implement logic to move in the fourth direction while trying to follow Rule 1
    # (placing the largest value in a corner).

    # This is a placeholder logic. You should replace it with your own implementation.
    return LEFT  # Move in the fourth direction (LEFT) as a fallback option.

def get_valid_moves(board):
    # Implement logic to determine valid moves based on the current board state.
    # You should return a list of valid move directions.

    # Access the board array and determine in which direction you can move

    # This is a placeholder logic. You should replace it with your own implementation.
    valid_moves = [UP, DOWN, LEFT, RIGHT]
    return valid_moves

def get_valid_moves(board):
    valid_moves = []

    # Check if moving DOWN is a valid option based on the current board state.
    if can_move_down(board):
        valid_moves.append(DOWN)

    # Check if moving LEFT is a valid option based on the current board state.
    if can_move_left(board):
        valid_moves.append(LEFT)

    # You can add additional checks for other directions if needed.

    return valid_moves

def can_move_down(board):
    # Implement logic to check if moving DOWN is a valid option based on the current board state.
    # You can analyze the board to determine if moving down is possible.
    # Return True if it's a valid move, otherwise return False.
    
    #Check the board
    


    # This is a placeholder logic. You should replace it with your own implementation.
    return True  # Placeholder logic; replace with actual condition

def can_move_left(board):
    # Implement logic to check if moving LEFT is a valid option based on the current board state.
    # You can analyze the board to determine if moving left is possible.
    # Return True if it's a valid move, otherwise return False.

    # This is a placeholder logic. You should replace it with your own implementation.
    return True  # Placeholder logic; replace with actual condition


def can_move_right(board):
    # Implement logic to check if moving LEFT is a valid option based on the current board state.
    # You can analyze the board to determine if moving left is possible.
    # Return True if it's a valid move, otherwise return False.

    # This is a placeholder logic. You should replace it with your own implementation.
    return True  # Placeholder logic; replace with actual condition

def can_move_up(board):
    # Implement logic to check if moving LEFT is a valid option based on the current board state.
    # You can analyze the board to determine if moving left is possible.
    # Return True if it's a valid move, otherwise return False.

    # This is a placeholder logic. You should replace it with your own implementation.
    return True  # Placeholder logic; replace with actual condition
