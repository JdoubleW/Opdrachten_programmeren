cijferICOR = 7
cijferPROG = 7
cijferCSN = 7



aver = (cijferICOR + cijferPROG + cijferCSN) / 3

text1 = 'Mijn cijfers, gemiddeld een'
text2 = ' ,leveren een beloning van €'

rew = (cijferICOR + cijferPROG + cijferCSN) * 30


print(text1 + ' ' + str(aver) + text2 + str(rew))

print(cijferICOR)
print(cijferPROG)
print(cijferCSN)

print(text1)
print(text2)