import csv

with open('newfile.csv', 'w') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('Artikelnummer','Artikelcode','Naam','Voorraad','Prijs'))

    HP = int(121), 'ABC123', 'Highlight pen', int(231), float(0.56)
    NM = int(123), 'PQR678', 'Nietmachine', int(587), float(9.99)
    BL = int(128), 'ZYX163', 'Bureaulamp', int(34), float(19.95)
    MS = int(137), 'MLK709', 'Monitorstandaard', int(66), float(32.50)
    IH = int(271), 'TRS665', 'Ipad hoes', int(155), float(19.01)
    writer.writerow((HP))
    writer.writerow((NM))
    writer.writerow((BL))
    writer.writerow((MS))
    writer.writerow((IH))

with open('newfile.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')

    lijst = []
    controle = 0
    for duurst in reader:
        if float(duurst['Prijs']) > controle:
            controle = float(duurst['Prijs'])
            lijst = duurst
    print("Het duurste artikel is", lijst['Naam'], "en die kost", lijst['Prijs'], "Euro")


with open('newfile.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')

    lijst = []
    controle = 100000
    for kleinst in reader:
        if int(kleinst['Voorraad']) < controle:
            controle = int(kleinst['Voorraad'])
            lijst = kleinst

    print("Er zijn slechts", lijst['Voorraad'], "exemplaren in voorraad van het product met nummer", lijst['Artikelnummer'])


with open('newfile.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')

    lijst = []
    for totaal in reader:
        getallen = int(totaal["Voorraad"])
        lijst.append(getallen)

    print("In totaal hebben wij", sum(lijst), "producten in ons magazijn liggen.")

