
def count_adjacent_squares(matrix):
    rows = len(matrix)
    if rows == 0:
        return 0  # Empty matrix
    
    cols = len(matrix[0])
    if cols == 0:
        return 0  # Empty rows

    count = 0  # Initialize count

    for row in range(rows):
        for col in range(cols):
            print(row, col)
            for cell_in_row in range(cols):
                # in range and only the rows bellow
                if cell_in_row < cols and cell_in_row > row:
                    print('\t',cell_in_row, col)
            
            
            # Check if the current cell is not empty
            # if matrix[row][col] != 0:
                
            #     for j in range(cols):
            #         # Check the cell below (if within bounds)
            #         if j + 1 < rows and matrix[row][col] == matrix[row][j+1]:
            #             print("(",row,",",col,") (", j ,",", col, ")")
            #             print(matrix[row][col],  matrix[row][j])
            #             count += 1

    return count

# Example usage:
matrix = [
    [1, 2, 2, 3],
    [0, 2, 2, 4],
    [1, 5, 6, 7],
    [5, 5, 6, 7]
]

result = count_adjacent_squares(matrix)
print("Count of adjacent squares below with the same value:", result)
