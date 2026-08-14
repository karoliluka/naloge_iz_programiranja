#.py
import os

def vse_py(root): #vse datoteke v pythonProject/naloge_iz_programiranja/naloge_iz_programiranja ki se končajo na .py
    for koren, mape, datoteke in os.walk(root):
        for dat in datoteke:
            if dat.endswith(".py"):
                print(os.path.join(koren, dat))

#vse_py("/Users/lukakaroli/PycharmProjects/pythonProject/naloge_iz_programiranja/naloge_iz_programiranja")

#ID3v1
def idv3(mapa):
    for dat in sorted(os.listdir(mapa)):
        if not dat.endswith(".mp3"):
            continue

        polna_pot = os.path.join(mapa, dat)
        with open(polna_pot, "rb") as f:
            f.seek(-128, 2)
            zadnjih_128 = f.read(128)

        if zadnjih_128[:3] != b"TAG":
            continue

        naslov = zadnjih_128[3:33].decode("latin-1").rstrip("\x00")
        izvajalec = zadnjih_128[33:63].decode("latin-1").rstrip("\x00")
        album = zadnjih_128[63:93].decode("latin-1").rstrip("\x00")
        leto = zadnjih_128[93:97].decode("latin-1").rstrip("\x00")

        print(f" Title: {naslov}")
        print(f"Artist: {izvajalec}")
        print(f" Album: {album}")
        print(f"  Year: {leto}")
        print(f"  File: {dat}")
        print()

#print(idv3("/Users/lukakaroli/PycharmProjects/pythonProject/naloge_iz_programiranja/naloge_iz_programiranja/oblikovanje_nizov_in_delo_z_datotekami/sponzorska_plata"))

def preberi_vse(mapa):
    vsebine = {}
    for dat in sorted(os.listdir(mapa)):
        pot = os.path.join(mapa, dat)
        if os.path.isfile(pot):
            with open(pot, encoding="utf-8") as f:
                vsebine[dat] = f.read()
    return vsebine

def imata_skupen_del(besedilo1, besedilo2, dolzina=1000):
    podnizi1 = {besedilo1[i:i + dolzina] for i in range(len(besedilo1) - dolzina + 1)}
    for i in range(len(besedilo2) - dolzina + 1):
        if besedilo2[i:i + dolzina] in podnizi1:
            return True
    return False

def poisci_plagiatorja(mapa, dolzina=1000):
    vsebine = preberi_vse(mapa)
    imena = list(vsebine)
    for i in range(len(imena)):
        for j in range(i + 1, len(imena)):
            ime1, ime2 = imena[i], imena[j]
            if imata_skupen_del(vsebine[ime1], vsebine[ime2], dolzina):
                print(f"{ime1} in {ime2} sta si podobna (skupni del dolg vsaj {dolzina} znakov)")

poisci_plagiatorja("/Users/lukakaroli/PycharmProjects/pythonProject/naloge_iz_programiranja/naloge_iz_programiranja/oblikovanje_nizov_in_delo_z_datotekami/datoteke")