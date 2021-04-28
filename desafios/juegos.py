import csv, requests


with open("./appstore_games.csv") as juegos:
    
    # convierte el objeto dictReader en una lista
    archivo = list(csv.DictReader(juegos))

    # recorre la lista de objetos conseguida antes y imprime los juegos
    # gratuitos en español
    for row in archivo:
        if (row['Price'] == '0') and ('ES' in row['Languages']):
            print(row['Name'])
    
    # crea una nueva lista de los juegos con mas reseñas ordenada de mayor a menor
    maximos = (sorted(archivo, key = lambda archivo: archivo['User Rating Count'], reverse= True)[:10])
    
    # recorre la lista de maximos y usa el modulo requests
    # para conseguir las imagenes de los juegos
    for i, item in enumerate(maximos):
        icon_url = item['Icon URL']
        icono = requests.get(icon_url)
        with open(f'./imagenes/{i}.jpg', 'wb') as f:
            f.write(icono.content)
