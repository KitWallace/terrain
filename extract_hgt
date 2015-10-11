"""
  parameters  
       lat/long bounding box (top/left bottom/right) and base
       source   strm_3sec  or  strm_1sec
              
   
  use numpy to read in the hgt files
  extract the subarrays required, merge into a single array, flip and output to stdout
  

"""

import sys, math, os
from numpy import *

def load_hgt (path) :

  siz = os.path.getsize(path)
  dim = int(math.sqrt(siz/2))
#   assert dim*dim*2 == siz, 'Invalid file size'
  return fromfile(path, dtype('>i2'), dim*dim).reshape((dim, dim))
   
lat_tl = float(sys.argv[1])
long_tl = float(sys.argv[2])
lat_br = float(sys.argv[3])
long_br= float(sys.argv[4])
source = sys.argv[5]

lat_min = min(lat_tl,lat_br)
lat_max = max(lat_tl,lat_br)
long_min = min(long_tl,long_br)
long_max = max(long_tl,long_br)


lat_min_d = int(math.floor(lat_min))
lat_max_d = int(math.ceil(lat_max))-1
long_min_d = int(math.floor(long_min))
long_max_d = int(math.ceil(long_max))-1

# print (lat_min_d,  long_min_d, lat_max_d, long_max_d)
for latd in range(lat_min_d,lat_max_d + 1)  :
   if latd > 0 :
       latDir = "N"
   else : 
       latDir = "S"
   for longd in range(long_min_d,long_max_d + 1)  :
       if longd > 0 :
          longDir = "E"
       else : 
          longDir = "W"

       tile = (latDir +"%02u" + longDir + "%03u") % (abs(latd),abs(longd))
#       print ("// " + tile)
       h=load_hgt(source + "/"+ tile+".hgt")
       samples= h.shape[0]   #  its square 
       tile_lat_min = samples - int(min (1.0, lat_tl - latd) * samples)
       tile_lat_max=  samples - int(max (0.0 , lat_br - latd) * samples)
       tile_long_max = int(min (1.0, long_br - longd) * samples)
       tile_long_min = int(max (0.0 , long_tl - longd) * samples)
#       print(tile_lat_min, tile_lat_max, tile_long_min, tile_long_max)
       he= h[tile_lat_min: tile_lat_max,tile_long_min:tile_long_max]
       if (longd ==long_min_d) :
           strip = he 
       else :
           strip = hstack([strip,he])
   if (latd == lat_min_d) :
       surface = strip
   else :
       surface = vstack([strip,surface])
surface = flipud(surface)
# print surface.shape
savetxt(sys.stdout,surface,"%d")
       
