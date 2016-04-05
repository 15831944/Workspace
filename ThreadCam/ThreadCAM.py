import math

class threadCAM():
	def __init__(self, cuttingData):
		self.threadingToolValues	= cuttingData.threadingToolValues
		self.groovingToolValues		= cuttingData.groovingToolValues
		self.threadDataValues		= cuttingData.threadDataValues
		self.miscDataValues			= cuttingData.miscDataValues
		
		self.typeConversion()
		
		self.units					= cuttingData.units
		self.threadEnd				= self.findThreadEnd()
		if self.units == 'Imperial':
			self.initImperial()
		elif self.units == 'Metric':
			self.initMetric()
		self.startPoint = self.findStartPoint()
		self.feed = self.pitch
		self.threadPasses = self.depthOfCut(self.threadingToolValues['NAP'])
		self.groovingPasses = self.depthOfCut(self.groovingToolValues['numberPasses'])
		self.threadDataValues["frontAngle"] = math.radians(self.threadDataValues["frontAngle"])
		self.threadDataValues["backAngle"] = math.radians(self.threadDataValues["backAngle"])
	
	def initImperial(self):
		self.pitch = 1/self.threadDataValues["TPI"]
		self.threadingRPM = round((self.threadingToolValues["velocity"]*12)/(math.pi*(self.threadDataValues["diameter"])))
		self.groovingRPM = round((self.groovingToolValues["velocity"]*12)/(math.pi*(self.threadDataValues["diameter"])))
	
	def initMetric(self):
		self.pitch = self.threadDataValues["TPI"] #Bad name, pitch in this case
		self.threadingRPM = round((self.threadingToolValues["velocity"]*1000)/(math.pi*(self.threadDataValues["diameter"])))
		self.groovingRPM = round((self.groovingToolValues["velocity"]*1000)/(math.pi*(self.threadDataValues["diameter"])))
	
	def findThreadEnd(self):
		absEnd = 0
		if self.threadDataValues["measure"] == 'Z1':
			absEnd = self.threadDataValues["threadLength"] + self.threadDataValues["frontLength"]
		elif self.threadDataValues["measure"] == 'Z2':
			absEnd = self.threadDataValues["threadLength"]
		elif self.threadDataValues["measure"] == 'Z3':
			absEnd = self.threadDataValues["threadLength"]\
				+ self.threadDataValues["frontLength"]\
				- self.threadDataValues["backLength"]
		return -absEnd
	
	def findStartPoint(self):
		self.pitchCount = round((abs(self.threadEnd)/self.pitch) + 3)
		# if self.pitchCount % 0.5 < 0.05:
			# self.pitchCount -= self.pitchCount % 0.5
		# else:
			# self.pitchCount -= self.pitchCount % 0.5
			# self.pitchCount += 0.5
		return (self.pitchCount*self.pitch)+self.threadEnd
	
	def chamferOffset(self, cLength, DOCf, angle):
		return cLength - (DOCf/math.tan(angle))
		
	def depthOfCut(self, numOfPasses):
		DOC = []
		DOC.append(((0.6495*self.pitch)/math.sqrt(numOfPasses-1))*math.sqrt(0.3))
		for i in range(1, numOfPasses):
			DOC.append(((0.6495*self.pitch)/math.sqrt(numOfPasses-1))*math.sqrt(i))
		return DOC
	
	def threadCode(self, lastPass = False):
		threadString =\
			"G28;\n" +\
			"T{0:02.0f}{0:02.0f};\n\n"
		threadString = threadString.format(
			self.threadingToolValues["toolNumber"])
		
		if lastPass:
			operation = "Thread - Last Pass"
		else:
			operation = "Thread"
	
		threadString +=\
			"(Operation: {})\n" +\
			"(Clamping Unit ID: {})\n" +\
			"(Cutting Unit ID: {})\n" +\
			"(Insert ID: {})\n" +\
			"(Vc: {:.0f})\n" +\
			"(RPM: {:.0f})\n" +\
			"(Fn: {:.6f})\n\n"
		threadString = threadString.format(
			operation,
			self.threadingToolValues["clampingID"],
			self.threadingToolValues["unitID"],
			self.threadingToolValues["insertID"],
			self.threadingToolValues["velocity"],
			self.threadingRPM,
			self.feed)
		
		threadString +=\
			"(Thread)\n" +\
			"G97 S{} M03;\n" +\
			"G00 G54 Z{:.4f};\n" +\
			"X{:.4f} M24;\n" +\
			"Z{:.4f} M08;\n\n"
		threadString = threadString.format(
			self.threadingRPM,
			self.miscDataValues['safePointZ'],
			self.miscDataValues['safePointX'],
			self.startPoint)
		
		if lastPass:
			passIndex = -1
		else:
			passIndex = 0
		
		threadString +=\
			"G92 X{:.4f} Z{:.4f} F{:.6f};\n"
		threadString = threadString.format(
			self.threadDataValues["diameter"] - 2*self.threadPasses[passIndex],
			self.miscDataValues["safeEndZ"],
			self.feed)
		
		if not lastPass:
			for d in self.threadPasses[1:-1]:
				threadString += "X{:.4f};\n"
				threadString = threadString.format(
					self.threadDataValues["diameter"] - 2*d)
				
		threadString +=\
			"\nG80;\n\n" +\
			"G28 X{:.4f} M09;\n" +\
			"G28;\n" +\
			"M01;\n\n"
		threadString = threadString.format(
			self.miscDataValues["retract"])
		return threadString
	
	def clipFrontCode(self):
		frontString =\
			"G28;\n" +\
			"T{0:02.0f}{0:02.0f};\n\n"
		frontString = frontString.format(
			self.groovingToolValues["toolNumber"])

		frontString +=\
			"(Operation: Clip Thread)\n" +\
			"(Clamping Unit ID: {})\n" +\
			"(Cutting Unit ID: {})\n" +\
			"(Insert ID: {})\n" +\
			"(Vc: {:.0f})\n" +\
			"(RPM: {:.0f})\n" +\
			"(Fn: {:.6f})\n\n"
		frontString = frontString.format(
			self.groovingToolValues["clampingID"],
			self.groovingToolValues["unitID"],
			self.groovingToolValues["insertID"],
			self.groovingToolValues["velocity"],
			self.groovingRPM,
			self.feed)
		
		frontString +=\
			"(Clip Thread)\n" +\
			"G97 S{:.0f} M03;\n" +\
			"G00 G54 Z{:.4f};\n" +\
			"X{:.4f}\n" +\
			"Z{:.4f} M08;\n\n" +\
			"(Front)\n"
		frontString = frontString.format(
			self.groovingRPM,
			self.miscDataValues['safePointZ'],
			self.miscDataValues['safePointX'],
			self.startPoint + self.threadingToolValues['PDX'])
		
		CO = self.chamferOffset(self.threadDataValues["frontLength"],
						self.groovingPasses[-1],
						self.threadDataValues["frontAngle"])
		
		for c in self.groovingPasses:
			frontString +=\
				"X{:.4f};\n" +\
				"G32 Z{:.4f} F{:.6f};\n" +\
				"X{:.4f} Z{:.4f};\n" +\
				"G00 Z{:.4f};\n\n"
			
			cutX = self.threadDataValues["diameter"] - 2*c
			firstZ = -self.pitch - CO
			exitZ = -(((self.miscDataValues['followThrough']-cutX)/2)/math.tan(self.threadDataValues['frontAngle'])) + firstZ
			
			frontString = frontString.format(
				cutX,
				firstZ,
				self.feed,
				self.miscDataValues['followThrough'],
				exitZ,
				self.startPoint + self.threadingToolValues['PDX'])
		return frontString
		
	def clipBackCode(self):
		toolComp = self.threadingToolValues["PDX"] - self.groovingToolValues["toolWidth"]
		ZStart = self.startPoint - (self.pitchCount-4)*(self.pitch) + toolComp
		backString =\
			"(Back)\n" +\
			"G00 X{:.4f}\n\n"
		backString = backString.format(
			self.miscDataValues['followThrough'])
			
		for c in self.groovingPasses:
			cutX = self.threadDataValues["diameter"] - 2*c
			enterZ = (((self.miscDataValues['followThrough']-cutX)/2)/math.tan(self.threadDataValues['backAngle']))
			
			backString +=\
				"G32 Z{0:.4f} F{1:.6f};\n" +\
				"X{2:.4f} Z{3:.4f};\n" +\
				"X{2:.4f} Z{4:.4f};\n" +\
				"G00 X{5:.4f} Z{4:.4f};\n" +\
				"Z{6:.4f};\n\n"
			
			backString = backString.format(
				self.threadEnd + enterZ + toolComp,
				self.feed,
				cutX,
				self.threadEnd + toolComp,
				self.miscDataValues["safeEndZ"],
				self.miscDataValues['followThrough'],
				ZStart)
			
		backString +=\
			"G28 U0 M09\n" +\
			"G28\n" +\
			"M01\n\n"
		return backString
	
	def typeConversion(self):
		floatConv = ['toolNumber', 'velocity', 'PDX']
		for f in floatConv:
			self.threadingToolValues[f] = float(self.threadingToolValues[f])
		floatConv = ['toolNumber', 'velocity', 'toolWidth']
		for f in floatConv:
			self.groovingToolValues[f] = float(self.groovingToolValues[f])
		floatConv = ['threadLength', 'frontAngle', 'frontLength', 'diameter', 'backAngle', 'backLength', 'TPI']
		for f in floatConv:
			self.threadDataValues[f] = float(self.threadDataValues[f])
		floatConv = ['safePointX', 'safePointZ', 'safeEndZ', 'retract', 'zShift', 'followThrough']
		for f in floatConv:
			self.miscDataValues[f] = float(self.miscDataValues[f])
		
		self.threadingToolValues['NAP'] = int(self.threadingToolValues['NAP'])
		self.groovingToolValues['numberPasses'] = int(self.groovingToolValues['numberPasses'])
		