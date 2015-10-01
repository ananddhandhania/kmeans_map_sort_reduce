#!/usr/bin/env python

DIMENSION = 4
import sys

previous_cluster = -1
sum = [0,0,0,0]
cluster_size = 0

def add(sample,sum):
	for i in range(len(sample)):
		sum[i] = float(sum[i]) + float(sample[i])
	return sum


def normalized(sum,cluster_size):
	for i in range(len(sum)):
		sum[i] = float(sum[i])/cluster_size
	return sum

for line in sys.stdin:
	line = line.strip()
	cluster,sample_string = line.split("\t")
	sample_string = sample_string.replace("[","")
	sample_string = sample_string.replace("]","")
	sample_string  =sample_string.replace("'","")
	sample = sample_string.split(",")
	if previous_cluster == cluster:
		sum = add(sample,sum)
		cluster_size = cluster_size + 1
	else :
		if previous_cluster != -1:
			print previous_cluster,'\t',normalized(sum,cluster_size)
		sum = sample
		cluster_size = 1
		previous_cluster = cluster

print previous_cluster,'\t',normalized(sum,cluster_size)		
