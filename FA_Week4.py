def inlezen_beginstation(stations):
    """"Controleer of de invoer overeenkom met een waarde in de lijst."""

    while True:
        invoer_beginstation = input("Wat is je beginstation? : ")
        check = invoer_beginstation in stations
        if check == False:
            print("Deze trein komt niet in", invoer_beginstation)

        else:
            return invoer_beginstation


def inlezen_eindstation(stations, beginstation):
    """"Controleer of de invoer overeenkom met een waarde in de lijst en controleer of het station erna of ervoor kom."""

    while True:
        invoer_eindstation = input("Wat is je eindstation? : ")
        check = invoer_eindstation in stations
        if check == False:
            print("Deze trein komt niet in", invoer_eindstation)

        else:
            if stations.index(invoer_eindstation) > stations.index(beginstation):
                return invoer_eindstation
            else:
                print("Dit was een station op dit traject, de trein komt hier niet meer langs.")

def omroepen_reis(stations, beginstation, eindstation):
    """"Weergeef welk station nummer het begin en eindstation zijn, weergeef wat de afstand is, weergeef de prijs en weergeef alle stations die in dit traject tegenkom."""

    stationnummer_begin = stations.index(beginstation) + 1
    stationnummer_eind = stations.index(eindstation) + 1
    print("Het begin station", beginstation, "is het ", stationnummer_begin, "e", "station in het traject.")
    print("Het eind station", eindstation, "is het ", stationnummer_eind, "e", "station in het traject.")

    afstand = print("De afstand bedraagt", stationnummer_eind - stationnummer_begin, "station(s).")
    prijs = print("De prijs van het kaartje is", 5 * (stationnummer_eind - stationnummer_begin), "euro.")
    print()

    print("Jij stapt in de trein in:", beginstation)
    for stations in stations[stationnummer_begin:stations.index(eindstation)]:
        print('-', stations)
    print("Jij stapt uit in:", eindstation)

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
