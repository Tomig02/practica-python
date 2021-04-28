import csv, json, PySimpleGUI as sg
from collections import defaultdict

def artistas_famosos(cant):
    ''' devuelve una lista de los artistas con mas seguidores
        en spotify.
        La cantidad de elementos de la lista depende del numero 
        que se le pase
    '''
    # crea una lista con el contanido del dataset
    data = cargar_datos('artistas_spotify')

    # definicion de la key para el sort
    sort_key = lambda data: 0 if data['followers'].split('.')[0] == '' else int(data['followers'].split('.')[0]) 
    
    # ordena la lista de mayor a menor y se queda con los 10 primeros
    lista_datos = sorted(data, key= sort_key, reverse=True)[:cant]
    guardar_datos(lista_datos, 'opcion1')

    # retorna una lista de x elementos ordenada de mayor a menor
    return lista_datos

def olimpiadas_oro(cant):
    ''' devuelve una lista de los atletas con medallas de oro 
        que participen en la disciplina de atletismo.
        La cantidad de elementos de la lista depende del numero 
        que se le pase 
    '''
    # crea una lista con el contenido del dataset
    data = cargar_datos('olimpiads_verano')
    
    # limpia de los datos a todos los atletas que no hagan atletismo o no tengan medallas de oro 
    olimpicos = [item for item in data if (item['Discipline'] == 'Athletics') and (item['Medal'] == 'Gold')]
    
    # acumula las medallas de oro por atleta y se queda con los 10 mejores
    acumular = defaultdict(int)
    for item in olimpicos:
        acumular[item['Athlete']] += 1
    res = sorted(acumular.items(), key= lambda item: item[1], reverse= True)[:cant]
    
    # busca los datos de los 10 mejores atletas
    lista = []
    for item in res:

        # esto me rendi y lo busque en stack overflow, no sabria como
        # explicarlo 
        atleta = next(node for node in olimpicos if node['Athlete'] == item[0])
        new_item ={
            'nombre': atleta['Athlete'],
            'nacionalidad': atleta['Country'],
            'genero': atleta['Gender'],
            'pais': atleta['Country'],
            'medallas': item[1]
        }

        lista.append(new_item)

    guardar_datos(lista, 'opcion2')
    return lista

def guardar_datos(data, nombre):

    # crea un json con los datos creados
    with open(f'data/{nombre}.json', mode='w') as json_file:
        json.dump(data, json_file)
         

def cargar_datos(nombre):
    data = []
    try:
        with open(f'data/{nombre}.csv', encoding='utf-8') as archivo:
            data = list(csv.DictReader(archivo))
    except:
        print("Hay un problema con el dataset")

    return data