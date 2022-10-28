# Taylor series
from sympy import *
x, y = symbols('x y')
f = Function('f')(x)
y = f

def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def taylor_series(y_diff, x0, y0, h):
    sum = 0
    for i in range(5):
        print(y_diff)
        sum += (h ** i) * y_diff.subs(x, x0).subs(y, y0) / fact(i)
        y_diff = diff(y_diff, x)
    return sum

y_diff = x ** 2 * y - 1
x0 = 0
y0 = 1
h = 0.1
Y = 0.2

# taylor_series(y_diff, x0, y0, h)
print(taylor_series(y_diff, x0, y0, h))

def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

from sympy import *
x, y = symbols('x y')
f = Function('f')(x)
y_diff = x ** 2 * y - 1
x0 = 0
y0 = 1
h = 0.1
Y = 0.2

eq = diff(y_diff, x)
eq = eq.subs(x, x0)
eq = eq.subs(Derivative(y, x), 7)
eq = eq.subs(y, y0)
sum = 0
sum2 = 0

for i in range(5):
    sum += (h ** i) * y_diff.subs(x, x0).subs(y, y0) / fact(i)
    sum2 += (h ** i) * y_diff.subs(x, x0).subs(Derivative(y, x), y0) / fact(i)
    y_diff = diff(y_diff, x)




# Eulers method

from sympy import *
x, y = symbols('x y')

y_diff = (x - y) / 2
x0 = 0
y0 = 1
h = 0.1
X_ = 0.2
X = x0
Y = y0

while X <= X_:
    Y = Y + h * y_diff.subs(x, X).subs(y, Y)
    print(y_diff.evalf(subs = {x : X, y:Y}))
    X += h
print(Y)




# Modified Eulers method

from sympy import *
x, y = symbols('x y')

y_diff = (x - y) / 2
x0 = 0
y0 = 1
h = 0.1
X_ = 0.2
X = x0
Y = y0

while X != X_:
    Y = Y + h * y_diff.subs(x, X + 0.5 * h).subs(y, Y + 0.5 * h * y_diff.subs(x, X).subs(y, Y))
    X += h
print(Y)




# Runge-Kutta Method of Third Order

from sympy import *
x, y = symbols('x y')

y_diff = (x - y) / 2
x0 = 0
y0 = 1
h = 0.1
X_ = 0.2
X = x0
Y = y0

while X != X_:
    k1 = h * y_diff.subs(x, X).subs(y, Y)
    k2 = h * y_diff.subs(x, X + h / 2).subs(y, Y + k1 / 2)
    k3 = h * y_diff.subs(x, X + h).subs(y, Y + 2 * k2 - k1)
    Y = Y + (k1 + 4 * k2 + k3) / 6
    X += h

print(Y)




# Runge-Kutta Method of fourth Order

from sympy import *
x, y = symbols('x y')

y_diff = (x - y) / 2
x0 = 0
y0 = 1
h = 0.1
X_ = 0.2
X = x0
Y = y0

while X != X_:
    k1 = h * y_diff.subs(x, X).subs(y, Y)
    k2 = h * y_diff.subs(x, X + h / 2).subs(y, Y + k1 / 2)
    k3 = h * y_diff.subs(x, X + h / 2).subs(y, Y + k2 / 2)
    k4 = h * y_diff.subs(x, X + h).subs(y, Y + k3)
    Y = Y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    X += h

print(Y)
