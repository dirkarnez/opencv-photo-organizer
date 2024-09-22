import argparse
import cv2
from pathlib import Path
from os import listdir, getcwd
from os.path import isfile, join

# Load the pre-trained face detector 
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def is_image(path:str) -> bool:
    return isfile(path) and (path.endswith(".jpg") or path.endswith(".jpeg"))

# mypath=Path(getcwd())
# print(mypath)

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("--directory", help="The directory to be scanned non-recursively", type=str)
args = parser.parse_args()
mypath=args.directory

print(f"Scanning {mypath}")

only_image_files = [join(mypath, f) for f in listdir(mypath) if is_image(join(mypath, f)) ]
with open('has_face.txt', 'w') as has_face, open('has_no_face.txt', 'w') as has_no_face:
    for i, image_file in enumerate(only_image_files):
        # Read the input image
        image = cv2.imread(image_file)

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

        if a > 0:
            has_face.write(f"{image_file}\n")
        else:
            has_no_face.write(f"{image_file}\n")

