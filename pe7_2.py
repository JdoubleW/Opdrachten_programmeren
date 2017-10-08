invoer = input("Geef een string van vier letters: ")

while len(invoer) != 4:
    invoer = input("Geef een string van vier letters: ")

    if len(invoer) == 4:
        break

print("Inlezen van correcte string:", invoer ,  "is geslaagd")