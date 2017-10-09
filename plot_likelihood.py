import numpy as np
import pickle,gzip
import sys
from pylab import *
fname = sys.argv[1]
data = pickle.load(gzip.open(fname))
results = data['results']
x = np.zeros(len(results.keys()));y = np.zeros(len(results.keys())) 

max_lk = max(results.values())
min_lk = min(results.values())
for i,key in enumerate(sorted(results.keys())):
	x[i] = float(key)
	y[i] = (results[key] - min_lk)/(max_lk -min_lk)



plot(x,y);show()
