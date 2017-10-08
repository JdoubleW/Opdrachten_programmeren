diction = {}

def ticker(filename):
    """"Creeërt een dictionary van een file."""
    with open(filename) as file:
        for line in file:
            (key, val) = line.rstrip('\n').split(':')
            diction[key] = val
        return diction

ticker('ticker')

bedrijf = input("Enter Company name: ")
for key, value in diction.items():
    if bedrijf == key:
        print("Ticker symbol:", value)



print()

tickersymbol = input("Enter Ticker symbol: ")

for key, value in diction.items():
    if tickersymbol == value:
        print("Company name:", key)
