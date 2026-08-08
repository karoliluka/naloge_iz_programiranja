from math import *
s = int(input("Vnesite dolžino poti: "))
leta = 0
while s > 0:
    neasfaltirano = (s + 2) // 3
    print(neasfaltirano)
    s -= neasfaltirano
    leta += 1
print(leta)