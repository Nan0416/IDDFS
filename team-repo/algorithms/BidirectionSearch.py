# Team CQQT 
# Member Nan Qin
# userid qinxx232
# Birdirectional Search


from copy import deepcopy
from collections import deque
from node import Node


def Bidirectional_search(problem):
	Node.recordPath = problem.setFlag
	node_init = Node(problem.initial)
	node_goal = Node(problem.goal)
	if problem.isIntersection(node_init.getState(), node_goal.getState()):
		return deque([node_goal.getState()])
	explored_state_init = []
	explored_state_goal = []	
	frontier_init = deque()
	frontier_init.append(node_init)
	frontier_goal = deque()
	frontier_goal.append(node_goal)
	layer_init = []
	layer_goal = []
	
	while len(frontier_init) > 0 and len(frontier_goal) > 0:
		#put into explored list
		for i in layer_init:
			explored_state_init.append(i.getState())
		for i in layer_goal:
			explored_state_goal.append(i.getState())
		
		layer_init = []
		layer_goal = []
		
		# expand a node that comes from the initial state.
		# also remove the explored stated.
		while len(frontier_init) > 0:
			# get all node of the same layer
			temp_init = frontier_init.popleft()
			temp_expand_init = temp_init.expand(problem)
			for next_node in temp_expand_init:
				if next_node.getState() not in explored_state_init:
					layer_init.append(next_node)
		# expand a node that comes from the goal state.
		# also remove the explored stated.	
		while len(frontier_goal) > 0:
			temp_goal = frontier_goal.popleft()
			temp_expand_goal = temp_goal.expand(problem)
			for next_node in temp_expand_goal:
				if next_node.getState() not in explored_state_goal:
					layer_goal.append(next_node)
			
		flag = True
		for node_from_init in layer_init:
			for node_from_goal in layer_goal:	
				if problem.isIntersection(node_from_init.getState(), node_from_goal.getState()):
					# different problems have different form of solutions,
					# eg. solution of sudoku is just a state,
					# solution of tower of hanoi is a path.
					# so the problem's result method helps return result.
				
					return problem.result(node_from_init, node_from_goal)
				if flag:
					# flag used to guarantee frontier_goal only includes every node once.
					frontier_goal.append(node_from_goal)
			flag = False
			frontier_init.append(node_from_init)
			
	return None
