from NeuroPy import NeuroPy
from time import sleep
import numpy as np
import pandas as pd

X=[]
dataset=20
neuropy = NeuroPy("COM5")
neuropy.start()

try:
    while True:
        while(len(X)<dataset):
            print(str(len(X)))
            a = np.array([neuropy.attention,neuropy.meditation,neuropy.rawValue,neuropy.delta,neuropy.theta,neuropy.lowAlpha,neuropy.highAlpha,neuropy.lowBeta,neuropy.highBeta,neuropy.lowGamma,neuropy.midGamma])
            X.append(a)
            sleep(0.5)

        break
finally:
    print("making the dataset")
    df = pd.DataFrame(X)
    df.to_excel('concentrate.xlsx')
    neuropy.stop()