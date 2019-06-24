import cv2
import sys
from os import walk
from os import mkdir

# Get user supplied values
dirPath = "images/Portrait"

f = []
for (dirpath, dirnames, filenames) in walk(dirPath):
    f.extend(filenames)

print(f)

haar = "haarcascade_default.xml"

try:
    mkdir(dirPath + "/detected")
except:
    pass

try:
    for image_F in f:
        # Get user supplied values
        #imagePath = 'images/' + image_F
        imagePath = dirPath + '/' + image_F
        print("imagePath: " + imagePath)
        cascPath = haar

        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(cascPath)

        # Read the image
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.519,
            minNeighbors=5,
            minSize=(20, 20)
        )
        print("Haar: " + haar)
        print("Found {0} faces!".format(len(faces)))

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        detectedPath = (dirPath + "/detected/" + image_F)
        print(detectedPath)
        cv2.imwrite( detectedPath, image )
        #cv2.imshow("Faces found", image)
        #cv2.waitKey(0)
except Exception as e:
    print(e)
    pass
