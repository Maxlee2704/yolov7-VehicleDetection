import shutil
import numpy as np
import pandas
import pandas as pd

dtframe =  pd.read_csv('../Dataset.csv').values
num = dtframe.shape[0]

train = int(0.7* num)
val = num - train

for i in range(val):
    IMG = 'D:/BKU/Monhoc/222/project2/Dataset/Data/label/'+str(dtframe[i,0])
    LBL = 'D:/BKU/Monhoc/222/project2/Dataset/Data/label/' + str(dtframe[i, 1])
    PATH_IMG = '/Data/val/images/'
    PATH_LBL = '/Data/val/labels/'
    try:
        shutil.move(IMG,PATH_IMG)
        shutil.move(LBL, PATH_LBL)
    except:
        continue