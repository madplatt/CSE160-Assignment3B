from PIL import Image
import numpy
 
 
img= Image.open("maze.png")
np_img = numpy.array(img)
numpy.set_printoptions(threshold=numpy.inf)

print(np_img)