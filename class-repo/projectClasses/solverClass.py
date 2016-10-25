# generic Solver Class
# Create a file solver.py in your team repo.
# Each team member create a solver class for your specific algorithm in the 1 file

# Use this format ...
'''
class SolverBacktracking(Solver)
  - testCase format is CrossMathPuzzle object
  - SolverBacktracking.solve() returns list of rows
  
class SolverBidirectional(Solver)
  - testCase format is integer, representing number of discs for Towers
  - SolverBidirectional.solve() returns list of moves

class SolverIDDFS(Solver)
  - testCase format is integer, representing number of discs for Towers
  - SolverIDDFS.solve() returns list of moves

class SolverAStar(Solver)
  - testCase format is SlidingPuzzle object
  - SolverAStar.solve() returns list of tile positions

class SolverGA(Solver)
  - testCase format is integer, representing number of queens
  - SolverGA.solve() returns list of n integers

class SolverSA(Solver)
  - testCase format is integer, representing number of queens
  - SolverSA.solve() returns list of n integers
'''

'''
A test will look something like this:

for t in testCases :
  solver = SolverBacktracking( t.test )
  if ( t.solution == solver.solve() ) :
    passed += 1
    logger.log( t.test, True )
'''

class Solver(object):

  # The input parameters must be as is here
  def __init__( self, testCase, goal=None ):
    self.testCase = testCase
    self.goal = goal
    self.solution = None
    self.userid = 'lars1050' ### PUT THE PERSON WHO WROTE THE ALGORITHM HERE!!
    # This is a good place to create a problem instance.

  # return a solution in the specified format
  # An instance of a solver will be specific to the testCase, thus
  # the details of how to handle it will be hidden inside this method.
  def solve( self ):
    return None

  # print the solution in a user-friendly way
  def printSolution( self ):
    if self.solution:
      print(self.solution)

  # You can modify your solver class in any way, provided that above methods exist
    


