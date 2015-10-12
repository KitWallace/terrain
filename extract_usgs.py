""""
  Read single tiles from USGS each tile covers a degree of lat and long
  parameters
     1  tile id   eg  w005n54e

""""
import sys
import zipfile
import numpy as np
import shapefile

def load_tile(tile) :  #return the elevation array for this tile 
      an= "usgs/"+tile+"/"+tile+".shp"
      print(an)
      
      sf = shapefile.Reader(an)
      return sf

tile= argv[1]
a = load_tile(tile)

print(a.fields)
print(len(a.shapes()))

for i in range(len(a.shapes())) :
   print(a.shapes()[i].z[0], len(a.shapes()[i].points) )
