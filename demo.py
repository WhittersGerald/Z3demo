from z3 import *

s = Solver()

p = Bool('p')
q = Bool('q')
prop = Implies(p, q) == Or(Not(p), q)

s.push()
print("Proof that p=>q is logically equilvalent to (!p)v(q) by showing the negation of the equality is unsatisfiable.")
s.add(Not(prop))
print(s.check())
print()
s.pop()

input()
s.push()

a = Real('a')
b = Real('b')
c = Real('c')

s.add(2*a + b + 3*c == 1,
    2*a + 6*b + 8*c == 3,
    6*a + 8*b + 18*c == 5)

s.check()
print("Solution to the linear system: \n\
    2a + b + 3c = 1\n\
    2a + 6b + 8c = 3\n\
    6a + 8b + 18c = 5")
print(s.model())
s.pop()

input()

s.push()

x = Int('x')
y = Int('y')
z = Int('z')
f = Function('f', IntSort(), IntSort())

s.add(f(x) == f(y), f(y) == f(z))
print("First assert that f(x) = f(y) and that f(y) = f(z) and show that it is satisifiable.")
print(s.check())
print("Now also assert that f(x) != f(z) and show that is is unsatisfiable")
s.add(Not(f(x) == f(z)))
print(s.check())
print("This shows that if f(x) = f(y) and f(y) = f(z) then f(x) = f(z) (transitivity)")

s.pop()