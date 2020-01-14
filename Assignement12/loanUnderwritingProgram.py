#!/usr/bin/env python

import sys
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Python Loan Program Manager'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 1200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.firstName = QLineEdit(self)
        self.firstName.move(20, 20)
        self.firstName.resize(280,40)
        self.firstName.setPlaceholderText("first name")

        self.lastName = QLineEdit(self)
        self.lastName.move(20, 80)
        self.lastName.resize(280,40)
        self.lastName.setPlaceholderText("last name")

        self.socialSecuNumber = QLineEdit(self)
        self.socialSecuNumber.move(20, 140)
        self.socialSecuNumber.resize(280,40)
        self.socialSecuNumber.setPlaceholderText("social security number")

        self.loanAmount = QLineEdit(self)
        self.loanAmount.move(20, 200)
        self.loanAmount.resize(400,40)
        self.loanAmount.setPlaceholderText("loan value")

        self.loanDuration = QLineEdit(self)
        self.loanDuration.move(20, 260)
        self.loanDuration.resize(280,40)
        self.loanDuration.setPlaceholderText("loan duration")

        self.interestRate = QLineEdit(self)
        self.interestRate.move(20, 320)
        self.interestRate.resize(280,40)
        self.interestRate.setPlaceholderText("interest rate")

        self.income = QLineEdit(self)
        self.income.move(20, 380)
        self.income.resize(280,40)
        self.income.setPlaceholderText("income")

        self.creditScore = QLineEdit(self)
        self.creditScore.move(20, 440)
        self.creditScore.resize(280,40)
        self.creditScore.setPlaceholderText("credit score")

        
        # Create a button in the window
        self.button = QPushButton('Submit', self)
        self.button.move(20,500)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        fName = self.firstName.text()
        lName = self.lastName.text()
        sSecu = self.socialSecuNumber.text()
        loanAmnt = self.loanAmount.text()
        loanDur = self.loanDuration.text()
        interestR = self.interestRate.text()
        inc = self.income.text()
        credScore = self.creditScore.text()
        annualInterestPayement = (int(loanAmnt) * int(interestR))
        incomeRatio = (20/100)*int(inc)
        loanToIncome = int(loanAmnt) / int(inc)
        if int(annualInterestPayement) > int(incomeRatio) or int(loanToIncome) > 4 or int(credScore) < 600:
            QMessageBox.question(self, 'Python Loan Manager', "Mr, Mrs: " + fName + " " + lName + "\nWith the social security number " + sSecu + " isn't eligible to barrow $" + loanAmnt + " on " + loanDur + "months at the interest rate of " + interestR + "%\nHis/her income is: $" + inc + "\nHis/her credit score is $" + credScore + "\nThe Annual Interest Rate is: " + str(annualInterestPayement) + "%\nThe client income ratio (20% of your incomes) is: " + str(incomeRatio) + "\nThe client loan-to-income value is: " + str(loanToIncome), QMessageBox.Ok, QMessageBox.Ok)
            if int(annualInterestPayement) > int(incomeRatio):
                QMessageBox.question(self, 'Python Loan Manager', "Mr, Mrs: " + fName + " " + lName + " annual interest rate payement is $" + str(annualInterestPayement) + " which is inferrior to is income ratio which is " + str(incomeRatio), QMessageBox.Ok, QMessageBox.Ok)
            if int(loanToIncome) > 4:
                QMessageBox.question(self, 'Python Loan Manager', "Mr, Mrs: " + fName + " " + lName + " loan-to-income ratio is " + str(loanToIncome) + " which is superrior to the limit which is 4", QMessageBox.Ok, QMessageBox.Ok)
            if int(credScore) < 600:
                QMessageBox.question(self, 'Python Loan Manager', "Mr, Mrs: " + fName + " " + lName + " credit score is $" + credScore + " the minimum as to be strictly superrior to $600", QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.question(self, 'Python Loan Manager', "You're loan is accepted", QMessageBox.Ok, QMessageBox.Ok)
        self.firstName.setText("")
        self.lastName.setText("")
        self.socialSecuNumber("")
        self.loanAmount("")
        self.loanAmount("")
        self.loanDuration("")
        self.interestRate("")
        self.income("")
        self.creditScore("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())