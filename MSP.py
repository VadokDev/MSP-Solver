
class MSP:

	def __init__(self, instanceFilename):
		self.instanceName = instanceFilename.split(".")[0]
		self.loadInstance(instanceFilename)

		self.agentsTotal = 0
		self.agents = {}
		self.meetingsTotal = 0
		self.meetings = {}

	def loadInstance(self, instanceFilename):
		with open(instanceFilename) as file:
			data = file.read().splitlines()

		self.agentsTotal = int(data[1])
		self.agents = dict.fromkeys(data[4].split(), {})
		self.meetingsTotal = int(data[7])
		self.meetings = dict.fromkeys(data[10].split(), {})
		print(data)
		print(self.agentsTotal)
		print(self.agents)
		print(self.meetingsTotal)
		print(self.meetings)
x = MSP("instance.dat")
