""" convert from an array file of elevations to a triangulated STL file 
  parameters
    1 base_m  - base height in m  - if -999 then use minimum elevation
    2 unit_m - horizontal metres per unit
    3 vscale - vertical scale  = default 1 
    4 latitude - to correct the longitude grid - 0 if no correction needed
    5 scale - overall scaling of object
    6 base_mm - height of base in mm (after scaling)

  input on stdin, output on stdout
  
  uses  generate_STL
  Chris Wallace  April 2014
       moded October 2015
  
"""

import sys, math
from generate_STL import *
from numpy import *

base_m = float(sys.argv[1])
unit_m= float(sys.argv[2])
vscale = float(sys.argv[3])
lat = float(sys.argv[4])
scale= float(sys.argv[5])
base_mm = float(sys.argv[6])

elev = loadtxt(sys.stdin)

if base_m == -999 :
   min= amin(elev)
else:
   min= base_m

elev -= min
vscale_per_unit = scale * vscale / unit_m
hscale = scale * cos(radians(lat))
elev =  elev * vscale_per_unit  # not *= 
elev += base_mm
elev = flipud(elev)

surface_to_STL(elev,[hscale,scale],0, "terrain", sys.stdout)

       
