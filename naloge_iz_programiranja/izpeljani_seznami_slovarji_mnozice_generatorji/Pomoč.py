from cmath import sqrt
from doctest import set_unittest_reportflags


def vsota_kvadratov(n):
    return sum([i**2 for i in range(n + 1)])


def vsota_kvadratov_pal(n):
    return sum([i**2 for i in range(n + 1) if str(i) == str(i)[::-1]])

def subs(niz, polozaj):
    izhod = ""
    for indeks in polozaj:
        izhod += niz[int(indeks)]
    return izhod
xs = [183, 168, 175, 176, 192, 180]

def mean(xs):
    return sum(el for el in xs) / len(xs)

def std(xs):
    return sqrt(sum([pow(x - mean(xs), 2) for x in xs]) / len(xs))
morse = {'A': '.-',
'B': '-...',
'C': '-.-.',
'D': '-..',
'E': '.',
'F': '..-.',
'G': '--.',
'H': '....',
'I': '..',
'J': '.---',
'K': '-.-',
'L': '.-..',
'M': '--',
'N': '-.',
'O': '---',
'P': '.--.',
'Q': '--.-',
'R': '.-.',
'S': '...',
'T': '-',
'U': '..-',
'V': '...-',
'W': '.--',
'X': '-..-',
'Y': '-.--',
'Z': '--..',
'1': '.----',
'2': '..---',
'3': '...--',
'4': '....-',
'5': '.....',
'6': '-....',
'7': '--...',
'8': '---..',
'9': '----.',
'0': '-----',
' ': ' '}

def valid(s):
    return sum([int(s[i]) * i for i, char in enumerate(s, reversed)]) % 11 == 0
s = '0306406152'
for i, stevilka in enumerate(s):


print(valid('0306406152'))

