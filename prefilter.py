import image_dehazer
import cv2
import numpy as np
import scipy


def dehaze(img):
    HazeCorrectedImg = image_dehazer.remove_haze(img)
    return HazeCorrectedImg

def addbright(img):
    X = np.float64(img)/255
    lamda = 4
    n, m, channel = img.shape
    I1 = (np.max(X) / np.log(np.max(X) + 1)) * np.log(X + 1)
    I2 = 1 - np.exp(-X)
    I3 = (I1 + I2) / (lamda + (I1 * I2))
    I4 = np.zeros_like(I3)
    z = (lamda * np.arctan(np.exp(I3)) - 0.5 * I3)
    I4 = scipy.special.erf(z)
    I5 = (I4 - np.min(I4)) / (np.max(I4) - np.min(I4))
    return I5

def Clights_dt(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    n, m = img.shape
    img = cv2.blur(img, (3, 3))
    ret, img_new = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)
    cnt, hierarchy = cv2.findContours(img_new, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(cnt)):
        x, y, w, h = cv2.boundingRect(cnt[i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return img
if __name__=='__main__':
    PATH = r'D:\BKU\Monhoc\222\project2\Dataset\Data\test\thi-tran-tam-dao-mo-ao-nhu-tien-canh-4-15415176-17135577.webp'
    img = cv2.imread(PATH)
