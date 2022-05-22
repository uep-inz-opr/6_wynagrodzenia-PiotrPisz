from re import M
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap


class Pracownik:
    def __init__(self, a , b):
        self.imie = a
        self.pensja = int(b)
    def oblicz_skladki(self):
        brutto = float(self.pensja)
        emerytalna = 0.0976*brutto
        emerytalna = round(emerytalna, 2)
        rentowa = 0.015*brutto
        rentowa = round(rentowa, 2)
        chorobowa = 0.0245*brutto
        chorobowa = round(chorobowa,2)
        c = emerytalna + rentowa + chorobowa
        d = brutto - c
        zdrowotna = 0.09*d
        zdrowotna = round(zdrowotna,2)
        wypadkowa = brutto * 0.0193
        wypadkowa = round(wypadkowa,2)
        fp = brutto * 0.0245
        fp = round(fp, 2)
        fgsp = 0.001 * brutto
        fgsp = round(fgsp,2)
        h = brutto - 111.35 - c
        h = round(h)
        i = h*0.18 - 46.33
        i = round(i,2)
        f = d*0.0775
        f = round(f,2)
        j = i - f
        j = round(j)
        netto = brutto - c - zdrowotna - j
        netto = round(netto, 2)
        skladki_pracodawcy =  emerytalna + 0.065*brutto + wypadkowa + fp + fgsp
        skladki_pracodawcy = round(skladki_pracodawcy, 2)
        koszt_pracodawcy = skladki_pracodawcy + brutto
        koszt_pracodawcy = round(koszt_pracodawcy, 2)
        netto = "{:.2f}".format(netto)
        skladki_pracodawcy = "{:.2f}".format(skladki_pracodawcy)
        return self.imie, netto, skladki_pracodawcy, koszt_pracodawcy

n = input()
n = int(n)
wyniki= []
suma = 0
for i in range(n):
    str1 =""
    m = input().strip()
    m = m.split()
    prac = Pracownik(m[0],m[1])
    funk = prac.oblicz_skladki()
    wyniki.append(funk)
    suma = suma + funk[-1]
    for ele in funk:
        str1 += str(ele) +" "
    str1 = str1[:-1]
    print(str1)
suma = round(suma, 2)
suma = "{:.2f}".format(suma)
print(suma)


