import numpy as np
import random
import math
import operator
 
def calcDist(dist1, dist2, length):
	distance = 0
	for x in range(length):
		distance += pow((dist1[x] - dist2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance) - 1
	for x in range(len(trainingSet)):
		dist = calcDist(testInstance, trainingSet[x],length)
		distances.append((trainingSet[x],dist))
	distances.sort(key = operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def findByRow(mat, row):
	return np.where((mat == row).all(1))[0]
	
def main():
	data_X = np.loadtxt("testdata.txt",delimiter = ',',usecols = (0,1,2,3,4))
	data_X = np.array(data_X)
	new = np.array([40,46,66,55,60])
	neighbors = getNeighbors(data_X, new, 1)
	neighbors = np.array(neighbors)
	num = findByRow(data_X, neighbors)

	if(0 <= num <= 19):
		print('输入 ' + repr(new))
		print('匹配 ' + repr(neighbors))
		print("这是一个好学生")
	if(20 <= num <= 39):
		print('输入 ' + repr(new))
		print('匹配 ' + repr(neighbors))
		print("这是一个中等学生")
	if(40 <= num <= 60):
		print('输入 ' + repr(new))
		print('匹配 ' + repr(neighbors))
		print("这是一个差学生")
	
main()