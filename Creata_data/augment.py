from sklearn.cluster import MeanShift
import os
import numpy as np
import pandas
import pandas as pd
import cv2
import imgaug as ia
import imgaug.augmenters as iaa

def reflect(img):
    reflect = cv2.flip(img, 1)
    return reflect

def add_noise(img):
    mean = 0
    stddev = 180
    noise = np.zeros(img.shape, np.uint8)
    cv2.randn(noise, mean, stddev)

    # Add noise to image
    noisy_img = cv2.add(img, noise)
    return noisy_img

def add_haze(img):
    for i in range(1):
        aug = iaa.Fog(seed=np.random.default_rng())
        img = aug.augment(image=img)
    return img

def add_rain(img):
    aug = iaa.Rain()
    images_aug = aug.augment(image=img)
    return images_aug
def add_dark(img):
    brightness = cv2.convertScaleAbs(img, alpha, beta)
    return brightness


def add_snow(img):
    aug = iaa.Snowflakes()
    images_aug = aug.augment(image=img)
    return images_aug

if __name__ == '__main__':
    PATH = '/Data/train/augment/Choose/img'
    file_list = os.listdir(PATH)


    for nImg in (file_list):
        try:
            PATHIMG = PATH +'/'+ nImg
            STORE = PATH +'/Filter/haze'+ nImg
            print(PATHIMG)
            img = cv2.imread(PATHIMG)
            img = add_haze(img)
            cv2.imwrite(STORE, img)
        except: continue