import csv, requests


with open("./appstore_games.csv") as juegos:
    archivo = list(csv.DictReader(juegos))

    for row in archivo:
        if 'ES' in row['Languages']:
            print(row['Name'])
    
    maximos = []
    for i in range(-10, 0):
        maximos = (sorted(archivo, key = lambda archivo: archivo['User Rating Count'], reverse= True)[:10])
    
    for i in range(0, len(maximos)):
        icon_url = maximos[i]['Icon URL']
        icono = requests.get(icon_url)
        with open(f'./imagenes/{i}.jpg', 'wb') as f:
            f.write(icono.content)