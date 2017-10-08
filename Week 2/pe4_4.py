old = "Test123"
def new_password(new):
    """"Kijkt of de nieuwe wachtwoord gelijk staat aan de oude wachtwoord en controleert of de lengte meer dan 6 karakters heeft."""
    res = new != old and len(new) >= 6
    return res
new = (input("Voer nieuw wachtwoord in: "))

if new_password(new):
    print("True")

else:
    print("False")