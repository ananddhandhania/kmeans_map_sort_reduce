#!/usr/bin/python

import sys
import numpy as np
from operator import itemgetter
a = np.array([["",""]])

for line in sys.stdin:
	line = line.strip()
	key,value = line.split("\t")
	a = np.append(a,[[key,value]], axis=0)

b = sorted(a, key=itemgetter(0))
for i in range(1,len(b)):
	print "%s\t%s" % (b[i][0],b[i][1])
