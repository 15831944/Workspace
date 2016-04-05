from tkinter import *
from tkinter.ttk import Combobox
from cuttingDataContainer import cuttingDataContainer
from tkinter import filedialog
import pickle
from ThreadCAM import threadCAM
import webbrowser

#TODO
#Safe starting spot
#Infeed type
#Max RPM
#Safe position
#Follow through plane
#End Z

class mainGUI:
	def __init__(self):
		root = Tk()
		
		root.wm_title("ThreadCam")
		
		self.threadingVelocityVar = StringVar()
		self.groovingVelocityVar = StringVar()
		self.pitchToggle = StringVar()
		
		self.threadingToolEntry = {}
		self.groovingToolEntry = {}
		self.threadDataEntry = {}
		self.miscDataEntry = {}

		#Menubar
		menuBar = Menu(root)

		fileMenu = Menu(menuBar, tearoff=0)
		fileMenu.add_command(label="Open", command=self.openCommand)
		fileMenu.add_command(label="Save", command=self.saveCommand)
		fileMenu.add_separator()
		fileMenu.add_command(label="Exit", command=root.quit)
		menuBar.add_cascade(label="File", menu=fileMenu)
		
		programMenu = Menu(menuBar, tearoff=0)
		programMenu.add_command(label="Generate", command=self.generateMenuCommand)
		programMenu.add_command(label="Report...", command=self.reportCommand)
		menuBar.add_cascade(label="Program", menu=programMenu)

		root.config(menu=menuBar)
		#End Menubar

		#Tool Data Frame
		toolDataFrame = Frame()
		toolDataFrame.grid(padx=5, row=0, column=0, sticky=EW)
		toolDataFrame.columnconfigure(2, weight=1)

		label = Label(toolDataFrame, text="Tool Data", font=("Lucida Console bold", 18))
		label.grid(row=0, column=0, sticky=W)
		
		self.unitsVar = StringVar()
		self.unitsVar.trace('w', self.unitsChange)
		self.unitsBox = Combobox(toolDataFrame, state='readonly', width=10, textvar=self.unitsVar)
		self.unitsBox['values'] = ('Imperial', 'Metric')
		self.unitsBox.current(0)
		self.unitsBox.grid(row=0, column=2, sticky=E, padx=5)

		separator = Frame(toolDataFrame, height=2, bd=1, relief=SUNKEN)
		separator.grid(pady=5, row=1, columnspan=7, sticky=EW)

		#Threading Tool Data Frame
		threadingToolFrame = Frame(toolDataFrame)
		threadingToolFrame.grid(row=2, column=0, sticky=EW)

		label = Label(threadingToolFrame, text="Threading Tool", font=("Lucida Console", 14))
		label.grid(row=0, column=0, sticky=W)

		Label(threadingToolFrame, text="Tool Number")		.grid(row=1, column=0, sticky=W)
		Label(threadingToolFrame,
					textvar=self.threadingVelocityVar)		.grid(row=2, column=0, sticky=W)
		Label(threadingToolFrame, text="PDX")				.grid(row=3, column=0, sticky=W)
		Label(threadingToolFrame, text="NAP")				.grid(row=4, column=0, sticky=W)

		self.threadingToolEntry["toolNumber"]				= Entry(threadingToolFrame, width=10)
		self.threadingToolEntry["velocity"]					= Entry(threadingToolFrame, width=10)
		self.threadingToolEntry["PDX"]						= Entry(threadingToolFrame, width=10)
		self.threadingToolEntry["NAP"]						= Entry(threadingToolFrame, width=10)

		self.threadingToolEntry["toolNumber"]				.grid(row=1, column=1, sticky=W)
		self.threadingToolEntry["velocity"]					.grid(row=2, column=1, sticky=W)
		self.threadingToolEntry["PDX"]						.grid(row=3, column=1, sticky=W)
		self.threadingToolEntry["NAP"]						.grid(row=4, column=1, sticky=W)
		
		separator = Frame(threadingToolFrame, height=0, bd=0, relief=SUNKEN)
		separator.grid(padx=5, pady=5, row=5, columnspan=7)
		
		Label(threadingToolFrame, text="Insert ID")			.grid(row=6, column=0, sticky=W)
		Label(threadingToolFrame, text="Cutting Unit ID")	.grid(row=8, column=0, sticky=W)
		Label(threadingToolFrame, text="Clamping Unit ID")	.grid(row=10, column=0, sticky=W)
		self.threadingToolEntry["insertID"]					= Entry(threadingToolFrame, width=30)
		self.threadingToolEntry["unitID"]					= Entry(threadingToolFrame, width=30)
		self.threadingToolEntry["clampingID"]				= Entry(threadingToolFrame, width=30)
		self.threadingToolEntry["insertID"]					.grid(row=7, column=0, columnspan=2, sticky=W)
		self.threadingToolEntry["unitID"]					.grid(row=9, column=0, columnspan=2, sticky=W)
		self.threadingToolEntry["clampingID"]				.grid(row=11, column=0, columnspan=2, sticky=W)
		
		#End Threading Tool Data Frame

		separator = Frame(toolDataFrame, height=2, bd=1, relief=SUNKEN)
		separator.grid(padx=10, row=3, column=1)

		#Grooving Tool Data Frame
		groovingToolFrame = Frame(toolDataFrame)
		groovingToolFrame.grid(row=2, column=2, sticky=EW)

		label = Label(groovingToolFrame, text="Grooving Tool", font=("Lucida Console", 14))
		label.grid(row=0, column=0, sticky=W)

		Label(groovingToolFrame, text="Tool Number")		.grid(row=1, column=0, sticky=W)
		Label(groovingToolFrame,
						textvar=self.groovingVelocityVar)	.grid(row=2, column=0, sticky=W)
		Label(groovingToolFrame, text="Tool Width")		.grid(row=3, column=0, sticky=W)
		Label(groovingToolFrame, text="Number of Passes")	.grid(row=4, column=0, sticky=W)

		self.groovingToolEntry["toolNumber"]				= Entry(groovingToolFrame, width=10)
		self.groovingToolEntry["velocity"]					= Entry(groovingToolFrame, width=10)
		self.groovingToolEntry["toolWidth"]					= Entry(groovingToolFrame, width=10)
		self.groovingToolEntry["numberPasses"]				= Entry(groovingToolFrame, width=10)
		
		self.groovingToolEntry["toolNumber"]				.grid(row=1, column=1, sticky=W)
		self.groovingToolEntry["velocity"]					.grid(row=2, column=1, sticky=W)
		self.groovingToolEntry["toolWidth"]					.grid(row=3, column=1, sticky=W)
		self.groovingToolEntry["numberPasses"]				.grid(row=4, column=1, sticky=W)
		
		separator = Frame(groovingToolFrame, height=0, bd=0, relief=SUNKEN)
		separator.grid(padx=5, pady=5, row=5, columnspan=7)
		
		Label(groovingToolFrame, text="Insert ID")			.grid(row=6, column=0, sticky=W)
		Label(groovingToolFrame, text="Cutting Unit ID")	.grid(row=8, column=0, sticky=W)
		Label(groovingToolFrame, text="Clamping Unit ID")	.grid(row=10, column=0, sticky=W)
		self.groovingToolEntry["insertID"]					= Entry(groovingToolFrame, width=30)
		self.groovingToolEntry["unitID"]					= Entry(groovingToolFrame, width=30)
		self.groovingToolEntry["clampingID"]				= Entry(groovingToolFrame, width=30)
		self.groovingToolEntry["insertID"]					.grid(row=7, column=0, columnspan=2, sticky=W)
		self.groovingToolEntry["unitID"]					.grid(row=9, column=0, columnspan=2, sticky=W)
		self.groovingToolEntry["clampingID"]				.grid(row=11, column=0, columnspan=2, sticky=W)
		
		#End Grooving Tool Data Frame

		separator = Frame(toolDataFrame, height=2, bd=1, relief=SUNKEN)
		separator.grid(padx=5, pady=10, row=9, columnspan=6)
		#End Tool Data Frame

		#Thread Data Frame
		threadDataFrame = Frame()
		threadDataFrame.grid(padx=5, row=1, column=0, sticky=EW)
		threadDataFrame.columnconfigure(2, weight=1)

		w = Label(threadDataFrame, text="Thread Data", font=("Lucida Console bold", 18))
		w.grid(row=0, column=0, sticky=W)
		
		infoButton = Button(threadDataFrame, text="Info", command=self.threadInfoCommand)
		infoButton.grid(row=0, column=2, sticky=E, padx=5)

		separator = Frame(threadDataFrame, height=2, bd=1, relief=SUNKEN)
		separator.grid(pady=5, row=1, columnspan=7, sticky=EW)

		# photo = PhotoImage(file="Thread dimensions.gif")
		# w = Label(threadDataFrame, image=photo)
		# w.photo = photo
		# w.grid(padx=5, pady=5, row=2, columnspan=7, sticky=EW)
		
		#Thread Geometry Frame
		threadGeometryFrame = Frame(threadDataFrame)
		threadGeometryFrame.grid(row=2, column=0, columnspan=7, sticky=EW)
		threadGeometryFrame.columnconfigure(0, weight=3)
		threadGeometryFrame.columnconfigure(2, weight=1)
		threadGeometryFrame.columnconfigure(5, weight=5)
		
		Label(threadGeometryFrame, text="Thread Length")	.grid(row=0, column=0, sticky=W)
		Label(threadGeometryFrame, text="Chamfer Angle")	.grid(row=1, column=0, sticky=W)
		Label(threadGeometryFrame, text="Chamfer Length")	.grid(row=2, column=0, sticky=W)
		Label(threadGeometryFrame, text="Geometry")			.grid(row=3, column=0, sticky=W)
		
		Label(threadGeometryFrame, text="Front (A)")		.grid(row=1, column=1, sticky=W)
		Label(threadGeometryFrame, text="Front (a)")		.grid(row=2, column=1, sticky=W)
		Label(threadGeometryFrame,
			text="Max Crest\nDiameter",justify=LEFT)		.grid(row=3, column=1, sticky=W)
		
		self.threadDataEntry["threadLength"]				= Entry(threadGeometryFrame, width=10)
		self.threadDataEntry["frontAngle"]					= Entry(threadGeometryFrame, width=10)
		self.threadDataEntry["frontLength"]					= Entry(threadGeometryFrame, width=10)
		self.threadDataEntry["diameter"]					= Entry(threadGeometryFrame, width=10)
					
		self.threadDataEntry["threadLength"]				.grid(row=0, column=2, sticky=W)
		self.threadDataEntry["frontAngle"]					.grid(row=1, column=2, sticky=W)
		self.threadDataEntry["frontLength"]					.grid(row=2, column=2, sticky=W)
		self.threadDataEntry["diameter"]					.grid(row=3, column=2, sticky=W)
		
		Label(threadGeometryFrame, text="Measure")			.grid(row=0, column=3, sticky=W)
		Label(threadGeometryFrame, text="Back (B)")			.grid(row=1, column=3, sticky=W)
		Label(threadGeometryFrame, text="Back (b)")			.grid(row=2, column=3, sticky=W)
		Label(threadGeometryFrame,
					textvar=self.pitchToggle)				.grid(row=3, column=3, sticky=W)
		
		self.threadDataEntry["backAngle"]					= Entry(threadGeometryFrame, width=10)
		self.threadDataEntry["backLength"]					= Entry(threadGeometryFrame, width=10)
		self.threadDataEntry["TPI"]							= Entry(threadGeometryFrame, width=10)
		
		self.threadDataEntry["backAngle"]					.grid(row=1, column=4, sticky=W)
		self.threadDataEntry["backLength"]					.grid(row=2, column=4, sticky=W)
		self.threadDataEntry["TPI"]							.grid(row=3, column=4, sticky=W)
		
		self.threadDataEntry["measure"] = Combobox(threadGeometryFrame, state='readonly', width=3)
		self.threadDataEntry["measure"]['values'] = ('Z1', 'Z2', 'Z3')
		self.threadDataEntry["measure"].grid(row=0, column=4, sticky=W)
		#End Thread Geometry Frame
		
		separator = Frame(threadDataFrame, height=2, bd=1, relief=SUNKEN)
		separator.grid(padx=5, pady=10, row=3, columnspan=6)

		#Misc Data Frame
		miscDataFrame = Frame()
		miscDataFrame.grid(padx=5, row=3, column=0, sticky=EW)
		miscDataFrame.columnconfigure(2, weight=1)

		w = Label(miscDataFrame, text="Miscellaneous Data", font=("Lucida Console bold", 18))
		w.grid(row=0, column=0, sticky=W)
		
		infoButton = Button(miscDataFrame, text="Info", command=self.miscInfoCommand)
		infoButton.grid(row=0, column=2, sticky=E, padx=5)
		
		separator = Frame(miscDataFrame, height=2, bd=1, relief=SUNKEN)
		separator.grid(padx=5, pady=5, row=1, columnspan=7, sticky=EW)
		
		miscDataSubFrame = Frame(miscDataFrame)
		miscDataSubFrame.grid(row=2, column=0, sticky=EW)
		miscDataSubFrame.columnconfigure(0, pad=30)
		miscDataSubFrame.columnconfigure(1, pad=10)
		miscDataSubFrame.columnconfigure(2, pad=30)
		
		Label(miscDataSubFrame, text="Safe Point")		.grid(row=0, column=0, sticky=W)
		Label(miscDataSubFrame, text="Safe End")		.grid(row=0, column=2, sticky=W)
		Label(miscDataSubFrame, text="Retract Point")	.grid(row=1, column=0, sticky=W)
		Label(miscDataSubFrame, text="Z Shift")			.grid(row=1, column=2, sticky=W)
		
		safePointFrame = Frame(miscDataSubFrame)
		safePointFrame.grid(row=0, column=1, sticky=EW)
		Label(safePointFrame, text="X")					.grid(row=0, column=0, sticky=W)
		Label(safePointFrame, text="Z")					.grid(row=0, column=2, sticky=W)
		self.miscDataEntry["safePointX"]				= Entry(safePointFrame, width=10)
		self.miscDataEntry["safePointZ"]				= Entry(safePointFrame, width=10)
		self.miscDataEntry["safePointX"]				.grid(row=0, column=1, sticky=W)
		self.miscDataEntry["safePointZ"]				.grid(row=0, column=3, sticky=W)
		
		safeEndFrame = Frame(miscDataSubFrame)
		safeEndFrame.grid(row=0, column=3, sticky=EW)
		Label(safeEndFrame, text="Z")					.grid(row=0, column=0, sticky=W)
		self.miscDataEntry["safeEndZ"]					= Entry(safeEndFrame, width=10)
		self.miscDataEntry["safeEndZ"]					.grid(row=0, column=1, sticky=W)
		
		retractPointFrame = Frame(miscDataSubFrame)
		retractPointFrame.grid(row=1, column=1, sticky=W)
		Label(retractPointFrame, text="X")				.grid(row=0, column=0, sticky=W)
		self.miscDataEntry["retract"]					= Entry(retractPointFrame, width=10)
		self.miscDataEntry["retract"]					.grid(row=0, column=1, sticky=W)
		
		zShiftFrame = Frame(miscDataSubFrame)
		zShiftFrame.grid(row=1, column=3, sticky=E)
		Label(zShiftFrame, text="Z")					.grid(row=0, column=0, sticky=W)
		self.miscDataEntry["zShift"]					= Entry(zShiftFrame, width=10)
		self.miscDataEntry["zShift"]					.grid(row=0, column=1, sticky=W)

		followThroughFrame = Frame(miscDataSubFrame)
		followThroughFrame.grid(row=2, column=0, columnspan=5, sticky=W)
		followThroughFrame.columnconfigure(0, pad=30)
		
		Label(followThroughFrame, text="Clipping Follow Through Plane")\
														.grid(row=0, column=0, sticky=W)
		Label(followThroughFrame, text="X")				.grid(row=0, column=1, sticky=W)
		self.miscDataEntry["followThrough"]				= Entry(followThroughFrame, width=10)
		self.miscDataEntry["followThrough"]				.grid(row=0, column=2, sticky=W)
		
		separator = Frame(root, height=2, bd=1, relief=SUNKEN)
		separator.grid(padx=5, pady=5, row=4, columnspan=7, sticky=EW)

		#Browse Frame
		browseFrame = Frame(root)
		browseFrame.grid(row=5, column=0, sticky=EW, padx=5)
		browseFrame.columnconfigure(0, weight=1)

		self.FileEntry = Entry(browseFrame)						#Attribute
		self.FileEntry.grid(row=0, column=0, sticky=EW)
		browseButton = Button(browseFrame, text="Browse", command=self.browseCommand)	#Attribute
		browseButton.grid(row=0, column=1, sticky=W)
		#End Browse Frame

		GenerateButton = Button(root, text="Generate", command=self.generateCommand)		#Attribute
		GenerateButton.grid(row=6, column=0, sticky=EW, padx=5, pady=5)

		root.resizable(0, 0)

		root.mainloop()
	
	def generateCommand(self):
		filename = self.FileEntry.get()
		if filename == "":
			filename = filedialog.asksaveasfilename(defaultextension='.nc',
				filetypes=[(".NC files", ".nc"), ("Text files", ".txt"), ("All files", ".*")])
		if filename != "":
			self.generateCode(filename)
	
	def generateMenuCommand(self):
		filename = filedialog.asksaveasfilename(defaultextension='.nc',
			filetypes=[(".NC files", ".nc"), ("Text files", ".txt"), ("All files", ".*")])
		if filename != "":
			self.generateCode(filename)
		
	
	def generateCode(self, filename):
		currentData = self.readEntry()
		currentGen = threadCAM(currentData)
		threadCode = currentGen.threadCode()
		frontCode = currentGen.clipFrontCode()
		backCode = currentGen.clipBackCode()
		lastPassCode = currentGen.threadCode(True)
		
		try:
			text_file = open(filename, "w")
			text_file.write(threadCode)
			text_file.write(frontCode)
			text_file.write(backCode)
			text_file.write(lastPassCode)
			text_file.close()
			webbrowser.open(filename)
		except:
			print("Write failed")
	
	def openCommand(self):
		filename = filedialog.askopenfilename(filetypes=[("ThreadCAM files", ".tc"), ("All files", ".*")])
		try:
			with open(filename, 'rb') as input:
				currentData = pickle.load(input)
				for v in currentData.threadingToolValues.keys():
					self.threadingToolEntry[v].delete(0, END)
					self.threadingToolEntry[v].insert(0, currentData.threadingToolValues[v])
				for v in currentData.groovingToolValues.keys():
					self.groovingToolEntry[v].delete(0, END)
					self.groovingToolEntry[v].insert(0, currentData.groovingToolValues[v])
				for v in currentData.threadDataValues.keys():
					self.threadDataEntry[v].delete(0, END)
					self.threadDataEntry[v].insert(0, currentData.threadDataValues[v])
				for v in currentData.miscDataValues.keys():
					self.miscDataEntry[v].delete(0, END)
					self.miscDataEntry[v].insert(0, currentData.miscDataValues[v])
				
				if currentData.threadDataValues["measure"] == 'Z1':
					self.threadDataEntry["measure"].current(0)
				if currentData.threadDataValues["measure"] == 'Z2':
					self.threadDataEntry["measure"].current(1)
				if currentData.threadDataValues["measure"] == 'Z3':
					self.threadDataEntry["measure"].current(2)
				if currentData.units == 'Imperial':
					self.unitsBox.current(0)
				elif  currentData.units == 'Metric':
					self.unitsBox.current(1)
		except:
			print("No file")
		return
	
	def saveCommand(self):
		filename = filedialog.asksaveasfilename(defaultextension='.tc', filetypes=[("ThreadCAM files", ".tc"), ("All files", ".*")])
		try:
			with open(filename, 'wb') as output:
				currentData = self.readEntry()
				#print(currentData)
				pickle.dump(currentData, output, pickle.HIGHEST_PROTOCOL)
		except:
			print("No file")
		return
	
	def reportCommand(self):
		return
		
	def browseCommand(self):
		filename = filedialog.asksaveasfilename(defaultextension='.nc')
		self.FileEntry.delete(0, END)
		self.FileEntry.insert(0, filename)
		return
	
	def threadInfoCommand(self):
		return
		
	def miscInfoCommand(self):
		return
	
	def readEntry(self):
		threadingToolValues	= {v : self.threadingToolEntry[v].get() for v in self.threadingToolEntry.keys()}
		groovingToolValues 	= {v : self.groovingToolEntry[v].get() for v in self.groovingToolEntry.keys()}
		threadDataValues	= {v : self.threadDataEntry[v].get() for v in self.threadDataEntry.keys()}
		miscDataValues		= {v : self.miscDataEntry[v].get() for v in self.miscDataEntry.keys()}
		currentUnits = self.unitsVar.get()
		#print(threadingToolValues)
		#print(groovingToolValues)
		#print(threadDataValues)
		return cuttingDataContainer(threadingToolValues, groovingToolValues, threadDataValues, miscDataValues, currentUnits)
		
	def unitsChange(self, index, value, op):
		currentUnits = self.unitsVar.get()
		if currentUnits == 'Imperial':
			self.threadingVelocityVar.set('Velocity (ft/min)')
			self.groovingVelocityVar.set('Velocity (ft/min)')
			self.pitchToggle.set('TPI')
		elif currentUnits == 'Metric':
			self.threadingVelocityVar.set('Velocity (m/min)')
			self.groovingVelocityVar.set('Velocity (m/min)')
			self.pitchToggle.set('Pitch')
		#print("combobox updated to "+ self.unitsVar.get())
		return

if __name__ == "__main__":
	mainGUI()