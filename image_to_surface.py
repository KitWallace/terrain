""" convert from a JPEG image to an array file of elevations 
  parameters
    1 image file name
    2 width in units of the scaled image
    3  0 = normal, 1 = invented
    output array of values [0.. 1) on stdout
  
   uses  PIL, numpy
   Chris Wallace  April 2014
  
"""
from PIL import Image
import numpy,sys

file = sys.argv[1]
width = float(sys.argv[2])
invert = int(sys.argv[3])

pic = Image.open(file)
dim = pic.size
ratio =  width /dim[0]
dim_resize = (int(dim[0]*ratio),int(dim[1]*ratio)) 
pic_resize = pic.resize(dim_resize,Image.ANTIALIAS)
pic_greyscale = pic_resize.convert("L")
pic_array = numpy.array(pic_greyscale).reshape((dim_resize[1],dim_resize[0]))
pic_array2 = pic_array / 256.0
if invert == 1 :
   pic_array2 = 1 - pic_array2
numpy.savetxt(sys.stdout,pic_array2,"%f")
