import json

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
		self.agents = dict.fromkeys(data[4].split(), [])
		self.meetingsTotal = int(data[7])
		self.meetings = dict.fromkeys(data[10].split(), 0)

		for i in range(13, self.agentsTotal + 13):
			d = data[i].split()
			self.agents[d[0]] = d[1::]

		for i in range(self.agentsTotal + 15, self.agentsTotal + self.meetingsTotal + 15):
			d = data[i].split()
			self.meetings[d[0]] = dict({'dur': 0, 'start': 0, 'dist': dict(zip(d[1::2], map(int, d[2::2])))})

		for i in range(self.agentsTotal + self.meetingsTotal + 17, self.agentsTotal + self.meetingsTotal * 2 + 17):
			d = data[i].split()
			self.meetings[d[0]]['dur'] = int(d[1])
			
		print(data)
		print(self.agentsTotal)
		print(self.agents)
		print(self.meetingsTotal)
		print(json.dumps(self.meetings, sort_keys=True, indent=4))

x = MSP("instance.dat")
