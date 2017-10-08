def gemiddelde(invoer):
    # zoekt naar spaties en scheid het van elkaar.
    split = invoer.split()
    # kijk hoeveel woorden er zijn.
    woorden = len(split)


    if woorden < 10:
        print("Te weinig ingevoerd.")

    else:
        split = invoer.split()
        for woorden in split:
            if len(woorden) <= 4:
                print(woorden)

invoer = str(input("Geef lijst met minimaal 10 strings: "))
print(gemiddelde(invoer))