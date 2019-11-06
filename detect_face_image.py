import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('allstar.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
i = 0
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    print("x:",x, "y:",y, "w:",w, "h:",h)
    # Crop the image
    crop_img = img[y:y+h, x:x+w]
    cv2.imshow("cropped", crop_img)
    cv2.imwrite('cropped'+i+'.png',crop_img)
    # Display the output
    cv2.imshow('img', img)
    cv2.imwrite('foto.png',img)
    i = i + 1

cv2.waitKey()
