#!/usr/bin/env python
import rospy
import numpy as np
import cv2
import autopy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import time
hay_imagen_en_juego = False
def callback(msg):
    global hay_imagen_en_juego    
    hay_imagen_en_juego = False

    # hay que recortar la pantalla
    print('llegue')    
    #pub = rospy.Publisher('/img_2', Image, queue_size=10)
    #pub.publish(cv_b.cv2_to_imgmsg(img_thresh))

#captura de pantalla
"""
mensaje a recibir:
siempre que no haya una imagen en juego
  1-imagen_original_modificada

capturar pantalla

mensaje a enviar:
imagen_pantalla
""" 

def callback(msg):
    global hay_imagen_en_juego
    cv_b = CvBridge()
    pub = rospy.Publisher('/img', Image, queue_size=1)
    pub.publish(msg)

   
def talker():
    global hay_imagen_en_juego
    pub = rospy.Publisher('/img', Image, queue_size=1)
   
    cv_b = CvBridge()
    
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        #captura de pantalla
        captura = autopy.bitmap.capture_screen()
        captura.save('/home/ros/catkin_ws/src/practica1/src/captura.png')
        img = cv2.imread('/home/ros/catkin_ws/src/practica1/src/captura.png')
        #rospy.Subscriber("/img_5", Image, callback)
        #if hay_imagen_en_juego == False:
        pub.publish(cv_b.cv2_to_imgmsg(img, 'bgr8'))
        time.sleep(5)
        hay_imagen_en_juego = True
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

