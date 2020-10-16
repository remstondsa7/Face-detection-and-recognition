import cv2 ,os
import numpy as np
from PIL import Image
import pickle
import smtplib
from twilio.rest import Client
count1=1

sender='remstondsa7@gmail.com'
receiver='remstondsa7@gmail.com'
password='R7045525160n'

account_sid="ACd00a1fe6fe91e58aef029aa803d7e8bb"
auth_token="0d0e44dde69321d88ca901c8be4e587c"


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(r'C:\Users\win\Desktop\processing\trainingdata.yml')
cascadePath = r"C:\Users\win\Desktop\processing\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
smtp_server=smtplib.SMTP_SSL('smtp.gmail.com',465)
smtp_server.login(sender,password)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,3,3),2)
        Id,conf = recognizer.predict(gray[y:y+h,x:x+w])
        
        if(conf>50):
            if(Id==1):
                Id="REMSTON"
                
                while(count1!=0):
                    subject="Authentication Required"
                    body=Id+" is detected in your web cam"
                    msg=f'Subject: {subject}\n\n{body}'
                    smtp_server.sendmail(sender,receiver,msg)
                    smtp_server.close()
                    count1=count1-1
                    

                
            elif(Id==2):
                Id="BILL GATES"
                
            elif(Id==3):
                Id="BILL GATES"
                
        else:
            Id="Unknown"
        cv2.putText(im,str(Id), (x,y+h),font, 0.5,(0,0,0),2)
    cv2.imshow('im',im) 
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


