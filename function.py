from math import sin, exp, log as sin, e, log


class Function:
    def __init__(self, expression, outputVar, inputVar):
        self.expression = expression
        self.input = inputVar
        self.output = outputVar

    def evaluate(self, value):
        exp = self.expression.replace(self.input, value)
        return eval(exp)

    def gradient(self, inputVal, res=1 * 10 ** -9):
        exp1 = eval(self.expression.replace(self.input, str(inputVal)))
        exp2 = eval(self.expression.replace(self.input, str(inputVal + res)))
        diff = exp2 - exp1
        gradient = diff / res
        return gradient

    def area(self, lowerBound, upperBound, res=1 * 10 ** -3):
        diff = (upperBound - lowerBound) // res
        dx = res
        A = 0
        x = lowerBound
        for i in range(int(diff)):
            dy = eval(self.expression.replace(self.input, str(x)))
            dA = dy * dx
            A += dA
            x += res
        return A
