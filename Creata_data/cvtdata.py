import os
import numpy as np
import pandas
import pandas as pd

dtframe =  pd.read_csv('dataset-vehicles/labels/Book1.csv').values
num = dtframe.shape[0]


def change(stg):
    new = ''
    clas = stg[0]
    if clas == '1':
        newzz = '0' + stg[1:]
    elif clas == '0':
        new = '1' + stg[1:]
    elif clas == '4':
        new = '2' + stg[1:]
    elif clas == '3':
        new = '5' + stg[1:]
    return new

for i in range(num):
    stg = ''
    final= ''
    lst = []
    PATH = 'dataset-vehicles/labels/val/'+dtframe[i,0]
    print(PATH)
    fd = open(PATH,'r')
    stg = fd.read()
    matrix = stg[:-1].split('\n')


    for i in range(len(matrix)):
        lst.append(change(matrix[i]))

    final = '\n'.join(lst)

    fd = open(PATH,'w')
    fd.write(final)
    fd.close()
