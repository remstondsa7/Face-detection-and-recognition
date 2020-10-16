import cv2
import numpy as np
from PIL import Image
import os
path = r'C:\Users\win\Desktop\dataset1'

recognizer = cv2.face.LBPHFaceRecognizer_create()
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    print(imagePaths)

getImagesAndLabels(path)
