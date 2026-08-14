"""def zapisi_ovire(ime_datoteke, ovire):
    kljuci = [kljuc for kljuc, vrednosti in ovire.items()]
    urejeni_kljuci = sorted(kljuci)

    for kljuc in urejeni_kljuci:
        for vrstica, vrednosti in ovire.items():
            niz = ""
            if vrstica == kljuc:
                vzorec_vrstica = f"{vrstica:03}:"
                niz += vzorec_vrstica
                for (x0, x1) in vrednosti:
                    koordinata = f"{x0:>4}-{x1:<4}"
                    niz += f"{koordinata}"
    return niz



ovire = {4: [(5, 6), (9, 11)],
 13: [(5, 8), (9, 11), (17, 19), (22, 25), (90, 100)],
 5: [(9, 11), (19, 20), (30, 34)],
}

print(zapisi_ovire("banana.txt", ovire))
"""

def preberi_ovire(ime_datoteke):
    slovar = dict()
    with open(ime_datoteke) as datoteka:
        vsebina = datoteka.read()
        bloki = vsebina.strip().split("\n\n")

    for blok in bloki:
        seznam = []
        blok = blok.splitlines()
        y = blok[0]
        for (x0, x1) in zip(blok[1::2], blok[2::2]):
            seznam.append((int(x0), int(x1)))
        slovar[int(y)] = seznam
    return slovar

print(preberi_ovire("/Users/lukakaroli/PycharmProjects/pythonProject/naloge_iz_programiranja/naloge_iz_programiranja/oblikovanje_nizov_in_delo_z_datotekami/ovire.txt"))