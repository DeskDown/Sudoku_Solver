## Python script to solve any Sudoku puzzle

This repo contains Python 3.* script to solve a given sudoku puzzle.

The solution guarantees that the number from 1 till 9:

* Appears exactly once in each row
* Appears exactly once in each column

* Appears exactly ones in 3 * 3 mini puzzles

A few rules indicates that the number should appear only once on the diagonals, the script tries to solve the puzzle with this restriction, if no solution is possible it tries again to find a solution with only three restrictions stated above.
