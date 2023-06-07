import shutil
import numpy as np
import pandas
import pandas as pd

dtframe =  pd.read_csv(r'D:\BKU\Monhoc\222\FINAL\train\B2.csv').values
num = dtframe.shape[0]

train = int(0.8* num)
val = num - train

for i in range(val):
    IMG = 'D:/BKU/Monhoc/222/Data_Final/train-20230525T090710Z-001/train/images/'+str(dtframe[i,0])
    LBL = 'D:/BKU/Monhoc/222/Data_Final/train-20230525T090710Z-001/train/labels/' + str(dtframe[i, 1])
    PATH_IMG = 'D:/BKU/Monhoc/222/Data_Final/train-20230525T090710Z-001/val/images/'
    PATH_LBL = 'D:/BKU/Monhoc/222/Data_Final/train-20230525T090710Z-001/val/labels/'
    try:
        shutil.move(IMG,PATH_IMG)
        shutil.move(LBL, PATH_LBL)
    except:
        continue