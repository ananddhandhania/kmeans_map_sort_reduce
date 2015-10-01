#!/usr/bin/env python

from math import sqrt
import sys

DIMENSION = 4
CLUSTERS = 2

current_means_file = open("means","rb")

mean = []
listOfCentres = []

def rms(x,mean):
	sum = 0
	for i in range(len(mean)):
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