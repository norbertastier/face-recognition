import cv2

alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)

filename = "people_photo.jpg"

img = cv2.imread(filename, 0)

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

faces = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=4)

face_increment = 0

for x, y, w, h in faces:
    cropped_image = img[y : y + h, x : x + w]

    target_file_name = "detected_faces/face_{0}.jpg".format(face_increment)

    face_increment += 1

    cv2.imwrite(
        target_file_name,
        cropped_image,
    )