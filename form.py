# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormCalculator(object):
    def setupUi(self, FormCalculator):
        FormCalculator.setObjectName("FormCalculator")
        FormCalculator.resize(361, 392)
        self.lcd_field = QtWidgets.QLCDNumber(FormCalculator)
        self.lcd_field.setGeometry(QtCore.QRect(10, 30, 341, 61))
        self.lcd_field.setSmallDecimalPoint(True)
        self.lcd_field.setDigitCount(9)
        self.lcd_field.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcd_field.setObjectName("lcd_field")
        self.label_calculator = QtWidgets.QLabel(FormCalculator)
        self.label_calculator.setGeometry(QtCore.QRect(20, 10, 81, 17))
        self.label_calculator.setObjectName("label_calculator")
        self.button_0 = QtWidgets.QPushButton(FormCalculator)
        self.button_0.setGeometry(QtCore.QRect(10, 320, 61, 61))
        self.button_0.setObjectName("button_0")
        self.button_1 = QtWidgets.QPushButton(FormCalculator)
        self.button_1.setGeometry(QtCore.QRect(10, 250, 61, 61))
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(FormCalculator)
        self.button_2.setGeometry(QtCore.QRect(80, 250, 61, 61))
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(FormCalculator)
        self.button_3.setGeometry(QtCore.QRect(150, 250, 61, 61))
        self.button_3.setObjectName("button_3")
        self.button_4 = QtWidgets.QPushButton(FormCalculator)
        self.button_4.setGeometry(QtCore.QRect(10, 180, 61, 61))
        self.button_4.setObjectName("button_4")
        self.button_5 = QtWidgets.QPushButton(FormCalculator)
        self.button_5.setGeometry(QtCore.QRect(80, 180, 61, 61))
        self.button_5.setObjectName("button_5")
        self.button_6 = QtWidgets.QPushButton(FormCalculator)
        self.button_6.setGeometry(QtCore.QRect(150, 180, 61, 61))
        self.button_6.setObjectName("button_6")
        self.button_7 = QtWidgets.QPushButton(FormCalculator)
        self.button_7.setGeometry(QtCore.QRect(10, 110, 61, 61))
        self.button_7.setObjectName("button_7")
        self.button_8 = QtWidgets.QPushButton(FormCalculator)
        self.button_8.setGeometry(QtCore.QRect(80, 110, 61, 61))
        self.button_8.setObjectName("button_8")
        self.button_9 = QtWidgets.QPushButton(FormCalculator)
        self.button_9.setGeometry(QtCore.QRect(150, 110, 61, 61))
        self.button_9.setObjectName("button_9")
        self.button_dot = QtWidgets.QPushButton(FormCalculator)
        self.button_dot.setGeometry(QtCore.QRect(80, 320, 61, 61))
        self.button_dot.setObjectName("button_dot")
        self.button_division = QtWidgets.QPushButton(FormCalculator)
        self.button_division.setGeometry(QtCore.QRect(220, 110, 61, 61))
        self.button_division.setObjectName("button_division")
        self.button_multiplication = QtWidgets.QPushButton(FormCalculator)
        self.button_multiplication.setGeometry(QtCore.QRect(220, 180, 61, 61))
        self.button_multiplication.setObjectName("button_multiplication")
        self.button_subtraction = QtWidgets.QPushButton(FormCalculator)
        self.button_subtraction.setGeometry(QtCore.QRect(220, 250, 61, 61))
        self.button_subtraction.setObjectName("button_subtraction")
        self.button_addition = QtWidgets.QPushButton(FormCalculator)
        self.button_addition.setGeometry(QtCore.QRect(220, 320, 61, 61))
        self.button_addition.setObjectName("button_addition")
        self.button_equals = QtWidgets.QPushButton(FormCalculator)
        self.button_equals.setGeometry(QtCore.QRect(290, 320, 61, 61))
        self.button_equals.setObjectName("button_equals")
        self.button_percent = QtWidgets.QPushButton(FormCalculator)
        self.button_percent.setGeometry(QtCore.QRect(150, 320, 61, 61))
        self.button_percent.setObjectName("button_percent")
        self.button_clear = QtWidgets.QPushButton(FormCalculator)
        self.button_clear.setGeometry(QtCore.QRect(290, 110, 61, 61))
        self.button_clear.setObjectName("button_clear")
        self.button_sqrt = QtWidgets.QPushButton(FormCalculator)
        self.button_sqrt.setGeometry(QtCore.QRect(290, 180, 61, 61))
        self.button_sqrt.setObjectName("button_sqrt")
        self.button_exponentiation = QtWidgets.QPushButton(FormCalculator)
        self.button_exponentiation.setGeometry(QtCore.QRect(290, 250, 61, 61))
        self.button_exponentiation.setObjectName("button_exponentiation")

        self.retranslateUi(FormCalculator)
        QtCore.QMetaObject.connectSlotsByName(FormCalculator)

    def retranslateUi(self, FormCalculator):
        _translate = QtCore.QCoreApplication.translate
        FormCalculator.setWindowTitle(_translate("FormCalculator", "Калькулятор"))
        self.label_calculator.setText(_translate("FormCalculator", "Калькулятор"))
        self.button_0.setText(_translate("FormCalculator", "0"))
        self.button_1.setText(_translate("FormCalculator", "1"))
        self.button_2.setText(_translate("FormCalculator", "2"))
        self.button_3.setText(_translate("FormCalculator", "3"))
        self.button_4.setText(_translate("FormCalculator", "4"))
        self.button_5.setText(_translate("FormCalculator", "5"))
        self.button_6.setText(_translate("FormCalculator", "6"))
        self.button_7.setText(_translate("FormCalculator", "7"))
        self.button_8.setText(_translate("FormCalculator", "8"))
        self.button_9.setText(_translate("FormCalculator", "9"))
        self.button_dot.setText(_translate("FormCalculator", "."))
        self.button_division.setText(_translate("FormCalculator", "/"))
        self.button_multiplication.setText(_translate("FormCalculator", "*"))
        self.button_subtraction.setText(_translate("FormCalculator", "-"))
        self.button_addition.setText(_translate("FormCalculator", "+"))
        self.button_equals.setText(_translate("FormCalculator", "="))
        self.button_percent.setText(_translate("FormCalculator", "%"))
        self.button_clear.setText(_translate("FormCalculator", "C"))
        self.button_sqrt.setText(_translate("FormCalculator", "sqrt"))
        self.button_exponentiation.setText(_translate("FormCalculator", "^"))
