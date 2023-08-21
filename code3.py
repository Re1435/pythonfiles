a = int(input())
b = int(input())
c = int(input())

eq1 = (-b + (b**2 - 4 * a * c)**0.5)/2 * a
eq2 = (-b - (b**2 - 4 * a * c)**0.5)/2 * a
print(round(eq1, 2))
print(round(eq2, 2))
