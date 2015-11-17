"""
   missing data  -s coded as -999 - this filter uses clip to ensure that  the minimum elevation is the value of parameter 0


"""

import sys, math
from numpy import *

min_elev = float(sys.argv[1])
elev = loadtxt(sys.stdin)
sys.stderr.write("set minimum to "+ str(min_elev)+'\n')
# replace missing data -9999 by 0 
clip(elev,min_elev,9999999,elev)
savetxt(sys.stdout,elev,"%1.2f")
