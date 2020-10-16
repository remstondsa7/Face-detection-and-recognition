import numpy
import matplotlib
import cv2
img=cv2.imread("C:\\Users\\win\\Desktop\\pics\\d.jpeg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier("C:\\Users\\win\\Desktop\\pyCharm\\img1\\haarcascade_frontalface_default.xml")
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resized=cv2.resize(img,(int(img.shape[1]),int(img.shape[0]*2)))
cv2.imshow("REMO",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


