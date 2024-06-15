# -*- coding: utf-8 -*-
"""A simple calculator that can perform basic operations."""

import sys

from PyQt5.QtWidgets import QApplication, QWidget

from form import Ui_FormCalculator


class Calculator(QWidget, Ui_FormCalculator):
    """The main class of the application."""

    def __init__(self):
        """Inits calculator app."""
        # Setup app window
        super().__init__()
        self.setupUi(self)  # method from Ui_FormCalculator
        self.setFixedSize(self.size())  # method from QWidget

        # Setup app buttons
        self._setup_buttons()

        # Main variables
        self.operation = ""  # action that will be performed (+, -, /, *, etc.)
        self.current_num = ""  # current number entered by the user
        self.previous_num = ""  # previous number already entered by the user

    def _setup_buttons(self):
        """Setting up buttons in the application window."""
        self.button_0.clicked.connect(lambda: self.add_symbol("0"))
        self.button_1.clicked.connect(lambda: self.add_symbol("1"))
        self.button_2.clicked.connect(lambda: self.add_symbol("2"))
        self.button_3.clicked.connect(lambda: self.add_symbol("3"))
        self.button_4.clicked.connect(lambda: self.add_symbol("4"))
        self.button_5.clicked.connect(lambda: self.add_symbol("5"))
        self.button_6.clicked.connect(lambda: self.add_symbol("6"))
        self.button_7.clicked.connect(lambda: self.add_symbol("7"))
        self.button_8.clicked.connect(lambda: self.add_symbol("8"))
        self.button_9.clicked.connect(lambda: self.add_symbol("9"))

        self.button_dot.clicked.connect(lambda: self.add_symbol("."))

        self.button_division.clicked.connect(lambda: self.choose_operation("/"))
        self.button_multiplication.clicked.connect(lambda: self.choose_operation("*"))
        self.button_subtraction.clicked.connect(lambda: self.choose_operation("-"))
        self.button_addition.clicked.connect(lambda: self.choose_operation("+"))
        self.button_percent.clicked.connect(lambda: self.choose_operation("%"))
        self.button_sqrt.clicked.connect(lambda: self.choose_operation("sqrt"))
        self.button_exponentiation.clicked.connect(lambda: self.choose_operation("**"))

        self.button_equals.clicked.connect(lambda: self.calculate())

        self.button_clear.clicked.connect(lambda: self.clear_field())

    def add_symbol(self, symbol: str) -> None:
        """
        Add a symbol to the current number.
        It must be a digit (0-9) or a point.

        Args:
            symbol (str): A digit (0-9) or a point to be added to a number.
        """
        # If the user adds a point and it is already in the current number
        if symbol == "." and "." in self.current_num:
            pass  # Pass, because the float num can't contain more than 2 dots

        # If the user adds a period, but the number has not yet been entered
        elif symbol == "." and not self.current_num.strip():
            self.current_num = "0."

        else:
            self.current_num = self.current_num + symbol

        self.lcd_field.display(self.current_num)

    def calculate(self):
        """
        Calculate an expression entered by the user.
        To perform the operation, the built-in function eval() is used.
        """
        # If the user did not enter the previous (first) number
        if not self.previous_num.strip():
            return
        
        # If the user has not entered the current (second) number
        if not self.current_num.strip():
            self.current_num = "0"

        result = eval(f"{self.previous_num} {self.operation} {self.current_num}")

        self.current_num = str(result)
        self.previous_num = ""
        self.operation = ""

        self.lcd_field.display(self.current_num)

    def choose_operation(self, operation: str = ""):
        """
        User choice of operation and ability to enter a second number.

        Args:
            operation (str): Mathematical operation on numbers (addition +, multiplication *, etc.).
        """
        self.operation = operation

        if self.previous_num.strip():
            return

        self.current_num, self.previous_num = "", self.current_num

    def clear_field(self):
        """Clears the current number and displays zero in the field."""
        self.current_num = ""
        self.lcd_field.display(0)


def main():
    """If __name__ == __main__."""
    app = QApplication([])
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
