
class MSP:

	def __init__(self, instanceFilename):
		self.instanceName = instanceFilename.split(".")[0]
		self.loadInstance(instanceFilename)

	def loadInstance(self, instanceFilename):
		instanceFile = open(instanceFilename, "r+")
		with open(instanceFile) as file:
			# parseStuff

x = MSP("instance.dat")
