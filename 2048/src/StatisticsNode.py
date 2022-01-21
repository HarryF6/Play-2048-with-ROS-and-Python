
import rospy
import numpy as np
import cv2
import subprocess
import autopy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from practica1.msg import Mensaje_N4
import time
matriz_ant = []

def callback(msg):
    global matriz_ant
    cv_b = CvBridge()
    if(matriz_ant != msg.matrix):
        print("-------------------------------------------")
        print("--------------Numeros detectados:----------")
        print(msg.matrix)
        print("-----El bot ha realizado el movimiento:----")
        print(msg.action)
        print("-------------------------------------------")
        pub = rospy.Publisher('/img_tratada', Image, queue_size=1)
        pub.publish(msg.img)
        #cv2.imshow("img_detectada", cv_b.imgmsg_to_cv2(msg.img))
        #cv2.waitKey(0)
        
    matriz_ant = msg.matrix




def listener():

    rospy.init_node('listener6', anonymous=True)

    rospy.Subscriber("/img_5", Mensaje_N4, callback)

 
    rospy.spin()

if __name__ == '__main__':
    listener()
