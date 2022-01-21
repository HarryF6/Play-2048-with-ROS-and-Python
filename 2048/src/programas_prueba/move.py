
import cv2
import numpy as np
import autopy
import ctypes
import time
from subprocess import Popen, PIPE
var1 = 0
#vec = [0,0,2,4,0,0,4,8,0,2,16,32,0,2,2,16]
#vec = [0,2,0,0,0,0,0,4,0,8,4,2,4,16,8,2]
vec = [0,16,2,2,
        0,0,2,8,
        0,4,4,16,
        0,4,16,16]

for i in range(0,3):
    if(vec[i] == vec[i+1] and (vec[i] != 0 and vec[i+1] != 0)):
        var1 = var1 + 1

for i in range(4,7):
    if(vec[i] == vec[i+1] and (vec[i] != 0 and vec[i+1] != 0)):
        var1 = var1 + 1

for i in range(8,11):
    if(vec[i] == vec[i+1] and (vec[i] != 0 and vec[i+1] != 0)):
        var1 = var1 + 1

for i in range(12,15):
    if(vec[i] == vec[i+1] and (vec[i] != 0 and vec[i+1] != 0)):
        var1 = var1 + 1

col1 = [0,4,8]
col2 = [1,5,9]
col3 = [2,6,10]
col4 = [3,7,11]
var2 = 0
for i in col1:
    if(vec[i] == vec[i+4] and (vec[i] != 0 and vec[i+4] != 0)):
        var2 = var2 + 1

for i in col2:
    if(vec[i] == vec[i+4] and (vec[i] != 0 and vec[i+4] != 0)):
        var2 = var2 + 1

for i in col3:
    if(vec[i] == vec[i+4] and (vec[i] != 0 and vec[i+4] != 0)):
        var2 = var2 + 1
        
for i in col4:
    if(vec[i] == vec[i+4] and (vec[i] != 0 and vec[i+4] != 0)):
        var2 = var2 + 1




vec2 = [0,4,8,12]
for i in vec2:
    if(vec[i] == vec[i+3] and (vec[i] != 0 and vec[i+1] == 0 and vec[i+2] == 0 and vec[i+3] != 0)):
        var1 = var1 + 1


for i in range(0,2):
    if(vec[i] == vec[i+2] and (vec[i] != 0 and vec[i+2] != 0 and vec[i+1] == 0)):
        var1 = var1 + 1
for i in range(4,6):
    if(vec[i] == vec[i+2] and (vec[i] != 0 and vec[i+2] != 0 and vec[i+1] == 0)):
        var1 = var1 + 1
for i in range(8,10):
    if(vec[i] == vec[i+2] and (vec[i] != 0 and vec[i+2] != 0 and vec[i+1] == 0)):
        var1 = var1 + 1
for i in range(12,14):
    if(vec[i] == vec[i+2] and (vec[i] != 0 and vec[i+2] != 0 and vec[i+1] == 0)):
        var1 = var1 + 1

col1 = [0,4]
col2 = [1,5]
col3 = [2,6]
col4 = [3,7]
for i in col1:
    if(vec[i] == vec[i+8] and (vec[i] != 0 and vec[i+4] == 0 and vec[i+8] != 0)):
        var2 = var2 + 1
for i in col2:
    if(vec[i] == vec[i+8] and (vec[i] != 0 and vec[i+4] == 0 and vec[i+8] != 0)):
        var2 = var2 + 1
for i in col3:
    if(vec[i] == vec[i+8] and (vec[i] != 0 and vec[i+4] == 0 and vec[i+8] != 0)):
        var2 = var2 + 1
for i in col4:
    if(vec[i] == vec[i+8] and (vec[i] != 0 and vec[i+4] == 0 and vec[i+8] != 0)):
        var2 = var2 + 1



vec2 = [0,1,2,3]
for i in vec2:
    if(vec[i] == vec[i+12] and (vec[i] != 0 and vec[i+12] != 0 and vec[i+4] == 0 and vec[i+8] == 0)):
        var2 = var2 + 1



if var2 > var1:
    ceros_arriba = 0
    ceros_abajo = 0
    
    #contamos ceros arriba
    for i in range(0, 8, 1):
        if vec[i] == 0:
            ceros_arriba +=1
        #print("valor:" + str(v[i]))
        #print(i)
    #contamos ceros abajo
    for i in range(8, 15, 1):
        if vec[i] == 0:
            ceros_abajo +=1
   
    if ceros_arriba > ceros_abajo:
        print("mover arriba")
    else:
        print("mover abajo")

else:
    ceros_izquierda = 0
    ceros_derecha = 0

#contamos ceros a la izquierda
    for i in range(0, 16, 4):
        if vec[i] == 0:
            ceros_izquierda +=1
    for i in range(1, 17, 4):
        if vec[i] == 0:
            ceros_izquierda +=1  

#contamos ceros a la derecha
    for i in range(2, 18, 4):
        if vec[i] == 0:
            ceros_derecha +=1
    for i in range(3, 19, 4):
        if vec[i] == 0:
            ceros_derecha +=1  

    if ceros_derecha > ceros_izquierda:
        print("mover derecha")
    else:
        print("mover izquierda") 



