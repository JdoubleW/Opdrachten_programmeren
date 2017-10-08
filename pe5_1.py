celsius = int(-30)
afk = ['F', 'C']
def convert(celsius):
    return celsius * 1.8 + 32
cel = [-30, -20, -10, 0, 10, 20, 30, 40]
def table(cel):
    for value in cel:
        fahrenheit = convert(value)
        print('F{:5}    C{:5}'.format(fahrenheit, value))
print(table(cel))