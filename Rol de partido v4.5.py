import numpy as np
import random

def RondadeGrupos(equipos):
    
    resultados = np.zeros((4, 4))
    puntos_goles = {equipo: {'puntos': 0, 'goles': 0} for equipo in equipos}

    
    for i in range(len(equipos)):
        for j in range(i+1, len(equipos)):  
            if i != j:
                golesLocal = random.randint(0, 5)
                golesVisitante = random.randint(0, 5)
                resultados[i][j] = golesLocal
                resultados[j][i] = golesVisitante

                
                if golesLocal > golesVisitante:
                    puntos_goles[equipos[i]]['puntos'] += 3
                elif golesVisitante > golesLocal:
                    puntos_goles[equipos[j]]['puntos'] += 3
                else:
                    puntos_goles[equipos[i]]['puntos'] += 1
                    puntos_goles[equipos[j]]['puntos'] += 1

                puntos_goles[equipos[i]]['goles'] += golesLocal
                puntos_goles[equipos[j]]['goles'] += golesVisitante

    print(resultados)

    for i in range(len(equipos)):
        for j in range(i+1, len(equipos)):  
            print(f'{equipos[i]} {int(resultados[i][j])} - {int(resultados[j][i])} {equipos[j]}')

    
    for equipo in equipos:
        print(f'{equipo} tiene {puntos_goles[equipo]["puntos"]} puntos y {puntos_goles[equipo]["goles"]} goles')

 
    equipos_ordenados = sorted(equipos, key=lambda x: (puntos_goles[x]['puntos'], puntos_goles[x]['goles']), reverse=True)

    
    ganadores = equipos_ordenados[:2]

    return ganadores

equipos = np.array(['Bolivar', 'Millonarios', 'Flamengo', 'Palestino'])
ganadores = RondadeGrupos(equipos)
print("Equipos ganadores del grupo:", ganadores)