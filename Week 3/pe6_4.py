studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(studentencijfers):
    # berekent alle gemiddelde cijfers van elke leerlingen
    totaal0 = sum(studentencijfers[0])
    totaal1 = sum(studentencijfers[1])
    totaal2 = sum(studentencijfers[2])
    totaal3 = sum(studentencijfers[3])
    return totaal0 / 3, totaal1 / 3, totaal2 / 3, totaal3 / 3,


def gemiddelde_van_alle_studenten(studentencijfers):
    # een gemiddelde van alle studenten
    for row in studentencijfers:
        print(row)
    totaal0 = sum(studentencijfers[0])
    totaal1 = sum(studentencijfers[1])
    totaal2 = sum(studentencijfers[2])
    totaal3 = sum(studentencijfers[3])
    return (totaal0 + totaal1 + totaal2 + totaal3) / 12

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))