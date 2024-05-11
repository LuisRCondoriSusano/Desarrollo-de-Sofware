
cantidad = int(input("Dame un numero pequeño: "))

def forlista(cantidad):
    for x in range(1, cantidad+1):
        if ((x % 1 == 0) and (x % x == 0) and (x % 2 != 0) and (x % 3 != 0)):
            print (x, "De la lista for es primo")
    return x
x = forlista(cantidad)

def whilelista(cantidad):
    y = 1
    while y < (cantidad+1):
        if ((y % 1 == 0) and (y % y == 0) and (y % 2 != 0) and (y % 3 != 0)):
            print (y, "De la lista while es primo")
        y += 1
    return y
y = whilelista(cantidad)
