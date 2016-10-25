#Test Cases for Project

crossmathTests.py: Class and test puzzle with solution.
INPUT: class with .rows and .cols
SOLUTION: list of rows

slidingpuzzleTests.py: Class and test puzzle with goal.
INPUT: list of rows
GOAL: list of rows
SOLUTION: list of tile locations representing order of tiles moved into blank space

nQueens : There is no need for a test file.
INPUT: "n" for an nxn board
SOLUTION: a list of rows (i.e. 1 through n) representing the placement of a queen in each of the n columns

TowerOfHanoi : There is no need for a test file.
INPUT: "n" for a puzzle with n discs. Discs start on peg 1.
GOAL: All n discs on peg 3
SOLUTION: an ordered list signifying the move from peg to peg.
For example: [[1,3],[1,2],[3,2],[1,3],[2,1],[2,3],[1,3]], which represents
  1) move top disc from peg 1 to 3,
  2) move top disc from peg 1 to 2,
  3) move top disc from peg 3 to 2 ...

Stacks might be useful for representing each peg. Discs could be numbered from 1 to n, where the largest is 1. It might also be useful to use a sentinal of "0" to represent the bottom of an empty peg.


