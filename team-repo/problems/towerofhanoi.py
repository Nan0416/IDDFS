# Team: CQQT
# Member: Nan Qin
# Student id: 5212291
# user id: qinxx232


from AIproblem import AIproblem
from copy import deepcopy
from collections import deque
class TowerOfHanoi(AIproblem):
	def __init__(self, size):
		initialState = [deque() , deque() ,deque()]
		self.size = size
		i = size
		while i > 0:
			initialState[0].append(i)
			i -= 1
		
		goal = [deque(), deque()]
		goal.append(deepcopy(initialState[0]))
		AIproblem.__init__(self, initialState, size, goal = goal)
		self.setFlag = True
		
	def getActions(self, state):
		actions = []
		l0 = len(state[0])
		l1 = len(state[1])
		l2 = len(state[2])
		if l0:
			temp0 = state[0][l0-1]
			if l1:
				temp1 = state[1][l1-1] 
				if l2:
					temp2 = state[2][l2-1] 
					if temp0 < temp1:
						actions.append([0,1])
					else:
						actions.append([1,0])
					if temp0 < temp2: 
						actions.append([0,2])
					else:
						actions.append([2,0])
					if temp1 < temp2:
						actions.append([1,2])
					else:
						actions.append([2,1])
							
				else:
					actions.append([0,2])
					actions.append([1,2])
					if temp0 < temp1:
						actions.append([0,1])
					else:
						actions.append([1,0])

			else:
				if l2:
					temp2 = state[2][l2-1]
					actions.append([0,1])
					actions.append([2,1])
					if temp0 < temp2:
						actions.append([0,2])
					else:
						actions.append([2,0])
				else:
					actions.append([0,1])
					actions.append([0,2])
			
		else:
			if l1:
				if l2:
					actions.append([1,0])
					actions.append([2,0])
					if state[1][l1-1] < state[2][l2-1]:
						actions.append([1,2])
					else:
						actions.append([2,1])
				else:
					actions.append([1,0])
					actions.append([1,2])
			else:
				actions.append([2,0])
				actions.append([2,1])
					
		return actions
	def applyAction( self, state, action ) :
		
		if not action:
			return []
		else:
			newState = deepcopy(state)
			newState[action[1]].append(newState[action[0]].pop())
			return newState
			
	def isIntersection(self, state1, state2):
		# for bidirectional checking
		result = True
		i = 0
		while i < 3 and result:
			result = result and (state1[i] == state2[i])
			i += 1
		return result
	def isGoal(self, state):
		
		result = True
		i = 0
		while i < 3 and result:
			result = result and (state[i] == self.goal[i])
			i += 1
		return result
	
	def result(self, node1, node2 = None):
		# bidirection has two input
		if node2:
			#print(node2.recordPath,"===")
			result = deque()
			while node1.parent:
				result.appendleft(node1.getState())
				node1 = node1.parent
			result.appendleft(self.initial)
			# avoid to append repeate intersected nodes.
			node2 = node2.parent
			while node2.parent:
				result.append(node2.getState())
				node2 = node2.parent
			result.append(self.goal)
			
		else:
			result = deque()
			while node1.parent:
				result.appendleft(node1.getState())
				node1 = node1.parent
			result.appendleft(self.initial)
		movement = []
		left = result.popleft()
		while len(result) > 0:
			right = result.popleft()
			temp = [0,0]
			i = 0
			while i < 3:
				if len(left[i]) < len(right[i]):
					temp[1] = i
				elif len(left[i]) > len(right[i]):
					temp[0] = i
				i += 1
			movement.append(temp)
			left = right
			
		return movement
					
	def print_result(self, solution):
		i = 1
		for move in solution:
			print("Step ", i, " : From ", move[0]+1, " to ", move[1]+1, ".", sep = "")
			i += 1
		
		
#	def print_result(self, result):
#		print("Result: ", len(result)-1)
#		i = 0
#		while i < self.size:
#			print("  ", end="")
#			i += 1
#		print("1st", end="")
#		i = 0
#		while i < self.size:
#			print("  ", end="")
#			i += 1
#		print("2nd", end="")
#		i = 0
#		while i < self.size:
#			print("   ", end="")
#			i += 1
#		print("3rd", end="\n")
#		for i in result:
#			for j in i:
#				for k in j:
#					print("",k, end="")
#				l = self.size - len(j)
#				print("       ", end="")
#				while l > 0:
#					print("  ",end="")
#					l -= 1
#			print()

