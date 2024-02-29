# ProyectoED
El proyecto ha sido realizado finalmente por Adrián Uceta Gamaza y Manuel Ripalda Delgado, debido a que el tercer integrante no ha podido colaborar.

El proyecto se puede explicar por capas, las cuales coinciden con el número de ficheros .py que contiene.

· El main llama primero a una función que lee el fichero liga.csv y lo guarda en una lista de diccionarios (cada diccionario es un partido). Dicha lista se usa como parámetro para la función impClasificacion, perteneciente al módulo homónimo, la cual imprime la clasificación de la Liga Santander.

· El módulo impClasificación tan solo tiene una función, la cual genera un listado de nombres de los equipos de la liga mediante la función equipos del módulo tabla, y genera una lista de tuplas ordenadas por el total de puntos de los equipos mediante la función infoEquipos del módulo tabla. Luego, imprime la clasificación con un formato de fácil legibilidad.

· El módulo tabla contiene las dos funciones mencionadas en el párrafo anterior: 
    - La función equipos recibe como parámetro la lista de diccionarios inicial, y va recogiendo los equipos visitantes en  una lista hasta que se repita algún nombre, en cuyo caso retorna la lista de equipos. De este modo, se evita recorrer la lista de diccionarios entera, y solo se recorren un par de jornadas, no las casi 40 que se dan en una temporada. Se recogen los visitantes y no los locales porque de este modo se pueden recoger todos los equipos.
    - La función infoEquipos recibe como parámetros la lista de diccionarios y la lista de los nombres de los equipos, y se encarga de generar una lista de tuplas, cada cual contiene un equipo junto con sus partidos ganados, empatados, perdidos y el total de puntos sumados a lo largo de la temporada, en ese orden. Por cada equipo, recorre los diccionarios y en función del resultado de la función quienGana del módulo datosEquipos, va sumando victorias, empates o derrotas dentro de una lista llamada 'resultados'. Luego, se halla el total de puntos pasándole la lista resultados a la función puntos del módulo datosEquipos, el cual devuelve el total de puntos; finalmente se genera una tupla con los datos obtenidos y se guarda en la lista de tuplas. Sin embargo, no retorna la lista de tuplas, sino que retorna la lista ordenada por puntos mediante la función clasificacion del módulo datosEquipos.

· El módulo datosEquipos contiene las tres funciones usadas dentro de la función infoEquipos:
    - La función quienGana determina si gana, empata o pierde el local. Recibe el resultado del partido como parámetro, y puesto que es una cadena, mediante el método split se divide en dos variables. Si empatan, devuelve 0, si gana el equipo local devuelve 1, si gana el equipo visitante devuelve -1.
    - La función puntos recibe como parámetro una lista con las victorias, empates y derrotas de un equipo, y calcula y retorna el total de puntos obtenidos en función de los resultados.
    - La función clasificación recibe como parámetro la lista de tuplas, y la retorna ordenada por el total de puntos de mayor a menor, mediante la función sorted del paquete predeterminado de python. 