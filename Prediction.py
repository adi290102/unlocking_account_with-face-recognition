import cv2
import numpy as np
import os
from os import listdir
from os.path import isfile, join

# Get the training data we previously made
dataset_path = 'D:\\ML_Project\\DataSet\\'

#creating list of files present in DataSet directory
onlyfiles = [file for file in listdir(dataset_path) if isfile(join(dataset_path, file))]

# Creating arrays for training data and labels
Training_Data, Labels = [], []

# Open training images in our datapath
# Create a numpy array for training data
for i, files in enumerate(onlyfiles):
    image_path = dataset_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)

# Create a numpy array for both training data and labels
Labels = np.asarray(Labels, dtype=np.int32)

model = cv2.face.LBPHFaceRecognizer_create() 

# Initialize facial recognizer
#model = cv2.face_LBPHFaceRecognizer.create()
# model=cv2.f
# NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()

# Let's train our model 
model.train(np.asarray(Training_Data), np.asarray(Labels))
print("Model trained successfully")


def face_detector(img, size=0.5):
  
    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi
  
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(1)
while True:

    ret, frame = cap.read()

    image, face = face_detector(frame)

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Pass face to prediction model
        # "results" comprises of a tuple containing the label and the confidence value
        results = model.predict(face)
        if results[1] < 500:
            confidence = int( 100 * (1 - (results[1])/400) )
            display_string = str(confidence) + '% Confident it is User'

        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)

        if confidence > 80:
            cv2.putText(image, "Hey there", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            os.system('curl https://205h6snh8k.execute-api.ap-south-1.amazonaws.com/test/unlock')
            cv2.imshow('Face Recognition', image )

        else:
            cv2.putText(image, "i dont know", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Face Recognition', image )

    except:
        cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        #cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.imshow('Face Recognition', image )
        pass

    if cv2.waitKey(1) == 27: #27 is the Esc Key
        break

cap.release()
cv2.destroyAllWindows()
