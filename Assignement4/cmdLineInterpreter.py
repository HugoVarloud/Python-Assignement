#!/opt/anaconda3/bin/python3
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import glob
import random
import math

def productUtility():
    utilityValue = []
    numberOfProd = []
    if len(sys.argv) > 1:
        print('No args needed')
        quit()
    else:
        lines = sys.stdin
    print('please enter a product')
    for line in lines:    
        if line != 'Donuts\n':
            print('Only Donuts please')
            quit()
        else:
            sys.stdin.flush()
            print('Please enter the maximum quantity')
            for li in lines:
                i = 1
                for l in range(int(li)):
                    print(" For", i ,"donut what added happiness do you get?")
                    numberOfProd.append(i)
                    addedHappiness = sys.stdin
                    utilityValue.append(int(addedHappiness.readline()))
                    i = i + 1
                break
            break
    print(utilityValue)
    print(numberOfProd)
    plt.plot(numberOfProd, utilityValue)
    plt.xlabel('Product')
    plt.ylabel('Utility')
    plt.show()
    exit()

def main():
    productUtility()

if __name__ == "__main__":
    main()