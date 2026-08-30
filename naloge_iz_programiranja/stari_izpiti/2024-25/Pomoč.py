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

postaje = {'LIDL BEŽIGRAD': {'latitude': 46.063797,
                             'longitude': 14.506854,
                             'capacity': 20,
                             'bikes': 9},
           'ŠMARTINSKI PARK': {'latitude': 46.065206,
                               'longitude': 14.529911,
                               'capacity': 20,
                               'bikes': 2},
           'SAVSKO NASELJE 1-ŠMARTINSKA CESTA': {'latitude': 46.062475,
                                                 'longitude': 14.524321,
                                                 'capacity': 20,
                                                 'bikes': 0},
           'ČRNUČE': {'latitude': 46.102446,
                      'longitude': 14.530213,
                      'capacity': 20,
                      'bikes': 11},
           'VILHARJEVA CESTA': {'latitude': 46.06005,
                                'longitude': 14.51302,
                                'capacity': 20,
                                'bikes': 18},
           'MASARYKOVA DDC': {'latitude': 46.05763,
                              'longitude': 14.514264,
                              'capacity': 18,
                              'bikes': 10},
           'POGAČARJEV TRG-TRŽNICA': {'latitude': 46.051093,
                                      'longitude': 14.507186,
                                      'capacity': 18,
                                      'bikes': 9},
           'CANKARJEVA UL.-NAMA': {'latitude': 46.052431,
                                   'longitude': 14.503257,
                                   'capacity': 26,
                                   'bikes': 8},
           'ANTONOV TRG': {'latitude': 46.041753,
                           'longitude': 14.477016,
                           'capacity': 20,
                           'bikes': 4},
           'PRUŠNIKOVA': {'latitude': 46.090608,
                          'longitude': 14.471637,
                          'capacity': 20,
                          'bikes': 1},
           'TEHNOLOŠKI PARK': {'latitude': 46.04843,
                               'longitude': 14.461086,
                               'capacity': 20,
                               'bikes': 9},
           'KOSEŠKI BAJER': {'latitude': 46.068443,
                             'longitude': 14.470913,
                             'capacity': 20,
                             'bikes': 14},
           'TIVOLI': {'latitude': 46.05952,
                      'longitude': 14.4982,
                      'capacity': 20,
                      'bikes': 1},
           'TRŽNICA MOSTE': {'latitude': 46.055801,
                             'longitude': 14.534156,
                             'capacity': 21,
                             'bikes': 16},
           'GRUDNOVO NABREŽJE-KARLOVŠKA C.': {'latitude': 46.045748,
                                              'longitude': 14.506196,
                                              'capacity': 18,
                                              'bikes': 7},
           'LIDL-LITIJSKA CESTA': {'latitude': 46.047689,
                                   'longitude': 14.547416,
                                   'capacity': 20,
                                   'bikes': 4},
           'ŠPORTNI CENTER STOŽICE': {'latitude': 46.08259,
                                      'longitude': 14.52016,
                                      'capacity': 26,
                                      'bikes': 24},
           'ŠPICA': {'latitude': 46.040213,
                     'longitude': 14.512044,
                     'capacity': 18,
                     'bikes': 15},
           'ROŠKA - STRELIŠKA': {'latitude': 46.045,
                                 'longitude': 14.51846,
                                 'capacity': 20,
                                 'bikes': 13},
           'BAVARSKI DVOR': {'latitude': 46.05682,
                             'longitude': 14.50551,
                             'capacity': 20,
                             'bikes': 3},
           'STARA CERKEV': {'latitude': 46.06342,
                            'longitude': 14.494588,
                            'capacity': 14,
                            'bikes': 2},
           'SITULA': {'latitude': 46.059433,
                      'longitude': 14.52051,
                      'capacity': 20,
                      'bikes': 0},
           'ILIRSKA ULICA': {'latitude': 46.053144,
                             'longitude': 14.513479,
                             'capacity': 18,
                             'bikes': 9},
           'LIDL - RUDNIK': {'latitude': 46.020012,
                             'longitude': 14.532479,
                             'capacity': 20,
                             'bikes': 9},
           'KOPALIŠČE KOLEZIJA': {'latitude': 46.042867,
                                  'longitude': 14.495239,
                                  'capacity': 20,
                                  'bikes': 19},
           "MCDONALD'S - ŠMARTINSKA": {'latitude': 46.069408,
                                       'longitude': 14.541228,
                                       'capacity': 20,
                                       'bikes': 0},
           'POVŠETOVA - KAJUHOVA': {'latitude': 46.051512,
                                    'longitude': 14.539272,
                                    'capacity': 20,
                                    'bikes': 6},
           'DUNAJSKA C.-PS MERCATOR': {'latitude': 46.074193,
                                       'longitude': 14.511134,
                                       'capacity': 18,
                                       'bikes': 2},
           'CITYPARK': {'latitude': 46.068805,
                        'longitude': 14.546257,
                        'capacity': 20,
                        'bikes': 2},
           'KOPRSKA ULICA': {'latitude': 46.033408,
                             'longitude': 14.482468,
                             'capacity': 8,
                             'bikes': 3},
           'LIDL - VOJKOVA CESTA': {'latitude': 46.07589,
                                    'longitude': 14.52011,
                                    'capacity': 20,
                                    'bikes': 17},
           'POLJANSKA-POTOČNIKOVA': {'latitude': 46.048982,
                                     'longitude': 14.522709,
                                     'capacity': 20,
                                     'bikes': 10},
           'POVŠETOVA-GRABLOVIČEVA': {'latitude': 46.051863,
                                      'longitude': 14.530349,
                                      'capacity': 19,
                                      'bikes': 14},
           'PARK NAVJE-ŽELEZNA CESTA': {'latitude': 46.06361,
                                        'longitude': 14.51315,
                                        'capacity': 20,
                                        'bikes': 7},
           'ZALOG': {'latitude': 46.06043,
                     'longitude': 14.613797,
                     'capacity': 20,
                     'bikes': 9},
           'CESTA NA ROŽNIK': {'latitude': 46.053241,
                               'longitude': 14.486206,
                               'capacity': 20,
                               'bikes': 5},
           'HOFER-KAJUHOVA': {'latitude': 46.056405,
                              'longitude': 14.540901,
                              'capacity': 20,
                              'bikes': 11},
           'DUNAJSKA C.-PS PETROL': {'latitude': 46.065136,
                                     'longitude': 14.509112,
                                     'capacity': 20,
                                     'bikes': 4},
           'STUDENEC': {'latitude': 46.054615,
                        'longitude': 14.576031,
                        'capacity': 20,
                        'bikes': 18},
           'PARKIRIŠČE NUK 2-FF': {'latitude': 46.046377,
                                   'longitude': 14.501256,
                                   'capacity': 20,
                                   'bikes': 3},
           'BRATOVŠEVA PLOŠČAD': {'latitude': 46.08929,
                                  'longitude': 14.513751,
                                  'capacity': 20,
                                  'bikes': 10},
           'KONGRESNI TRG-ŠUBIČEVA ULICA': {'latitude': 46.050388,
                                            'longitude': 14.504623,
                                            'capacity': 20,
                                            'bikes': 9},
           'BS4-STOŽICE': {'latitude': 46.086761,
                           'longitude': 14.514151,
                           'capacity': 20,
                           'bikes': 11},
           'GERBIČEVA - ŠPORTNI PARK SVOBODA': {'latitude': 46.039384,
                                                'longitude': 14.485458,
                                                'capacity': 20,
                                                'bikes': 5},
           'ŽIVALSKI VRT': {'latitude': 46.052454,
                            'longitude': 14.472149,
                            'capacity': 20,
                            'bikes': 6},
           'VOKA - SLOVENČEVA': {'latitude': 46.075207,
                                 'longitude': 14.504734,
                                 'capacity': 20,
                                 'bikes': 17},
           'BTC CITY/DVORANA A': {'latitude': 46.065297,
                                  'longitude': 14.543996,
                                  'capacity': 20,
                                  'bikes': 10},
           'TRNOVO': {'latitude': 46.03784,
                      'longitude': 14.50001,
                      'capacity': 20,
                      'bikes': 14},
           'P+R BARJE': {'latitude': 46.02749,
                         'longitude': 14.49958,
                         'capacity': 20,
                         'bikes': 10},
           'ROŽNA DOLINA-ŠKRABČEVA UL.': {'latitude': 46.051439,
                                          'longitude': 14.49273,
                                          'capacity': 18,
                                          'bikes': 9},
           'KINO ŠIŠKA': {'latitude': 46.06928,
                          'longitude': 14.48971,
                          'capacity': 26,
                          'bikes': 5},
           'BRODARJEV TRG': {'latitude': 46.054398,
                             'longitude': 14.553319,
                             'capacity': 20,
                             'bikes': 8},
           'ZALOŠKA C.-GRABLOVIČEVA C.': {'latitude': 46.05441,
                                          'longitude': 14.52978,
                                          'capacity': 16,
                                          'bikes': 15},
           'DOLENJSKA C. - STRELIŠČE': {'latitude': 46.038866,
                                        'longitude': 14.517605,
                                        'capacity': 20,
                                        'bikes': 19},
           'ŠTEPANJSKO NASELJE 1-JAKČEVA ULICA': {'latitude': 46.053047,
                                                  'longitude': 14.545125,
                                                  'capacity': 19,
                                                  'bikes': 15},
           'SOSESKA NOVO BRDO': {'latitude': 46.045617,
                                 'longitude': 14.462281,
                                 'capacity': 20,
                                 'bikes': 20},
           'TRŽNICA KOSEZE': {'latitude': 46.074315,
                              'longitude': 14.475483,
                              'capacity': 18,
                              'bikes': 16},
           'ALEJA - CELOVŠKA CESTA': {'latitude': 46.077302,
                                      'longitude': 14.482581,
                                      'capacity': 20,
                                      'bikes': 9},
           'MERCATOR CENTER ŠIŠKA': {'latitude': 46.087079,
                                     'longitude': 14.475439,
                                     'capacity': 22,
                                     'bikes': 13},
           'GH ŠENTPETER-NJEGOŠEVA C.': {'latitude': 46.05257,
                                         'longitude': 14.51928,
                                         'capacity': 24,
                                         'bikes': 0},
           'HOFER - POLJE': {'latitude': 46.053718,
                             'longitude': 14.589284,
                             'capacity': 20,
                             'bikes': 6},
           'VIŠKO POLJE': {'latitude': 46.046189,
                           'longitude': 14.469037,
                           'capacity': 20,
                           'bikes': 16},
           'BONIFACIJA': {'latitude': 46.039641,
                          'longitude': 14.472664,
                          'capacity': 21,
                          'bikes': 18},
           'P + R DOLGI MOST': {'latitude': 46.037003,
                                'longitude': 14.465229,
                                'capacity': 20,
                                'bikes': 18},
           'DRAVLJE': {'latitude': 46.07984,
                       'longitude': 14.479952,
                       'capacity': 20,
                       'bikes': 12},
           'POLJE': {'latitude': 46.05722,
                     'longitude': 14.583537,
                     'capacity': 20,
                     'bikes': 19},
           'SUPERNOVA LJUBLJANA - RUDNIK': {'latitude': 46.021586,
                                            'longitude': 14.536745,
                                            'capacity': 20,
                                            'bikes': 14},
           'SREDNJA FRIZERSKA ŠOLA': {'latitude': 46.080522,
                                      'longitude': 14.491439,
                                      'capacity': 20,
                                      'bikes': 5},
           'TRG OF-KOLODVORSKA UL.': {'latitude': 46.057421,
                                      'longitude': 14.510265,
                                      'capacity': 26,
                                      'bikes': 26},
           'TRG MDB': {'latitude': 46.047565,
                       'longitude': 14.495687,
                       'capacity': 20,
                       'bikes': 9},
           'TRŽAŠKA C.-ILIRIJA': {'latitude': 46.044629,
                                  'longitude': 14.486699,
                                  'capacity': 20,
                                  'bikes': 5},
           'PREŠERNOV TRG-PETKOVŠKOVO NABREŽJE': {'latitude': 46.051367,
                                                  'longitude': 14.506542,
                                                  'capacity': 20,
                                                  'bikes': 17},
           'MERCATOR MARKET - CELOVŠKA C. 163': {'latitude': 46.073264,
                                                 'longitude': 14.485942,
                                                 'capacity': 20,
                                                 'bikes': 6},
           'SAVSKO NASELJE 2-LINHARTOVA CESTA': {'latitude': 46.064546,
                                                 'longitude': 14.518013,
                                                 'capacity': 20,
                                                 'bikes': 8},
           'BREG': {'latitude': 46.046498,
                    'longitude': 14.505148,
                    'capacity': 20,
                    'bikes': 5},
           'BTC CITY ATLANTIS': {'latitude': 46.063081,
                                 'longitude': 14.547851,
                                 'capacity': 20,
                                 'bikes': 14},
           'IKEA': {'latitude': 46.06488,
                    'longitude': 14.53833,
                    'capacity': 20,
                    'bikes': 5},
           'MIKLOŠIČEV PARK': {'latitude': 46.054168,
                               'longitude': 14.50706,
                               'capacity': 18,
                               'bikes': 4},
           'BARJANSKA C.-CENTER STAREJŠIH TRNOVO': {'latitude': 46.04081,
                                                    'longitude': 14.49951,
                                                    'capacity': 20,
                                                    'bikes': 5},
           'LEK - VEROVŠKOVA': {'latitude': 46.076856,
                                'longitude': 14.500222,
                                'capacity': 20,
                                'bikes': 0},
           'AMBROŽEV TRG': {'latitude': 46.049877,
                            'longitude': 14.516308,
                            'capacity': 18,
                            'bikes': 7},
           'VOJKOVA - GASILSKA BRIGADA': {'latitude': 46.068727,
                                          'longitude': 14.516858,
                                          'capacity': 20,
                                          'bikes': 7},
           'RAKOVNIK': {'latitude': 46.036284,
                        'longitude': 14.522948,
                        'capacity': 20,
                        'bikes': 19},
           'KOPALIŠČE ILIRIJA': {'latitude': 46.056404,
                                 'longitude': 14.500927,
                                 'capacity': 20,
                                 'bikes': 0},
           'PREGLOV TRG': {'latitude': 46.054554,
                           'longitude': 14.55908,
                           'capacity': 20,
                           'bikes': 15},
           'PLEČNIKOV STADION': {'latitude': 46.06942,
                                 'longitude': 14.51052,
                                 'capacity': 18,
                                 'bikes': 4}}
