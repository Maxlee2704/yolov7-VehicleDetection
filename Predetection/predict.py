from keras.models import load_model
import tensorflow as tf
import time
import os
import cv2
import numpy as np
model = load_model('Train.h5')
label = ["Dark","Haze","Ok"]
#model.summary()
#####################################################################
if __name__ == "__main__":
    PATH = r'D:\BKU\Monhoc\222\project2\Dataset\Data\train\augment\ban-xe-tai-3-5-tan-cu-tai-thai-nguyen.jpg'
    img = cv2.imread(PATH)
    print(img.shape)
    img = np.expand_dims(img , axis = 0)
    print(img.shape)
    result = model.predict(img)
    i = np.argmax(result)
    print(label[i])