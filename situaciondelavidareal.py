import random
import numpy as np

def Lineaquellego(LineadeBus, linea1, linea2, linea3):
    Lineas = [linea1, linea2, linea3]
    LineadeBusAleatoria = random.randint(0, 2)
    LineadeBus = Lineas[LineadeBusAleatoria]
    print("Su línea es:", LineadeBus)
    return LineadeBus

def SituaciondelaVidaReal():
    lineas = np.array(['linea1', 'linea2', 'linea3'])
    print("Espere a cualquier línea que lo lleve")
    LineadeBusAleatoria = int(input("Elija una línea (1, 2, 3): ")) 
    Destino = "Universidad"
    Linea1 = 1
    Linea2 = 2
    Linea3 = 3
    
    if LineadeBusAleatoria in [Linea1, Linea2, Linea3]:
        print("Rumbo correcto")
    else:
        print("Recalcular ruta")
        
    
    CarnetUni = input("¿Tiene carnet universitario? (SI/NO): ")
    if CarnetUni.upper() == "SI":
        print("Pagará 1 Bs.")
    else:
        print("Pagará 1.80 Bs.")
    
    Accidente = input("¿Ocurrió un accidente? (SI/NO): ")
    if Accidente.upper() == "SI":
        print("Camine hasta la U.")
    else:
        Trafico = input("¿Hay tráfico? (SI/NO): ")
        if Trafico.upper() == "SI":
            print("Camine hasta la U.")
        else:
            print("Quedarse sentado")

# Repetir cinco veces
for dia in range(1, 6):
    print(f"\nDía {dia} ")
SituaciondelaVidaReal()
