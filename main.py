import cv2 

# Load the pre-trained face detector 
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Read the input image
image = cv2.imread('Donald_Trump_official_portrait.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image 
faces = face_detector.detectMultiScale(gray)
a = len(faces)

# # Draw bounding boxes around the detected faces
# for (x, y, w, h) in faces: cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# # Display the output image
# cv2.imshow('Face Detection', image)

# cv2.waitKey(0)

print("has face" if a > 0 else "has not face")