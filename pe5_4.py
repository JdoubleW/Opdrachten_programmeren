import datetime
vandaag = datetime.datetime.today()
time = vandaag.strftime("%a %d %b %Y, %H:%M:%S, ")

outfile = open('hardlopers.txt', 'a')
outfile.write(time)
naam = input("Naam:")
outfile.write(naam)
outfile.write('\n')

outfile.close()