import cv2, os
from cv2 import *
import sys

# @TODO: Fix no frame selected error.
# @TODO: Implement logs and try catch.
def GetProcessedImage(userName, count):
    # Padding to face.
    # @TODO: Move this configuration variable.
    left = 100
    right = 100
    top = 100
    bottom = 100

    # Capture Video Stream. 
    video_capture = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.25,
            minNeighbors=4,
            minSize=(220, 220),
            maxSize=(300, 300),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        if faces is not None:
            faces_exact = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=6,
                minSize=(260, 260),
                maxSize=(260, 260),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # Draw a rectangle around the faces - red range
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        # Draw a rectangle around the faces - green range
        for (p, q, r, s) in faces_exact:
            cv2.rectangle(faces_exact, (p-10, q-10), (p+r+10, q+s+10), (0, 255, 0), 3)  
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            video_capture.release()
            cv2.destroyAllWindows()
            exit()
        if cv2.waitKey(1) & 0xFF == ord('n'):
            if ret:    # frame captured without any errors
                namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
                imshow("cam-test",frame)
                waitKey(0)
                destroyWindow("cam-test")
                crop_image = gray[y-top:y+h+bottom, x-left:x+w+right]
                # Resizing image.
                resized_image = cv2.resize(crop_image,(260, 260), interpolation = cv2.INTER_AREA)
                if mode == 'train':
                    if not count >= 10 or cv2.waitKey(1) & 0xFF != ord('q'):
                        # Create Folder if not exist.
                        if not os.path.exists("../training_images/" + userName):
                            os.makedirs("../training_images/" + userName)
                        cv2.imwrite("../training_images/"+userName+"/"+str(count)+".pgm", resized_image)
                    # Exit.
                    video_capture.release()
                    cv2.destroyAllWindows()
                    exit()
                if mode == 'test':
                    if not count >= 2 or cv2.waitKey(1) & 0xFF != ord('q'):
                        if not os.path.exists("../test_images/" + userName):
                            os.makedirs("../test_images/" + userName)
                        cv2.imwrite("../test_images/"+userName+"/"+str(count)+".pgm", resized_image)
                    # Exit.        
                    video_capture.release()
                    cv2.destroyAllWindows()
                    exit()
                count+=1
 
 # Main function
cascPath = sys.argv[1]
userName = sys.argv[2]
mode = sys.argv[3]
faceCascade = cv2.CascadeClassifier(cascPath)
# Display the resulting frame    
count = 1
for count in range(1,10):
    image_capturer = GetProcessedImage(userName, count)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()




