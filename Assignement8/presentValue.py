#!/opt/anaconda3/bin/python3
import math
import sys

def futureValue():
    pv = int(input('>>enter the present value\n'))
    r = float(input('>>enter the interest rate\n'))
    n = int(input('>>enter the number of years\n'))
    res = pv * (1+r)**n
    print('>>' + str(res))
    
def presentValue():
    fv = int(input('>>enter the future value\n'))
    r = float(input('>>enter the rate\n'))
    n = int(input('>>enter the number of years\n'))
    pv = fv / (1+r)**n
    print('>>' + str(round(pv,2)))

def option():
    print('Run either with Fv.exe or Pv.exe flag')

def funcManager():
    if len(sys.argv) < 2:
        option()
        sys.exit(1)
    arg = sys.argv[1]
    if arg == 'Fv.exe':
        futureValue()
    elif arg == 'Pv.exe':
        presentValue()
    else:
        option()

def main():
    funcManager()

if __name__ == "__main__":
    main()