# Sliding puzzle sample problems will be collected here.
# Puzzles can be in different sizes
# This file will be used to run tests for grading

# To generate your own examples, you can write a function that starts at the goal
# and makes a series of random moves. You define how many moves.
# This becomes your starting puzzle, and you have the solution.

class SlidingPuzzle(object) :
  def __init__( self, board, goal=None ):
    if not len(board) == len(board[0]):
      print('Puzzle must be square')
      return None
    
    # The board is a list of rows. Numbers are 1..n. The blank space is represented by 0
    self.board = board
    self.size = len(self.board)*len(self.board)
    self.rowLength = len(self.board)
    self.solution = []

    if not goal:
      # If not specified the goal state will be tiles ordered by rows with the blank space in the lower right.
      self.goal = []
      for tile in range(1, self.size, self.rowLength):
        self.goal.append(list( range( tile, tile+self.rowLength )))
      self.goal[self.rowLength-1][self.rowLength-1] = 0
    else:
      self.goal = goal

SlidingPuzzleTests = []
SlidingPuzzleTests.append( SlidingPuzzle( [[8,0,6],[5,4,7],[2,3,1]] ))

              





  
