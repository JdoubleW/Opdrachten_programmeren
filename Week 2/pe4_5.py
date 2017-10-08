a = int(input("Voer getal in: "))
b = int(input("Voer getal in: "))
c = int(input("Voer getal in: "))

GG = [a, b, c]

A = GG[0]
B = GG[1]
C = GG[2]

def kwadraten_som(GG):

    if GG[0] < 0:
        GG.remove(A)
        kwadraat = GG[0] * GG[0], GG[1] * GG[1]
        totaal = sum(kwadraat)
        return totaal

    if GG[1] < 0:
        GG.remove(B)
        kwadraat = GG[0] * GG[0], GG[1] * GG[1]
        totaal = sum(kwadraat)
        return totaal

    if GG[2] < 0:
        GG.remove(C)
        kwadraat = GG[0] * GG[0], GG[1] * GG[1]
        totaal = sum(kwadraat)
        return totaal

    else:
        kwadraat = GG[0] * GG[0], GG[1] * GG[1], GG[2] * GG[2]
        totaal = sum(kwadraat)
        return totaal

print(kwadraten_som(GG))