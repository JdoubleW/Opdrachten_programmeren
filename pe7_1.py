invoer = int(input("Geef een getal: "))
lijst = []

while invoer != 0:
    lijst.append(invoer)
    totaal = sum(lijst)
    invoer = int(input("Geef een getal: "))

print("Er zijn", len(lijst),  "getallen ingevoer, de som is: ", totaal)