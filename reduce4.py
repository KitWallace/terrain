"""
 average 4 adjacent points to reduce the size of the array 


"""
import sys, math
from numpy import *

elev = loadtxt(sys.stdin)
maxi = elev.shape[0]
maxj = elev.shape[1]
sys.stderr.write('input ' + ', '.join(map(str, elev.shape ))+ "\n")

ni = maxi //2 
nj = maxj //2

sys.stderr.write('output ' + ', '.join((str(ni),str(nj)))+ "\n")

r= zeros([ni,nj])

for i in range(0, maxi-1,2) :
     for j in range(0, maxj-1,2) :
        c = elev[i,j]+elev[i+1,j]+elev[i+1,j+1]+elev[i,j+1]
        r[i//2,j//2] = c/4
savetxt(sys.stdout,r,"%1.2f")
