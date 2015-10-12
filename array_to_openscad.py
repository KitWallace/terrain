
import sys, math
from numpy import *

def surface_to_openSCAD (surface,name,f) :
    f.write( "// surface" + name   + "\n")
    maxi = surface.shape[1]-1
    maxj = surface.shape[0]-1
    f.write("surface = [ \n")
    for i in range(0, maxi) :
       f.write("[ \n")
       for j in range(0, maxj) :
          f.write( str(surface[j][i]) + ", ")
       f.write("],\n")
    f.write("];\n")


surface = loadtxt(sys.stdin)

surface_to_openSCAD(surface,"surface", sys.stdout)
