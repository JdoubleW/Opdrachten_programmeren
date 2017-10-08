def sorted_list(invoer):
    # zoekt naar - en scheid het van elkaar.
    split = invoer.split('-')
    lijst = list(split)
    sort = lijst.sort()

    return lijst

def kleinst(invoer):
    # maakt een lijst en pakt de kleinste waarde
    split = invoer.split('-')
    lijst = list(split)
    sort = lijst.sort()
    return min(lijst)

def aantal(invoer):
    # maakt een lijst en kijkt hoeveel getallen in de lijst staan
    split = invoer.split('-')
    lijst = list(split)
    return len(lijst)

def totaal(invoer):
    #maakt een lijst en berekent hoeveel getallen erin staan
    split = invoer.split('-')
    lijst = list(split)
    waarde = map(int, lijst)
    return sum(waarde)

def gemiddelde(invoer):
    # maakt een lijst en berekend het gemiddelde uit
    split = invoer.split('-')
    lijst = list(split)
    waarde = map(int, lijst)
    return sum(waarde) / len(lijst)


invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

print("Gesorteerd list van ints: ", str(sorted_list(invoer)), "\n" +
      "Grootste getal:", max(invoer), "en Kleinst getal: ", kleinst(invoer), "\n" +
      "Aantal getallen:", aantal(invoer), "en Som van de getallen: ", totaal(invoer), "\n" +
      "Gemiddelde:", gemiddelde(invoer))