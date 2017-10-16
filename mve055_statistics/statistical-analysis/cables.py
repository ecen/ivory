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
	
def printStats(listA, t99, t95):
	print("----------------------")
	print("N = {0}".format(len(listA)))
	print("Mean: {0:.4f}".format(stat.mean(listA)))
	print("Sample stdDev: {0:.4f}".format(stat.stdDeviation(listA)))
	print("99% Conf Interval: [{0:.4f}, {1:.4f}]".format(*stat.confIntervalMean(t99, listA)))
	print("95% Conf Interval: [{0:.4f}, {1:.4f}]".format(*stat.confIntervalMean(t95, listA)))

printStats(lengths1, 2.896, 1.860)
printStats(lengths2, 2.567, 1.740)

stat.wilcoxonRankSum(lengths1, lengths2)