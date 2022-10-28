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
