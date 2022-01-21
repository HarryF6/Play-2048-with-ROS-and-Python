#!/usr/bin/env python
from numpy.core.numeric import False_
import rospy
import numpy as np
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from practica1.msg import Mensaje_N3

num2048 = False
img_anterior = cv2.imread('/home/ros/catkin_ws/src/practica1/src/prueba.jpg')
def callback(msg):
    global num2048
    global img_anterior
    msg_n4 = Mensaje_N3()
    #convertimos la imagen de sensor Image a Opencv Mat
    cv_b = CvBridge()
    try:
      cv_image = cv_b.imgmsg_to_cv2(msg)
    except CvBridgeError as e:
      print(e)
    if num2048 == False:
        #print('p3')
        #se quita ruido
        img_no_ruido = cv2.fastNlMeansDenoisingColored(cv_image,None,5,5,7,21)
        #escalamos la imagen
        img_r = cv2.resize(img_no_ruido, (480,480), fx=0, fy=0)
        #convertimos a escala de grises
        img_gray = cv2.cvtColor(img_r, cv2.COLOR_BGR2GRAY)
        #doble tratamiento de reduccion de ruido
        img_Blur = cv2.medianBlur(img_gray, 3)
        img_Blur = cv2.GaussianBlur(img_Blur, (3, 3), 0)
        #creamos un elemento estructurante de forma elipsoidal y tamano 350/350
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (450,450))
        #hacemos un cierre
        close = cv2.morphologyEx(img_Blur, cv2.MORPH_CLOSE, kernel)
        div = np.float32(img_Blur) / close
        #ajustamos el brillo
        img_brightness_adjust = np.uint8(cv2.normalize(div, div, 0, 255, cv2.NORM_MINMAX))
        #aplicamos threshold
        img_thresh = cv2.adaptiveThreshold(img_brightness_adjust, 255,
                                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY_INV, 11, 7)
        #cv2.imwrite('/home/ros/catkin_ws/src/practica1/src/prueba.jpg', img_thresh)
        #cogemos el tamano de la imagen entre 4, para poder obtener subimagenes donde se encuentren los numeros
        w=img_r.shape[0]/4
        h=img_r.shape[1]/4
        cont = 0
        vec_numeros=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        vec_img=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #doble for y aplicacion del algoritmo para obtener las subimagenes recortadas y almacenadas en un vector
        for i in range(4):
            for j in range(4):
                """print('imagen')
                print(cont)
                print(i*w,j*h)
                print(i*w + w,j*h+h)"""
                #recorte = img_thresh([i*w, i*w+w],[j*h,j*h+h])
                vec_img[cont] = img_thresh[i*w:i*w+w, j*h:j*h+h]
                cont = cont + 1
                #cv2.imwrite('/home/ros/catkin_ws/src/practica1/src/recortes/'+str(cont)+'.jpg', vec_img[cont])
        #imagenes recortadas
        #carga de las imagenes de prueba para el detector de caracteristicas
        vec_prueb=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        vec_prueb[0] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_2.png')
        vec_prueb[1] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_4.png')
        vec_prueb[2] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_8.png')
        vec_prueb[3] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_16.png')
        vec_prueb[4] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_32.png')
        vec_prueb[5] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_64.png')
        vec_prueb[6] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_128.png')
        vec_prueb[7] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_256.png')
        vec_prueb[8]  = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_512.png')
        vec_prueb[9]  = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_1024.png')
        vec_prueb[10]  = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_2048.png')
        matrix = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        vec_num = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        n_pruebas = 0
        #for para recorrer el vector de las subimagenes
        for i in range(0,16):
            #print("----------")
            for j in range(0,11): # si se amplia hasta 2048 el range es de 0 a 11
                #aplicacion del detector sift
                sift = cv2.xfeatures2d.SIFT_create()
                keypoints1, descriptors1 = sift.detectAndCompute(vec_img[i], None)
                keypoints2, descriptors2 = sift.detectAndCompute(vec_prueb[j], None)
                FLAN_INDEX_KDTREE = 0
                index_params = dict (algorithm = FLAN_INDEX_KDTREE, trees=5)
                search_params = dict (checks=50)
                flann = cv2.FlannBasedMatcher(index_params, search_params)
                matches = flann.knnMatch (descriptors1, descriptors2,k=2)
                good_matches = []
                for m1, m2 in matches:
                    if m1.distance < 0.5 * m2.distance:
                        good_matches.append([m1])
                vec_num[j] = len(good_matches)

            #eleccion del numero que hay en la subimagen
            max_value = max(vec_num)
            ind = vec_num.index(max_value)
            if(max_value > 1 ):
                if(ind == 0):
                    matrix[i] = 2
                elif(ind == 1):
                    matrix[i] = 4
                elif(ind == 2):
                    matrix[i] = 8
                elif(ind == 3):
                    matrix[i] = 16
                elif(ind == 4):
                    matrix[i] = 32
                elif(ind == 5):
                    matrix[i] = 64
                elif(ind == 6):
                    matrix[i] = 128
                elif(ind == 7):
                    matrix[i] = 256
                elif(ind == 8):
                    matrix[i] = 512
                elif(ind == 9):
                    matrix[i] = 1024
                elif(ind == 10):
                    matrix[i] = 2048
                    num2048 = True
            else:
                matrix[i] = 0
            vec_num = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        # enviar mensaje mediante topic
        img_anterior = cv_image
        msg_n4.img = cv_b.cv2_to_imgmsg(img_thresh)
        msg_n4.matrix = matrix
        
       
        pub = rospy.Publisher('/img_3', Mensaje_N3, queue_size=1)
        pub.publish(msg_n4)
    else:
        print("Juego terminado")


#tratamiento de imagen
"""
mensaje a recibir:
imagen_pantalla_recortada

Pasos:
1- detectar bordes
2- recortar la imagen como una matriz 4x4(16subimagenes) cada subimagen equivale
a una casilla
3- detectar numeros, comparando con una carpeta o un detector
4- crear una matriz 4x4, que contenga en cada casilla el numero detectado y
0 si no hay nada

NECESARIO: mensaje custom, Image y Int[][]


mensaje a enviar:
imagen_recortada
vector de numeros
"""	    
    
def listener():

    rospy.init_node('listener2', anonymous=True)

    rospy.Subscriber("/img_2", Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
