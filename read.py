import cv2 as cv 

# img = cv.imread('Resources/Photos/cat_large.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0)

# Reading Videos

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read('Resources/Videos/dog.mp4')
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): # Her kare arasında 20ms bekler ve d tuşuna basılınca video gösterimi durdurulur.
        break

capture.release()
cv.destroyAllWindows()
