
from copy import deepcopy
from time import time

class MSP:

	def __init__(self, instanceFilename):
		self.instanceName = instanceFilename.split(".")[0]
		self.loadInstance(instanceFilename)
		self.initializeBounds()
		self.printInstance()
		self.initializeSolution()
		self.solveInstance()
		self.printSolution()

	def loadInstance(self, instanceFilename):
		with open(instanceFilename) as file:
			data = file.read().splitlines()

		self.agents = data[4].split()
		self.agentsTotal = int(data[1])
		self.agentsData = dict.fromkeys(data[4].split(), [])

		self.meetings = data[10].split()
		self.meetingsTotal = int(data[7])
		self.meetingsData = dict.fromkeys(self.meetings, 0)

		for i in range(13, self.agentsTotal + 13):
			d = data[i].split()
			self.agentsData[d[0]] = d[1::]

		for i in range(self.agentsTotal + 15, self.agentsTotal + self.meetingsTotal + 15):
			d = data[i].split()
			self.meetingsData[d[0]] = dict({'dur': 0, 'agents': [], 'start': 0, 'dist': dict(zip(d[1::2] + [d[0]], list(map(int, d[2::2])) + [0]))})

		for i in range(self.agentsTotal + self.meetingsTotal + 17, self.agentsTotal + self.meetingsTotal * 2 + 17):
			d = data[i].split()
			self.meetingsData[d[0]]['dur'] = int(d[1])

		for agent, meetings in self.agentsData.items():
			for meeting in meetings:
				if not agent in self.meetingsData[meeting]['agents']:
					self.meetingsData[meeting]['agents'].append(agent)

		self.B = dict.fromkeys(self.meetingsData.keys(), -1)

		for m1 in self.meetings:
			self.B[m1] = dict.fromkeys(self.meetingsData.keys(), 0)
			for m2 in self.meetings:
				if set(self.meetingsData[m1]['agents']) & set(self.meetingsData[m1]['agents']):
					self.B[m1][m2] = 1

	def initializeBounds(self):
		self.lowerBound = 0
		self.upperBound = sum(v['dur'] for _, v in self.meetingsData.items()) + sum(sum(v['dist'].values()) for _, v in self.meetingsData.items())

	def initializeSolution(self):
		self.minValue = float("inf")
		self.minSol = {}

	def printInstance(self):
		print("Instance name:", self.instanceName)
		print("Total Agents:", self.agentsTotal)
		print("Total Meetings:", self.meetingsTotal)
		print("Details:")

		for m, data in self.meetingsData.items():
			print(" Meeting:", m )
			print("   Agents:", ' '.join(data['agents']) )
			print("   Duration:", data['dur'] )

	def printSolution(self):
		print("Instance", self.instanceName, "solved.")
		print("Iterations:", self.iterations)
		print("Objetive function value:", self.minValue)
		print("Elapsed time: %s [s]" % (self.endTime - self.startTime))
		print("Scheduling details:")

		for m, schedule in self.minSol.items():
			print(" Meeting:", m, "scheduled at", schedule)

	def checkSolution(self, sol):
		O = dict.fromkeys(self.meetingsData.keys(), -1)

		for m1 in self.meetings:
			O[m1] = dict.fromkeys(self.meetingsData.keys(), 0)
			for m2 in self.meetings:
				if m1 == m2:
					continue

				if self.B[m1][m2] and sol[m1] < sol[m2]:
					O[m1][m2] = 1

		for m1 in self.meetings:
			for m2 in self.meetings:
				if m1 == m2:
					continue

				if (sol[m1] + self.meetingsData[m1]['dur'] + self.meetingsData[m1]['dist'][m2]) * O[m1][m2] * self.B[m1][m2] > sol[m2]:
					return False

				if O[m1][m2] + O[m2][m1] != 1:
					return False
		return True

	def getSolutionValue(self, sol):
		val = 0
		for m1 in self.meetings:
			for m2 in self.meetings:
				val += abs(sol[m1] + self.meetingsData[m1]['dur'] - sol[m2])

		return val

	def doBacktracking(self, sol, m):
		for i in range(self.lowerBound, self.upperBound + 1):
			self.iterations += 1
			sol[self.meetings[m]] = i
				
			if m < len(self.meetings) - 1:
				self.doBacktracking(sol, m + 1)
			else:
				if not self.checkSolution(sol):
					continue
					
				solValue = self.getSolutionValue(sol)
				if solValue < self.minValue:
					self.minValue = solValue
					self.minSol = deepcopy(sol)

	def solveInstance(self):
		sol = dict.fromkeys(self.meetingsData.keys(), 0)
		self.iterations = 0
		self.startTime = time()
		self.doBacktracking(sol, 0)
		self.endTime = time()

x = MSP("exampleInstance.dat")
