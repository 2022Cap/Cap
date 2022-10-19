import matplotlib.pyplot as plt
import numpy as np
from lmfit import Model
from sklearn.metrics import r2_score
from pathlib import Path                                                                                                #15줄 파일경로 에러 해결하려고 넣음(1/3)

def RC(seg_length, voltage,node):
    V = []
    capacitance = []
    resistance = []
    admittance = []

    file_path = Path(r"/Users/kimjihyun/Documents/jihyun_github/JIHYUN/2022cap_jh/Cap/Eyediagram/main/data/sample")     #15줄 파일경로 에러 해결하려고 넣음(2/3)
    lines = open(file_path+"/"+node+'_CV_result_ac_des.plt' ,'r').readlines()                                           #15줄 파일경로 에러 해결하려고 넣음(3/3)

    # lines = open(node+'_CV_result_ac_des.plt' ,'r').readlines()                                                       #파일경로 에러
    for i in range(len(lines)):
        if lines[i] == '      1.00000000000000E+09\n':
            split = lines[i+1].split('   ')
            split = lines[i+1]
            V.append(float(split[5:26]))
            capacitance.append(float(split[75:95])*1e15) # [fF/um]
            admittance.append(-float(split[97:118])) # [S/um]
            resistance.append((-float(split[97:118])/((2*np.pi*1e9)**2*float(split[75:95])**2))/1e3)
            # resistance.append(1/-float(split[]))

    fp1 = np.polyfit(V,resistance,2)
    f1 = np.poly1d(fp1)
    Ad = f1(voltage)


    fp2 = np.polyfit(V,capacitance,2)
    f2 = np.poly1d(fp2)
    Cp = f2(voltage)

    R = (f1(voltage)/((2*np.pi*1e9)**2*(f2(voltage)*1e-15)**2))/1e3
    
    return fp1, fp2