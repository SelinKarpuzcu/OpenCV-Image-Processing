import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype = 'uint8') # np.zeros(width, height, renk kanalı sayısı)
cv.imshow('Blank', blank)

# # 1. Paint the image a certain colour
# # blank[:] = 0, 0, 255  # BGR
# # cv.imshow('Green', blank)

# # blank[200:300, 300:400] = 0, 0, 255  # BGR
# # cv.imshow('Green', blank)

# # 2.  Draw a Rectangle
# # cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=2)
# # cv.imshow('Retangle', blank)

# # cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
# # cv.imshow('Retangle', blank)

# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1) # cv.FILLED yerine -1 yazılabilir
# cv.imshow('Retangle', blank)

# # 3. Draw a Circle
# # cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
# # cv.imshow('Circle', blank)

# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)

# # 4. Draw a Line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Selin!!!', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)