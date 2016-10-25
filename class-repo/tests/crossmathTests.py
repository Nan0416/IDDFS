# Test puzzles for the crossmath problem will be collected here.
# This file will be used to run tests for grading

# Input format has rows and columns, each of which is a list of 2.
# Crossmath puzzles will be generated of any size n, such that n is a perfect square

# To create your own test puzzles of any size, write a function
# that randomly places n numbers in the n boxes, place random operators,
# apply the operators and generate the answers to each equation.
# This produces the solution for testing, and once you remove the interior
# numbers, you have a test puzzle to solve.

# See opDictionary.py for conversion from char to mathematical functions.

class CrossMathPuzzle(object) :
  def __init__( self, rows, cols, solution=[] ):
    # Each row and col has 2 elements: a list of operators, and the answer
    self.rows = rows
    self.cols = cols
    if not len(self.rows) == len(self.cols) :
      print('Not Valid Puzzle')
      return None
    self.size = len(self.rows)*len(self.rows)

    # The solution is a list of rows.
    self.solution = solution

CrossMathTests = []

#http://www2.stetson.edu/~efriedma/published/cross/index.html
CrossMathTests.append( CrossMathPuzzle(
  [[['+','+'],15],[['+','*'],24],[['+','-'],14]],
  [[['+','-'], 3],[['*','-'],12],[['/','/'], 4]],
  [[4,3,8],[5,7,2],[6,9,1]] ) )





  
