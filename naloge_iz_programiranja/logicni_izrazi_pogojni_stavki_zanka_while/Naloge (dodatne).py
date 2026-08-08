#Kvadratna enačba
"""
from math import *
a = float(input("Vpiši a: "))
b = float(input("Vpiši b: "))
c = float(input("Vpiši c: "))

D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + sqrt(D)) / 2*a
    x2 = (-b - sqrt(D)) / 2*a
    print("Enačba ima dve realni rešitvi: ", x1, "in", x2)
elif D == 0:
    x = -b / (2*a)
    print("Enačba ima eno realno rešitev: ", x)
else:
    print("Enačba nima realnih rešitev.")
"""

#Poštevanka števila 7
"""
i = 1
while i < 101:
    if i % 7 == 0 or "7" in str(i):
        print("BUM", end=" ")
    else:
        print(i, end=" ")
    i += 1
"""

#Vsote
"""
i = 0
n = int(input("Vpišite n: "))
vsota = 0
while i < n + 1:
    vsota += i
    i += 1
print(vsota)
"""

#Kvadrati
"""
from math import *
n = int(input("Vpiši število: "))
if sqrt(n)**2 == n:
    print("Število je kvadrat.")
else:
    print("Število ni kvadrat.")
"""

#Kocke
"""
st_kock = int(input("Vpiši število kock: "))
n = 0
while n**2 < st_kock:
    n += 1
razlika = n**2 - st_kock

print("Potrebujemo škatlo širine", n, "v kateri je prostora še za", razlika, "kock.")
"""

#Delitelji
"""
n = int(input("Vpiši število: "))
i = 1
while i < n + 1:
    if n % i == 0:
        print(i)
    i += 1
"""

#Trikotnik iz zvezdic
"""
h = int(input("Vpiši višino: "))
for i in range(1, h + 1):
    print(i * "*")
"""

#Smrekica
"""
h = int(input("Vpiši višino: "))
for i in range(1, h + 1):
    print(' ' * (h - i) + '*' * (2 * i - 1))
"""