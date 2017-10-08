def jazz(getallen):
    count = 0
    for getal in getallen:
        if getal > 4:
            count = count + 1
    return count

reeks = [3,4,5,6]
res = jazz(reeks)
print(res)