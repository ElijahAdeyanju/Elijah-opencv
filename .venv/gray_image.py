import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

img = cv2.imread(r"C:\Users\Ozai\PycharmProjects\main.py\images\girls.jpg.jpeg")
if img is None:
    print("No image")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

cv2.imshow('img', gray)
cv2.waitKey()