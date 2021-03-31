nombres = [
    'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 
    'CESAR', 'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 
    'Fabián', 'Facundo', 'Facundo', 'FEDERICO', 'FEDERICO', 'GONZALO',
    'Gregorio', 'Ignacio', 'Jonathan', 'Jonathan', 'Jorge', 'JOSE',
    'JUAN', 'Juan', 'Juan', 'Julian', 'Julieta', 'LAUTARO', 'Leonel', 'LUIS',
    'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'NICOLÁS',
    'Noelia', 'Pablo', 'Priscila', 'TOMAS', 'Tomás', 'Ulises', 'Yanina'
]
eval_1 = [
    81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3,
    35, 67, 10, 57, 11, 69, 12, 77, 13, 86, 48, 65,
    51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37,
    42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74
]
eval_2 = [
    30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 
    13, 34, 96, 71, 86, 37, 64, 13, 8, 87, 14, 14, 
    49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
    95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10
]

estudiantes = []
pos = 0
max_prom = 0

# recorre la lista de nombres calculando el promedio del alumno 
# y acumulandolo en el promedio general, luego guarda al estudiante y
# su nota en una tupla 
for nombre in nombres:
    nota = (eval_1[pos] + eval_2[pos]) / 2
    max_prom += nota

    estudiantes.append((nombre, nota))
    pos += 1

# promedio general
max_prom = max_prom / len(estudiantes)
print("promedio general: ", max_prom)

# imprime promedios menores a la media
prom_bajo = []
for alum in estudiantes:
    if alum[1] < max_prom:
        print(alum[0], ", prom: ", alum[1])