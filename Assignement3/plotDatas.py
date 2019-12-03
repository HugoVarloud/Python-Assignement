#!/opt/anaconda3/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import glob
import random
import math

def plotDatas():
    dFrame = pd.read_csv("world_bank_gdp.csv")
    df = pd.read_csv("world_bank_tariff.csv")
    randomDataFrame = []
    i = 0
    while i < 10:
        rd = random.randint(6, 269)
        if (dFrame.iloc[rd][2] == '' or df.iloc[rd][2] == ''):
            i = i
        else:
            randomDataFrame.append([df.iloc[rd][1], df.iloc[rd][2], dFrame.iloc[rd][2]])
            i = i + 1
    print(randomDataFrame)
    for j in range(0, 10):
            plt.plot(randomDataFrame[j][1], randomDataFrame[j][2], 'ro')
            plt.text(randomDataFrame[j][1], randomDataFrame[j][2], randomDataFrame[j][0])
    plt.xlabel('Tariff')
    plt.ylabel('GDP')
    plt.show()

def main():
    plotDatas()

if __name__ == '__main__':
    main()