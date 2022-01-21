#!/usr/bin/env python
import rospy
import numpy as np
import cv2
import subprocess
import time
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from practica1.msg import Mensaje_N4
import autopy
import sys
matriz_ant = []
def callback(msg):
    #mover el raton a x e y
    autopy.mouse.move(500, 200)
    global matriz_ant
    #click del raton
    autopy.mouse.click()
    #se comprueba que las matrices sean diferentes
    if matriz_ant != msg.matrix:
      if(msg.action == "abajo"):
        #clica flecha abajo
        print("abajo")
        autopy.key.tap(autopy.key.Code.DOWN_ARROW)
      elif(msg.action == "arriba"):
        #clica flecha arriba
        print("arriba")
        autopy.key.tap(autopy.key.Code.UP_ARROW)
      elif(msg.action == "derecha"):
        #clica flecha derecha
        print("derecha")
        autopy.key.tap(autopy.key.Code.RIGHT_ARROW)
      elif(msg.action == "izquierda"):
        #clica flecha izquierda
        print("izquierda")
        autopy.key.tap(autopy.key.Code.LEFT_ARROW)
      pub = rospy.Publisher('/img_6', String, queue_size=1)
      pub.publish(msg.action)
    matriz_ant = msg.matrix
    #time.sleep(5)
    



    
def listener():

    rospy.init_node('listener4', anonymous=True)

    rospy.Subscriber("/img_5", Mensaje_N4, callback, queue_size=1)

 
    rospy.spin()

if __name__ == '__main__':
    listener()
