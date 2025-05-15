import cv2
import os

def detect_faces(image_path):
    # Check if the file exists
    if not os.path.exists(image_path):
        print(f"Error: The image file at {image_path} does not exist.")
        return False
    
    # Load the cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Read the input image
    img = cv2.imread(image_path)
    
    # Check if image is loaded successfully
    if img is None:
        print(f"Error: Failed to load the image at {image_path}.")
        return False
    
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()
    
    return len(faces) > 0

if __name__ == "__main__":
    image_path = 'path_to_your_image.jpg'
    if detect_faces(image_path):
        print("Face detected")
    else:
        print("No face detected")