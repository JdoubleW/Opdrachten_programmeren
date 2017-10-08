import csv
bestand = 'D:\HBO\Programmeren\oprdachten files\gamers.csv'


with open(bestand, 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')

    lijst = []
    controle = 0
    for row in reader:
        if int(row[2]) > controle:
            controle = int(row[2])
            lijst = row


    print("De hoogste score is", lijst[2], "op", lijst[1], "behaald door", lijst[0])