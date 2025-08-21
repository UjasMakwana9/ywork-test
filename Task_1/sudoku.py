def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:  # Check row
            return False
        if board[i][col] == num:  # Check column
            return False
        # Check 3x3 box
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False
    return True

def solve_sudoku_iterative(board):
    stack = []
    # Find all empty cells
    empties = [(r, c) for r in range(9) for c in range(9) if board[r][c] == '.']
    idx = 0
    while idx < len(empties):
        row, col = empties[idx]
        found = False
        # Try next possible value
        start = int(board[row][col]) + 1 if board[row][col] != '.' else 1
        for num in range(start, 10):
            if is_valid(board, row, col, str(num)):
                board[row][col] = str(num)
                stack.append((idx, num))
                idx += 1
                found = True
                break
        if not found:
            board[row][col] = '.'
            if not stack:
                return False  # No solution
            idx, last_num = stack.pop()
            row, col = empties[idx]
            board[row][col] = str(last_num)
    return True

given_input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

if solve_sudoku_iterative(given_input):
    for row in given_input:
        print(row)
else:
    print("No solution found")