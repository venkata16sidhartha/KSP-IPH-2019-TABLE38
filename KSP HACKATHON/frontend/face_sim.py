from keras_facenet import FaceNet
import cv2
import numpy as np
import numpy
from tqdm import tqdm

embedder = FaceNet()
path = "G:/KSP HACKATHON/frontend/frontend/"
images_path = ["static/img/gopi.jpg", "static/img/gopi1.jpg", "static/img/adi.jpg","static/img/din.jpg", "static/img/ani.jpg", "static/img/sidh.jpg"]
images = []

for i in tqdm(images_path):
    print(path+i)
    img = cv2.imread(path + i)
    img = cv2.resize(img,(480,480))
    img = numpy.asarray(img)
    images.append(img)

images = np.array(images)
print(images.shape)
# images is a list of images, each as an
# np.ndarray of shape (H, W, 3).
embeddings = embedder.embeddings(images)

import math
print(embeddings.shape)
# print(embeddings[0][:50])
temp1= 0
temp2 = 0
temp3 = 0
temp4 = 0
temp5 = 0
for i in range(len(embeddings[0])):
    temp1 += ((embeddings[0][i]) - (embeddings[1][i])) #--same
    temp2 += ((embeddings[0][i]) - (embeddings[2][i]))#diff
    temp3 += ((embeddings[0][i]) - (embeddings[3][i]))#diff
    temp4 += ((embeddings[0][i]) - (embeddings[4][i]))#diff
    temp5 += ((embeddings[0][i]) - (embeddings[5][i]))#diff

res = ([abs(temp1), abs(temp2),abs(temp3),abs(temp4),abs(temp5)])
print(res)
for c,i in enumerate(res):
    if i<0.20:
        print("the similar person(s) is/are : ", c+1)
