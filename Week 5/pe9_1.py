while True:
    try:
        personen = int(input("Hoeveel personen gaan er mee op reis? "))
        if personen < 0:
            print("Negatieve getallen zijn niet toegestaan!")
            continue
        print(4356 / personen)

    except ValueError:
        print("Gebruik cijfers voor het invoeren van het aantal!")

    except ZeroDivisionError:
        print("Kan getal niet delen door 0!")

    except:
        print("Onjuiste invoer!")

