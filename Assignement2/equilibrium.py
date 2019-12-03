#!/opt/anaconda3/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

def csvReader():
    df = pd.read_csv("data.csv")
    ax = plt.gca()
    plt.ylim((10, 100))
    df.plot(kind='line', x='price', y=' quanity demanded', color='blue', ax=ax)
    df.plot(kind='line', x='price', y=' quantity supplied', color='orange', ax=ax)
    plt.show()

    # price = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
    # quantityDemanded = [10, 14, 18, 22, 28, 35, 45, 57, 73, 100]
    # quantitySupplied = [100, 97, 94, 89, 84, 77, 68, 57, 40, 0]
    # plt.plot(price, quantityDemanded)
    # plt.plot(price, quantitySupplied)
    # plt.show()

def main():
    csvReader()

if __name__ == '__main__':
    main()