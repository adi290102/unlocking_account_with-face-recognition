import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    if faces == ():
        return None
    
    # Crop all faces found
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face
    
cap = cv2.VideoCapture(1)
count = 0

# Collect 200 samples of your face from webcam input
while True:

    ret, photo = cap.read()
    if face_extractor(photo) is not None:
        count += 1
        face = cv2.resize(face_extractor(photo), (200, 200)) #getting the face and changing size of image
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY) #convert colour image to black-white (grayscale)

        # Save file in specified directory with unique name
        file_name_path = 'D:\\ML_Project\\DataSet\\test\\' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)

        # Put count on images and display live count
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.imshow('Face Cropper', face)
        
    else:
        pass

    if cv2.waitKey(1) == 27 or count == 200: #27 is the Esc Key
        break
        
cap.release()
cv2.destroyAllWindows() #upon completion close the window      
print("Collecting Samples Complete")
cap.release()
