import cv2
import numpy as np

original = cv2.imread('/home/ros/catkin_ws/src/practica1/src/recortes/14.jpg')
image_to_compare = cv2.imread('/home/ros/catkin_ws/src/practica1/src/recortes/comp_2.jpg')

cv2.imshow("bN", image_to_compare)
#img_new = cv2.resize(image_to_compare, (120,120), fx=0.75, fy=0.75)
#cv2.imwrite('/home/ros/catkin_ws/src/practica1/src/recortes/comp_2.jpg', img_new)
# 1) Check if 2 images are equals
if original.shape == image_to_compare.shape:
    print('Las imagenes tiene el mismo tamano y canal')
    difference = cv2.subtract(original, image_to_compare)
    b, g, r = cv2.split(difference)
    print(cv2.countNonZero(b))
    if (cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
        print('Las imagenes son completamente iguales')
    else: 
        print('Las imagenes no son iguales')

# 2) Check la similitud de las dos imagenes
shift = cv2.xfeatures2d.SIFT_create()
kp_1, desc_1 = shift.detectAndCompute(original, None)
kp_2, desc_2 = shift.detectAndCompute(image_to_compare, None)

print("Keypoints 1st image", str(len(kp_1)))
print("Keypoints 2st image", str(len(kp_2)))

index_params = dict(algorithm=0, trees=5)
search_params = dict()

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(desc_1, desc_2, k=2)

good_points = []
for m, n in matches:
    if m.distance < 0.6*n.distance:
        good_points.append(m)

print("GOOD matches",len(good_points))

# Estas nuevas lineas son para crear el archivo y pintar los matches de las imagenes
result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)
cv2.imshow("Result", cv2.resize(result, None, fx = 0.4, fy=0.4))
cv2.imwrite("Feature_matching.jpg", result)

cv2.imshow("Original", original)
cv2.imshow("Duplicate", image_to_compare)
cv2.waitKey(0)
cv2.destroyAllWindows()