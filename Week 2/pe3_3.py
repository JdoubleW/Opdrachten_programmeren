age = eval(input('Wat is je leeftijd?'))
passport = input('Heb je een paspoort?')

if age >= 18 and passport == 'Ja':
    print("Gefeliciteerd! Jij mag stemmen!")

else:
    print("Jij mag niet stemmen.")