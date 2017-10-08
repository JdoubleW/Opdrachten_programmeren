lijst = ['a','b','c']

def wijzig(lijst):
    """"Verwijder de letters"""
    res = lijst.remove('a'), lijst.remove('b'), lijst.remove('c')


print(lijst)
wijzig(lijst)
lijst = ['d', 'e', 'f']
print(lijst)