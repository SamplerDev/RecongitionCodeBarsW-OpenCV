import cv2

import numpy as np

from pyzbar.pyzbar import decode #biblioteca para deteccion de codigo de barras y qr

#detectar camara
cap = cv2.VideoCapture(0)
#ancho camara

cap.set(3,640)

#alto de la camara

cap.set(4,480)

#leer archivo credenciales

with open('Data/credenciales.txt') as f:

    #las lineas de codigo se guardan en un arreglo

    mydatalist=f.read().splitlines()

#imprimir los codigos de access

print(mydatalist)

#mientras el bucle funcione

while True:

    #se guarda la imagen de la camara

        success, img= cap.read()

#detectar los codigos de barra en la imagen,corre en fps x seg, por eso tira tantas confirmaciones

        for barcode in decode(img):

            mydata= barcode.data.decode('utf-8','ean-8')

            print(mydata)

            if mydata in mydatalist:
                myOutput = 'existe'
                color=(0,255,0)
            else:
                myOutput= 'no existe'
                color = (0,0,250)

            print(myOutput)

#marca las cordenadas del codigo de barras
            pts= np.array([barcode.polygon],np.int32)
        #modifica el array pts    
            pts = pts.reshape((-1,1,2))
        #crea el cuadro de color segun el estado
            cv2.polylines(img,[pts],True,color,5)  #imagen, coordenadas, el poligono es cerrado, el espesor del poligono

#muestra la img

        cv2.imshow('Result',img)

#espera 1ms para detener la camara

#        
        cv2.waitKey(1)