#!/opt/anaconda3/bin/python3
import numpy as np

def currencyManager():
    usCurrency = [[1], [1.22], [0.75], [1.10], [0.67]]
    tab = [[], [], [], [], []]
    
    for i in range(len(usCurrency)):
        for j in range(len(usCurrency)):
            tab[i].append(usCurrency[i][0]/usCurrency[j][0])
            
    print(tab)
def main():
    currencyManager()

if __name__ == '__main__':
    main()