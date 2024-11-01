import cv2
import sys

image_path = 'photo.jpg'
image = cv2.imread(image_path)
if image is None:
    print(f"Не удалось загрузить изображение {image_path}")
    sys.exit(1)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(f"Найдено {len(faces)} лицо(а) на изображении.")
