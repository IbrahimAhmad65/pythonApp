#/bin/python3
import numpy as np
from PIL import Image

def processbad(array):
    #arr = np.zeros([array.size(),array[0].size(),array[0][0].size])
    arr = np.zeros([int(np.size(array)/8),
        int(np.size(array[0])/8),3],
        dtype=np.byte)
#    print (arr)
    counter = 0
    count = 0
    for i in array:
        for b in i:
            array[counter][count][0] = b[0]
            array[counter][count][1] = b[1]
            array[counter][count][2] = b[2]
            count +=1
        counter +=1
    image = Image.fromarray(arr)
    return image


def process(img, red, green, blue):
    array = np.array(img)# [widthxheightxpixels] 
    
    r = array[:,:,0]
    g = array[:,:,1]
    b = array[:,:,2]

    return np.logical_and(np.logical_not(np.ma.masked_equal(r, red).mask), np.logical_and(np.logical_not(np.ma.masked_equal(b, blue).mask), (np.logical_not(np.ma.masked_equal(g, green).mask))))
    
    #return np.ma.masked_equal(r,0)

    counter = 0
    count = 0
    for i in array:
        for b in i:
            if(b[0] < 1 and b[1] < 1 and b[2] < 1):
                array[counter][count] = [255,255,255,255]
                #print(b)
            else:
                array[counter][count] = [0,0,0,255]
            count +=1
        counter +=1
        count = 0
    image = Image.fromarray(array)
    return image


img = Image.open('checker.png')

#array = 255 - array
#invimg = Image.fromarray(array)
#invimg.save('testgrey-inverted.png')

img = Image.fromarray(process(img,0,0,0))
img.save("newchecker.png")
