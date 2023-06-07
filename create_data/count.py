import os
import numpy as np
import pandas
import shutil
import pandas as pd

dtframe =  pd.read_csv(r'D:\BKU\Monhoc\222\FINAL\train\B2.csv').values
num = dtframe.shape[0]


def count(stg, num0, num1, num2, num3, num4, num5, num6):

    if stg != '':
        clas = stg[0]
        if clas == '0':
            num0 +=1
        elif clas == '1':
            num1 +=1
        elif clas == '2':
            num2 +=1

        elif clas == '3':
            num3 += 1
        elif clas == '4':
            num4 +=1
        elif clas == '5':
            num5 += 1
    else:
        num6 +=1
    return num0,num1,num2,num3,num4,num5,num6

num0,num1,num2,num3,num4,num5,num6 =0,0,0,0,0,0,0


for i in range(num):
    PATH = 'D:/BKU/Monhoc/222/FINAL/train/labels/' + dtframe[i,0]
    IMG =  'D:/BKU/Monhoc/222/FINAL/train/images/' + dtframe[i,1]
    NEW = 'D:/BKU/Monhoc/222/FINAL/train/human/' + dtframe[i, 1]
    NEW2 = 'D:/BKU/Monhoc/222/FINAL/train/human/' + dtframe[i, 0]
    try:
        fd = open(PATH,'r')
        stg = fd.read()
        matrix = stg[:-1].split('\n')

        for j in range(len(matrix)):
            #print(matrix[j])
            num0,num1,num2,num3,num4,num5,num6 = count(matrix[j],num0,num1,num2,num3,num4,num5,num6)
            #print(num0, num1, num2, num3, num4, num5, num6)
            #print(num2)
            if num2 != 0 :
                print(IMG)
                shutil.move(IMG,NEW)
                shutil.move(PATH, NEW2)
                num0, num1, num2, num3, num4, num5, num6 = 0, 0, 0, 0, 0, 0, 0
            num0, num1, num2, num3, num4, num5, num6 = 0, 0, 0, 0, 0, 0, 0
    except:
        num0, num1, num2, num3, num4, num5, num6 = 0, 0, 0, 0, 0, 0, 0
        continue
print(num0,num1,num2,num3,num4,num5,num6)



