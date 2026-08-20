from collections import defaultdict

stari = [(1, 3, 1), (2, 2, 3), (9, 13, 5)]
novi = [(1, 1, 2), (10, 14, 7), (5, 9, 10), (4, 8, 3)]

def nabava(stari, novi):
    slovar_starih = defaultdict(int) #kljuc je dolzina ovire, vrednosti pa stevilo ovir dolzine dolzina npr. 5 : 3 -> 3 ovire dolzine 5
    for (x0, x1, y) in stari:
        dolzina = x1 - x0 + 1
        slovar_starih[dolzina] += 1

    slovar_novih = defaultdict(int)
    for (x0, x1, y) in novi:
        dolzina = x1 - x0 + 1
        slovar_novih[dolzina] += 1
print(nabava(stari, novi))