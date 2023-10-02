#!/usr/bin/python3
"""program that solves the N queens problem

The N queens puzzle is the challenge
of placing N non-attacking queens on an N×N chessboard .

Usage:
    $./101-nqueens.py N

N must be a number >= 4.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


if __name__ == "__main__":
    n_args = len(sys.argv)
    if n_args != 2:
        print("Uage: nqueens N")
        sys.exit(1)
    N = sys.argv[1]
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
