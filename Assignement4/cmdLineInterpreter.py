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
            print('Please enter the maximum quantity')
            
            for li in lines:
                i = 1
                for l in range(int(li)):
                    print(" For", i ,"donut what added happiness do you get?")
                    utilityValue.append([i])
                    if i == 1:
                        print('10')
                        utilityValue.append([10])
                        # utilityValue.append('10')
                    if i == 2:
                        print('8')
                        utilityValue.append([8])
                        # utilityValue.append('8')
                    if i == 3:
                        print('5')
                        utilityValue.append([5])
                        # utilityValue.append('5')
                    if i == 4:
                        print('0')
                        utilityValue.append([0])
                        # utilityValue.append('0')
                    if i == 5:
                        print('-6')
                        utilityValue.append([-6])
                        # utilityValue.append('-6')
                    if i == 6:
                        print('-20')
                        utilityValue.append([-20])
                        # utilityValue.append('-20'
                    i = i + 1
                break
        break
    print(utilityValue)
    plt.plot(utilityValue)
    plt.xlabel('Product')
    plt.ylabel('Utility')
    plt.show()

    print(utilityValue)
    # plt.plot(utilityValue)
    # plt.show()
    quit()

def main():
    productUtility()

if __name__ == "__main__":
    main()