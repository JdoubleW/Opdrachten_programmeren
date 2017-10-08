file = open("kaartnummers", 'r')

for line in file:
    kaart = line.split(',')

    print(kaart[1], "heeft kaartnummer:", kaart[0])
file.close()