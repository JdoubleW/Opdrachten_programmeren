def namen():
    """"Sla de naam op en onthou hoevaak de naam tegen komt in de lijst"""
    diction = {}
    lijst = []
    invoer = input("Volgende naam: ")
    lijst.append(invoer)

    while len(invoer) != 0:
        invoer = input("Volgende naam: ")
        lijst.append(invoer)
        if len(invoer) == 0:
            for item in lijst:
                if item in diction:
                    diction[item] += 1
                else:
                    diction[item] = 1

        for value in diction:
            if diction[value] == 1:
                uitvoer = print('Er is 1 student met de naam', value )

            else:
                uitvoer2 = print('Er zijn', diction[value], 'studenten met de naam', value )


print(namen())