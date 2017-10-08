def toon_aantal_kluizen_vrij():
    # kijkt naar hoeveel kluizen er vrij zijn door de regels te tellen.
    infile = open("kluizen", 'r')
    linelist = infile.readlines()
    infile.close
    return len(linelist)


def nieuwe_kluis():
    # maak een lijst met alle kluisnummers. lees alle regels van kluizen en doorloop het met een for loop.
    infile = open("kluizen", 'r')
    linelist = infile.readlines()
    kluisjes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for waarde in linelist:
        tempdata = waarde.split(';')
        kluisjes.remove(int(tempdata[0]))
    infile.close()
    if len(kluisjes)<=0:
        return"Geen kluisjse"

    kluisjes[0]
    wachtwoord = input("Wacthwoord: ")
    file = open("kluizen", 'a')
    file.write("{};{}\n".format(kluisjes[0], wachtwoord))
    file.close()
    return 'Uw kluisnummer is: ', kluisjes[0]


def kluis_openen(invoer):
    kluisnummer = int(input("Vul uw kluisnummer in:"))
    wachtwoord = input("Vul uw wachtwoord in:")

    infile = open("kluizen", 'r')
    linelist = infile.readlines()
    for waarde in linelist:
        split_lijst = waarde.split(';')
        split_lijst[1] = split_lijst[1].replace("\n", "")

        if wachtwoord == split_lijst[1] and kluisnummer == int(split_lijst[0]):
            return "Toegang verleend"

    return "Toegang geweigerd"


invoer = int(input("1: Ik wil weten hoeveel kluizen er nog vrij zijn. \n"
                   "2: Ik wil een nieuwe kluis. \n"
                   "3: Ik wil even iets uit mijn kluis halen. \n"))

if invoer == 1:
    print("Er zijn", 12 - toon_aantal_kluizen_vrij(), 'kluizen beschikbaar.')

elif invoer == 2:
    print(nieuwe_kluis())

elif invoer == 3:
    print(kluis_openen(invoer))

else:
    print("Verkeerde invoer")
