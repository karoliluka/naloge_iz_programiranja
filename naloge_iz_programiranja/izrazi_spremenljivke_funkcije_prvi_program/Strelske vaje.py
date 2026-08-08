from math import *

v = float(input("Vpišite hitrost izstrelka: "))
kot = float(input("Vpišite kot izstrelka: "))

s = (pow(v, 2) * sin(2 * radians(kot))) / 9.807
print("Izstrelek bo letel:", s, "m.")

