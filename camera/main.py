import numpy as np
from PIL import Image

def process(array, red, green, blue,error):
    r = array[:,:,0]
    g = array[:,:,1]
    b = array[:,:,2]
    rmin = red - error
    rmax = red + error
    gmax = green + error
    gmin = green - error
    bmin = green - error
    bmax = green + error
    return (r < rmax) & (r > rmin) & (b > bmin) & (b < bmax) & (g < gmax) & (g > gmin)
img = Image.open('cow.png')
arr = process(np.array(img),0,0,0,20)
print(arr)
img = Image.fromarray(arr)
img.save("newchecker.png")
