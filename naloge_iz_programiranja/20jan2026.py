
import unittest
import random
import warnings
from itertools import pairwise
from collections import defaultdict
from operator import itemgetter

def postaje(povezave):
    mnozica_koncnih, mnozica_prehodnih, mnozica_krizisc = set(), set(), set()
    for postaja, povezane_postaje in povezave.items():
        st_razlicnih_povezav = set()
        for ime_povezane_postaje, cas_odhoda, cas_prihoda in povezane_postaje:
            st_razlicnih_povezav.add(ime_povezane_postaje)

        if len(st_razlicnih_povezav) == 1:
            mnozica_koncnih.add(postaja)
        elif len(st_razlicnih_povezav) == 2:
            mnozica_prehodnih.add(postaja)
        elif len(st_razlicnih_povezav) > 2:
            mnozica_krizisc.add(postaja)

    return mnozica_koncnih, mnozica_prehodnih, mnozica_krizisc

def naslednja_povezava(povezave, odkod, kam, cas):
    for ime_povezane, cas_odhoda, cas_prihoda in povezave[odkod]:
        if ime_povezane == kam and cas <= cas_odhoda:
            return cas_odhoda, cas_prihoda
    return None

def potovalni_cas(povezave, pot, zacetek):
    pot_cas = 0
    for p1, p2 in zip(pot, pot[1:]):
        podatki = naslednja_povezava(povezave, p1, p2, zacetek)
        if podatki:
            cas_odhoda, cas_prihoda = podatki[0], podatki[1]
            cakanje = cas_odhoda - zacetek
            pot_cas += abs(cas_odhoda - cas_prihoda) + cakanje
            zacetek = cas_prihoda
        else:
            return None
    return pot_cas


def vozni_red(povezave, linija, ime_dat):
    f = open(ime_dat, "wt", encoding="utf-8")

    for odkod, kam in pairwise(linija):
        casi = []
        for k, odhod, prihod in povezave[odkod]:
            if k == kam:
                casi.append(f"{odhod // 60:0>2}:{odhod % 60:0>2}")
        f.write(f'{odkod:>20}  {"  ".join(casi)}\n')

    casi = []
    for k, odhod, prihod in povezave[odkod]:
        if k == kam:
            casi.append(f"{prihod // 60:0>2}:{prihod % 60:0>2}")
    f.write(f'{kam:>20}  {"  ".join(casi)}\n')


def cas_prihoda(povezave, odkod, kam, cas, omejitev):
    if odkod == kam:
        return cas
    najkrajsi = None
    for vmesna, odhod, prihod in povezave[odkod]:
        if odhod >= cas and prihod <= omejitev:
            cp = cas_prihoda(povezave, vmesna, kam, prihod, omejitev)
            if cp is not None and (najkrajsi is None or cp < najkrajsi):
                najkrajsi = cp
                omejitev = najkrajsi
    return najkrajsi

class Potnik:
    def __init__(self, zacetna_postaja, trenunti_cas):
        self.zacetna_postaja = zacetna_postaja
        self.trenutni_cas = trenunti_cas
        self.trenutna_postaja = zacetna_postaja
        self.cakanje = 0

    def premik(self, kam):
        for ime_povezave, cas_odhoda, cas_prihoda in povezave[self.trenutna_postaja]:
            if ime_povezave == kam and self.trenutni_cas <= cas_odhoda:
                self.cakanje += abs(cas_odhoda - self.trenutni_cas)
                self.trenutna_postaja = kam
                self.trenutni_cas = cas_prihoda
                break

    def kje(self):
        return self.trenutna_postaja, self.trenutni_cas

    def izguba(self):
        return self.cakanje

