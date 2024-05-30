#!/usr/bin/python3
"""N Queens Puzzle Solver"""
import sys


def print_solutions(solutions):
    """Print all solutions in the required format"""
    for solution in solutions:
        print(solution)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, col, solutions):
    """Utilize backtracking to find all solutions"""
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, solutions)
            board[i][col] = 0


def solve_nqueens(n):
    """Solve the N Queens puzzle and print solutions"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
