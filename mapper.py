#!/usr/bin/env python

from math import sqrt
import sys

DIMENSION = int(sys.argv[1])

current_means_file = open(sys.argv[2],"rb")

mean = []
listOfCentres = []

def rms(x,mean):
	sum = 0
	if len(x) != len(mean):
		raise Exception('Dimension of feature vector ' + str(len(x)) + ' does not match the dimension of mean vector ' + str(len(mean)))
	for i in range(len(x)):
		sum = sum + float(pow(float(x[i]) - float(mean[i]),2))
	return sqrt(sum)

def nearestCluster(x,listOfCentres):
	distance = float("inf")
	cluster = -1
	if len(x) == DIMENSION:
		for i in range(len(listOfCentres)):
			distanceWithCurrentCluster = rms(x,listOfCentres[i])
			if distanceWithCurrentCluster < distance :
				distance = distanceWithCurrentCluster
				cluster = i+1		
	else :
		raise Exception('Dimension : ' + str(DIMENSION) + ' does not match the size of feature : ' + str(len(x)))	
	return cluster

for line in current_means_file:
	line = line.strip()
	means = line.split("\t")
	listOfCentres.append(means)


for line in sys.stdin:
	line = line.strip()
	line = line.replace("[","")
	line = line.replace("]","")
	line = line.split(",")
	a= nearestCluster(line, listOfCentres)
	print a,'\t',line 
