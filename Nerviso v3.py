import random
def manost1():
    manoj1t1=random.randint(1,13)
    manoj2t1=random.randint(1,13)
    manoj3t1=random.randint(1,13)
    manoj4t1=random.randint(1,13)
    return manoj1t1,manoj2t1,manoj3t1,manoj4t1
def manost2(manoj1t1,manoj2t1,manoj3t1,manoj4t1):
    manoj1t2=random.randint(1,13)
    manoj2t2=random.randint(1,13)
    manoj3t2=random.randint(1,13)
    manoj4t2=random.randint(1,13)
    return manoj1t2,manoj2t2,manoj3t2,manoj4t2
def Conteoronda1(conteopartida):
    conteoj1=conteopartida
    conteoj2=conteopartida+1
    conteoj3=conteopartida+2
    conteoj4=conteopartida+3
    if(conteoj2>=14):
        conteoj2=conteoj2-13
    elif(conteoj3>=14):
            conteoj3=conteoj3-13
    elif(conteoj4>=14):
                conteoj4=conteoj4-13
    return conteoj1,conteoj2,conteoj3,conteoj4
def Conteoronda2(conteoj1,conteoj2,conteoj3,conteoj4):
    conteoj1t2=conteoj1
    conteoj2t2=conteoj2+1
    conteoj3t2=conteoj3+2
    conteoj4t2=conteoj3+3
    if(conteoj1t2>=14):
        conteoj1t2=conteoj1t2-13
    elif(conteoj2t2>=14):
        conteoj2t2=conteoj2-13
    elif(conteoj3t2>=14):
        conteoj3t2=conteoj3-13
    elif(conteoj4t2>=14):
        conteoj4t2=conteoj4-13
    return conteoj1t2,conteoj2t2,conteoj3t2,conteoj4t2
    

conteoj1,conteoj2,conteoj3,conteoj4=Conteoronda1(conteopartida=random.randint(1,13))
conteoj1t2,conteoj2t2,conteoj3t2,conteoj4t2=Conteoronda2(conteoj1,conteoj2,conteoj3,conteoj4)
manoj1t1,manoj2t1,manoj3t1,manoj4t1=manost1()
manoj1t2,manoj2t2,manoj3t2,manoj4t2=manost2(manoj1t1,manoj2t1,manoj2t1,manoj2t1)
#print ("RONDA #1")
#print ("Conteo: ",conteoj1)
#print ("Jugador 1:", manoj1t1)
#print ("Conteo: ",conteoj2)
#print ("Jugador 2:", manoj2t1)
#print ("Conteo: ",conteoj3)
#print ("Jugador 3:", manoj3t1)
#print ("Conteo: ",conteoj4)
#print ("Jugador 4:", manoj4t1)
if (manoj1t1 == conteoj1):
    nerviosoj=random.randint(1,4)
    print ("RONDA #1")
    print ("Conteo: ",conteoj1)
    print ("Jugador 1:", manoj1t1)
    print ("El jugador ", nerviosoj, "perdio")
elif (manoj2t1 == conteoj2):
    nerviosoj=random.randint(1,4)
    print ("RONDA #1")
    print ("Conteo: ",conteoj1)
    print ("Jugador 1:", manoj1t1)
    print ("Conteo: ",conteoj2)
    print ("Jugador 2:", manoj2t1)
    print ("El jugador ", nerviosoj, "perdio")
elif (manoj3t1 == conteoj3):
    nerviosoj=random.randint(1,4)
    print ("RONDA #1")
    print ("Conteo: ",conteoj1)
    print ("Jugador 1:", manoj1t1)
    print ("Conteo: ",conteoj2)
    print ("Jugador 2:", manoj2t1)
    print ("Conteo: ",conteoj3)
    print ("Jugador 3:", manoj3t1)
    print ("El jugador ", nerviosoj, "perdio")
elif (manoj4t1 == conteoj4):
    nerviosoj=random.randint(1,4)
    print ("El jugador ", nerviosoj, "perdio")
    print ("RONDA #1")
    print ("Conteo: ",conteoj1)
    print ("Jugador 1:", manoj1t1)
    print ("Conteo: ",conteoj2)
    print ("Jugador 2:", manoj2t1)
    print ("Conteo: ",conteoj3)
    print ("Jugador 3:", manoj3t1)
    print ("Conteo: ",conteoj4)
    print ("Jugador 4:", manoj4t1)
    #RONDA NUMERO 2
