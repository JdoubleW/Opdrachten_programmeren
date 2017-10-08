import datetime
import csv

vandaag = datetime.datetime.today()
time = vandaag.strftime("%a %d %b %Y at %H:%M, ")
bestand = 'D:\HBO\Programmeren\oprdachten files\inloggers.csv'


with open(bestand, 'w') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('Tijd', 'Achternaam', 'Voorletters', 'Geboortedatum', 'Email'))

    while True:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break

        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")


        writer.writerow((time, naam, voorl, gbdatum, email))