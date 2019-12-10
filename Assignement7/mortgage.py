#!/opt/anaconda3/bin/python3
import math
import csv

def scheduleWriter(m, res, p, r, resScd):
    with open('schedule.csv', mode='w') as schedule_file:
        schedule_writer = csv.writer(schedule_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        schedule_writer.writerow(['Months', 'Payment', 'Principal', 'Interest rate', 'Loan balance'])
        for oneMonth in range(m):
            schedule_writer.writerow([oneMonth, res, p, r, resScd])

def mPayement(p, r, n):
    res = (p * r) * (((1+r)**n)/(((1+r)**n)-1))
    return res

def outPayement(p, r, n, m):
    res = p * (( ((1+r)**n) - ((1+r)**m) ) / (((1+r)**n)-1))
    return res

def inptManager():
    p = int(input('Enter P value please (Principal): '))
    r = float(input('Enter r value please (monthly interest rate ex: 0.005): '))
    n = int(input('Enter n value please (number of months): '))
    res = mPayement(p, r, n)
    print('Fixed Monthly Payement = ' + str(res))
    m = int(input('Enter m value please (number of months): '))
    resScd = outPayement(p, r, n, m)
    print('Outstanding Loan Balance = ' + str(resScd))
    scheduleWriter(int(m), int(res), int(p), int(r), int(resScd))


def main():
    inptManager()

if __name__ == "__main__":
    main()