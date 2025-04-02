import cv2
import numpy as np

#carga de la imagen
imagen=cv2.imread('monedas.jpg')

#convertir a grises
grises= cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

#desenfoque gaussiano - suaviza las imagenes
desen=cv2.GaussianBlur(grises,(3,3),0)

#saca los bordes internos 
canny= cv2.Canny(desen,60,100)

#modelado de kernel - 
kernel = np.ones((3,3),np.uint8)


#mostar imagen
cv2.imshow('imagen',imagen)
cv2.imshow('imagen grises',grises) 
cv2.imshow('imagen desenfocada',desen) 
cv2.imshow('canny',canny) 
#cv2.imshow('umbral',umbral[1]) 
cv2.waitKey(0)
cv2.destroyAllWindows()