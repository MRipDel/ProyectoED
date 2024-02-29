# Determina resultado. Devuelve 1 si gana local, 0 si empata, -1 si pierde.
def quienGana(resultado):

    goles_local,goles_visitante=resultado.split("-")
    
    if goles_local==goles_visitante:
        return 0
    elif goles_local>goles_visitante:
        return 1
    else:
        return -1

# Recibe lista de partidos empatados ganados, empatados y perdidos. Devuelve el total de puntos. +3/victoria, +1/empate, 0/derrota.
def puntos(info):
    
   puntos=info[0]*3+info[1]
   return puntos

# Ordena la lista recibida en función de los puntos.
def clasificacion(datos):
    return sorted(datos, key=lambda equipo: equipo[4], reverse=True)