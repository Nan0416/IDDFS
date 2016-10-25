# Team: CQQT
# Member: Nan Qin
# Student id: 5212291
# user id: qinxx232


from AIproblem import AIproblem
from copy import deepcopy
from collections import deque


class Kenken(AIproblem):
	def __init__(self, rule, size):
		# rule, inital, size
		self.rule = rule
		initial = []
		temp = []
		i = 0
	
		while i < size:
			temp.append(0)
			i += 1
			
		i = 0
		while i < size:
			initial.append(temp)
			temp = deepcopy(temp)
			i += 1
	
		for i in self.rule:
			# initialize the known element.
			if i[0][0] == " ":
				initial[i[1][0]][i[1][1]] = i[0][1]
		AIproblem.__init__(self, initial, size)
		self.setFlag = False
				
	def getActions(self, state):
		i = 0
		flag = False
		while i < self.size:
			j = 0
			while j < self.size:
				if state[i][j] == 0:
					flag = True
					break
				j += 1
			if flag:
				break
			i += 1
		if not flag:
			return []
		position = [i,j]
		actions = []
		row = state[i]
		col = []
		k = 0
		while k < self.size:
			col.append(state[k][j])
			k += 1
		k = 1
		choice = []
		while k <= self.size:
			if (k not in row) and (k not in col):
				new_position = deepcopy(position)
				new_position.append(k)
				actions.append(new_position)
			k += 1
		return actions
		
	def applyAction(self, state, action):
		if action:
			new_state = deepcopy(state)
			new_state[action[0]][action[1]] = action[2]
			return new_state
		else:
			return [] 
				
	
	def isGoal(self, state):
		
		for i in state:
			if 0 in i:
				return False
		result = True		
		# check operation's constriant
		for i in self.rule:
			if i[0][0] == "/":
				f_r = i[1][0]
				f_c = i[1][1]
				s_r = i[2][0]
				s_c = i[2][1]
				
				result = result and ((state[f_r][f_c] / state[s_r][s_c] == i[0][1]) or (state[s_r][s_c] / state[f_r][f_c] == i [0][1])) 
			elif i[0][0] == "-":
				f_r = i[1][0]
				f_c = i[1][1]
				s_r = i[2][0]
				s_c = i[2][1]
				
				result = result and ((state[f_r][f_c] - state[s_r][s_c] == i[0][1]) or (state[s_r][s_c] - state[f_r][f_c] == i [0][1]))
			elif i[0][0] == "*":
				rs = 1
				for ele in i[1:]:
					 rs *= state[ele[0]][ele[1]]
				result = result and (rs == i[0][1])
			elif i[0][0] == "+":
				rs = 0
				for ele in i[1:]:
					 rs += state[ele[0]][ele[1]]
				result = result and (rs == i[0][1])
			elif i[0][0] == " ":
				pass
				# do nothing.
			else:
				print("operator error")
				return False
			if not result:
				return False
		return result
		
	def result(self, node):
		return node.getState()

	def print_result(self, result):
		
		# print("Result: ")
		for i in result:
			for j in i:
				print("  ",j, end="")
			print()
	

