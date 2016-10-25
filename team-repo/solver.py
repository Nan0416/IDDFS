import sys,os
sys.path.append('algorithms')
sys.path.append('problems')
sys.path.append( os.path.realpath('..') + '/class-repo/projectClasses' )
import time
from towerofhanoi import TowerOfHanoi
from kenken import Kenken
from memory_profiler import *
from BidirectionSearch import Bidirectional_search
from IDDFS import IDDFS
# a revised version for IDDFSv2
from IDDFS import RevisedIDDFSv2
from IDDFS import RevisedIDDFSv3
from solverClass import Solver
from sliding import SlidingPuzzle

class IDDFSSlidingv2(Solver):
	def __init__(self, testCase):
		Solver.__init__(self, testCase)
		self.problem = SlidingPuzzle(self.testCase)
		self.userid = "qinxx232"
	#@profile
	def solve(self):
		self.solution = RevisedIDDFSv2(self.problem)
		return self.solution
	def printSolution(self):
		if self.solution:
			print("Using IDDFS: ")
			self.problem.print_result(self.solution)

class IDDFSSliding(Solver):
	def __init__(self, testCase):
		Solver.__init__(self, testCase)
		self.problem = SlidingPuzzle(self.testCase)
		self.userid = "qinxx232"
	#@profile
	def solve(self):
		self.solution = IDDFS(self.problem)
		return self.solution
	def printSolution(self):
		if self.solution:
			print("Using IDDFS: ")
			self.problem.print_result(self.solution)



'''
print(" ==== === == IDDFS == === ====")

a = time.time()
print('current time,', a)
testCase = [[1,2,3,4], [0, 5, 7, 8],[9, 6, 10, 12],[13, 14,11, 15 ]] #
s = IDDFSSliding(testCase)
s.solve()
print("time clapsed, ", time.time() - a)
s.printSolution()
'''
'''
print(" ==== === == Revisedv2 == === ====")

a = time.time()
print('current time,', a)
testCase = [[1,2,3,4], [5, 6, 7, 8],[9, 10,11, 12],[13, 14,15, 0 ]] #
s = IDDFSSlidingv2(testCase)
s.solve()
print("time clapsed, ", time.time() - a)
s.printSolution()
'''
'''

	
print(" ==== === == 17 IDDFS == === ====")

a = time.time()
print('current time,', a)
testCase = [[2,5,3,4], [1,8,10,12],[9,6, 7, 15],[13,0, 14, 11]] #
s = IDDFSSliding(testCase)
s.solve()
print("time clapsed, ", time.time() - a)
s.printSolution()

print(" ==== === == 17 Revisedv2 == === ====")

a = time.time()
print('current time,', a)
testCase = [[2,5,3,4], [1,8,10,12],[9,6, 7, 15],[13,0, 14, 11]] # #
s = IDDFSSlidingv2(testCase)
s.solve()
print("time clapsed, ", time.time() - a)
s.printSolution()


'''




class SolverIDDFST(Solver):
	# IDDFS solves Tower of Hanoi
	def __init__(self, testCase):
		Solver.__init__(self, testCase)
		self.problem = TowerOfHanoi(self.testCase)
		self.userid = "qinxx232"
	#@profile
	def solve(self):
		self.solution = IDDFS(self.problem)
		return self.solution
		
	def printSolution(self):
		if self.solution:
			print("Using IDDFS: ")
			self.problem.print_result(self.solution)
'''
for i in [1, 2, 3, 4]:
	print('---- IDDFS on Tower of Hanoi, case', i , "----")
	s = SolverIDDFST(i)
	s.solve()
	s.printSolution()
'''





	

class SolverIDDFSt(Solver):
	# IDDFS solves Tower of Hanoi
	def __init__(self, testCase):
		Solver.__init__(self, testCase)
		self.problem = TowerOfHanoi(self.testCase)
		self.userid = "qinxx232"
	#@profile	
	def solve(self):
		self.solution = RevisedIDDFSv2(self.problem)
		return self.solution
		
	def printSolution(self):
		if self.solution:
			print("Using IDDFS: ")
			self.problem.print_result(self.solution)

s= SolverIDDFSt(5)
s.solve()
s.printSolution()

'''
for i in[1,2,3,4,5,6,7,8,9,10]:
	print('==== === == Revised >> Tower of Hanoi, case', i, "== === ====")
	s = SolverIDDFSt(i)
	s.solve()
	s.printSolution()		

'''	
