
# A partir de la lista recibida, genera los datos de la clasificación y los imprime por pantalla.
from Modulos import tabla

def impClasificacion(liga):

    equipos=tabla.equipos(liga)

    clasificacion=tabla.infoEquipos(liga, equipos)

    print('LIGA SANTANDER\n|Equipo\t\t|\tGan\t|\tEmp\t|\tDerr\t|\tPuntos\t|')
    for i in clasificacion:
        if len(i[0])>6:
            print(f'|{i[0]}\t|\t{i[1]}\t|\t{i[2]}\t|\t{i[3]}\t|\t{i[4]}\t|')
        else:
            print(f'|{i[0]}\t\t|\t{i[1]}\t|\t{i[2]}\t|\t{i[3]}\t|\t{i[4]}\t|')
