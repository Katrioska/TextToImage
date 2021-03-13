from PIL import Image
import numpy as np
from math import sqrt, ceil

string = "Hello World!"
ascii_list = []

### STRING TO ASCII LIST ###
for i in string:
    pixel = ord(i)
    ascii_list.append(pixel)

### SIZE (X,Y) OF IMAGE DEFINED, IMAGE LIST VAR DEFINED (var that be used to create np array)
size = ceil(sqrt(len(ascii_list)))
pixels = []
for sizey in range(size):
    pixels.append([])

### ASCII_LIST SEPARATION BY SIZE VAR,
dict_axisY = {}
tempList = []

cont_axis_Y = 0
cont = 0
for num in ascii_list:
    tempList.append(num)
    cont += 1
    if cont >= size:
        dict_axisY[cont_axis_Y] = tempList.copy()
        tempList = []
        cont_axis_Y += 1
        cont = 0
if tempList != []:
    dict_axisY[cont_axis_Y] = tempList.copy()

### CHECK IF FINAL LINE HAS LOWER LEN THAN DEFINED SIZE ###
diference = size - len(dict_axisY[len(dict_axisY)-1])
if diference != 0 and diference < size:
    for i in range(diference):
        dict_axisY[len(dict_axisY)-1].append(0)

### CONVERT dict_AxisY TO pixels ###
cont = 0
for x in pixels:
    if cont == len(dict_axisY):
        for i in range(size):
            x.append((0, 0, 0))
    else:
        for i in dict_axisY[cont]:
            x.append((i, i, i))
    cont += 1

print(pixels)

### pixels TO NP array ###

array = np.array(pixels, dtype=np.uint8)

### CREATION OF IMAGE ###
image = Image.fromarray(array)
image.save("encTest.png")
