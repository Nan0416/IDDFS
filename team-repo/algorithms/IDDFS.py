# Team CQQT 
# Member Nan Qin
# userid qinxx232
# Birdirectional Search

import time
from copy import deepcopy
from collections import deque
from node import Node


def IDDFS(problem):
	nodeCounts = []
	depth = 1
	Node.recordPath = problem.setFlag
	start = time.time()
	while True:
		print(depth)
		Node.nodeCount = 0
		result = DLS(problem, depth, nodeCounts)
		
		print(depth, 'time:', time.time()-start, Node.nodeCount)
		start = time.time()
		if result:
			sums = 0
			for i in nodeCounts:
				sums += i
			print("|_|-|_|-\  result, #node:", result.nodeCount, "result depth, ", depth, "node Counts ", nodeCounts, sums)
			return problem.result(result)
		else:
			depth += 1
			

def DLS(problem, limit, nodeCounts):
	node = Node(problem.initial)
	froniter = deque()
	froniter.append(node)
	while len(froniter) > 0:
		node = froniter.pop()
		#print(node.state, limit, node.depth)
		if node.depth < limit:
			if problem.isGoal(node.getState()):
				nodeCounts.append(node.nodeCount)
				return node
			else:
				successor = node.expand(problem)
				for i in successor:
					# avoid graph search
					if not i.getState() == node.getState():
						froniter.append(i)
	nodeCounts.append(node.nodeCount)
	return None

#
#
# Because in each Depth-limited search, it may meet some nodes with same state but different 
# depths, therefore, we only need to test these states that we do not meet before, and these states that 
# we have dealt but with a lower depth
#
# using test when generate
#


def RevisedIDDFSv2(problem):
	nodeCounts = []
	Node.recordPath = problem.setFlag
	depth = 1
	start = time.time()
	while True:
		print(depth)
		
		Node.nodeCount = 0
		result = Revised_DLSv2(problem, depth, nodeCounts)
		print(depth, 'time:', time.time()-start, Node.nodeCount)
		start = time.time()
		if result:
			sums = 0
			for i in nodeCounts:
				sums += i
			print("|_|-|_|-\  result, #node:", result.nodeCount, "result depth, ", depth, "node Counts ", nodeCounts, sums)
			return problem.result(result)
		else:
			depth += 1
# test when generate
#from memory_profiler import *
#@profile
def Revised_DLSv2(problem, limit, nodeCounts):
	node = Node(problem.initial)
	froniter = deque()
	if problem.isGoal(node.getState()):
		return node
	explored_nodes = [node]
	froniter.append(node)
	while len(froniter) > 0:
		#print("length, ---", len(explored_nodes))
		node = froniter.pop()
		if node.depth < limit:
			if True:
				successor = node.expand(problem)
				for i in successor:
					#print('State,', i.getState())
					flag = True
					# avoid graph search
					for j in froniter:
						if i.getState() == j.getState():
							# since the node depth of froniter is less than or equal to node depth of successor
							# therefore, if we meet the same state, just ignore the node from successor
							
							#print("---- get future")
							flag = False
							break
					if flag:
						for j in explored_nodes:
							if i.getState() == j.getState() and i.depth >= j.depth:
							#print('---- get explored')
								flag = False
								break
					
							
					if flag:
						
						if problem.isGoal(i.getState()):
							nodeCounts.append(node.nodeCount)
							return i
						explored_nodes.append(i)	
						froniter.append(i)
	nodeCounts.append(node.nodeCount)				
	return None


'''
def nextdepth(current):
	if current < 50:
		current += 10
	elif current < 80:
		current += 8
	elif current < 350:
		current += 40
	else:
		current += 80
	return current
'''
def RevisedIDDFSv3(problem):
	Node.recordPath = problem.setFlag
	depth = 15
	flag_hasfound = False
	solution = 0
	solution = None
	while True:
		print("current depth:", depth)
		result = Revised_DLSv3(problem, depth)
		if result:
			solution = result
			#print(result.depth)
			depth = result.depth - 1
		else:
			if solution:
				return solution
			depth = depth + 10
# test when generate
def Revised_DLSv3(problem, limit):
	
	node = Node(problem.initial)
	froniter = deque()
	if problem.isGoal(node.getState()):
		return node
	explored_nodes = [node]
	froniter.append(node)
	while len(froniter) > 0:
		#print("length ",len(explored_nodes))
		node = froniter.pop()
		if node.depth < limit:
			if True:
				successor = node.expand(problem)
				for i in successor:
					#print('state, ',i.getState())
					flag = True
					# avoid graph search
					for j in froniter:
						if i.getState() == j.getState():
							# since the node depth of froniter is less than or equal to node depth of successor
							# therefore, if we meet the same state, just ignore the node from successor
							
							#print("---- get future")
							flag = False
							break
					for j in explored_nodes:
						if i.getState() == j.getState() and i.depth >= j.depth:
							#print('---- get explored')
							flag = False
							break
					
							
					if flag:
						if problem.isGoal(i.getState()):
							return i
						explored_nodes.append(i)	
						froniter.append(i)
					
	return None
