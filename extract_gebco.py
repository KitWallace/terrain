"""
  extract depths from gebco bathymetric data obtained from
  British Oceanographic Data Centre http://www.bodc.ac.uk
  from where the data from a selected lat/long bounding box can be downloaded with either 1 minute or 30 second 

resolution
  needs netCDF4  http://code.google.com/p/netcdf4-python/
  
  this script extracts a bounding box from a larger downloaded source file.  For example the file may contain the   

whole of the Mediterranean 
  and the script extracts smaller areas from the whole
  .nc files in gebco  subdirectory
  parameters
     top left lat, long
     bottom right lat,long
          
  Chris Wallace
  kitwallace.co.uk
"""

def latlong_to_array(lat,long) :
   return [ int((long - xrangemin  ) /scale) , int((yrangemax - lat) / scale)]
   
import netCDF4
from numpy import * 
from generate_STL import *
import sys

lat_max = float(sys.argv[1])
long_min = float(sys.argv[2])
lat_min = float(sys.argv[3])
long_max = float(sys.argv[4])
 

d= netCDF4.Dataset(sys.stdin, 'r')

scale = d.variables['spacing'][0]
xrangemin = d.variables['x_range'][0]
yrangemax = d.variables['y_range'][1]

tl = latlong_to_array(lat_max,long_min)
br = latlong_to_array(lat_min,long_max)

depths = d.variables['z'][:]
depths = depths.reshape(d.variables['dimension'][1], d.variables['dimension'][0])
d.close()
depths = depths[ tl[1]: br[1],tl[0]: br[0]]


//print depths in row matrix format
savetxt(sys.stdout,depths,"%d")
