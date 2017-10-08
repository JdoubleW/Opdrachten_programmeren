afstandKM = float(input("Hoeveel kilometer?"))

def standaardprijs(afstandKM):

    #Hier wordt gekeken of de waarde hoger dan 50 KM is of lager dan 0KM. Als het tussen 0 en 50 zit geef dan normale waarde.
    if afstandKM >= 50:
        prijs = 15 + (afstandKM - 50) * 0.60
        return prijs

    if afstandKM <= 0:
        prijs = 0
        return prijs
    else:
        prijs = afstandKM * 0.60

    return prijs

print(standaardprijs(afstandKM))

leeftijd = int(input("Wat is je leeftijd?"))
weekendrit = int(input("Reis je in het weekend?"))  # 1 is in het weekend, 0 is door de weeks.

def ritprijs(leeftijd, weekendrit, afstandKM):
    #Als weekendrit gelijk staat aan 1 dan wordt dit uitgevoerd:
    if weekendrit == 1:
        #Als leeftijd lager is dan 12 of 65 of hoger dan wordt er 35 % korting gegeven.
        if leeftijd < 12 or leeftijd >= 65:
            prijs = standaardprijs(afstandKM) * 0.65
            return prijs

        #Als leeftijd tussen 12 en 65 ligt dan wordt er 40 % korting gegeven.
        if leeftijd >= 12 or leeftijd < 65:
            prijs = standaardprijs(afstandKM) * 0.6
            return prijs

    # Als weekendrit gelijk staat aan 0 dan wordt dit uitgevoerd:
    else:
        # Als leeftijd lager is dan 12 of 65 of hoger dan wordt er 30 % korting gegeven.
        if weekendrit == 0 and leeftijd < 12 or leeftijd >= 65:
            prijs = standaardprijs(afstandKM) * 0.7
            return prijs

        # Als leeftijd tussen 12 en 65 ligt dan wordt er geen korting gegeven.
        if weekendrit == 0 and leeftijd >= 12 or leeftijd < 65:
            prijs = standaardprijs(afstandKM)
            return prijs

print(ritprijs(leeftijd, weekendrit, afstandKM))
