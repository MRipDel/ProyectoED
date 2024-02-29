# Se usan dos funciones, una para crear un diccionario, y otro que la usa para mostrar los resultados.
from Modulos import leerPartidos, impClasificacion as clasi

liga=leerPartidos.leerPartidos()

clasi.impClasificacion(liga)

