import fire

import pyCalc
from pyCalc import (
    add_as_string,
    subtract_as_string,
    divide_as_string,
    multiply_as_string
)

class Calculator(object):
    
    def add(self, num1, num2):
        return add_as_string(num1, num2)
    
    def subtract(self, num1, num2):
        return subtract_as_string(num1, num2)
    def divide(self, num1, num2):
        return divide_as_string(num1, num2)
    def multiply(self, num1, num2):
        return multiply_as_string(num1, num2)
    
if __name__ == '__main__':
    fire.Fire(Calculator)
    