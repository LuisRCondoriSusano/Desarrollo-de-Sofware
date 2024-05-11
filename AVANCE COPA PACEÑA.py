import numpy as np
print("COMIENZA LA COPA PACEÑA Y SE DA ARRANQUE A LA FASE DE GRUPOS")
print("PASAN A CUARTOS DE FINAL LOS SIGUIENTES EQUIPOS DEL GRUPO A")
def grupoA ():
    equipos=np.array(["The strongest" , "Real Tomayapo" , "Real Santa Cruz" , "San Antonio"])
    puntaje=np.array([0,1,3])
    resultadofinal=np.array([])
    for equipo in equipos:
#         print(equipo)
        resultadoparcial=np.random.choice(puntaje,6)
#         print(resultadoparcial)
        suma=resultadoparcial.sum()
#         print(suma)
        resultadofinal=np.append(resultadofinal,suma)
#         print(equipos)
#         print(resultadofinal)
    primerlugarA=equipos[np.argmax(resultadofinal)]
    segundolugarA=equipos[np.argsort(resultadofinal)[-3]]
    print("primer lugar GRUPO A:",primerlugarA)
    print("segundo lugar GRUPO A:",segundolugarA)
    return primerlugarA,segundolugarA
primerlugarA,segundolugarA=grupoA ()

print("PASAN A CUARTOS DE FINAL LOS SIGUIENTES EQUIPOS DEL GRUPO B")
def grupoB ():
    equipos=np.array(["Aurora","nacional potosi","royal pari","blooming"])
    puntaje=np.array([0,1,3])
    resultadofinal=np.array([])
    for equipo in equipos:
#         print(equipo)
        resultadoparcial=np.random.choice(puntaje,6)
#         print(resultadoparcial)
        suma=resultadoparcial.sum()
#         print(suma)
        resultadofinal=np.append(resultadofinal,suma)
#         print(equipos)
#         print(resultadofinal)
    primerlugarB=equipos[np.argmax(resultadofinal)]
    segundolugarB=equipos[np.argsort(resultadofinal)[-3]]
    print("primer lugar GRUPO B:",primerlugarB)
    print("segundo lugar GRUPO B:",segundolugarB)
    return primerlugarB,segundolugarB
primerlugarB,segundolugarB=grupoB ()

print("PASAN A CUARTOS DE FINAL LOS SIGUIENTES EQUIPOS DEL GRUPO C")
def grupoC ():
    equipos=np.array(["Always ready","guabira","independiente petrolero","FC universitario"])
    puntaje=np.array([0,1,3])
    resultadofinal=np.array([])
    for equipo in equipos:
#         print(equipo)
        resultadoparcial=np.random.choice(puntaje,6)
#         print(resultadoparcial)
        suma=resultadoparcial.sum()
#         print(suma)
        resultadofinal=np.append(resultadofinal,suma)
#         print(equipos)
#         print(resultadofinal)
    primerlugarC=equipos[np.argmax(resultadofinal)]
    segundolugarC=equipos[np.argsort(resultadofinal)[-3]]
    print("primer lugar GRUPO C:",primerlugarC)
    print("segundo lugar GRUPO C:",segundolugarC)
    return primerlugarC,segundolugarC
primerlugarC,segundolugarC=grupoC ()

print("PASAN A CUARTOS DE FINAL LOS SIGUIENTES EQUIPOS DEL GRUPO D")
def grupoD ():
    equipos=np.array(["Bolivar","sanjose","wilstermann","oriente petrolero"])
    puntaje=np.array([0,1,3])
    resultadofinal=np.array([])
    for equipo in equipos:
#         print(equipo)
        resultadoparcial=np.random.choice(puntaje,6)
#         print(resultadoparcial)
        suma=resultadoparcial.sum()
#         print(suma)
        resultadofinal=np.append(resultadofinal,suma)
#         print(equipos)
#         print(resultadofinal)
    primerlugarD=equipos[np.argmax(resultadofinal)]
    segundolugarD=equipos[np.argsort(resultadofinal)[-3]]
    print("primer lugar GRUPO D:",primerlugarD)
    print("segundo lugar GRUPO D:",segundolugarD)
    return primerlugarD,segundolugarD
primerlugarD,segundolugarD=grupoD ()


