#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from practica1.msg import Mensaje_N4
from practica1.msg import Mensaje_N3
var1 = 0
var2 = 0
def callback(msg):
    msg_n5 = Mensaje_N4()
    var1 = 0
    var2 = 0
    #comprueba casillas colindantes en filas
    vec = msg.matrix
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
    #comprueba casillas colindantes en columna
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
    
    #comprueba entre dos casillas y dos huecos con 0, filas
    vec2 = [0,4,8,12]
    for i in vec2:
        if(vec[i] == vec[i+3] and (vec[i] != 0 and vec[i+1] == 0 and vec[i+2] == 0 and vec[i+3] != 0)):
            var1 = var1 + 1

    #comprueba entre dos casillas y un hueco con 0, filas
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

    #comprueba entre dos casillas y un hueco con 0, columnas
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


    #comprubea entre dos casillas y dos huecos con 0, columnas
    vec2 = [0,1,2,3]
    for i in vec2:
        if(vec[i] == vec[i+12] and (vec[i] != 0 and vec[i+12] != 0 and vec[i+4] == 0 and vec[i+8] == 0)):
            var2 = var2 + 1


    #comprobamos cuantas condiciones positivas hay mas, si en fila o en columna
    msgn5 = ""
    if var2 > var1:
        #si hay mas en columnas
        ceros_arriba = 0
        ceros_abajo = 0
        
        #contamos ceros arriba
        for i in range(0, 8, 1):
            if vec[i] == 0:
                ceros_arriba +=1
            
        #contamos ceros abajo
        for i in range(8, 15, 1):
            if vec[i] == 0:
                ceros_abajo +=1
    
        if ceros_arriba > ceros_abajo:
            msgn5 = "arriba"
        else:
            msgn5 = "abajo"

    elif var1 > var2:
        #hay mas en filas
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
            msgn5 = "derecha"
        else:
            msgn5 = "izquierda"
    else:

        ceros_q1 = 0
        ceros_q2 = 0
        igual = [0,0,0,0]
        #contamos ceros arriba
        ind = [0,1,4,5]
        for i in ind:
            if vec[i] == 0:
                ceros_q1 +=1
        
        ind = [2,3,6,7]
        #contamos ceros abajo
        for i in ind:
            if vec[i] == 0:
                ceros_q2 +=1
        
        ceros_q3 = 0
        ceros_q4 = 0
        ind = [8,9,12,13]
        #contamos ceros a la izquierda
        for i in ind:
            if vec[i] == 0:
                ceros_q3 +=1
        
        ind = [10,11,14,15]
        for i in ind:
            if vec[i] == 0:
                ceros_q4 +=1 
        igual[0] = ceros_q1 + ceros_q3
        igual[1] = ceros_q2 + ceros_q1
        igual[2] = ceros_q4 + ceros_q2
        igual[3] = ceros_q4 + ceros_q3
        max_value = max(igual)
        indice = igual.index(max_value)
        if indice == 0:
            if ceros_q1 > ceros_q3:
                msgn5 = "arriba"
            elif ceros_q1 < ceros_q3:
                msgn5 = "abajo"
            else:
                msgn5 = "izquierda"
        elif indice == 1:
            if ceros_q2 > ceros_q1:
                msgn5 = "derecha"
            elif ceros_q2 < ceros_q1:
                msgn5 = "izquierda"
            else:
                msgn5 = "arriba"
        elif indice == 2:
            if ceros_q4 > ceros_q3:
                msgn5 = "derecha"
            elif ceros_q4 < ceros_q3:
                msgn5 = "izquierda"
            else:
                msgn5 = "abajo"
        elif indice == 3:
            if ceros_q2 > ceros_q4:
                msgn5 = "arriba"
            elif ceros_q2 < ceros_q4:
                msgn5 = "abajo"
            else:
                msgn5 = "derecha"


    #preparacion del mensaje custom
    msg_n5.action = msgn5
    msg_n5.img = msg.img
    msg_n5.matrix = vec
    pub = rospy.Publisher('/img_5', Mensaje_N4, queue_size=1)
    pub.publish(msg_n5)

def listener():

    rospy.init_node('listener3', anonymous=True)

    rospy.Subscriber('/img_3', Mensaje_N3, callback, queue_size=1)

 
    rospy.spin()

if __name__ == '__main__':
    listener()
