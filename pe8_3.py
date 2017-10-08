def code(invoerstring):
    """"Zet de tekens om naar een nieuwe waarde"""
    tekst = ''
    for letter in invoerstring:
        omzet = ord(letter) + 3
        letters = chr(omzet)
        tekst += letters
    return tekst


invoerstring = input("Naam + beginstation + eindstation: ")
print(code(invoerstring))