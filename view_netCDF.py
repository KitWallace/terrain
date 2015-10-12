import netCDF4
import sys

name= sys.argv[1]
d= netCDF4.Dataset(name+'.nc', 'r')

print d.data_model
print "groups ",len(d.groups.keys())
for k in d.groups.keys() :
  v = d.groups[k]
  print k, v

print "dimensions ",len(d.dimensions.keys())
for k in d.dimensions.keys() :
  v = d.dimensions[k]
  print k, v
  
print "variables ",len(d.variables.keys())
for k in d.variables.keys() :
  v = d.variables[k]
  print k, v
  print v[:]

d.close()    
    
