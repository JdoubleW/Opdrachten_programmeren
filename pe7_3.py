#key = studentnamen, value = cijfers
cijfers = {'Kevin' : 9, 'test' : 5, 'appel' : 7, 'banaan' : 7,
           'Piet': 7, 'Henk' : 9, 'Sjaak' : 10, 'Gert' : 9}

print(cijfers)
for namen in cijfers.items():
    if namen[1] >= 9:
        print(namen)
