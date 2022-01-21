import cv2
import numpy as np
img = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/juego_10.jpg')
#img=img[0:110,0:110]
img = cv2.resize(img, (480,480), fx=0, fy=0)
cv2.imwrite('/home/ros/catkin_ws/src/practica1/src/caracteristicas/juego_10.jpg', img)