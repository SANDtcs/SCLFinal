# Runge-kutta method

from sympy import *
x, y = symbols('x y')

y_diff = (2 * x * y) / (1 + x ** 2)
x0 = 0
y0 = 0
h = 0.1
X_ = 0.4
X = x0
Y = y0
xList = []
yList = []

while X < X_:
    xList.append(X)
    k1 = h * y_diff.subs(x, X).subs(y, Y)
    k2 = h * y_diff.subs(x, X + h / 2).subs(y, Y + k1 / 2)
    k3 = h * y_diff.subs(x, X + h / 2).subs(y, Y + k2 / 2)
    k4 = h * y_diff.subs(x, X + h).subs(y, Y + k3)
    Y = Y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    yList.append(Y)
    X += h

print(xList)
print(yList)

n = len(xList) - 1
h = xList[1] - xList[0]

# Predicting
value = yList[n - 3] + (4 * h / 3) * (2 * y_diff.subs(x, xList[n - 2]).subs(y, yList[n - 2]) - y_diff.subs(x, xList[n - 1]).subs(y, yList[n - 1]) + 2 * y_diff.subs(x, xList[n]).subs(y, yList[n]))

# Correcting
value = yList[n - 1] + (h / 3) * (y_diff.subs(x, xList[n - 1]).subs(y, yList[n - 1]) + 4 * y_diff.subs(x, xList[n]).subs(y, yList[n]) + y_diff.subs(x, xList[n] + h).subs(y, value))
print(value)

n = len(xList) - 1
h = xList[1] - xList[0]

# Predicting
value = yList[n] + (h / 24) * (55 * y_diff.subs(x, xList[n]).subs(y, yList[n]) - 59 * y_diff.subs(x, xList[n - 1]).subs(y, yList[n - 1]) + 37 * y_diff.subs(x, xList[n - 2]).subs(y, yList[n - 2]) - 9 * y_diff.subs(x, xList[n - 3]).subs(y, yList[n - 3]))

# Correcting
value = yList[n] + (h / 24) * (9 * y_diff.subs(x, xList[n] + h).subs(y, value) + 19 * y_diff.subs(x, xList[n]).subs(y, yList[n]) - 5 * y_diff.subs(x, xList[n - 1]).subs(y, yList[n - 1]) + y_diff.subs(x, xList[n - 2]).subs(y, yList[n - 2]))
print(value)


# Eulers
y_diff = (2 * x * y) / (1 + x ** 2)
x0 = 0
y0 = 0
h = 0.1
X_ = 0.4
X = x0
Y = y0
xList = []
yList = []

while X < X_:
    Y = Y + h * y_diff.subs(x, X).subs(y, Y)
    xList.append(X)
    yList.append(Y)
    X += h
print(Y)


#modified Eulers method

y_diff = (2 - y ** 2) / (5 * x)
x0 = float(4.00)
y0 = float(1.00)
h = float(0.10)
X_ = float(4.35)
X = x0
Y = y0
xList = []
yList = []
xList.append(x0)
yList.append(y0)
X += h

while X < X_:
    Y = Y + h * y_diff.subs(x, X + 0.5 * h).subs(y, Y + 0.5 * h * y_diff.subs(x, X).subs(y, Y))
    xList.append(X)
    yList.append(Y)
    X += h

print(xList)
print(yList)