print("SE EMPIEZA CON LOS CUARTOS DE FINAL TENIENDOSE LOS SIGUIENTES CLASIFICADOS")
def cuartos1 ():
    equipos=np.array(["primerlugarA","segundolugarB","primerlugarC","segundolugarD"])
    puntaje=np.array([0,1,3])
    resultadofinal=np.array([])
    for equipo in equipos:
#         print(equipo)
        resultadoparcial=np.random.choice(puntaje,4)
#         print(resultadoparcial)
        suma=resultadoparcial.sum()
#         print(suma)
        resultadofinal=np.append(resultadofinal,suma)
#         print(equipos)
#         print(resultadofinal)
    primerlugarcuartos1=equipos[np.argmax(resultadofinal)]
    segundolugarcuartos1=equipos[np.argsort(resultadofinal)[-2]]
    print("el primer clasificado a semifinales es:",primerlugarcuartos1)
    print("el segundo clasificado a semifinales es:",segundolugarcuartos1)
    return primerlugarcuartos1,segundolugarcuartos1
primerlugarcuartos1,segundolugarcuartos1=cuartos1 ()


def cuartos2 ():
    equipos=np.array(["primerlugarB","segundolugarA","primerlugarD","segundolugarC"])
    puntaje=np.array([0,1,3])
    resultadofinal=np.array([])
    for equipo in equipos:
#         print(equipo)
        resultadoparcial=np.random.choice(puntaje,4)
#         print(resultadoparcial)
        suma=resultadoparcial.sum()
#         print(suma)
        resultadofinal=np.append(resultadofinal,suma)
#         print(equipos)
#         print(resultadofinal)
    primerlugarcuartos2=equipos[np.argmax(resultadofinal)]
    segundolugarcuartos2=equipos[np.argsort(resultadofinal)[-2]]
    print("el tercer clasificado a semifinales es:",primerlugarcuartos2)
    print("el cuarto clasificado a semifinales es:",segundolugarcuartos2)
    return primerlugarcuartos2,segundolugarcuartos2
primerlugarcuartos2,segundolugarcuartos2=cuartos2 ()

print("LLEGAMOS A LAS SEMIFINALES, DONDE SE DECIDIRA QUIENES SERAN LOS CONTENDIENTES AL TITULO")
def semifinal1 ():
    equipos=np.array(["primerlugarcuartos1","segundolugarcuartos2"])
    puntaje=np.array([0,1])
    resultadofinal=np.array([])
    for equipo in equipos:
#         print(equipo)
        resultadoparcial=np.random.choice(puntaje,2)
#         print(resultadoparcial)
        suma=resultadoparcial.sum()
#         print(suma)
        resultadofinal=np.append(resultadofinal,suma)
#         print(equipos)
#         print(resultadofinal)
    ganadorsemifinal1=equipos[np.argmax(resultadofinal)]
    print("el ganador de la semifinal 1 es:",ganadorsemifinal1)
    return ganadorsemifinal1
ganadorsemifinal1=semifinal1()

def semifinal2 ():
    equipos=np.array(["primerlugarcuartos2","segundolugarcuartos1"])
    puntaje=np.array([0,1])
    resultadofinal=np.array([])
    for equipo in equipos:
#         print(equipo)
        resultadoparcial=np.random.choice(puntaje,2)
#         print(resultadoparcial)
        suma=resultadoparcial.sum()
#         print(suma)
        resultadofinal=np.append(resultadofinal,suma)
#         print(equipos)
#         print(resultadofinal)
    ganadorsemifinal2=equipos[np.argmax(resultadofinal)]
    print("el ganador de la semifinal 2 es:",ganadorsemifinal2)
    return ganadorsemifinal2
ganadorsemifinal2=semifinal2()

print("LA GRAN FINAL DE LA COPA PACEÑA, EL CAMPEON ES:")
def final ():
    equipos=np.array(["ganadorsemifinal1","ganadorsemifinal2"])
    puntaje=np.array([0,1])
    resultadofinal=np.array([])
    for equipo in equipos:
#         print(equipo)
        resultadoparcial=np.random.choice(puntaje,2)
#         print(resultadoparcial)
        suma=resultadoparcial.sum()
#         print(suma)
        resultadofinal=np.append(resultadofinal,suma)
#         print(equipos)
#         print(resultadofinal)
    ganadorfinal=equipos[np.argmax(resultadofinal)]
    print("el ganador de la copa paceña es:",ganadorfinal)
    return ganadorfinal
ganadorfinal=final()