class Test(unittest.TestCase):
    povezave42 = {
        'Ajdovščina': [('Prvačina', 561, 584), ('Prvačina', 786, 802), ('Prvačina', 1029, 1051)],
        'Bled': [('Bohinj', 404, 429), ('Jesenice', 461, 479), ('Bohinj', 507, 526), ('Jesenice', 557, 579),
                 ('Bohinj', 599, 614), ('Jesenice', 633, 651), ('Bohinj', 687, 710), ('Jesenice', 727, 751),
                 ('Bohinj', 782, 800), ('Jesenice', 805, 830), ('Bohinj', 871, 894), ('Jesenice', 898, 921),
                 ('Bohinj', 955, 975), ('Jesenice', 999, 1021), ('Bohinj', 1040, 1058), ('Jesenice', 1097, 1115),
                 ('Bohinj', 1135, 1158), ('Jesenice', 1180, 1196), ('Bohinj', 1236, 1258), ('Jesenice', 1276, 1291)],
        'Bohinj': [('Most na Soči Anhovo', 429, 445), ('Bled', 438, 461), ('Most na Soči Anhovo', 526, 551),
                   ('Bled', 537, 557), ('Most na Soči Anhovo', 614, 633), ('Bled', 617, 633), ('Bled', 709, 727),
                   ('Most na Soči Anhovo', 710, 726), ('Bled', 789, 805), ('Most na Soči Anhovo', 800, 817),
                   ('Bled', 882, 898), ('Most na Soči Anhovo', 894, 917), ('Bled', 974, 999),
                   ('Most na Soči Anhovo', 975, 994), ('Most na Soči Anhovo', 1058, 1082), ('Bled', 1075, 1097),
                   ('Most na Soči Anhovo', 1158, 1175), ('Bled', 1162, 1180), ('Bled', 1254, 1276),
                   ('Most na Soči Anhovo', 1258, 1281)],
        'Brežice': [('Krško', 380, 404), ('Krško', 437, 459), ('Dobova', 488, 505), ('Krško', 500, 518), ('Krško', 558, 579),
                    ('Dobova', 564, 583), ('Dobova', 609, 634), ('Krško', 611, 631), ('Krško', 672, 693), ('Dobova', 679, 695),
                    ('Krško', 730, 746), ('Dobova', 757, 782), ('Krško', 786, 808), ('Dobova', 808, 826), ('Krško', 851, 870),
                    ('Dobova', 874, 890), ('Krško', 902, 922), ('Dobova', 916, 937), ('Krško', 964, 989),
                    ('Dobova', 1002, 1023), ('Krško', 1027, 1043), ('Dobova', 1045, 1067), ('Krško', 1084, 1100),
                    ('Dobova', 1108, 1128), ('Krško', 1149, 1173), ('Dobova', 1170, 1194), ('Dobova', 1210, 1226),
                    ('Krško', 1214, 1233), ('Krško', 1279, 1304), ('Dobova', 1280, 1299), ('Dobova', 1334, 1349)],
        'Celje': [('Polzela', 389, 410), ('Šentjur', 403, 427), ('Šentjur', 465, 482), ('Polzela', 475, 492),
                  ('Laško', 496, 521), ('Šentjur', 533, 550), ('Laško', 560, 582), ('Polzela', 563, 587),
                  ('Šentjur', 593, 618), ('Laško', 629, 651), ('Polzela', 645, 660), ('Šentjur', 661, 686),
                  ('Laško', 690, 709), ('Šentjur', 706, 728), ('Polzela', 735, 751), ('Laško', 739, 758),
                  ('Šentjur', 762, 777), ('Laško', 782, 801), ('Polzela', 823, 848), ('Šentjur', 831, 852),
                  ('Laško', 844, 859), ('Šentjur', 887, 904), ('Laško', 898, 914), ('Polzela', 909, 927),
                  ('Šentjur', 941, 956), ('Laško', 958, 980), ('Polzela', 996, 1016), ('Šentjur', 1000, 1021),
                  ('Laško', 1025, 1046), ('Šentjur', 1058, 1078), ('Laško', 1067, 1092), ('Polzela', 1084, 1106),
                  ('Šentjur', 1122, 1142), ('Laško', 1155, 1173), ('Polzela', 1180, 1199), ('Šentjur', 1186, 1207),
                  ('Laško', 1200, 1221), ('Šentjur', 1236, 1261), ('Laško', 1269, 1284), ('Šentjur', 1286, 1306),
                  ('Laško', 1313, 1333), ('Laško', 1370, 1393)],
        'Divača': [('Sežana', 393, 416), ('Postojna', 399, 423), ('Prešnica', 415, 440), ('Pivka', 415, 438),
                   ('Prešnica', 420, 445), ('Postojna', 464, 488), ('Sežana', 473, 495), ('Prešnica', 483, 506),
                   ('Postojna', 514, 532), ('Prešnica', 538, 559), ('Prešnica', 542, 564), ('Pivka', 543, 561),
                   ('Sežana', 556, 579), ('Postojna', 585, 604), ('Prešnica', 603, 628), ('Postojna', 629, 651),
                   ('Sežana', 648, 665), ('Prešnica', 652, 676), ('Prešnica', 656, 678), ('Pivka', 660, 677),
                   ('Postojna', 700, 719), ('Prešnica', 729, 748), ('Sežana', 733, 755), ('Postojna', 752, 772),
                   ('Pivka', 774, 798), ('Prešnica', 777, 801), ('Prešnica', 789, 805), ('Postojna', 817, 842),
                   ('Sežana', 823, 842), ('Prešnica', 861, 882), ('Postojna', 883, 902), ('Pivka', 884, 903),
                   ('Prešnica', 898, 913), ('Sežana', 904, 926), ('Prešnica', 906, 923), ('Postojna', 928, 951),
                   ('Prešnica', 965, 989), ('Sežana', 994, 1013), ('Postojna', 998, 1016), ('Pivka', 1010, 1028),
                   ('Prešnica', 1015, 1037), ('Prešnica', 1040, 1056), ('Postojna', 1057, 1076), ('Sežana', 1088, 1107),
                   ('Prešnica', 1097, 1112), ('Postojna', 1112, 1131), ('Pivka', 1131, 1151), ('Prešnica', 1132, 1147),
                   ('Postojna', 1161, 1183), ('Prešnica', 1175, 1193), ('Sežana', 1175, 1192), ('Postojna', 1224, 1240),
                   ('Prešnica', 1224, 1244), ('Pivka', 1243, 1265), ('Prešnica', 1248, 1268), ('Prešnica', 1280, 1305),
                   ('Postojna', 1287, 1304)],
        'Dobova': [('Brežice', 362, 380), ('Brežice', 421, 437), ('Brežice', 477, 500), ('Brežice', 536, 558),
                   ('Brežice', 595, 611), ('Brežice', 652, 672), ('Brežice', 709, 730), ('Brežice', 766, 786),
                   ('Brežice', 826, 851), ('Brežice', 886, 902), ('Brežice', 944, 964), ('Brežice', 1007, 1027),
                   ('Brežice', 1066, 1084), ('Brežice', 1126, 1149), ('Brežice', 1189, 1214), ('Brežice', 1255, 1279)],
        'Domžale': [('Kamnik', 377, 402), ('Ljubljana', 381, 401), ('Kamnik', 439, 454), ('Ljubljana', 441, 460),
                    ('Ljubljana', 493, 515), ('Kamnik', 495, 511), ('Kamnik', 550, 568), ('Ljubljana', 550, 568),
                    ('Kamnik', 611, 632), ('Ljubljana', 612, 630), ('Kamnik', 676, 698), ('Ljubljana', 676, 700),
                    ('Ljubljana', 732, 747), ('Kamnik', 736, 755), ('Kamnik', 794, 813), ('Ljubljana', 799, 820),
                    ('Kamnik', 858, 878), ('Ljubljana', 858, 873), ('Kamnik', 916, 940), ('Ljubljana', 920, 942),
                    ('Ljubljana', 977, 1001), ('Kamnik', 980, 997), ('Ljubljana', 1033, 1051), ('Kamnik', 1036, 1060),
                    ('Ljubljana', 1095, 1120), ('Kamnik', 1101, 1119), ('Kamnik', 1150, 1172), ('Ljubljana', 1151, 1168),
                    ('Ljubljana', 1206, 1221), ('Kamnik', 1217, 1236), ('Ljubljana', 1255, 1277), ('Kamnik', 1269, 1288)],
        'Gorica': [('Prvačina', 383, 399), ('Most na Soči Anhovo', 399, 420), ('Prvačina', 461, 482),
                   ('Most na Soči Anhovo', 487, 512), ('Prvačina', 551, 569), ('Most na Soči Anhovo', 572, 595),
                   ('Prvačina', 638, 661), ('Most na Soči Anhovo', 662, 686), ('Prvačina', 729, 751),
                   ('Most na Soči Anhovo', 756, 774), ('Prvačina', 821, 837), ('Most na Soči Anhovo', 847, 862),
                   ('Prvačina', 914, 930), ('Most na Soči Anhovo', 937, 955), ('Prvačina', 995, 1020),
                   ('Most na Soči Anhovo', 1027, 1051), ('Prvačina', 1091, 1109), ('Most na Soči Anhovo', 1119, 1141),
                   ('Prvačina', 1170, 1191), ('Most na Soči Anhovo', 1212, 1233), ('Prvačina', 1251, 1266)],
        'Grobelno': [('Slovenska Bistrica', 448, 471), ('Šentjur', 458, 481), ('Šmarje pri Jelšah', 482, 507),
                     ('Slovenska Bistrica', 498, 521), ('Šentjur', 519, 543), ('Slovenska Bistrica', 568, 584),
                     ('Šentjur', 586, 610), ('Slovenska Bistrica', 634, 651), ('Šentjur', 646, 668),
                     ('Šmarje pri Jelšah', 656, 673), ('Šentjur', 698, 722), ('Slovenska Bistrica', 710, 730),
                     ('Šentjur', 749, 765), ('Slovenska Bistrica', 753, 772), ('Slovenska Bistrica', 797, 816),
                     ('Šentjur', 802, 824), ('Šmarje pri Jelšah', 841, 859), ('Šentjur', 863, 878),
                     ('Slovenska Bistrica', 874, 898), ('Slovenska Bistrica', 919, 941), ('Šentjur', 919, 941),
                     ('Slovenska Bistrica', 974, 996), ('Šentjur', 978, 1002), ('Šmarje pri Jelšah', 1022, 1045),
                     ('Šentjur', 1028, 1046), ('Slovenska Bistrica', 1041, 1066), ('Slovenska Bistrica', 1094, 1117),
                     ('Šentjur', 1108, 1131), ('Slovenska Bistrica', 1158, 1182), ('Šentjur', 1158, 1176),
                     ('Šmarje pri Jelšah', 1201, 1219), ('Šentjur', 1223, 1246), ('Slovenska Bistrica', 1224, 1248),
                     ('Šentjur', 1279, 1298), ('Slovenska Bistrica', 1284, 1300), ('Slovenska Bistrica', 1325, 1342),
                     ('Šentjur', 1335, 1350)],
        'Grosuplje': [('Ribnica', 358, 377), ('Ivančna Gorica', 403, 426), ('Ribnica', 420, 436), ('Ivančna Gorica', 459, 475),
                      ('Škofljica', 463, 487), ('Ribnica', 483, 502), ('Škofljica', 509, 525), ('Ivančna Gorica', 524, 548),
                      ('Ribnica', 536, 560), ('Ivančna Gorica', 581, 600), ('Škofljica', 582, 606), ('Ribnica', 592, 613),
                      ('Ivančna Gorica', 631, 654), ('Škofljica', 642, 661), ('Ribnica', 653, 677), ('Škofljica', 697, 717),
                      ('Ivančna Gorica', 702, 724), ('Ribnica', 712, 730), ('Škofljica', 754, 776),
                      ('Ivančna Gorica', 762, 778), ('Ribnica', 771, 796), ('Škofljica', 809, 828),
                      ('Ivančna Gorica', 810, 834), ('Ribnica', 828, 844), ('Škofljica', 870, 893),
                      ('Ivančna Gorica', 877, 901), ('Ribnica', 888, 909), ('Ivančna Gorica', 931, 952),
                      ('Škofljica', 941, 956), ('Ribnica', 945, 965), ('Škofljica', 989, 1011), ('Ivančna Gorica', 992, 1010),
                      ('Ribnica', 1002, 1023), ('Škofljica', 1045, 1068), ('Ivančna Gorica', 1052, 1069),
                      ('Ribnica', 1061, 1077), ('Škofljica', 1101, 1126), ('Ivančna Gorica', 1115, 1130),
                      ('Ribnica', 1125, 1147), ('Škofljica', 1175, 1193), ('Ivančna Gorica', 1179, 1203),
                      ('Ribnica', 1183, 1204), ('Škofljica', 1231, 1254), ('Ivančna Gorica', 1236, 1261),
                      ('Ribnica', 1242, 1261), ('Škofljica', 1287, 1306), ('Ivančna Gorica', 1307, 1326),
                      ('Škofljica', 1359, 1381)],
        'Hodoš': [('Murska Sobota', 419, 439), ('Murska Sobota', 526, 543), ('Murska Sobota', 642, 660),
                  ('Murska Sobota', 762, 785), ('Murska Sobota', 880, 897), ('Murska Sobota', 992, 1014),
                  ('Murska Sobota', 1117, 1133), ('Murska Sobota', 1228, 1248)],
        'Hoče': [('Pragersko', 396, 412), ('Pragersko', 468, 485), ('Maribor', 508, 527), ('Pragersko', 521, 546),
                 ('Maribor', 562, 585), ('Pragersko', 577, 597), ('Maribor', 620, 638), ('Pragersko', 642, 663),
                 ('Pragersko', 691, 714), ('Maribor', 698, 720), ('Pragersko', 747, 768), ('Maribor', 775, 792),
                 ('Pragersko', 809, 825), ('Maribor', 815, 830), ('Maribor', 857, 873), ('Pragersko', 868, 885),
                 ('Pragersko', 920, 938), ('Maribor', 936, 958), ('Maribor', 977, 993), ('Pragersko', 978, 997),
                 ('Maribor', 1041, 1064), ('Pragersko', 1045, 1068), ('Pragersko', 1099, 1114), ('Maribor', 1105, 1130),
                 ('Pragersko', 1154, 1177), ('Maribor', 1163, 1182), ('Pragersko', 1213, 1238), ('Maribor', 1224, 1244),
                 ('Pragersko', 1274, 1298), ('Maribor', 1283, 1306), ('Maribor', 1350, 1371), ('Maribor', 1380, 1402)],
        'Hrastnik': [('Zidani Most', 393, 412), ('Zidani Most', 464, 487), ('Litija', 475, 490), ('Zidani Most', 511, 533),
                     ('Litija', 548, 564), ('Zidani Most', 585, 601), ('Litija', 605, 624), ('Zidani Most', 643, 668),
                     ('Litija', 663, 685), ('Zidani Most', 702, 717), ('Litija', 705, 724), ('Zidani Most', 762, 787),
                     ('Litija', 781, 804), ('Zidani Most', 826, 842), ('Litija', 835, 853), ('Litija', 886, 907),
                     ('Zidani Most', 892, 917), ('Zidani Most', 951, 970), ('Litija', 954, 970), ('Zidani Most', 999, 1015),
                     ('Litija', 1001, 1024), ('Zidani Most', 1061, 1077), ('Litija', 1071, 1092), ('Zidani Most', 1113, 1133),
                     ('Litija', 1125, 1150), ('Litija', 1179, 1198), ('Zidani Most', 1186, 1204), ('Zidani Most', 1234, 1257),
                     ('Litija', 1270, 1285), ('Litija', 1303, 1323), ('Litija', 1383, 1398)],
        'Ilirska Bistrica': [('Pivka', 413, 430), ('Pivka', 539, 564), ('Pivka', 662, 682), ('Pivka', 786, 811),
                             ('Pivka', 896, 914), ('Pivka', 1017, 1039), ('Pivka', 1138, 1154), ('Pivka', 1250, 1268)],
        'Imeno': [('Podčetrtek', 485, 501), ('Podčetrtek', 658, 680), ('Podčetrtek', 827, 850), ('Podčetrtek', 1007, 1023),
                  ('Podčetrtek', 1179, 1195)],
        'Ivančna Gorica': [('Trebnje', 426, 446), ('Grosuplje', 447, 463), ('Trebnje', 475, 498), ('Grosuplje', 494, 509),
                           ('Trebnje', 548, 571), ('Grosuplje', 563, 582), ('Trebnje', 600, 615), ('Grosuplje', 620, 642),
                           ('Trebnje', 654, 673), ('Grosuplje', 676, 697), ('Trebnje', 724, 746), ('Grosuplje', 733, 754),
                           ('Trebnje', 778, 794), ('Grosuplje', 789, 809), ('Trebnje', 834, 853), ('Grosuplje', 845, 870),
                           ('Trebnje', 901, 925), ('Grosuplje', 919, 941), ('Trebnje', 952, 971), ('Grosuplje', 967, 989),
                           ('Trebnje', 1010, 1035), ('Grosuplje', 1030, 1045), ('Trebnje', 1069, 1084),
                           ('Grosuplje', 1085, 1101), ('Trebnje', 1130, 1148), ('Grosuplje', 1153, 1175),
                           ('Trebnje', 1203, 1228), ('Grosuplje', 1207, 1231), ('Trebnje', 1261, 1278),
                           ('Grosuplje', 1272, 1287), ('Trebnje', 1326, 1348), ('Grosuplje', 1342, 1359)],
        'Jesenice': [('Kranj', 357, 377), ('Bled', 389, 404), ('Kranj', 414, 439), ('Kranj', 469, 493), ('Bled', 484, 507),
                     ('Kranj', 526, 548), ('Bled', 577, 599), ('Kranj', 585, 610), ('Kranj', 642, 657), ('Bled', 670, 687),
                     ('Kranj', 696, 716), ('Bled', 758, 782), ('Kranj', 762, 786), ('Kranj', 824, 849), ('Bled', 854, 871),
                     ('Kranj', 887, 904), ('Bled', 939, 955), ('Kranj', 944, 962), ('Kranj', 1003, 1027), ('Bled', 1025, 1040),
                     ('Kranj', 1066, 1084), ('Bled', 1119, 1135), ('Kranj', 1120, 1136), ('Kranj', 1180, 1197),
                     ('Bled', 1211, 1236), ('Kranj', 1237, 1261)],
        'Kamnik': [('Domžale', 359, 381), ('Domžale', 417, 441), ('Domžale', 474, 493), ('Domžale', 531, 550),
                   ('Domžale', 596, 612), ('Domžale', 655, 676), ('Domžale', 713, 732), ('Domžale', 774, 799),
                   ('Domžale', 833, 858), ('Domžale', 896, 920), ('Domžale', 959, 977), ('Domžale', 1013, 1033),
                   ('Domžale', 1070, 1095), ('Domžale', 1126, 1151), ('Domžale', 1181, 1206), ('Domžale', 1236, 1255)],
        'Koper': [('Prešnica', 362, 383), ('Prešnica', 418, 439), ('Prešnica', 475, 495), ('Prešnica', 535, 560),
                  ('Prešnica', 598, 614), ('Prešnica', 659, 677), ('Prešnica', 718, 734), ('Prešnica', 774, 793),
                  ('Prešnica', 835, 860), ('Prešnica', 896, 912), ('Prešnica', 955, 974), ('Prešnica', 1012, 1035),
                  ('Prešnica', 1066, 1091), ('Prešnica', 1125, 1144), ('Prešnica', 1186, 1209), ('Prešnica', 1240, 1264)],
        'Kočevje': [('Ribnica', 361, 383), ('Ribnica', 417, 438), ('Ribnica', 476, 492), ('Ribnica', 541, 563),
                    ('Ribnica', 601, 626), ('Ribnica', 657, 677), ('Ribnica', 714, 736), ('Ribnica', 774, 794),
                    ('Ribnica', 830, 849), ('Ribnica', 895, 910), ('Ribnica', 956, 977), ('Ribnica', 1015, 1038),
                    ('Ribnica', 1073, 1095), ('Ribnica', 1128, 1143), ('Ribnica', 1187, 1205), ('Ribnica', 1249, 1274)],
        'Kranj': [('Škofja Loka', 377, 397), ('Jesenice', 396, 414), ('Škofja Loka', 439, 464), ('Jesenice', 451, 476),
                  ('Škofja Loka', 493, 518), ('Jesenice', 522, 537), ('Škofja Loka', 548, 569), ('Jesenice', 564, 582),
                  ('Škofja Loka', 610, 633), ('Jesenice', 634, 659), ('Škofja Loka', 657, 675), ('Jesenice', 701, 719),
                  ('Škofja Loka', 716, 737), ('Jesenice', 746, 767), ('Škofja Loka', 786, 806), ('Jesenice', 813, 830),
                  ('Škofja Loka', 849, 871), ('Jesenice', 867, 888), ('Škofja Loka', 904, 923), ('Jesenice', 935, 955),
                  ('Škofja Loka', 962, 985), ('Jesenice', 999, 1015), ('Škofja Loka', 1027, 1048), ('Jesenice', 1047, 1070),
                  ('Škofja Loka', 1084, 1101), ('Jesenice', 1112, 1130), ('Škofja Loka', 1136, 1153), ('Jesenice', 1163, 1188),
                  ('Škofja Loka', 1197, 1222), ('Jesenice', 1226, 1242), ('Škofja Loka', 1261, 1283),
                  ('Jesenice', 1294, 1316)],
        'Krško': [('Sevnica', 404, 424), ('Sevnica', 459, 481), ('Brežice', 470, 488), ('Sevnica', 518, 542),
                  ('Brežice', 542, 564), ('Sevnica', 579, 600), ('Brežice', 584, 609), ('Sevnica', 631, 655),
                  ('Brežice', 656, 679), ('Sevnica', 693, 717), ('Brežice', 736, 757), ('Sevnica', 746, 762),
                  ('Brežice', 784, 808), ('Sevnica', 808, 829), ('Brežice', 853, 874), ('Sevnica', 870, 890),
                  ('Brežice', 899, 916), ('Sevnica', 922, 939), ('Brežice', 985, 1002), ('Sevnica', 989, 1005),
                  ('Brežice', 1023, 1045), ('Sevnica', 1043, 1067), ('Brežice', 1083, 1108), ('Sevnica', 1100, 1120),
                  ('Brežice', 1145, 1170), ('Sevnica', 1173, 1197), ('Brežice', 1192, 1210), ('Sevnica', 1233, 1248),
                  ('Brežice', 1265, 1280), ('Sevnica', 1304, 1325), ('Brežice', 1309, 1334)],
        'Laško': [('Celje', 382, 403), ('Celje', 445, 465), ('Celje', 508, 533), ('Zidani Most', 521, 541),
                  ('Celje', 576, 593), ('Zidani Most', 582, 597), ('Celje', 636, 661), ('Zidani Most', 651, 669),
                  ('Celje', 684, 706), ('Zidani Most', 709, 730), ('Celje', 747, 762), ('Zidani Most', 758, 773),
                  ('Zidani Most', 801, 823), ('Celje', 808, 831), ('Zidani Most', 859, 880), ('Celje', 864, 887),
                  ('Zidani Most', 914, 939), ('Celje', 924, 941), ('Celje', 979, 1000), ('Zidani Most', 980, 1002),
                  ('Celje', 1042, 1058), ('Zidani Most', 1046, 1062), ('Zidani Most', 1092, 1116), ('Celje', 1105, 1122),
                  ('Celje', 1161, 1186), ('Zidani Most', 1173, 1190), ('Celje', 1211, 1236), ('Zidani Most', 1221, 1238),
                  ('Celje', 1271, 1286), ('Zidani Most', 1284, 1305), ('Zidani Most', 1333, 1349),
                  ('Zidani Most', 1393, 1413)],
        'Lipovci': [('Ljutomer', 464, 484), ('Murska Sobota', 468, 493), ('Ljutomer', 568, 585), ('Murska Sobota', 596, 611),
                    ('Ljutomer', 676, 694), ('Murska Sobota', 716, 732), ('Ljutomer', 809, 829), ('Murska Sobota', 839, 860),
                    ('Ljutomer', 921, 937), ('Murska Sobota', 944, 966), ('Ljutomer', 1037, 1058),
                    ('Murska Sobota', 1072, 1091), ('Ljutomer', 1150, 1170), ('Murska Sobota', 1195, 1213),
                    ('Ljutomer', 1265, 1288), ('Murska Sobota', 1301, 1318)],
        'Litija': [('Hrastnik', 377, 393), ('Hrastnik', 441, 464), ('Ljubljana', 490, 507), ('Hrastnik', 495, 511),
                   ('Ljubljana', 564, 586), ('Hrastnik', 565, 585), ('Hrastnik', 623, 643), ('Ljubljana', 624, 646),
                   ('Hrastnik', 680, 702), ('Ljubljana', 685, 701), ('Ljubljana', 724, 748), ('Hrastnik', 746, 762),
                   ('Hrastnik', 804, 826), ('Ljubljana', 804, 828), ('Ljubljana', 853, 874), ('Hrastnik', 872, 892),
                   ('Ljubljana', 907, 927), ('Hrastnik', 930, 951), ('Ljubljana', 970, 986), ('Hrastnik', 979, 999),
                   ('Ljubljana', 1024, 1047), ('Hrastnik', 1039, 1061), ('Ljubljana', 1092, 1107), ('Hrastnik', 1098, 1113),
                   ('Ljubljana', 1150, 1172), ('Hrastnik', 1168, 1186), ('Ljubljana', 1198, 1222), ('Hrastnik', 1217, 1234),
                   ('Ljubljana', 1285, 1309), ('Ljubljana', 1323, 1343), ('Ljubljana', 1398, 1414)],
        'Ljubljana': [('Domžale', 357, 377), ('Škofja Loka', 359, 378), ('Litija', 360, 377), ('Logatec', 362, 377),
                      ('Škofljica', 362, 382), ('Domžale', 416, 439), ('Škofja Loka', 418, 435), ('Škofljica', 421, 439),
                      ('Litija', 421, 441), ('Logatec', 422, 447), ('Domžale', 471, 495), ('Litija', 475, 495),
                      ('Škofja Loka', 477, 501), ('Škofljica', 483, 505), ('Logatec', 486, 504), ('Domžale', 531, 550),
                      ('Škofja Loka', 533, 548), ('Litija', 542, 565), ('Škofljica', 544, 564), ('Logatec', 545, 562),
                      ('Škofja Loka', 593, 616), ('Domžale', 595, 611), ('Škofljica', 601, 616), ('Litija', 601, 623),
                      ('Logatec', 604, 620), ('Škofja Loka', 657, 680), ('Domžale', 660, 676), ('Škofljica', 661, 680),
                      ('Litija', 662, 680), ('Logatec', 669, 687), ('Škofja Loka', 714, 729), ('Domžale', 719, 736),
                      ('Škofljica', 721, 740), ('Litija', 721, 746), ('Logatec', 729, 750), ('Škofja Loka', 774, 794),
                      ('Škofljica', 776, 793), ('Domžale', 779, 794), ('Litija', 785, 804), ('Logatec', 793, 813),
                      ('Škofljica', 833, 856), ('Škofja Loka', 835, 851), ('Domžale', 838, 858), ('Litija', 850, 872),
                      ('Logatec', 856, 871), ('Škofljica', 888, 907), ('Domžale', 895, 916), ('Škofja Loka', 899, 915),
                      ('Litija', 906, 930), ('Logatec', 915, 934), ('Škofljica', 952, 976), ('Škofja Loka', 954, 976),
                      ('Domžale', 955, 980), ('Litija', 961, 979), ('Logatec', 972, 993), ('Škofja Loka', 1010, 1031),
                      ('Škofljica', 1013, 1036), ('Domžale', 1015, 1036), ('Litija', 1023, 1039), ('Logatec', 1036, 1060),
                      ('Škofja Loka', 1068, 1088), ('Škofljica', 1074, 1096), ('Domžale', 1076, 1101), ('Litija', 1083, 1098),
                      ('Logatec', 1102, 1125), ('Škofja Loka', 1132, 1148), ('Domžale', 1132, 1150), ('Škofljica', 1135, 1154),
                      ('Litija', 1144, 1168), ('Logatec', 1162, 1183), ('Škofja Loka', 1192, 1208), ('Domžale', 1192, 1217),
                      ('Škofljica', 1195, 1218), ('Litija', 1200, 1217), ('Logatec', 1219, 1238), ('Domžale', 1247, 1269),
                      ('Škofja Loka', 1254, 1275), ('Škofljica', 1259, 1283)],
        'Ljutomer': [('Lipovci', 450, 468), ('Ptuj', 484, 500), ('Lipovci', 572, 596), ('Ptuj', 585, 605),
                     ('Lipovci', 694, 716), ('Ptuj', 694, 711), ('Lipovci', 819, 839), ('Ptuj', 829, 851),
                     ('Lipovci', 927, 944), ('Ptuj', 937, 953), ('Lipovci', 1056, 1072), ('Ptuj', 1058, 1079),
                     ('Ptuj', 1170, 1195), ('Lipovci', 1173, 1195), ('Lipovci', 1279, 1301), ('Ptuj', 1288, 1313)],
        'Logatec': [('Postojna', 377, 397), ('Ljubljana', 441, 465), ('Postojna', 447, 463), ('Postojna', 504, 521),
                    ('Ljubljana', 512, 535), ('Ljubljana', 557, 577), ('Postojna', 562, 582), ('Postojna', 620, 641),
                    ('Ljubljana', 626, 646), ('Ljubljana', 675, 699), ('Postojna', 687, 709), ('Ljubljana', 736, 756),
                    ('Postojna', 750, 770), ('Ljubljana', 791, 808), ('Postojna', 813, 838), ('Ljubljana', 865, 880),
                    ('Postojna', 871, 887), ('Ljubljana', 927, 943), ('Postojna', 934, 949), ('Ljubljana', 968, 987),
                    ('Postojna', 993, 1017), ('Ljubljana', 1036, 1054), ('Postojna', 1060, 1078), ('Ljubljana', 1091, 1107),
                    ('Postojna', 1125, 1150), ('Ljubljana', 1146, 1161), ('Postojna', 1183, 1199), ('Ljubljana', 1206, 1227),
                    ('Postojna', 1238, 1261), ('Ljubljana', 1256, 1273), ('Ljubljana', 1325, 1342)],
        'Maribor': [('Hoče', 377, 396), ('Ruše', 426, 447), ('Hoče', 447, 468), ('Hoče', 501, 521), ('Šentilj', 527, 547),
                    ('Hoče', 559, 577), ('Ruše', 560, 575), ('Šentilj', 585, 608), ('Hoče', 619, 642), ('Šentilj', 638, 655),
                    ('Ruše', 674, 691), ('Hoče', 675, 691), ('Šentilj', 720, 744), ('Hoče', 730, 747), ('Hoče', 788, 809),
                    ('Šentilj', 792, 814), ('Ruše', 793, 811), ('Šentilj', 830, 850), ('Hoče', 851, 868),
                    ('Šentilj', 873, 897), ('Hoče', 901, 920), ('Ruše', 919, 938), ('Šentilj', 958, 982), ('Hoče', 960, 978),
                    ('Šentilj', 993, 1016), ('Hoče', 1021, 1045), ('Ruše', 1036, 1055), ('Šentilj', 1064, 1088),
                    ('Hoče', 1078, 1099), ('Šentilj', 1130, 1155), ('Hoče', 1138, 1154), ('Ruše', 1150, 1167),
                    ('Šentilj', 1182, 1201), ('Hoče', 1198, 1213), ('Šentilj', 1244, 1263), ('Hoče', 1258, 1274),
                    ('Šentilj', 1306, 1327), ('Šentilj', 1371, 1394), ('Šentilj', 1402, 1420)],
        'Metlika': [('Črnomelj', 357, 380), ('Črnomelj', 410, 431), ('Črnomelj', 475, 499), ('Črnomelj', 533, 550),
                    ('Črnomelj', 596, 618), ('Črnomelj', 655, 680), ('Črnomelj', 713, 736), ('Črnomelj', 770, 786),
                    ('Črnomelj', 828, 848), ('Črnomelj', 889, 908), ('Črnomelj', 953, 971), ('Črnomelj', 1013, 1029),
                    ('Črnomelj', 1068, 1091), ('Črnomelj', 1128, 1151), ('Črnomelj', 1189, 1210), ('Črnomelj', 1247, 1271)],
        'Mokronog': [('Sevnica', 443, 464), ('Trebnje', 451, 467), ('Sevnica', 552, 570), ('Trebnje', 578, 600),
                     ('Sevnica', 679, 700), ('Trebnje', 685, 702), ('Sevnica', 791, 811), ('Trebnje', 799, 815),
                     ('Sevnica', 928, 949), ('Trebnje', 928, 947), ('Sevnica', 1044, 1061), ('Trebnje', 1046, 1062),
                     ('Sevnica', 1166, 1181), ('Trebnje', 1168, 1193)],
        'Most na Soči Anhovo': [('Bohinj', 420, 438), ('Gorica', 445, 470), ('Bohinj', 512, 537), ('Gorica', 551, 571),
                                ('Bohinj', 595, 617), ('Gorica', 633, 656), ('Bohinj', 686, 709), ('Gorica', 726, 751),
                                ('Bohinj', 774, 789), ('Gorica', 817, 837), ('Bohinj', 862, 882), ('Gorica', 917, 932),
                                ('Bohinj', 955, 974), ('Gorica', 994, 1012), ('Bohinj', 1051, 1075), ('Gorica', 1082, 1098),
                                ('Bohinj', 1141, 1162), ('Gorica', 1175, 1192), ('Bohinj', 1233, 1254),
                                ('Gorica', 1281, 1298)],
        'Murska Sobota': [('Lipovci', 439, 464), ('Hodoš', 493, 513), ('Lipovci', 543, 568), ('Hodoš', 611, 635),
                          ('Lipovci', 660, 676), ('Hodoš', 732, 756), ('Lipovci', 785, 809), ('Hodoš', 860, 880),
                          ('Lipovci', 897, 921), ('Hodoš', 966, 989), ('Lipovci', 1014, 1037), ('Hodoš', 1091, 1110),
                          ('Lipovci', 1133, 1150), ('Hodoš', 1213, 1229), ('Lipovci', 1248, 1265), ('Hodoš', 1318, 1340)],
        'Novo Mesto': [('Trebnje', 403, 425), ('Trebnje', 451, 475), ('Črnomelj', 466, 488), ('Črnomelj', 515, 533),
                       ('Trebnje', 523, 538), ('Trebnje', 572, 595), ('Črnomelj', 595, 614), ('Trebnje', 634, 656),
                       ('Črnomelj', 638, 655), ('Črnomelj', 690, 715), ('Trebnje', 696, 713), ('Trebnje', 751, 773),
                       ('Črnomelj', 766, 783), ('Trebnje', 807, 830), ('Črnomelj', 815, 837), ('Črnomelj', 869, 887),
                       ('Trebnje', 872, 894), ('Trebnje', 931, 948), ('Črnomelj', 949, 967), ('Trebnje', 988, 1007),
                       ('Črnomelj', 995, 1019), ('Trebnje', 1047, 1063), ('Črnomelj', 1053, 1072), ('Črnomelj', 1105, 1127),
                       ('Trebnje', 1110, 1131), ('Črnomelj', 1167, 1186), ('Trebnje', 1168, 1189), ('Trebnje', 1230, 1253),
                       ('Črnomelj', 1246, 1267), ('Trebnje', 1295, 1320), ('Črnomelj', 1297, 1314), ('Črnomelj', 1364, 1386)],
        'Opčine': [('Sežana', 390, 408), ('Sežana', 486, 507), ('Sežana', 573, 588), ('Sežana', 667, 688),
                   ('Sežana', 761, 776), ('Sežana', 847, 868), ('Sežana', 941, 962), ('Sežana', 1031, 1054),
                   ('Sežana', 1123, 1145), ('Sežana', 1203, 1222)],
        'Pivka': [('Divača', 430, 455), ('Ilirska Bistrica', 438, 455), ('Ilirska Bistrica', 561, 582), ('Divača', 564, 588),
                  ('Ilirska Bistrica', 677, 701), ('Divača', 682, 698), ('Ilirska Bistrica', 798, 817), ('Divača', 811, 830),
                  ('Ilirska Bistrica', 903, 922), ('Divača', 914, 932), ('Ilirska Bistrica', 1028, 1049),
                  ('Divača', 1039, 1063), ('Ilirska Bistrica', 1151, 1173), ('Divača', 1154, 1176),
                  ('Ilirska Bistrica', 1265, 1287), ('Divača', 1268, 1289)],
        'Podčetrtek': [('Stranje', 501, 521), ('Imeno', 551, 576), ('Stranje', 680, 701), ('Imeno', 706, 728),
                       ('Stranje', 850, 869), ('Imeno', 894, 913), ('Stranje', 1023, 1044), ('Imeno', 1089, 1111),
                       ('Stranje', 1195, 1215), ('Imeno', 1258, 1273)],
        'Polzela': [('Šoštanj', 410, 432), ('Celje', 426, 445), ('Šoštanj', 492, 512), ('Celje', 528, 548),
                    ('Šoštanj', 587, 611), ('Celje', 608, 630), ('Šoštanj', 660, 677), ('Celje', 710, 728),
                    ('Šoštanj', 751, 770), ('Celje', 799, 824), ('Šoštanj', 848, 869), ('Celje', 879, 894),
                    ('Šoštanj', 927, 950), ('Celje', 969, 989), ('Šoštanj', 1016, 1037), ('Celje', 1061, 1080),
                    ('Šoštanj', 1106, 1129), ('Celje', 1139, 1154), ('Šoštanj', 1199, 1214), ('Celje', 1240, 1260)],
        'Postojna': [('Divača', 397, 415), ('Logatec', 423, 441), ('Divača', 463, 483), ('Logatec', 488, 512),
                     ('Divača', 521, 538), ('Logatec', 532, 557), ('Divača', 582, 603), ('Logatec', 604, 626),
                     ('Divača', 641, 656), ('Logatec', 651, 675), ('Divača', 709, 729), ('Logatec', 719, 736),
                     ('Divača', 770, 789), ('Logatec', 772, 791), ('Divača', 838, 861), ('Logatec', 842, 865),
                     ('Divača', 887, 906), ('Logatec', 902, 927), ('Divača', 949, 965), ('Logatec', 951, 968),
                     ('Logatec', 1016, 1036), ('Divača', 1017, 1040), ('Logatec', 1076, 1091), ('Divača', 1078, 1097),
                     ('Logatec', 1131, 1146), ('Divača', 1150, 1175), ('Logatec', 1183, 1206), ('Divača', 1199, 1224),
                     ('Logatec', 1240, 1256), ('Divača', 1261, 1280), ('Logatec', 1304, 1325)],
        'Pragersko': [('Slovenska Bistrica', 412, 435), ('Ptuj', 417, 434), ('Slovenska Bistrica', 485, 502),
                      ('Hoče', 487, 508), ('Ptuj', 531, 551), ('Hoče', 546, 562), ('Slovenska Bistrica', 546, 564),
                      ('Slovenska Bistrica', 597, 622), ('Hoče', 601, 620), ('Ptuj', 654, 674),
                      ('Slovenska Bistrica', 663, 680), ('Hoče', 676, 698), ('Slovenska Bistrica', 714, 730),
                      ('Hoče', 755, 775), ('Slovenska Bistrica', 768, 784), ('Ptuj', 779, 796), ('Hoče', 791, 815),
                      ('Slovenska Bistrica', 825, 845), ('Hoče', 832, 857), ('Slovenska Bistrica', 885, 900),
                      ('Ptuj', 896, 912), ('Hoče', 921, 936), ('Slovenska Bistrica', 938, 955), ('Hoče', 957, 977),
                      ('Slovenska Bistrica', 997, 1013), ('Ptuj', 1012, 1033), ('Hoče', 1018, 1041),
                      ('Slovenska Bistrica', 1068, 1083), ('Hoče', 1090, 1105), ('Slovenska Bistrica', 1114, 1138),
                      ('Ptuj', 1130, 1154), ('Hoče', 1142, 1163), ('Slovenska Bistrica', 1177, 1200), ('Hoče', 1207, 1224),
                      ('Slovenska Bistrica', 1238, 1259), ('Ptuj', 1246, 1263), ('Hoče', 1264, 1283),
                      ('Slovenska Bistrica', 1298, 1318), ('Hoče', 1325, 1350), ('Hoče', 1360, 1380)],
        'Prešnica': [('Divača', 383, 399), ('Divača', 439, 464), ('Koper', 440, 458), ('Divača', 441, 460),
                     ('Rakitovec', 445, 470), ('Divača', 495, 514), ('Koper', 506, 527), ('Divača', 550, 572),
                     ('Koper', 559, 574), ('Divača', 560, 585), ('Rakitovec', 564, 581), ('Divača', 614, 629),
                     ('Koper', 628, 646), ('Rakitovec', 676, 699), ('Divača', 677, 700), ('Koper', 678, 696),
                     ('Divača', 681, 699), ('Divača', 734, 752), ('Koper', 748, 766), ('Divača', 793, 817),
                     ('Rakitovec', 801, 826), ('Koper', 805, 824), ('Divača', 806, 822), ('Divača', 860, 883),
                     ('Koper', 882, 907), ('Divača', 912, 928), ('Rakitovec', 913, 929), ('Divača', 917, 935),
                     ('Koper', 923, 947), ('Divača', 974, 998), ('Koper', 989, 1010), ('Divača', 1031, 1046),
                     ('Divača', 1035, 1057), ('Rakitovec', 1037, 1054), ('Koper', 1056, 1077), ('Divača', 1091, 1112),
                     ('Koper', 1112, 1133), ('Divača', 1144, 1161), ('Rakitovec', 1147, 1166), ('Divača', 1151, 1176),
                     ('Koper', 1193, 1213), ('Divača', 1209, 1224), ('Koper', 1244, 1268), ('Divača', 1261, 1285),
                     ('Divača', 1264, 1287), ('Rakitovec', 1268, 1288), ('Koper', 1305, 1326)],
        'Prvačina': [('Sežana', 399, 414), ('Gorica', 399, 421), ('Sežana', 482, 502), ('Gorica', 498, 519),
                     ('Ajdovščina', 531, 556), ('Sežana', 569, 587), ('Gorica', 589, 614), ('Sežana', 661, 683),
                     ('Gorica', 671, 688), ('Sežana', 751, 769), ('Gorica', 755, 779), ('Ajdovščina', 771, 786),
                     ('Sežana', 837, 859), ('Gorica', 855, 870), ('Sežana', 930, 945), ('Gorica', 945, 967),
                     ('Sežana', 1020, 1043), ('Ajdovščina', 1029, 1045), ('Gorica', 1032, 1055), ('Sežana', 1109, 1126),
                     ('Gorica', 1121, 1138), ('Sežana', 1191, 1213), ('Gorica', 1220, 1244), ('Ajdovščina', 1254, 1275),
                     ('Sežana', 1266, 1283)],
        'Ptuj': [('Ljutomer', 434, 450), ('Pragersko', 500, 523), ('Ljutomer', 551, 572), ('Pragersko', 605, 628),
                 ('Ljutomer', 674, 694), ('Pragersko', 711, 729), ('Ljutomer', 796, 819), ('Pragersko', 851, 874),
                 ('Ljutomer', 912, 927), ('Pragersko', 953, 972), ('Ljutomer', 1033, 1056), ('Pragersko', 1079, 1103),
                 ('Ljutomer', 1154, 1173), ('Pragersko', 1195, 1211), ('Ljutomer', 1263, 1279), ('Pragersko', 1313, 1337)],
        'Radeče': [('Sevnica', 432, 453), ('Zidani Most', 439, 456), ('Zidani Most', 501, 524), ('Sevnica', 506, 523),
                   ('Sevnica', 549, 566), ('Zidani Most', 557, 582), ('Sevnica', 622, 637), ('Zidani Most', 625, 641),
                   ('Zidani Most', 672, 688), ('Sevnica', 693, 712), ('Zidani Most', 740, 759), ('Sevnica', 741, 764),
                   ('Zidani Most', 787, 812), ('Sevnica', 809, 828), ('Zidani Most', 850, 866), ('Sevnica', 858, 876),
                   ('Zidani Most', 907, 932), ('Sevnica', 940, 961), ('Zidani Most', 962, 977), ('Sevnica', 985, 1005),
                   ('Zidani Most', 1026, 1046), ('Sevnica', 1040, 1060), ('Zidani Most', 1090, 1108), ('Sevnica', 1102, 1120),
                   ('Zidani Most', 1143, 1163), ('Sevnica', 1151, 1168), ('Zidani Most', 1222, 1247), ('Sevnica', 1224, 1241),
                   ('Zidani Most', 1265, 1284), ('Sevnica', 1276, 1293), ('Zidani Most', 1341, 1358)],
        'Rakitovec': [('Prešnica', 420, 441), ('Prešnica', 534, 550), ('Prešnica', 661, 681), ('Prešnica', 781, 806),
                      ('Prešnica', 902, 917), ('Prešnica', 1013, 1031), ('Prešnica', 1129, 1151), ('Prešnica', 1245, 1261)],
        'Ravne na Koroškem': [('Ruše', 417, 440), ('Ruše', 544, 561), ('Ruše', 667, 692), ('Ruše', 785, 809),
                              ('Ruše', 909, 924), ('Ruše', 1022, 1037), ('Ruše', 1142, 1160), ('Ruše', 1257, 1278)],
        'Ribnica': [('Kočevje', 377, 397), ('Grosuplje', 383, 405), ('Kočevje', 436, 453), ('Grosuplje', 438, 462),
                    ('Grosuplje', 492, 511), ('Kočevje', 502, 518), ('Kočevje', 560, 585), ('Grosuplje', 563, 581),
                    ('Kočevje', 613, 634), ('Grosuplje', 626, 647), ('Kočevje', 677, 702), ('Grosuplje', 677, 692),
                    ('Kočevje', 730, 746), ('Grosuplje', 736, 754), ('Grosuplje', 794, 813), ('Kočevje', 796, 820),
                    ('Kočevje', 844, 868), ('Grosuplje', 849, 872), ('Kočevje', 909, 934), ('Grosuplje', 910, 933),
                    ('Kočevje', 965, 981), ('Grosuplje', 977, 999), ('Kočevje', 1023, 1045), ('Grosuplje', 1038, 1056),
                    ('Kočevje', 1077, 1098), ('Grosuplje', 1095, 1117), ('Grosuplje', 1143, 1159), ('Kočevje', 1147, 1164),
                    ('Kočevje', 1204, 1221), ('Grosuplje', 1205, 1224), ('Kočevje', 1261, 1285), ('Grosuplje', 1274, 1298)],
        'Rogatec': [('Stranje', 501, 517), ('Stranje', 678, 703), ('Stranje', 852, 877), ('Stranje', 1025, 1042),
                    ('Stranje', 1209, 1233)],
        'Ruše': [('Maribor', 440, 465), ('Ravne na Koroškem', 447, 470), ('Maribor', 561, 585),
                 ('Ravne na Koroškem', 575, 591), ('Ravne na Koroškem', 691, 711), ('Maribor', 692, 716),
                 ('Maribor', 809, 829), ('Ravne na Koroškem', 811, 831), ('Maribor', 924, 940),
                 ('Ravne na Koroškem', 938, 954), ('Maribor', 1037, 1062), ('Ravne na Koroškem', 1055, 1073),
                 ('Maribor', 1160, 1184), ('Ravne na Koroškem', 1167, 1192), ('Maribor', 1278, 1302)],
        'Sevnica': [('Radeče', 424, 439), ('Mokronog', 431, 451), ('Krško', 453, 470), ('Radeče', 481, 501),
                    ('Krško', 523, 542), ('Radeče', 542, 557), ('Mokronog', 555, 578), ('Krško', 566, 584),
                    ('Radeče', 600, 625), ('Krško', 637, 656), ('Radeče', 655, 672), ('Mokronog', 670, 685),
                    ('Krško', 712, 736), ('Radeče', 717, 740), ('Radeče', 762, 787), ('Krško', 764, 784),
                    ('Mokronog', 782, 799), ('Krško', 828, 853), ('Radeče', 829, 850), ('Krško', 876, 899),
                    ('Radeče', 890, 907), ('Mokronog', 906, 928), ('Radeče', 939, 962), ('Krško', 961, 985),
                    ('Krško', 1005, 1023), ('Radeče', 1005, 1026), ('Mokronog', 1021, 1046), ('Krško', 1060, 1083),
                    ('Radeče', 1067, 1090), ('Krško', 1120, 1145), ('Radeče', 1120, 1143), ('Mokronog', 1148, 1168),
                    ('Krško', 1168, 1192), ('Radeče', 1197, 1222), ('Krško', 1241, 1265), ('Radeče', 1248, 1265),
                    ('Krško', 1293, 1309), ('Radeče', 1325, 1341)],
        'Sežana': [('Prvačina', 380, 399), ('Divača', 408, 424), ('Opčine', 416, 439), ('Prvačina', 479, 498),
                   ('Opčine', 495, 519), ('Divača', 507, 528), ('Prvačina', 566, 589), ('Opčine', 579, 600),
                   ('Divača', 588, 606), ('Prvačina', 649, 671), ('Opčine', 665, 687), ('Divača', 688, 709),
                   ('Prvačina', 740, 755), ('Opčine', 755, 774), ('Divača', 776, 800), ('Prvačina', 832, 855),
                   ('Opčine', 842, 865), ('Divača', 868, 890), ('Prvačina', 921, 945), ('Opčine', 926, 951),
                   ('Divača', 962, 983), ('Prvačina', 1009, 1032), ('Opčine', 1013, 1031), ('Divača', 1054, 1077),
                   ('Prvačina', 1105, 1121), ('Opčine', 1107, 1127), ('Divača', 1145, 1163), ('Opčine', 1192, 1209),
                   ('Prvačina', 1204, 1220), ('Divača', 1222, 1243)],
        'Slovenska Bistrica': [('Grobelno', 435, 458), ('Pragersko', 471, 487), ('Grobelno', 502, 519),
                               ('Pragersko', 521, 546), ('Grobelno', 564, 586), ('Pragersko', 584, 601),
                               ('Grobelno', 622, 646), ('Pragersko', 651, 676), ('Grobelno', 680, 698),
                               ('Pragersko', 730, 755), ('Grobelno', 730, 749), ('Pragersko', 772, 791),
                               ('Grobelno', 784, 802), ('Pragersko', 816, 832), ('Grobelno', 845, 863),
                               ('Pragersko', 898, 921), ('Grobelno', 900, 919), ('Pragersko', 941, 957),
                               ('Grobelno', 955, 978), ('Pragersko', 996, 1018), ('Grobelno', 1013, 1028),
                               ('Pragersko', 1066, 1090), ('Grobelno', 1083, 1108), ('Pragersko', 1117, 1142),
                               ('Grobelno', 1138, 1158), ('Pragersko', 1182, 1207), ('Grobelno', 1200, 1223),
                               ('Pragersko', 1248, 1264), ('Grobelno', 1259, 1279), ('Pragersko', 1300, 1325),
                               ('Grobelno', 1318, 1335), ('Pragersko', 1342, 1360)],
        'Stranje': [('Rogatec', 475, 496), ('Šmarje pri Jelšah', 521, 542), ('Podčetrtek', 529, 551), ('Rogatec', 666, 683),
                    ('Podčetrtek', 690, 706), ('Šmarje pri Jelšah', 701, 721), ('Rogatec', 842, 857),
                    ('Šmarje pri Jelšah', 869, 885), ('Podčetrtek', 874, 894), ('Rogatec', 1014, 1034),
                    ('Šmarje pri Jelšah', 1044, 1068), ('Podčetrtek', 1066, 1089), ('Rogatec', 1186, 1211),
                    ('Šmarje pri Jelšah', 1215, 1240), ('Podčetrtek', 1238, 1258)],
        'Trebnje': [('Mokronog', 420, 443), ('Ivančna Gorica', 425, 447), ('Novo Mesto', 446, 466),
                    ('Ivančna Gorica', 475, 494), ('Novo Mesto', 498, 515), ('Mokronog', 534, 552),
                    ('Ivančna Gorica', 538, 563), ('Novo Mesto', 571, 595), ('Ivančna Gorica', 595, 620),
                    ('Novo Mesto', 615, 638), ('Mokronog', 655, 679), ('Ivančna Gorica', 656, 676), ('Novo Mesto', 673, 690),
                    ('Ivančna Gorica', 713, 733), ('Novo Mesto', 746, 766), ('Ivančna Gorica', 773, 789),
                    ('Mokronog', 776, 791), ('Novo Mesto', 794, 815), ('Ivančna Gorica', 830, 845), ('Novo Mesto', 853, 869),
                    ('Ivančna Gorica', 894, 919), ('Mokronog', 906, 928), ('Novo Mesto', 925, 949),
                    ('Ivančna Gorica', 948, 967), ('Novo Mesto', 971, 995), ('Ivančna Gorica', 1007, 1030),
                    ('Mokronog', 1019, 1044), ('Novo Mesto', 1035, 1053), ('Ivančna Gorica', 1063, 1085),
                    ('Novo Mesto', 1084, 1105), ('Ivančna Gorica', 1131, 1153), ('Mokronog', 1144, 1166),
                    ('Novo Mesto', 1148, 1167), ('Ivančna Gorica', 1189, 1207), ('Novo Mesto', 1228, 1246),
                    ('Ivančna Gorica', 1253, 1272), ('Novo Mesto', 1278, 1297), ('Ivančna Gorica', 1320, 1342),
                    ('Novo Mesto', 1348, 1364)],
        'Velenje': [('Šoštanj', 393, 408), ('Šoštanj', 490, 509), ('Šoštanj', 577, 593), ('Šoštanj', 666, 687),
                    ('Šoštanj', 753, 776), ('Šoštanj', 843, 858), ('Šoštanj', 931, 953), ('Šoštanj', 1015, 1040),
                    ('Šoštanj', 1102, 1118), ('Šoštanj', 1194, 1218)],
        'Zidani Most': [('Laško', 364, 382), ('Radeče', 412, 432), ('Laško', 427, 445), ('Hrastnik', 456, 475),
                        ('Radeče', 487, 506), ('Laško', 488, 508), ('Hrastnik', 524, 548), ('Radeče', 533, 549),
                        ('Laško', 552, 576), ('Hrastnik', 582, 605), ('Radeče', 601, 622), ('Laško', 612, 636),
                        ('Hrastnik', 641, 663), ('Radeče', 668, 693), ('Laško', 668, 684), ('Hrastnik', 688, 705),
                        ('Radeče', 717, 741), ('Laško', 725, 747), ('Hrastnik', 759, 781), ('Laško', 784, 808),
                        ('Radeče', 787, 809), ('Hrastnik', 812, 835), ('Radeče', 842, 858), ('Laško', 842, 864),
                        ('Hrastnik', 866, 886), ('Laško', 899, 924), ('Radeče', 917, 940), ('Hrastnik', 932, 954),
                        ('Laško', 960, 979), ('Radeče', 970, 985), ('Hrastnik', 977, 1001), ('Radeče', 1015, 1040),
                        ('Laško', 1022, 1042), ('Hrastnik', 1046, 1071), ('Radeče', 1077, 1102), ('Laško', 1081, 1105),
                        ('Hrastnik', 1108, 1125), ('Radeče', 1133, 1151), ('Laško', 1136, 1161), ('Hrastnik', 1163, 1179),
                        ('Laško', 1194, 1211), ('Radeče', 1204, 1224), ('Hrastnik', 1247, 1270), ('Laško', 1251, 1271),
                        ('Radeče', 1257, 1276), ('Hrastnik', 1284, 1303), ('Hrastnik', 1358, 1383)],
        'Črnomelj': [('Novo Mesto', 380, 403), ('Novo Mesto', 431, 451), ('Metlika', 488, 507), ('Novo Mesto', 499, 523),
                     ('Metlika', 533, 551), ('Novo Mesto', 550, 572), ('Metlika', 614, 630), ('Novo Mesto', 618, 634),
                     ('Metlika', 655, 674), ('Novo Mesto', 680, 696), ('Metlika', 715, 737), ('Novo Mesto', 736, 751),
                     ('Metlika', 783, 798), ('Novo Mesto', 786, 807), ('Metlika', 837, 853), ('Novo Mesto', 848, 872),
                     ('Metlika', 887, 903), ('Novo Mesto', 908, 931), ('Metlika', 967, 990), ('Novo Mesto', 971, 988),
                     ('Metlika', 1019, 1034), ('Novo Mesto', 1029, 1047), ('Metlika', 1072, 1097), ('Novo Mesto', 1091, 1110),
                     ('Metlika', 1127, 1151), ('Novo Mesto', 1151, 1168), ('Metlika', 1186, 1208), ('Novo Mesto', 1210, 1230),
                     ('Metlika', 1267, 1283), ('Novo Mesto', 1271, 1295), ('Metlika', 1314, 1330), ('Metlika', 1386, 1405)],
        'Šentilj': [('Maribor', 361, 377), ('Maribor', 423, 447), ('Maribor', 480, 501), ('Maribor', 537, 559),
                    ('Maribor', 596, 619), ('Maribor', 652, 675), ('Maribor', 707, 730), ('Maribor', 770, 788),
                    ('Maribor', 831, 851), ('Maribor', 886, 901), ('Maribor', 941, 960), ('Maribor', 999, 1021),
                    ('Maribor', 1059, 1078), ('Maribor', 1118, 1138), ('Maribor', 1176, 1198), ('Maribor', 1233, 1258)],
        'Šentjur': [('Grobelno', 427, 448), ('Celje', 481, 496), ('Grobelno', 482, 498), ('Celje', 543, 560),
                    ('Grobelno', 550, 568), ('Celje', 610, 629), ('Grobelno', 618, 634), ('Celje', 668, 690),
                    ('Grobelno', 686, 710), ('Celje', 722, 739), ('Grobelno', 728, 753), ('Celje', 765, 782),
                    ('Grobelno', 777, 797), ('Celje', 824, 844), ('Grobelno', 852, 874), ('Celje', 878, 898),
                    ('Grobelno', 904, 919), ('Celje', 941, 958), ('Grobelno', 956, 974), ('Celje', 1002, 1025),
                    ('Grobelno', 1021, 1041), ('Celje', 1046, 1067), ('Grobelno', 1078, 1094), ('Celje', 1131, 1155),
                    ('Grobelno', 1142, 1158), ('Celje', 1176, 1200), ('Grobelno', 1207, 1224), ('Celje', 1246, 1269),
                    ('Grobelno', 1261, 1284), ('Celje', 1298, 1313), ('Grobelno', 1306, 1325), ('Celje', 1350, 1370)],
        'Škofja Loka': [('Kranj', 378, 396), ('Ljubljana', 397, 415), ('Kranj', 435, 451), ('Ljubljana', 464, 480),
                        ('Kranj', 501, 522), ('Ljubljana', 518, 535), ('Kranj', 548, 564), ('Ljubljana', 569, 588),
                        ('Kranj', 616, 634), ('Ljubljana', 633, 651), ('Ljubljana', 675, 690), ('Kranj', 680, 701),
                        ('Kranj', 729, 746), ('Ljubljana', 737, 756), ('Kranj', 794, 813), ('Ljubljana', 806, 824),
                        ('Kranj', 851, 867), ('Ljubljana', 871, 892), ('Kranj', 915, 935), ('Ljubljana', 923, 940),
                        ('Kranj', 976, 999), ('Ljubljana', 985, 1008), ('Kranj', 1031, 1047), ('Ljubljana', 1048, 1068),
                        ('Kranj', 1088, 1112), ('Ljubljana', 1101, 1124), ('Kranj', 1148, 1163), ('Ljubljana', 1153, 1178),
                        ('Kranj', 1208, 1226), ('Ljubljana', 1222, 1243), ('Kranj', 1275, 1294), ('Ljubljana', 1283, 1306)],
        'Škofljica': [('Grosuplje', 382, 403), ('Grosuplje', 439, 459), ('Ljubljana', 487, 502), ('Grosuplje', 505, 524),
                      ('Ljubljana', 525, 543), ('Grosuplje', 564, 581), ('Ljubljana', 606, 621), ('Grosuplje', 616, 631),
                      ('Ljubljana', 661, 678), ('Grosuplje', 680, 702), ('Ljubljana', 717, 737), ('Grosuplje', 740, 762),
                      ('Ljubljana', 776, 795), ('Grosuplje', 793, 810), ('Ljubljana', 828, 848), ('Grosuplje', 856, 877),
                      ('Ljubljana', 893, 915), ('Grosuplje', 907, 931), ('Ljubljana', 956, 974), ('Grosuplje', 976, 992),
                      ('Ljubljana', 1011, 1027), ('Grosuplje', 1036, 1052), ('Ljubljana', 1068, 1089),
                      ('Grosuplje', 1096, 1115), ('Ljubljana', 1126, 1143), ('Grosuplje', 1154, 1179),
                      ('Ljubljana', 1193, 1215), ('Grosuplje', 1218, 1236), ('Ljubljana', 1254, 1271),
                      ('Grosuplje', 1283, 1307), ('Ljubljana', 1306, 1325), ('Ljubljana', 1381, 1404)],
        'Šmarje pri Jelšah': [('Stranje', 507, 529), ('Grobelno', 542, 563), ('Stranje', 673, 690), ('Grobelno', 721, 738),
                              ('Stranje', 859, 874), ('Grobelno', 885, 906), ('Stranje', 1045, 1066), ('Grobelno', 1068, 1085),
                              ('Stranje', 1219, 1238), ('Grobelno', 1240, 1259)],
        'Šoštanj': [('Polzela', 408, 426), ('Velenje', 432, 452), ('Polzela', 509, 528), ('Velenje', 512, 531),
                    ('Polzela', 593, 608), ('Velenje', 611, 627), ('Velenje', 677, 694), ('Polzela', 687, 710),
                    ('Velenje', 770, 792), ('Polzela', 776, 799), ('Polzela', 858, 879), ('Velenje', 869, 891),
                    ('Velenje', 950, 966), ('Polzela', 953, 969), ('Velenje', 1037, 1053), ('Polzela', 1040, 1061),
                    ('Polzela', 1118, 1139), ('Velenje', 1129, 1154), ('Velenje', 1214, 1232), ('Polzela', 1218, 1240)]}

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    @staticmethod
    def _povezave(seed=42):
        p = """
        60, Ljubljana, Škofja Loka, Kranj, Jesenice
        90, Jesenice, Bled, Bohinj, Most na Soči Anhovo, Gorica
        90, Gorica, Prvačina, Sežana
        60, Koper, Prešnica, Divača, Postojna, Logatec, Ljubljana
        120, Divača, Pivka, Ilirska Bistrica
        240, Prvačina, Ajdovščina
        90, Divača, Sežana, Opčine
        120, Divača, Prešnica, Rakitovec
        60, Grosuplje, Ribnica, Kočevje
        60, Ljubljana, Škofljica, Grosuplje, Ivančna Gorica, Trebnje, Novo Mesto, Črnomelj, Metlika
        120, Trebnje, Mokronog, Sevnica
        60, Ljubljana, Domžale, Kamnik
        60, Ljubljana, Litija, Hrastnik, Zidani Most, Radeče, Sevnica, Krško, Brežice, Dobova
        90, Celje, Polzela, Šoštanj, Velenje
        60, Zidani Most, Laško, Celje, Šentjur, Grobelno, Slovenska Bistrica, Pragersko, Hoče, Maribor, Šentilj
        180, Grobelno, Šmarje pri Jelšah, Stranje, Podčetrtek, Imeno
        180, Stranje, Rogatec
        120, Pragersko, Ptuj, Ljutomer, Lipovci, Murska Sobota, Hodoš
        120, Maribor, Ruše, Ravne na Koroškem
        """

        rg = random.Random(seed)

        povezave = defaultdict(list)
        for vrstica in p.strip().splitlines():
            interval, *kraji = vrstica.strip().split(", ")
            interval = int(interval)
            for smer in (1, -1):
                zacetek = int(300 + max(interval / 2, rg.gauss(interval, interval / 20)))
                while zacetek < 21 * 60:
                    cas = zacetek
                    for k1, k2 in pairwise(kraji[::smer]):
                        trajanje = int(rg.randint(15, 25))
                        povezave[k1].append((k2, cas, cas + trajanje))
                        cas += trajanje
                    zacetek += int(max(interval / 2, rg.gauss(interval, interval / 20)))

        return {k: sorted(v, key=itemgetter(1)) for k, v in povezave.items()}

    def test_1_postaje(self):
        A, B, C, D, E, F = "ABCDEF"
        #
        #  A - B - C - D - E
        #          |
        #          F
        #
        povezave = {A: [(B, 15, 20), (B, 30, 40)],
                    B: [(A, 15, 20), (C, 15, 20), (A, 30, 40)],
                    C: [(B, 15, 20), (D, 15, 20), (F, 15, 20), (F, 30, 40)],
                    D: [(C, 15, 20), (E, 15, 20)],
                    E: [(D, 15, 20)],
                    F: [(C, 15, 20), (C, 30, 40), (C, 50, 60)]}
        koncne, prehodne, krizisca = postaje(povezave)
        self.assertEqual({A, E, F}, koncne)
        self.assertEqual({B, D}, prehodne)
        self.assertEqual({C}, krizisca)

        koncne, prehodne, krizisca = postaje(self.povezave42)
        self.assertEqual(
            {'Kočevje', 'Opčine', 'Ravne na Koroškem', 'Šentilj', 'Koper', 'Ilirska Bistrica', 'Metlika',
             'Velenje', 'Ajdovščina', 'Imeno', 'Rakitovec', 'Dobova', 'Rogatec', 'Kamnik', 'Hodoš'},
            koncne
        )
        self.assertEqual(
            {'Mokronog', 'Novo Mesto', 'Šentjur', 'Šoštanj', 'Polzela', 'Pivka', 'Ivančna Gorica', 'Logatec', 'Gorica',
             'Laško', 'Brežice', 'Podčetrtek', 'Ptuj', 'Jesenice', 'Litija', 'Ljutomer', 'Kranj', 'Lipovci',
             'Škofljica', 'Škofja Loka', 'Črnomelj', 'Ribnica', 'Šmarje pri Jelšah', 'Krško', 'Slovenska Bistrica',
             'Bled', 'Most na Soči Anhovo', 'Radeče', 'Bohinj', 'Domžale', 'Hoče', 'Postojna', 'Ruše', 'Hrastnik',
             'Murska Sobota'},
            prehodne
        )
        self.assertEqual(
            {'Prešnica', 'Sežana', 'Ljubljana', 'Sevnica', 'Pragersko', 'Celje', 'Divača', 'Trebnje', 'Grobelno',
             'Stranje', 'Zidani Most', 'Prvačina', 'Grosuplje', 'Maribor'},
            krizisca
        )

    def test_2a_naslednja_povezava(self):
        povezave = {"Zidani Most": [('Laško', 364, 382), ('Hrastnik', 365, 386),
                                    ('Laško', 375, 390), ('Radeče', 379, 395)],
                    "Laško": [("Zidani Most", 390, 410)],
                    "Hrastnik": [("Zidani Most", 400, 420)],
                    "Radeče": [("Zidani Most", 410, 450), ("Zidani Most", 480, 500)]
                    }
        self.assertEqual((375, 390), naslednja_povezava(povezave, "Zidani Most", "Laško", 370))
        self.assertEqual((375, 390), naslednja_povezava(povezave, "Zidani Most", "Laško", 375))
        self.assertEqual((364, 382), naslednja_povezava(povezave, "Zidani Most", "Laško", 300))
        self.assertEqual((365, 386), naslednja_povezava(povezave, "Zidani Most", "Hrastnik", 300))
        self.assertIsNone(naslednja_povezava(povezave, "Zidani Most", "Radeče", 500))
        self.assertIsNone(naslednja_povezava(povezave, "Zidani Most", "Sevnica", 0))

        self.assertEqual((416, 439), naslednja_povezava(self.povezave42, "Ljubljana", "Domžale", 400))
        self.assertEqual((1015, 1036), naslednja_povezava(self.povezave42, "Ljubljana", "Domžale", 1000))

    def test_2b_potovalni_cas(self):
        self.assertEqual(
            165,
            potovalni_cas(self.povezave42, ["Kranj", "Škofja Loka", "Ljubljana", "Litija", "Hrastnik"], 420)
        )
        self.assertEqual(
            66,
            potovalni_cas(self.povezave42, ["Zidani Most", "Radeče", "Sevnica"], 500)
        )
        self.assertIsNone(potovalni_cas(self.povezave42, ["Zidani Most", "Sevnica"], 500))
        self.assertIsNone(potovalni_cas(self.povezave42, ["Kranj", "Škofja Loka", "Ljubljana", "Litija", "Hrastnik"], 1250))

    def test_3_vozni_redi(self):
        vozni_red(self.povezave42, ["Ljubljana", "Škofja Loka", "Kranj", "Jesenice"], "LŠKJ.txt")
        with open("LŠKJ.txt", encoding="utf-8") as f:
            self.assertEqual("""
           Ljubljana  05:59  06:58  07:57  08:53  09:53  10:57  11:54  12:54  13:55  14:59  15:54  16:50  17:48  18:52  19:52  20:54
         Škofja Loka  06:18  07:15  08:21  09:08  10:16  11:20  12:09  13:14  14:11  15:15  16:16  17:11  18:08  19:08  20:08  21:15
               Kranj  06:36  07:31  08:42  09:24  10:34  11:41  12:26  13:33  14:27  15:35  16:39  17:27  18:32  19:23  20:26  21:34
            Jesenice  06:54  07:56  08:57  09:42  10:59  11:59  12:47  13:50  14:48  15:55  16:55  17:50  18:50  19:48  20:42  21:56""".strip("\n"),
                             f.read().rstrip())

        vozni_red(self.povezave42, ["Ljubljana", "Litija", "Hrastnik", "Zidani Most", "Radeče", "Sevnica"], "sava.txt")
        with open("sava.txt", encoding="utf-8") as f:
            self.assertEqual("""
           Ljubljana  06:00  07:01  07:55  09:02  10:01  11:02  12:01  13:05  14:10  15:06  16:01  17:03  18:03  19:04  20:00
              Litija  06:17  07:21  08:15  09:25  10:23  11:20  12:26  13:24  14:32  15:30  16:19  17:19  18:18  19:28  20:17
            Hrastnik  06:33  07:44  08:31  09:45  10:43  11:42  12:42  13:46  14:52  15:51  16:39  17:41  18:33  19:46  20:34
         Zidani Most  06:52  08:07  08:53  10:01  11:08  11:57  13:07  14:02  15:17  16:10  16:55  17:57  18:53  20:04  20:57
              Radeče  07:12  08:26  09:09  10:22  11:33  12:21  13:29  14:18  15:40  16:25  17:20  18:22  19:11  20:24  21:16
             Sevnica  07:33  08:43  09:26  10:37  11:52  12:44  13:48  14:36  16:01  16:45  17:40  18:40  19:28  20:41  21:33""".strip("\n"),
                             f.read().rstrip())

    def test_4_cas_prihoda(self):
        #     B - C
        #   / | \
        # A - D - G
        #   \   /
        #     -
        povezave = {
            "A": [("G", 0, 200), ("D", 5, 45), ("G", 5, 205), ("B", 10, 20), ("D", 15, 30), ("B", 20, 30), ("B", 30, 40), ("A", 50, 60)],
            "B": [("C", 0, 40), ("D", 0, 20), ("C", 5, 45), ("G", 5, 10), ("C", 10, 50), ("A", 20, 30), ("D", 20, 25), ("A", 40, 50), ("D", 40, 45), ("G", 45, 50), ("A", 60, 70)],
            "C": [("B", 60, 100)],
            "D": [("A", 0, 20), ("A", 20, 70), ("G", 25, 40), ("B", 30, 35), ("G", 45, 60)],
            "G": [("A", 0, 200), ("B", 10, 15), ("D", 35, 45)]
        }
        self.assertEqual(40, cas_prihoda(povezave, "A", "G", 0, 24 * 60))
        self.assertEqual(50, cas_prihoda(povezave, "A", "G", 25, 24 * 60))
        self.assertEqual(451, cas_prihoda(self.povezave42, "Ljubljana", "Kranj", 360, 24 * 60))
        self.assertEqual(1047, cas_prihoda(self.povezave42, "Ljubljana", "Kranj", 1000, 24 * 60))

    def test_5_potnik(self):
        global povezave
        try:
            povezave = self.povezave42

            ana = Potnik("Postojna", 600)
            self.assertEqual(("Postojna", 600), ana.kje())
            self.assertEqual(0, ana.izguba())

            ana.premik("Divača")
            self.assertEqual(("Divača", 656), ana.kje())
            self.assertEqual(41, ana.izguba())

            ana.premik("Kranj")
            self.assertEqual(("Divača", 656), ana.kje())
            self.assertEqual(41, ana.izguba())

            ana.premik("Prešnica")
            self.assertEqual(("Prešnica", 678), ana.kje())
            self.assertEqual(41, ana.izguba())

            ana.premik("Divača")
            self.assertEqual(("Divača", 699), ana.kje())
            self.assertEqual(44, ana.izguba())

            ana.premik("Sežana")
            self.assertEqual(("Sežana", 755), ana.kje())
            self.assertEqual(78, ana.izguba())
        finally:
            del povezave


if __name__ == "__main__":
    unittest.main()
