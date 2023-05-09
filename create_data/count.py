import os
import numpy as np
import pandas
import pandas as pd

dtframe =  pd.read_csv('../Data/val/val.csv').values
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
    PATH = 'D:/BKU/Monhoc/222/project2/Dataset/Data/val/labels/' + dtframe[i,0]
    try:
        fd = open(PATH,'r')
        stg = fd.read()
        matrix = stg[:-1].split('\n')

        for j in range(len(matrix)):
            #print(matrix[j])
            num0,num1,num2,num3,num4,num5,num6 = count(matrix[j],num0,num1,num2,num3,num4,num5,num6)
    except:
        continue
print(num0,num1,num2,num3,num4,num5,num6)



