"""
 average 9 adjacent points to reduce the size of the array  3 fold in each direction
 
"""
import sys, math
from numpy import *

elev = loadtxt(sys.stdin)
maxi = elev.shape[0]
maxj = elev.shape[1]
sys.stderr.write(sys.argv[0]+'\n')
sys.stderr.write('Input ' +', '.join(map(str, elev.shape ))+ "\n")

ni = maxi //3 
nj = maxj //3

sys.stderr.write('Output ' +', '.join((str(ni),str(nj)))+ "\n")

r= zeros([ni,nj])

for i in range(0, maxi-1,3) :
     for j in range(0, maxj-1,3) :
        c = elev[i,j]  +elev[i,j+1]  +elev[i,j+2]  +elev[i+1,j]+elev[i+1,j+1]+elev[i+1,j+2] +elev[i+2,j]+elev[i+2,j+1]+elev[i+2,j+2]
        r[i//3,j//3] = c/9
savetxt(sys.stdout,r,"%1.2f")
