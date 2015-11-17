"""
  parameters
      system LL (WSG84 lat//long ) or OS (ordinance Survey easting northing)
      top left 
      bottom right 
  
  extracts heights from uklidar 2m DTM data
  
  - edit to handle DTM and 1m resolution
  
  assumes data is in directory uklidar

  output as array to stdout
  
  Chris Wallace Nov 2015
  
  kitwallace.co.uk
  
"""
import sys
import numpy as np
from WGS84_to_UKGrid import *
from scipy import *

OSletters = [
["SV","SW","SX","SY","SZ","TV"],
["","SR","SS","ST","SU","TQ","TR"],
["","SM","SN","SO","SP","TL","TM"],
["","","SH","SJ","SK","TF","TG"],
["","","SC","SD","SE","TA"],
["","NW","NX","NY","NZ","OV"],
["","NR","NS","NT","NU"],
["NL","NM","NN","NO"],
["NF","NG","NH","NJ","NK"],
["NA","NB","NC","ND"],
["","HW","HX","HY","HZ"],
["","","","HT","HU"],
["","","","","HP"]
]

def OS_to_Grid4(e,n) :
     e1= e//100
     n1 =n//100
     prefix = OSletters[n1][e1]
     tile=prefix + str(e -100*e1) + str(n-100*n1)
     return tile.lower()

    
def load_tile(tile) :  #return the elevation array for this tile 
   prefix = tile[:2] 
   path="uklidar/"+tile+"_DTM_2m.asc"
   sys.stderr.write(path+"\n");
   return  np.loadtxt(path,  skiprows=6)

sys.stderr.write(sys.argv[0]+'\n')

system = sys.argv[1]
samples_per_tile = 500
rscale = 2
tile_size = samples_per_tile * rscale

if (system == "OS") :
   east_tl = float(sys.argv[2])
   north_tl = float(sys.argv[3])
   east_br = float(sys.argv[4])
   north_br= float(sys.argv[5])
elif (system == "LL"):
   lat_tl = float(sys.argv[2])
   long_tl = float(sys.argv[3])
   lat_br = float(sys.argv[4])
   long_br= float(sys.argv[5])
   (east_tl,north_tl) = WGS84toOSGB36(lat_tl, long_tl)
   (east_br,north_br) = WGS84toOSGB36(lat_br, long_br)
else:
   print("System " + system + " not known")

(east_tl,north_tl) = (int(east_tl),int(north_tl))
(east_br,north_br) = (int(east_br),int(north_br))

sys.stderr.write("Grid TL "+str(east_tl)+","+str(north_tl)+ " BR "+str(east_br)+","+str(north_br)+ "\n")

(grid_north_tl, grid_east_tl) = (int(north_tl/tile_size), int(east_tl/tile_size))
(grid_north_br, grid_east_br) = (int(north_br/tile_size), int(east_br/tile_size))

sys.stderr.write("Rounded TL "+str(grid_east_tl)+","+str(grid_north_tl)+ " BR "+str(grid_east_br)+","+str(grid_north_br)+ "\n")

for north in range(grid_north_br,grid_north_tl+ 1)  :
   for east in range(grid_east_tl,grid_east_br + 1)  :
       tile = OS_to_Grid4(east,north)
       h=load_tile(tile)
       tile_north_min = samples_per_tile - int(min (tile_size, north_tl - north * tile_size) / rscale)
       tile_north_max=  samples_per_tile - int(max (0 , north_br -  north * tile_size) / rscale )
       tile_east_max = int(min (tile_size, east_br - east * tile_size)/ rscale)
       tile_east_min = int(max (0 , east_tl -  east * tile_size) /rscale)
#        print(tile, tile_north_min, tile_north_max, tile_east_min, tile_east_max)
       he= h[tile_north_min: tile_north_max,tile_east_min:tile_east_max]
       if (east ==grid_east_tl) :
           strip = he 
       else :
           strip = hstack([strip,he])
   if (north == grid_north_br) :
       elev = strip
   else :
       elev = vstack([strip,elev])

# surface = flipud(surface)
sys.stderr.write("output " + ', '.join(map(str, elev.shape ))+ "\n")

savetxt(sys.stdout,elev,"%1.2f")

