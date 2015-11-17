"""
 analysis of an array
 
"""
import sys, math
from numpy import *

missing_value = -9999
elev = loadtxt(sys.stdin)
maxi = elev.shape[0]
maxj = elev.shape[1]

missing = 0
min = 999999999999
max = -99999999999
for i in range(0, maxi-1) :
     for j in range(0, maxj-1) :
        e = elev[i,j]
        if (e == missing_value) :
            missing=missing+1
        else :
           if (e < min):
               min = e
           if (e > max) :
               max = e

print("Shape " + ', '.join(map(str, elev.shape )))
print("Points " + str(elev.shape[0] * elev.shape[1]))
print("missing (" +str(missing_value) + ") " + str(missing))
print("min " +str(min) + " max " + str(max) + ' range ' + str(max-min))
 
