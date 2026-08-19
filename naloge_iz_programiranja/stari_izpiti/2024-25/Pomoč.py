from collections import defaultdict
def povezave(pot):
    odseki = set()
    seznam = [ime for ime in pot.split("-")]
    for ime1, ime2 in zip(seznam, seznam[1:]):
        odseki.add((ime1, ime2))
    return odseki

def popularni(poti, k):
    slovar_odsekov = defaultdict(int)
    for pot in poti:
        for odsek in povezave(pot):
            slovar_odsekov[odsek] += 1

    seznam_terk = []
    for odsek, stevilo_odsekov in slovar_odsekov.items():
        seznam_terk.append((odsek, stevilo_odsekov))

    sortiran_seznam_terk = sorted(seznam_terk, key=lambda odsek: odsek[1], reverse=True)

    mnozica_odsekov = set()
    for i in range(k):
        mnozica_odsekov.add(sortiran_seznam_terk[i][0])

    return mnozica_odsekov

ovire_list = [
    (3, 7, 5, 9),  # 0
    (2, 7, 3, 9),

    (8, 7, 10, 8),
    (9, 8, 10, 9),

    (6, 0, 7, 1),

    (0, 5, 2, 6), # 5
    (2, 5, 3, 6),

    (9, 4, 10, 5),

    (7, 1, 8, 2),
    (8, 1, 10, 2),
    (7, 2, 10, 3),  # 10

    (6, 5, 7, 6),
    (7, 5, 8, 6),
    (6, 6, 7, 7),

    (2, 3, 5, 4),
    (2, 1, 5, 3), # 15
    (1, 1, 2, 4),

    (7, 9, 8, 10),
    (6, 9, 7, 10)
]

def poisci_oviro(x, y, ovire):
    for x0, y0, x1, y1 in ovire:
        if x0 <= x < x1 and y0 <= y < y1:
            return (x0, y0, x1, y1)
    return None

def mozna_pot(x, y, pot, ovire):
    x, y = x, y
    for char in pot:
        if char == ">":
            x += 1
        elif char == "<":
            x -= 1
        elif char == "v":
            y += 1
        else:
            y -= 1

        if poisci_oviro(x, y, ovire):
            return False
        else:
            continue
    return True
plohe = [
            (7, 2), (7, 2), (8, 2), (8, 2),  # o10
            (2, 1), (3, 1), (4, 2),  # o15
            (6, 0), (6, 0), (6, 0),  # o4
            (2, 3), (2, 3),  # o14, a ostane
            (5, 6),  # o11, ostane
            (8, 7), (9, 7),  # o2
            (7, 9),
            (0, 0),
            (4, 6),
        ]

def kisel_dez(ovire, plohe):
    slovar = defaultdict(int)
    for ovira in ovire:
        for ploha in plohe:
            x, y = ploha
            x0, y0, x1, y1 = ovira
            if x0 <= x < x1 and y0 <= y < y1:
                slovar[ovira] += 1
    print(slovar)
    mnozica_uporabnih = set()
    mnozica_neuporabnih = set()
    for ovira, st in slovar.items():
        if st < 3:
            mnozica_uporabnih.add(ovira)
        else:
            mnozica_neuporabnih.add(ovira)

    return set(ovire) - mnozica_uporabnih


print((5 - 1) * (4 - 1))