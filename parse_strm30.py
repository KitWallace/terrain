"""
   read a SRTM-30 file and rewrite the elevations in file matrix form
   input on stdin, output on stdout
   
"""
import sys
def read_point(l) :
    (lat,long,el) = l.split()
    slat = int(float(lat)*120) 
    slong = int(float(long)*120)
    return (slat,slong,el)

def move_origin(p,origin) :
    latn = p[0] - origin[0]
    longn = origin[1] - p[1]
    return (latn,longn,p[2])
    
f = sys.stdin
l = f.readline()  # starts with a blankline
l = f.readline()  # first point is the top left corer of the bounding box and will be the origin
origin = read_point(l)
row = origin[2]
long = 0
for l in f.readlines() :
    p = read_point(l)
    po = move_origin(p,origin)
    if (po[1] == long) :
        row += " " + po[2]
    else :
        print row
        long = po[1]
        row = po[2]
print row
