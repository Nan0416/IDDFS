import sys,os
sys.path.append( os.path.realpath('..') + '/projectClasses' )

import math
import random
import copy

from opDictionary import ops

def flatten( Alist ):
  z = []
  for el in Alist:
    z.extend(el)
  return z

#---------------------------------------
def createCrossMathPuzzle( n ):
  
  # Check for valid size of puzzle
  if not int(math.sqrt(n))*math.sqrt(n) == n:
    print("n must be perfect square")
    return

  # Generate a randomly ordered list of 1 to n, then regroup into solution form
  rowLength = int(math.sqrt(n))
  opChoice = [ '+', '-','*' ]
  squares = [ i for i in range(1,n+1) ]
  random.shuffle(squares)
  solution = []
  for r in range(0,rowLength*rowLength,rowLength):
    solution.append( [ i for i in squares[r:r+rowLength] ] )

  # randomly generate operators for rows and columns
  rowops=[]
  for r in range(rowLength):
    opindex = [ random.randint(0,2) for i in range(rowLength-1) ]
    rowops.append( [ opChoice[i] for i in opindex ] )
  colops = []
  for c in range(rowLength):
    opindex = [ random.randint(0,2) for i in range(rowLength-1) ]
    colops.append( [ opChoice[i] for i in opindex ] )

  # apply the operators to the operands to get answer for each row
  rows = []
  operands = copy.copy(squares)
  # apply operator to first 2 elements (popped), then push results to use as operand for next operator
  for r in rowops:
    for o in r:
      operands.insert(0,ops[o](operands.pop(0), operands.pop(0)))
    rows.append( [ r,operands.pop(0) ] )

  # as above, apply the operators, except that we have to transpose the operands to apply to columns
  cols = []
  operands = copy.deepcopy(solution)
  # Thanks to Ian Johnson for a compact transpose
  operands = flatten(list(map(list,zip(*operands))))
  for c in colops:
    for o in c:
      operands.insert(0,ops[o](operands.pop(0), operands.pop(0)))
    cols.append( [ c,operands.pop(0) ] )

  return [ rows, cols, solution ]

if __name__ == "__main__":
  puzzle = createCrossMathPuzzle( 9 )
  print(puzzle)

    
