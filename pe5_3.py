kaartnummers = open("kaartnummers", 'r')

def numlines(kaartnummers):
    # telt hoeveel regels er zijn in een bestand
    infile = open("kaartnummers", 'r')
    linelist = infile.readlines()
    return len(linelist)

def highest(kaartnummers):
    # Zoekt naar de hoogste waarde in het bestand
    infile = open("kaartnummers", 'r')
    linelist = infile.readlines()
    print(linelist)
    hoogst = max(linelist)
    kaart, naam = hoogst.split(',')
    return kaart

def line(kaartnummers):
    # Zoekt naar de regel van de hoogste waarde in het bestand
    infile = open("kaartnummers", 'r')
    linelist = infile.readlines()
    hoogst = max(linelist)
    kaart, naam = hoogst.split(',')

    return kaart

print("Deze file telt",numlines('kaartnummers'), "regels." '\n' "Het grootste kaartnummer is:", highest(kaartnummers),
      "en dat staat op regel", line(kaartnummers))