def gemiddelde(sentence):
    # zoekt naar spaties en scheid het van elkaar.
    split = sentence.split()
    # kijk hoeveel woorden er zijn.
    woorden = len(split)
    # kijkt hoeveel letters er zijn
    letters = len(sentence)
    return len(sentence) / len(split)

sentence = str(input("Voer een zin in: "))

print(gemiddelde(sentence))