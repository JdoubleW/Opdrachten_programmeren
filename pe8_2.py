import random
def monopolyworp():
    """"Pakt 2 willekeurige getallen tussen de 1 en 6 en controleer of het dubbele waardes zijn."""
    getal1 = random.randrange(1, 7)
    getal2 = random.randrange(1, 7)
    totaal1 = getal1 + getal2
    counter = 0
    while getal1 == getal2:
        print(getal1, '+', getal2, '=', totaal1, '(dubbel)')
        counter += 1
        getal1 = random.randrange(1, 7)
        getal2 = random.randrange(1, 7)
        totaal1 = getal1 + getal2
        if counter == 2 and getal1 == getal2:
           print(getal1, '+', getal2, '=', 'direct naar gevangenis')
           break
    else:
        print(getal1, '+', getal2, '=', totaal1)

print(monopolyworp())