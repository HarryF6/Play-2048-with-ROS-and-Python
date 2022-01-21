import cv2
import numpy as np
import autopy
"""
captura = autopy.bitmap.capture_screen()
captura.save('captura.png')
"""

img_original = cv2.imread('/home/ros/catkin_ws/src/practica1/src/juego_1.jpg')

img_no_ruido = cv2.fastNlMeansDenoisingColored(img_original,None,5,5,7,21)
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

#detector de numeros
#   
#histogramas
cv2.imwrite('/home/ros/catkin_ws/src/practica1/src/caracteristicas/16.png', vec_img[15])

hist_v = cv2.calcHist(vec_img[15],[0],None,[256],[0,256])
hist_4 = cv2.calcHist(img_4,[0],None,[256],[0,256])

OPENCV_METHODS = (
	("Correlation", cv2.HISTCMP_CORREL),
	("Chi-Squared", cv2.HISTCMP_CHISQR),
	("Intersection", cv2.HISTCMP_INTERSECT),
	("Hellinger", cv2.HISTCMP_BHATTACHARYYA))

d = cv2.compareHist(hist_v,  hist_4, cv2.HISTCMP_CORREL)
print(d)

d = cv2.compareHist(hist_v,  hist_4, cv2.HISTCMP_CHISQR)
print(d)

d = cv2.compareHist(hist_v,  hist_4, cv2.HISTCMP_INTERSECT)
print(d)

d = cv2.compareHist(hist_v,  hist_4, cv2.HISTCMP_BHATTACHARYYA)
print(d)

#hog

#feature matching
"""
img1 = vec_img[15]
img2 = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_16.png', 0)
orb = cv2.ORB_create(nfeatures=500)
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
match_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None)
print(matches.count)
cv2.imshow('original image', img1)
cv2.imshow('test image', img2)
cv2.imshow('Matches', match_img)
cv2.waitKey()
"""
#sift
"""
ori =  vec_img[15] 
img = cv2.imread('/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_16.png', 0)
orb = cv2.ORB_create(nfeatures=200)
kp = orb.detect(img, None)
kp, des = orb.compute(img, kp)
img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
cv2.imshow('Original', ori)
cv2.imshow('ORB', img2)
cv2.waitKey()
"""
#surf
"""
img =vec_img[15]
ori = cv2.imread("/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_16.png")
surf = cv2.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img,None)
img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
cv2.imshow('Original', ori)
cv2.imshow('SURF', img2)
cv2.waitKey()
 """
#orb brute force
"""
img1 = vec_img[15]
img2 = cv2.imread("/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_16.png")

orb = cv2.ORB_create()
keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
keypoints2, descriptors2 = orb.detectAndCompute(img2, None)
bf = cv2.BFMatcher_create(cv2.NORM_HAMMING,crossCheck=True)
matches = bf.match(descriptors1, descriptors2)
single_match = matches[0]
print(len(matches))
matches = sorted(matches,key=lambda x:x.distance)
ORB_matches =cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:30], None, flags=2)
cv2.imshow('ORB+BruteForce',ORB_matches)
cv2.waitKey()
"""

#muyyyyyyyyyyyyyyyyyy okays

"""
#sift  brute force okay, mas problemas para detectar 2s
img1 = vec_img[15]
img2 = cv2.imread("/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_16.png")

sift = cv2.xfeatures2d.SIFT_create()
keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
keypoints2, descriptors2 = sift.detectAndCompute(img2, None)
bf = cv2.BFMatcher()
matches = bf.knnMatch (descriptors1, descriptors2,k=2)
good_matches = []

for m1, m2 in matches:
  if m1.distance < 0.6*m2.distance:
    good_matches.append([m1])
print(len(good_matches))
SIFT_matches =cv2.drawMatchesKnn(img1, keypoints1, img2, keypoints2, good_matches, None, flags=2)
cv2.imshow('SIFT+BruteForce',SIFT_matches)
cv2.waitKey()"""



#sift flann okay, muy okay
"""
img1 = vec_img[15]
img2 = cv2.imread("/home/ros/catkin_ws/src/practica1/src/caracteristicas/img_16.png")
sift = cv2.xfeatures2d.SIFT_create()
keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
keypoints2, descriptors2 = sift.detectAndCompute(img2, None)
FLAN_INDEX_KDTREE = 0
index_params = dict (algorithm = FLAN_INDEX_KDTREE, trees=5)
search_params = dict (checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch (descriptors1, descriptors2,k=2)
good_matches = []

for m1, m2 in matches:
  if m1.distance < 0.5 * m2.distance:
    good_matches.append([m1])
print(len(good_matches))  
flann_matches =cv2.drawMatchesKnn(img1, keypoints1, img2, keypoints2, good_matches, None, flags=2)
cv2.imshow('Sift+Flann',flann_matches)
cv2.waitKey()
"""

