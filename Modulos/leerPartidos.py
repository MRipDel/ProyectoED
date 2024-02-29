
# Se importa el csv y se devuelve una lista de diccionarios. Las claves son las columnas, los valores listas. 
import csv

def leerPartidos():
    
    lista=[]
    
    with open('Modulos\liga.csv') as fichero:
        
        lector=csv.DictReader(fichero, delimiter=',')

        next(lector)
        
        for i in lector:

            lista.append(i)

    return lista