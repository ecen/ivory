import sys
sys.path.insert(0, "../exercises/")

import statistical as stat
import math
import re


class Cable:
	def __init__(self, cableType, length, circumference):
		self.cableType = cableType
		self.length = length
		self.diameter = circumference / math.pi
		self.longType = ""
		if (cableType == "B"):
			self.longType = "Banana connector"
		elif (cableType == "P"):
			self.longType = "Power cable"
		elif (cableType == "BC"):
			self.longType = "Banana to Coaxial"
		elif (cableType == "CK"):
			self.longType = "Crocodile to Coaxial"
		elif (cableType == "RV"):
			self.longType = "RJ11 to DB9"
		elif (cableType == "U"):
			self.longType = "USB"
		elif (cableType == "V"):
			self.longType = "VGA"
		elif (cableType == "WV"):
			self.longType = "DB9"
		elif (cableType == "E"):
			self.longType = "Ethernet"
		elif (cableType == "C"):
			self.longType = "Coaxial"
	def __str__(self):
		return self.cableType + "\t" + str(self.length) + "\t" + "{0:.4f}".format(self.diameter)

dataFile = open("cablesDataRaw.txt", "r")

dataList = dataFile.readlines()

cableList = []
i = 0
for row in dataList:
	dataList[i] = row.replace("\n", "")
	entrys = re.split(r"\t+", dataList[i])
	cableType = entrys[0]
	length = int(entrys[1])
	circumference = int(entrys[2])
	cableList.append(Cable(cableType, length, circumference))
	#print(dataList[i])
	print(cableList[i])
	i += 1
	
lengths1 = []
for cable in cableList:
	if (cable.cableType == "P"):
		lengths1.append(cable.length)
		
lengths2 = []
for cable in cableList:
	if (cable.cableType == "B"):
		lengths2.append(cable.length)
		
print(lengths1)
print(lengths2)
	
def printStats(listA, t99, t95):
	print("----------------------")
	print("N = {0}".format(len(listA)))
	print("Mean: {0:.4f}".format(stat.mean(listA)))
	print("Sample stdDev: {0:.4f}".format(stat.stdDeviation(listA)))
	print("99% Conf Interval: [{0:.4f}, {1:.4f}]".format(*stat.confIntervalMean(t99, listA)))
	print("95% Conf Interval: [{0:.4f}, {1:.4f}]".format(*stat.confIntervalMean(t95, listA)))
	
def printData(listA, label):
	print("% --- {0} ---".format(label))
	print("{0}L = {1}".format(label, list(map(lambda c: c.length, listA))))
	print("{0}D = {1}".format(label, list(map(lambda c: c.diameter, listA))))

printStats(lengths1, 2.896, 1.860)
printStats(lengths2, 2.567, 1.740)

#print("\nFor Wilcoxon: ")
#stat.wilcoxonRankSum(lengths1, lengths2, "Power cable", "Banana connector")

print("\nFor matlab: ")
#print(list(map(lambda c: c.length, cableList)))
#print(list(map(lambda c: c.diameter, cableList)))
Bs = []
Ps = []
BCs = []
CKs = []
RVs = []
Us = []
Vs = []
WVs = []
Es = []
Cs = []
for cable in cableList:
	if (cable.cableType == "B"):
		Bs.append(cable);
	elif (cable.cableType == "P"):
		Ps.append(cable);
	elif (cable.cableType == "BC"):
		BCs.append(cable)
	elif (cable.cableType == "CK"):
		CKs.append(cable)
	elif (cable.cableType == "RV"):
		RVs.append(cable)
	elif (cable.cableType == "U"):
		Us.append(cable)
	elif (cable.cableType == "V"):
		Vs.append(cable)
	elif (cable.cableType == "WV"):
		WVs.append(cable)
	elif (cable.cableType == "E"):
		Es.append(cable)
	elif (cable.cableType == "C"):
		Cs.append(cable)
		
printData(Bs, "Banana")
printData(Ps, "Power")
printData(BCs, "BananaCoaxial")
printData(CKs, "CrocodileCoaxial")
printData(RVs, "RJ11DB89")
printData(Us, "USB")
printData(Vs, "VGA")
printData(WVs, "DB9")
printData(Es, "Ethernet")
printData(Cs, "Coaxial")

#print("\nFor LaTeX: ")
#for c in cableList:
#	print("{0}\t& {1}\t& {2:.1f}\t\\\\ \\hline".format(*[c.longType.ljust(20), c.length, c.diameter]))