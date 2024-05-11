import random

def CalcularGanador ():   
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    suma=dado1+dado2
    dado3 = random.randint(1,6)
    dado4 = random.randint(1,6)
    suma2=dado3+dado4
    resta1=suma-21
    resta2=suma2-21
    return resta1, resta2
resta1, resta2= CalcularGanador ()
print("la suma de los dados del J2 fue:", resta1+21)
print("la suma de los dados del J2 fue:", resta2+21)
def puntuacion():
    if (resta1>resta2):
        puntuacionJ1=1
        puntuacionJ2=0
    else:
        puntuacionJ1=0
        puntuacionJ2=1
    return puntuacionJ1,puntuacionJ2
puntuacionJ1,puntuacionJ2=puntuacion()
print("PUNTUACION")
print("Puntuacion jugador 1: ", puntuacionJ1)
print("Puntuacion jugador 2: ", puntuacionJ2)
