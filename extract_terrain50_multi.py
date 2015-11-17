"""
  parameters 
      system LL (WSG84 lat//long ) or OS (ordinance Survey easting northing)
      top left lat long
      bottom right lat long
  
  extracts heights from  Terrain 50 data
  
  assumes data is in directory terrain-50

  output to stdout
  
  Chris Wallace April 2014
  kitwallace.co.uk
  
"""
import sys
import zipfile
from WGS84_to_UKGrid import *
from scipy import *

def load_tile(tile) :  #return the elevation array for this tile 
   prefix = tile[:2] 
   a = zeros([200,200])
   fn="terrain-50/"+prefix+"/"+tile+"_OST50GRID_20130611.zip"
   try :
      zip = zipfile.ZipFile(fn,"r")
      an= tile.upper()+".asc"
      ascii = zip.read(an)
      lines = ascii.split("\n")
      for i in range(0,200) : 
         a[i] = array(lines[i+5].split(" "))  
      sys.stderr.write(fn+"\n")
   except :
      pass
   return a  

sys.stderr.write(sys.argv[0]+'\n')

system = sys.argv[1]

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
   sys.stderr.write("System " + system + " not known")
   
   
samples_per_tile = 200
rscale = 50
tile_size = samples_per_tile * rscale

(east_tl,north_tl) = (int(east_tl),int(north_tl))
(east_br,north_br) = (int(east_br),int(north_br))

sys.stderr.write("Grid TL "+str(east_tl)+","+str(north_tl)+ " BR "+str(east_br)+","+str(north_br)+ "\n")

(grid_north_tl, grid_east_tl) = (int(north_tl/tile_size), int(east_tl/tile_size))
(grid_north_br, grid_east_br) = (int(north_br/tile_size), int(east_br/tile_size))

sys.stderr.write("Rounded TL "+str(grid_east_tl)+","+str(grid_north_tl)+ " BR "+str(grid_east_br)+","+str(grid_north_br)+ "\n")


for north in range(grid_north_br,grid_north_tl+ 1)  :
   for east in range(grid_east_tl,grid_east_br + 1)  :
       tile = OS_to_Grid(east,north)
       h=load_tile(tile)
       tile_north_min = samples_per_tile - int(min (tile_size, north_tl - north * tile_size) / rscale)
       tile_north_max=  samples_per_tile - int(max (0 , north_br -  north * tile_size) / rscale )
       tile_east_max = int(min (tile_size, east_br - east * tile_size)/ rscale)
       tile_east_min = int(max (0 , east_tl -  east * tile_size) /rscale)
#       print(tile, tile_north_min, tile_north_max, tile_east_min, tile_east_max)
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
savetxt(sys.stdout,elev,"%d")

