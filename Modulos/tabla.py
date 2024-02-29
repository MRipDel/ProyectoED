from Modulos import datosEquipos
 # Recibe diccionario y devuelve nombres de los equipos.
def equipos(datosliga):
    equipos=[]
    for partido in datosliga:
        equipo=partido.get('Team 2')
        if equipo not in equipos:
            equipos.append(equipo)
        else:
            return equipos

# Recibe diccionario y nombre de los equipos, devuelve tuplas con partidos ganados, empatados, perdidos y puntos totales, y va ordenada en calidad de este último parámetro.
def infoEquipos(datosliga,equipos):
    clasificacion=[]
    for equipo in equipos:
        resultados=[0,0,0]  #ganados, empatados,perdidos en ese orden.
        for partido in datosliga:
            if equipo==partido.get('Team 1'):
                if datosEquipos.quienGana(partido.get('FT'))==1:
                    resultados[0]+=1
                elif datosEquipos.quienGana(partido.get('FT'))==0:
                    resultados[1]+=1
                else:
                    resultados[2]+=1
            elif equipo==partido.get('Team 2'):
                if datosEquipos.quienGana(partido.get('FT'))==1:
                    resultados[2]+=1
                elif datosEquipos.quienGana(partido.get('FT'))==0:
                    resultados[1]+=1
                else:
                    resultados[0]+=1
        puntos=datosEquipos.puntos(resultados)
        datos=(equipo,resultados[0],resultados[1],resultados[2],puntos)
        clasificacion.append(datos)

    return datosEquipos.clasificacion(clasificacion)


