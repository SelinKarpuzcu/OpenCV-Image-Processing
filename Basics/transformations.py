import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Boston Park', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation 
def rotate(img, angle, rotPoint=None): # rotPoint: Dönmenin gerçekleşeceği eksen noktası  angle: Döndürme açısı (derece cinsinden)
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # 1.0: Görselin ölçek faktörüdür. 
    # Burada 1.0 verilmesi, görselin döndürülürken boyutunun küçülmemesi veya büyümemesi anlamına gelir.
    dimensions = (width,height) # Yeni döndürülmüş görselin çıktı boyutları ayarlanır. 

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45) # Pozitif bir açı saat yönünün tersine, negatif bir açı ise saat yönünde döndürür.
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated_Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping (Çevirmek)
flip_0 = cv.flip(img, 0) # 0: Yatay (x) eksende ters çevirir
cv.imshow('Flip 0', flip_0)

flip_1 = cv.flip(img, 1) # 1: Dikey (y) eksende ters çevirir
cv.imshow('Flip 1', flip_1)

flip_neg_1 = cv.flip(img, -1) # -1: Hem yatay (x) hem de dikey (y) eksende ters çevirir
cv.imshow('Flip -1', flip_neg_1)

# Cropping 
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
    