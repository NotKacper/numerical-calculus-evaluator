from function import Function

# Data analysis of accuracy of a calculus calculator - numerical integral plus derivative evaluation

# 1st parameter = function to be operated on as a string
# 2nd is output parameter (i.e if function of time giving velocity this would be v)
# 3rd is input parameter
y = Function('x**(1/2)', 'y', 'x')

# y.gradient(a) returns slope of function at x=a input
# y.area(a, b) returns area between two limits of a function, x=a, x=b
# y.evaluate(a) returns value of y at x=a

print(y.gradient(2))
print(y.area(1, 4))
