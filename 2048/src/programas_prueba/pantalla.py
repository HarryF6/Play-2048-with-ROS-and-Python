
import numpy as np
import cv2
import autopy

captura = autopy.bitmap.capture_screen()
captura.save('/home/ros/catkin_ws/src/practica1/src/captura_prueba.png')
img = cv2.imread('/home/ros/catkin_ws/src/practica1/src/captura_prueba.png')

croppedImage = img[120:640, 50:570] #cambiar

img_no_ruido = cv2.fastNlMeansDenoisingColored(croppedImage,None,5,5,7,21)
img_gray = cv2.cvtColor(img_no_ruido, cv2.COLOR_BGR2GRAY)
img_Blur = cv2.medianBlur(img_gray, 3)
img_Blur = cv2.GaussianBlur(img_Blur, (3, 3), 0)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (450,450))
close = cv2.morphologyEx(img_Blur, cv2.MORPH_CLOSE, kernel)
div = np.float32(img_Blur) / close
img_brightness_adjust = np.uint8(cv2.normalize(div, div, 0, 255, cv2.NORM_MINMAX))
img_thresh = cv2.adaptiveThreshold(img_brightness_adjust, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 7)


cv2.imwrite('/home/ros/catkin_ws/src/practica1/src/contour_pruebas.jpg', img_thresh)


w=img_thresh.shape[0]/4
h=img_thresh.shape[1]/4
cont = 0
vec_img=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(4):
    for j in range(4):
        """print('imagen')
        print(cont)
        print(i*w,j*h)
        print(i*w + w,j*h+h)"""
        vec_img[cont] = img_thresh[i*w:i*w+w, j*h:j*h+h]
        #recorte = img_thresh([i*w, i*w+w],[j*h,j*h+h])
        cv2.imwrite('/home/ros/catkin_ws/src/practica1/src/recortes2/'+str(cont)+'.jpg', vec_img[cont])
       
        cont = cont + 1
    
vec_prueb=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
vec_prueb[0] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_2.png')
vec_prueb[1] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_4.png')
vec_prueb[2] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_8.png')
vec_prueb[3] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_16.png')
vec_prueb[4] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_32.png')
vec_prueb[5] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_64.png')
vec_prueb[6] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_128.png')
vec_prueb[7] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_256.png')
vec_prueb[8] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_512.png')
vec_prueb[9] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_1024.png')
vec_prueb[10] = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_2048.png')
matrix = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
vec_num = [0,0,0,0,0,0,0,0,0,0,0,0,0]
n_pruebas = 0

for i in range(0,16):
    #print("----------")
    for j in range(0,11):
        
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
        #print(len(good_matches)) 
        #print(j)
        vec_num[j] = len(good_matches)


    max_value = max(vec_num)
    #print(max_value)
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
    else:
        matrix[i] = 0
    vec_num = [0,0,0,0,0,0,0,0,0,0,0,0,0]


vec = matrix
var1 = 0
var2 = 0
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



msgn5 = ""
if var2 > var1:
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
        msgn5 = "derecha"
    else:
        msgn5 = "izquierda"

autopy.mouse.move(500, 200)

#click del raton
autopy.mouse.click()

if msgn5 =="derecha":
    autopy.key.tap(autopy.key.Code.RIGHT_ARROW)
elif msgn5 =="izquierda":
    autopy.key.tap(autopy.key.Code.LEFT_ARROW)
elif msgn5 =="arriba":
    autopy.key.tap(autopy.key.Code.UP_ARROW)
elif msgn5 == "abajo":
    autopy.key.tap(autopy.key.Code.DOWN_ARROW)
print(matrix)

