from json import dumps
from copy import deepcopy

class MSP:

	def __init__(self, instanceFilename):
		self.instanceName = instanceFilename.split(".")[0]
		self.loadInstance(instanceFilename)
		self.initializeBounds()
		self.printInstance()

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
			self.meetingsData[d[0]] = dict({'dur': 0, 'start': 0, 'dist': dict(zip(d[1::2], map(int, d[2::2])))})

		for i in range(self.agentsTotal + self.meetingsTotal + 17, self.agentsTotal + self.meetingsTotal * 2 + 17):
			d = data[i].split()
			self.meetingsData[d[0]]['dur'] = int(d[1])

	def printInstance(self):
		print("Instance:", self.instanceName)
		print("Total Agents:", self.agentsTotal)
		print("Agents detail:")
		print(dumps(self.agentsData, sort_keys=True, indent=4))
		print("Total Meetings:", self.meetingsTotal)
		print("Meetings detail:")
		print(dumps(self.meetingsData, sort_keys=True, indent=4))
		print("lowerBound:", self.lowerBound)
		print("upperBound:", self.upperBound)

	def initializeBounds(self):
		self.lowerBound = 0
		self.upperBound = sum(v['dur'] for _, v in self.meetingsData.items()) + len(self.meetingsData) * sum(sum(v['dist'].values()) for _, v in self.meetingsData.items())

	def initializeSolution(self):
		self.minValue = float("inf")
		self.minSol = {}

	def checkSolution(self, sol):
		return True

	def getSolutionValue(self, sol):
		return 1

	def doBacktracking(self, sol, m):
		for i in range(self.lowerBound, self.upperBound + 1):
			sol[self.meetings[m]] = i

			if not self.checkSolution(sol):
				continue

			if m < len(self.meetings):
				self.doBacktracking(self, sol, m + 1)
			else:
				solValue = self.getSolutionValue(sol)
				if solValue < self.minValue:
					self.minValue = solValue
					self.minSol = deepcopy(sol)

	def solveInstance(self):
		sol = dict.fromkeys(self.meetingsData.keys(), 0)
		self.doBacktracking(self, sol, 1)

x = MSP("instance.dat")
