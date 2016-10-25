
from AIproblem import AIproblem
from copy import deepcopy
from collections import deque

class SlidingPuzzle(AIproblem):
	def __init__(self, board):
		if not len(board) == len(board[0]):
			print('Puzzel must be square')
			return
		self.initial  = board
		self.size = len(self.initial) ** 2
		self.rowLength = len(self.initial)
		self.solution = []
		self.setFlag = True
		
	def getActions(self, state):
		# get the 0's position
		i = 0
		j = 0
		#actions = []
		flag = False
		while i < self.rowLength:
			j = 0
			while j < self.rowLength:
				if state[i][j] == 0:
					flag = True
					break
				j += 1
			if flag:
				break
			i += 1
		if i == self.rowLength or j == self.rowLength:
			print("Error detected. No legal actions exist.")
			return []
		#print('getActions, 0"s position	' ,state, i, j, state[i][j])
		if i == 0:
			if j == 0:
				return [[[0, 1],[0, 0]], [[1, 0], [0, 0]]]
			elif j == self.rowLength - 1:
				return [[[i, j-1],[i, j]], [[i+1, j], [i, j]]]
			else:
				return [[[i+1, j], [i, j]], [[i, j- 1], [i, j]], [[i, j + 1], [i, j]]]
		elif i == self.rowLength - 1:
			if j == 0:
				return [[[i - 1, j],[i ,j]], [[i , 1], [i ,j]]]
			elif j == self.rowLength - 1:
				return [[[i - 1, j],[i ,j]], [[i , j-1], [i ,j]]]
			else:
				return [[[i-1, j], [i, j]], [[i, j- 1], [i, j]], [[i, j + 1], [i, j]]]
		else:
			if j == 0:
				return [[[i - 1, j],[i ,j]], [[i + 1 , j], [i ,j]], [[i, j + 1], [i, j]]]
			elif j == self.rowLength - 1:
				return [[[i - 1, j],[i ,j]], [[i + 1 , j], [i ,j]], [[i , j -1 ], [i, j]]] 
			else:
				return [[[i-1, j], [i, j]], [[i, j- 1], [i, j]], [[i, j + 1], [i, j]], [[i+ 1, j], [i ,j]]]
		
	def applyAction( self, state, action ) :
		# action = [[1,2], [1,1]]
		if not action:
			return []
		else:
			
			newPosition= action[1]
			oldPosition = action[0]
			newState = deepcopy(state)
			newState[newPosition[0]][newPosition[1]] = newState[oldPosition[0]][oldPosition[1]]
			newState[oldPosition[0]][oldPosition[1]] = 0
			#print("new state, ", newState, state, action)
			return newState
					
	def isGoal(self, state):
		# the last element must be 0
		#print(state)
		if state[self.rowLength - 1][self.rowLength - 1]:
			return False
		i = 0
		j = 0
		flag = False
		while i < self.rowLength:
			j = 0
			while j < self.rowLength:
				if i == self.rowLength - 1 and j == self.rowLength - 1:
					if state[i][j] == 0:
						return True
				if not state[i][j] == i * self.rowLength + j + 1:
					return False
				j += 1
			i += 1
		return False
					

	def result(self, node):
		result = deque()
		while node.parent:
			result.appendleft(node.getState())
			node = node.parent
		result.appendleft(node.getState())
		return result
					
	

	def print_result(self, result):
		print(result)
		
