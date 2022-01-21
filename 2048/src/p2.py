#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def callback(msg):
    cv_b = CvBridge()

    try:
      cv_image = cv_b.imgmsg_to_cv2(msg)
    except CvBridgeError as e:
      print(e)
    #recortar imagen
    croppedImage = cv_image[120:640, 50:570] 
    #mejorar
      
    #print('p2')
    pub = rospy.Publisher('/img_2', Image, queue_size=1)
    pub.publish(cv_b.cv2_to_imgmsg(croppedImage))

#recorte de pantalla    
"""
mensaje a recibir:
imagen_pantalla


Recortar
1- dependiendo de donde este
2- detectar algun numero o algo y recortar

capturar pantalla

mensaje a enviar:
imagen_pantalla_recortada
"""  
def listener():

    rospy.init_node('listener2', anonymous=True)

    rospy.Subscriber("/img", Image, callback)

 
    rospy.spin()

if __name__ == '__main__':
    listener()
