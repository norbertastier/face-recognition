
# Face Recognition Project

## Description
This Face Recognition Project is designed to detect and recognize human faces in images. Utilizing OpenCV and Haar Cascade classifiers, it identifies faces in various photographs. The project includes a Jupyter Notebook (`processing.ipynb`) that demonstrates the process and an XML file for the Haar Cascade classifier (`haarcascade_frontalface_default.xml`).

## Installation
To run this project, you will need Python (I use 3.9 version.) and the following libraries installed. You can install using pip:

```bash
pip install opencv-python
pip install psycopg2
pip install numpy
pip install imgbeddings
pip install PIL
```
## Storage
Images are stored in PostgreSQL using pgvector. For local installation, you can use the docker image: 
https://github.com/pgvector/pgvector?tab=readme-ov-file#installation-notes

## Usage
Navigate to the project directory and open the Jupyter Notebook:

```bash
cd faceRecognition
jupyter notebook processing.ipynb
```

The notebook contains all necessary code and instructions for running the face detection algorithm. Simply execute the cells in order to process the images in the `detected_faces` directory.

