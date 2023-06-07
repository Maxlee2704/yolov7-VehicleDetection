import os
import numpy as np
import pandas
import pandas as pd

dtframe =  pd.read_csv(r'D:\BKU\Monhoc\222\BUS DETECTION.v3i.yolov7pytorch\train\labels\B2.csv').values
num = dtframe.shape[0]


def change(stg):
    new = ''
    clas = stg[0]
    if clas == '0':
        new = '3' + stg[1:]
    if clas == '1':
        new = '1' + stg[1:]
    if clas == '2':
        new = '2' + stg[1:]
    if clas == '3':
        new = '4' + stg[1:]


    return new

for i in range(num):
    stg = ''
    final= ''
    lst = []
    PATH = 'D:/BKU/Monhoc/222/Vehicle Detection.v2i.yolov7pytorch/train/labels/'+dtframe[i,0]
    print(PATH)
    fd = open(PATH,'r')
    stg = fd.read()
    matrix = stg[:-1].split('\n')

    try:
        for i in range(len(matrix)):
            lst.append(change(matrix[i]))

        final = '\n'.join(lst)

        fd = open(PATH,'w')
        fd.write(final)
        fd.close()
    except:
        pass
