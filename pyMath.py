import sympy
from sympy.abc import x
from sympy import *

print(sympy.solve(32 * x - 40, "x"))

print(sympy.solve(2 * x - (3/4) == x/5 + 1, "x"))

a = 2 * x - (3/4)
b = (x/5) + 1

print(sympy.solve(simplify(a - b), "x"))