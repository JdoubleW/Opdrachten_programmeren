def lang_genoeg(length):
    """"Kijkt of de waarde onder 120 zit."""
    res = length >= 120
    return res
length = eval(input("Hoe lang ben jij in centimeters?"))

if lang_genoeg(length):
    print("Je bent lang genoeg voor de attractie!")

else:
    print("Sorry, je bent te klein.")