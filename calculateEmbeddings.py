import numpy
from imgbeddings import imgbeddings
from PIL import Image

file_name = "detected_faces/face_1.jpg"

img = Image.open(file_name)

ibed = imgbeddings()

embedding = ibed.to_embeddings(img)[0]