elif (manoj1t2 == conteoj1t2):
    nerviosoj=random.randint(1,4)
    print ("RONDA #1")
    print ("Conteo: ",conteoj1)
    print ("Jugador 1:", manoj1t1)
    print ("Conteo: ",conteoj2)
    print ("Jugador 2:", manoj2t1)
    print ("Conteo: ",conteoj3)
    print ("Jugador 3:", manoj3t1)
    print ("Conteo: ",conteoj4)
    print ("Jugador 4:", manoj4t1)
    print ("RONDA #2")
    print ("Conteo: ",conteoj1t2)
    print ("Jugador 1:", manoj1t2)
    print ("El jugador ", nerviosoj, "perdio")
elif (manoj2t2 == conteoj2t2):
    nerviosoj=random.randint(1,4)
    print ("RONDA #1")
    print ("Conteo: ", conteoj1)
    print ("Jugador 1:", manoj1t1)
    print ("Conteo: ",conteoj2)
    print ("Jugador 2:", manoj2t1)
    print ("Conteo: ",conteoj3)
    print ("Jugador 3:", manoj3t1)
    print ("Conteo: ",conteoj4)
    print ("Jugador 4:", manoj4t1)
    print ("RONDA #2")
    print ("Conteo: ",conteoj1t2)
    print ("Jugador 1:", manoj1t2)
    print ("Conteo: ",conteoj2t2)
    print ("Jugador 2:", manoj2t2)
    print ("El jugador ", nerviosoj, "perdio")
elif (manoj3t2 == conteoj3t2):
    nerviosoj=random.randint(1,4)
    print ("RONDA #1")
    print ("Conteo: ", conteoj1)
    print ("Jugador 1:", manoj1t1)
    print ("Conteo: ",conteoj2)
    print ("Jugador 2:", manoj2t1)
    print ("Conteo: ",conteoj3)
    print ("Jugador 3:", manoj3t1)
    print ("Conteo: ",conteoj4)
    print ("Jugador 4:", manoj4t1)
    print ("RONDA #2")
    print ("Conteo: ",conteoj1t2)
    print ("Jugador 1:", manoj1t2)
    print ("Conteo: ",conteoj2t2)
    print ("Jugador 2:", manoj2t2)
    print ("Conteo: ",conteoj3t2)
    print ("Jugador 3:", manoj3t2)
    print ("El jugador ", nerviosoj, "perdio")
elif (manoj4t2 == conteoj4t2):
    nerviosoj=random.randint(1,4)
    
    print ("RONDA #1")
    print ("Conteo: ", conteoj1)
    print ("Jugador 1:", manoj1t1)
    print ("Conteo: ",conteoj2)
    print ("Jugador 2:", manoj2t1)
    print ("Conteo: ",conteoj3)
    print ("Jugador 3:", manoj3t1)
    print ("Conteo: ",conteoj4)
    print ("Jugador 4:", manoj4t1)
    print ("RONDA #2")
    print ("Conteo: ",conteoj1t2)
    print ("Jugador 1:", manoj1t2)
    print ("Conteo: ",conteoj2t2)
    print ("Jugador 2:", manoj2t2)
    print ("Conteo: ",conteoj3t2)
    print ("Jugador 3:", manoj3t2)
    print ("Conteo: ",conteoj4t2)
    print ("Jugador 4:", manoj4t2)
    print ("El jugador ", nerviosoj, "perdio")
else:
        print ("RONDA #1")
        print ("Conteo: ", conteoj1)
        print ("Jugador 1:", manoj1t1)
        print ("Conteo: ",conteoj2)
        print ("Jugador 2:", manoj2t1)
        print ("Conteo: ",conteoj3)
        print ("Jugador 3:", manoj3t1)
        print ("Conteo: ",conteoj4)
        print ("Jugador 4:", manoj4t1)
        print ("RONDA #2")
        print ("Conteo: ",conteoj1t2)
        print ("Jugador 1:", manoj1t2)
        print ("Conteo: ",conteoj2t2)
        print ("Jugador 2:", manoj2t2)
        print ("Conteo: ",conteoj3t2)
        print ("Jugador 3:", manoj3t2)
        print ("Conteo: ",conteoj4t2)
        print ("Jugador 4:", manoj4t2)
        print ("NADIE PERDIO EN LA RONDA #2")
